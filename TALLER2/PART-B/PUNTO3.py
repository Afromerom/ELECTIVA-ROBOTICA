from PyQt5 import QtCore, QtGui, QtWidgets
import RPi.GPIO as GPIO
import time
import threading

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 264)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(240, 10, 151, 81))
        self.label_8.setPixmap(QtGui.QPixmap("TALLER2/IMAGENES/ecci.jpg"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(10, 30, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 90, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 110, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 130, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.Tiemposec = QtWidgets.QTextEdit(Dialog)
        self.Tiemposec.setGeometry(QtCore.QRect(210, 110, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.Tiemposec.setFont(font)
        self.Tiemposec.setObjectName("Tiemposec")
        self.Inicio = QtWidgets.QPushButton(Dialog)
        self.Inicio.setGeometry(QtCore.QRect(210, 160, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.Inicio.setFont(font)
        self.Inicio.setObjectName("Inicio")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(160, 170, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.Tiempot = QtWidgets.QLabel(Dialog)
        self.Tiempot.setGeometry(QtCore.QRect(30, 170, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.Tiempot.setFont(font)
        self.Tiempot.setText("")
        self.Tiempot.setObjectName("Tiempot")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(250, 220, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.Tiempot_2 = QtWidgets.QLabel(Dialog)
        self.Tiempot_2.setGeometry(QtCore.QRect(120, 220, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.Tiempot_2.setFont(font)
        self.Tiempot_2.setText("")
        self.Tiempot_2.setObjectName("Tiempot_2")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(40, 220, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.Inicio.clicked.connect(self.start_countdown)  # Conecta el clic del botón a la función de cuenta regresiva

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Punto 3"))
        self.label.setText(_translate("Dialog", "Algoritmos de Robótica "))
        self.label_3.setText(_translate("Dialog", "Andrés Felipe Romero Medina"))
        self.label_7.setText(_translate("Dialog", "Ingeniería Mecatrónica"))
        self.label_2.setText(_translate("Dialog", "Nicolas Mejia Muñoz"))
        self.label_4.setText(_translate("Dialog", "2024 - 1"))
        self.label_5.setText(_translate("Dialog", "Ingrese por cuantos segundos "))
        self.label_6.setText(_translate("Dialog", "desea la toma de la lectura "))
        self.Inicio.setText(_translate("Dialog", "START"))
        self.label_9.setText(_translate("Dialog", "s"))
        self.label_10.setText(_translate("Dialog", "cm"))
        self.label_11.setText(_translate("Dialog", "Lectura: "))

    def start_countdown(self):
        seconds = int(self.Tiemposec.toPlainText())  # Obtiene los segundos ingresados
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Inicia el temporizador con una frecuencia de actualización de 1 segundo
        self.remaining_seconds = seconds
        self.start_sensor_reading()

    def update_time(self):
        self.remaining_seconds -= 1
        if self.remaining_seconds >= 0:
            self.Tiempot.setText(str(self.remaining_seconds))
        else:
            self.timer.stop()
            self.Tiempot.setText("Fin")

    def start_sensor_reading(self):
        self.sensor_thread = threading.Thread(target=self.continuously_read_sensor)
        self.sensor_thread.daemon = True
        self.sensor_thread.start()

    def continuously_read_sensor(self):
        try:
            while self.remaining_seconds > 0:
                dist = self.read_sensor()
                self.Tiempot_2.setText(str(dist))
                time.sleep(1)  # Leer cada segundo mientras el temporizador esté en marcha
        except Exception as e:
            print("Error reading sensor:", e)

    def read_sensor(self):
        TRIG = 3
        ECHO = 2
       
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(TRIG, GPIO.OUT)
        GPIO.setup(ECHO, GPIO.IN)

        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        pulse_start = time.time()
        pulse_end = time.time()

        while GPIO.input(ECHO)==0:
            pulse_start = time.time()

        while GPIO.input(ECHO)==1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 34000
        distance = round(distance, 2)

        return distance

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())