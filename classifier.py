# kb_train.py
# pip install pandas scikit-learn numpy joblib

import os, re, unicodedata, numpy as np, pandas as pd, joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report

# --- 1) CONFIG ---
csv_path = r"C:\Users\Pipe\Downloads\report1761178990333.csv"   # <-- ajusta si el nombre cambia
out_dir  = os.path.dirname(csv_path)

# --- 2) LECTURA ROBUSTA (auto-detecta separador y BOM) ---
df = pd.read_csv(csv_path, sep=None, engine="python", encoding="utf-8-sig")

# Renombra columnas típicas si vienen con variaciones de mayúsculas/espacios
def col(df, *names):
    for n in names:
        if n in df.columns: return n
    # prueba variantes sin espacios y lower
    cols_norm = {re.sub(r"\s+", "", c).lower(): c for c in df.columns}
    for n in names:
        key = re.sub(r"\s+", "", n).lower()
        if key in cols_norm: return cols_norm[key]
    return None

c_title   = col(df, "Title")
c_summary = col(df, "Summary")
c_desc    = col(df, "Description")
c_terms   = col(df, "Suggested Search Terms", "Suggested Terms", "Search Terms")
c_label   = col(df, "label", "Label", "Category")

# Crea columnas faltantes
for c in [c_title, c_summary, c_desc, c_terms, c_label]:
    if c is None: continue
for name, var in [("Title", c_title), ("Summary", c_summary), ("Description", c_desc),
                  ("Suggested Search Terms", c_terms), ("label", c_label)]:
    if var is None:
        df[name] = ""
    else:
        df.rename(columns={var: name}, inplace=True)

# --- 3) NORMALIZACIÓN (tolera vacíos) ---
def norm(s: str) -> str:
    if not isinstance(s, str): return ""
    s = s.lower()
    s = unicodedata.normalize("NFKD", s).encode("ascii","ignore").decode("utf-8","ignore")
    s = re.sub(r"<[^>]+>", " ", s)          # quita HTML
    s = re.sub(r"\s+", " ", s).strip()
    return s

for colname in ["Title","Summary","Description","Suggested Search Terms"]:
    if colname not in df.columns: df[colname] = ""
    df[colname] = df[colname].fillna("").apply(norm)

df["text"] = (df["Title"] + " " + df["Summary"] + " " + df["Description"]).str.strip()
df["n_words"] = df["text"].str.split().apply(len)
df = df[df["n_words"] >= 3].copy()  # quita filas sin señal

# --- 4) ETIQUETAS DÉBILES (si no hay label) ---
if "label" not in df.columns:
    df["label"] = np.nan
else:
    df["label"] = df["label"].fillna("").apply(norm).replace({"": np.nan})

def weak_label(terms: str):
    t = " " + (terms or "") + " "
    if any(k in t for k in ["install", "setup", "factory reset"]): return "Instalacion"
    if any(k in t for k in ["config", "parameter", "calibration", "settings", "io signals"]): return "Configuracion"
    if any(k in t for k in ["error", "code", "failed", "crash", "401", "firmware", "system update"]): return "Errores_Codigos"
    if any(k in t for k in ["troubleshooting", "diagnostic", "spec process", "console mode"]): return "Troubleshooting"
    if any(k in t for k in ["network", "ftp", "api", "integration", "zoc terminal", "rtc update"]): return "Integracion_Red"
    if any(k in t for k in ["license", "licensing", "activation"]): return "Licenciamiento"
    if any(k in t for k in ["hold mode", "batching", "operation", "start/stop"]): return "Operacion"
    return np.nan

mask = df["label"].isna()
df.loc[mask, "label"] = df.loc[mask, "Suggested Search Terms"].apply(weak_label)

# --- 5) ENTRENAR CLASIFICADOR (si hay suficientes etiquetas) ---
train_df = df.dropna(subset=["label"]).copy()

if len(train_df) >= 40 and train_df["label"].nunique() >= 2:
    vec = TfidfVectorizer(ngram_range=(1,2), min_df=2, max_df=0.95, sublinear_tf=True)
    clf = LinearSVC()
    pipe = Pipeline([("tfidf", vec), ("clf", clf)])

    X_tr, X_te, y_tr, y_te = train_test_split(
        train_df["text"], train_df["label"], test_size=0.2, stratify=train_df["label"], random_state=42
    )
    pipe.fit(X_tr, y_tr)

    print("\n== Reporte de validación ==")
    print(classification_report(y_te, pipe.predict(X_te)))
    joblib.dump(pipe, os.path.join(out_dir, "kb_classifier.joblib"))

    # Predice TODO y exporta para revisión
    preds = pipe.predict(df["text"])
    decision = pipe.decision_function(df["text"])
    conf = decision.max(axis=1) if decision.ndim == 2 else np.abs(decision)

    df["pred_label"] = preds
    df["confidence"] = conf

    out_path = os.path.join(out_dir, "predicciones_para_revision.csv")
    df.sort_values("confidence").to_csv(out_path, index=False)
    print(f"\nGuardado: {out_path}")
else:
    # Si no hay suficientes etiquetas, exporta un muestreo para que etiquetes rápido (active learning v0)
    seed_path = os.path.join(out_dir, "muestra_para_etiquetar.csv")
    sample = df.sample(n=min(200, len(df)), random_state=42)[["Title","Summary","Description","Suggested Search Terms"]]
    sample.to_csv(seed_path, index=False)
    print("\nNo hay suficientes etiquetas para entrenar.")
    print(f"Se creó una muestra para etiquetar manualmente: {seed_path}")
    print("Llena la columna 'label' (Instalacion, Configuracion, Operacion, Troubleshooting, Errores_Codigos, Integracion_Red, Licenciamiento) y vuelve a ejecutar el script.")
