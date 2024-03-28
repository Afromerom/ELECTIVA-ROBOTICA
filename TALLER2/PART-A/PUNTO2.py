
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(495, 340)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.min = QtWidgets.QTextEdit(Dialog)
        self.min.setGeometry(QtCore.QRect(10, 150, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.min.setFont(font)
        self.min.setObjectName("min")
        self.max = QtWidgets.QTextEdit(Dialog)
        self.max.setGeometry(QtCore.QRect(110, 150, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.max.setFont(font)
        self.max.setObjectName("max")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 90, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 30, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(10, 200, 191, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setObjectName("comboBox")
        self.create_function_selector()
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(30, 120, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(130, 120, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(270, 10, 151, 81))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("TALLER2/IMAGENES/ecci.jpg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 50, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.grafica = QtWidgets.QPushButton(Dialog)
        self.grafica.setGeometry(QtCore.QRect(10, 250, 191, 31))
        self.grafica.setObjectName("grafica")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(210, 100, 281, 230))
        self.widget.setObjectName("widget")
        self.widget_layout = QtWidgets.QVBoxLayout(self.widget)  # Add a layout to the widget

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.grafica.clicked.connect(self.plot_graph)

    def create_function_selector(self):
        self.comboBox.addItems(["Seno", "Coseno", "Tangente", "Cotangente", "Secante", "Cosecante"])

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Andrés Felipe Romero Medina"))
        self.label_3.setText(_translate("Dialog", "Algoritmos de Robótica"))
        self.label_5.setText(_translate("Dialog", "2024-1"))
        self.label_4.setText(_translate("Dialog", "Ingeniería Mecatrónica"))
        self.label_7.setText(_translate("Dialog", "Minímo"))
        self.label_8.setText(_translate("Dialog", "Máximo"))
        self.label.setText(_translate("Dialog", "Nicolas Mejia Muñoz"))
        self.grafica.setText(_translate("Dialog", "Gráfica"))

    def plot_graph(self):
        function_index = self.comboBox.currentIndex()
        min_value = float(self.min.toPlainText())
        max_value = float(self.max.toPlainText())

        x = np.linspace(min_value, max_value, 1000)
        if function_index == 0:  # Seno
            y = np.sin(x)
        elif function_index == 1:  # Coseno
            y = np.cos(x)
        elif function_index == 2:  # Tangente
            y = np.tan(x)
        elif function_index == 3:  # Cotangente
            y = 1.0 / np.tan(x)
        elif function_index == 4:  # Secante
            y = 1.0 / np.cos(x)
        elif function_index == 5:  # Cosecante
            y = 1.0 / np.sin(x)

        fig = plt.figure()
        plt.plot(x, y)
        plt.grid(True)

        canvas = FigureCanvas(fig)

        # Clear existing layout
        for i in reversed(range(self.widget_layout.count())):
            widget = self.widget_layout.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

        # Add canvas to layout
        self.widget_layout.addWidget(canvas)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

