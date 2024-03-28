from PyQt5 import QtCore, QtGui, QtWidgets
import RPi.GPIO as GPIO
import time

class Ui_Punto1(object):
    def setupUi(self, Punto1):
        Punto1.setObjectName("Punto1")
        Punto1.resize(400, 249)
        self.label_8 = QtWidgets.QLabel(Punto1)
        self.label_8.setGeometry(QtCore.QRect(240, 10, 151, 81))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("TALLER2\IMAGENES\ecci.jpg"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label = QtWidgets.QLabel(Punto1)
        self.label.setGeometry(QtCore.QRect(10, 10, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_7 = QtWidgets.QLabel(Punto1)
        self.label_7.setGeometry(QtCore.QRect(10, 30, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_4 = QtWidgets.QLabel(Punto1)
        self.label_4.setGeometry(QtCore.QRect(10, 90, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(Punto1)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Punto1)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(Punto1)
        self.textEdit.setGeometry(QtCore.QRect(220, 120, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.label_5 = QtWidgets.QLabel(Punto1)
        self.label_5.setGeometry(QtCore.QRect(10, 120, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Punto1)
        self.label_6.setGeometry(QtCore.QRect(10, 140, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.servo1 = QtWidgets.QSlider(Punto1)
        self.servo1.setGeometry(QtCore.QRect(120, 180, 201, 22))
        self.servo1.setOrientation(QtCore.Qt.Horizontal)
        self.servo1.setObjectName("servo1")
        self.servo1.setMinimum(0)  # Establecer mínimo en 0
        self.servo1.setMaximum(180)  # Establecer máximo en 180
        self.servo1.valueChanged.connect(self.controlar_servo1)
        self.servo1.setEnabled(False)  # Deshabilitado inicialmente
        self.servo2 = QtWidgets.QSlider(Punto1)
        self.servo2.setGeometry(QtCore.QRect(120, 210, 201, 22))
        self.servo2.setOrientation(QtCore.Qt.Horizontal)
        self.servo2.setObjectName("servo2")
        self.servo2.setMinimum(0)  # Establecer mínimo en 0
        self.servo2.setMaximum(180)  # Establecer máximo en 180
        self.servo2.valueChanged.connect(self.controlar_servo2)
        self.servo2.setEnabled(False)  # Deshabilitado inicialmente
        self.valor1 = QtWidgets.QLabel(Punto1)
        self.valor1.setGeometry(QtCore.QRect(330, 180, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.valor1.setFont(font)
        self.valor1.setText("")
        self.valor1.setObjectName("valor1")
        self.valor2 = QtWidgets.QLabel(Punto1)
        self.valor2.setGeometry(QtCore.QRect(330, 210, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.valor2.setFont(font)
        self.valor2.setText("")
        self.valor2.setObjectName("valor2")
        self.label_9 = QtWidgets.QLabel(Punto1)
        self.label_9.setGeometry(QtCore.QRect(30, 180, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Punto1)
        self.label_10.setGeometry(QtCore.QRect(30, 210, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")

        self.retranslateUi(Punto1)
        QtCore.QMetaObject.connectSlotsByName(Punto1)
        
        # Set GPIO numbering mode
        GPIO.setmode(GPIO.BOARD)

        # Set pin 11 as an output, and define as servo1 as PWM pin
        GPIO.setup(11, GPIO.OUT)
        self.servomotor1 = GPIO.PWM(11, 50)  # pin 11 for servo1, pulse 50Hz

        # Start PWM running, with value of 0 (pulse off)
        self.servomotor1.start(0)

    def retranslateUi(self, Punto1):
        _translate = QtCore.QCoreApplication.translate
        Punto1.setWindowTitle(_translate("Punto1", "PUNTO1"))
        self.label.setText(_translate("Punto1", "Algoritmos de Robótica "))
        self.label_7.setText(_translate("Punto1", "Ingeniería Mecatrónica"))
        self.label_4.setText(_translate("Punto1", "2024 - 1"))
        self.label_2.setText(_translate("Punto1", "Nicolas Mejia Muñoz"))
        self.label_3.setText(_translate("Punto1", "Andrés Felipe Romero Medina"))
        self.label_5.setText(_translate("Punto1", "Ingrese el número del servomotor "))
        self.label_6.setText(_translate("Punto1", "que desea manipular: "))
        self.label_9.setText(_translate("Punto1", "Servo 1"))
        self.label_10.setText(_translate("Punto1", "Servo 2"))

    def controlar_servo1(self, value):
        angle = value
        self.servomotor1.ChangeDutyCycle(2 + (angle / 18))
        time.sleep(0.5)
        self.servomotor1.ChangeDutyCycle(0)

    def controlar_servo2(self, value):
        pass  # Implementa el control del segundo servo aquí

    def verificar_texto(self):
        texto = self.textEdit.toPlainText()
        if texto == "1":
            self.servo1.setEnabled(True)
            self.servo2.setEnabled(False)
        else:
            self.servo1.setEnabled(False)
            self.servo2.setEnabled(False)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Punto1 = QtWidgets.QDialog()
    ui = Ui_Punto1()
    ui.setupUi(Punto1)
    ui.textEdit.textChanged.connect(ui.verificar_texto)
    Punto1.show()
    sys.exit(app.exec_())
