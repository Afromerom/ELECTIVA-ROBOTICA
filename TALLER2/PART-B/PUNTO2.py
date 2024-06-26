import RPi.GPIO as GPIO
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 227)

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

        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(10, 30, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(240, 10, 151, 81))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("TALLER2/IMAGENES/ecci.jpg"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.ButtonLed1 = QtWidgets.QPushButton(Dialog)
        self.ButtonLed1.setGeometry(QtCore.QRect(20, 120, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.ButtonLed1.setFont(font)
        self.ButtonLed1.setObjectName("ButtonLed1")

        self.ButtonLed2 = QtWidgets.QPushButton(Dialog)
        self.ButtonLed2.setGeometry(QtCore.QRect(210, 120, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.ButtonLed2.setFont(font)
        self.ButtonLed2.setObjectName("ButtonLed2")

        self.SliderLED1 = QtWidgets.QSlider(Dialog)
        self.SliderLED1.setGeometry(QtCore.QRect(20, 180, 161, 22))
        self.SliderLED1.setOrientation(QtCore.Qt.Horizontal)
        self.SliderLED1.setObjectName("SliderLED1")

        self.SliderLED2 = QtWidgets.QSlider(Dialog)
        self.SliderLED2.setGeometry(QtCore.QRect(210, 180, 161, 22))
        self.SliderLED2.setOrientation(QtCore.Qt.Horizontal)
        self.SliderLED2.setObjectName("SliderLED2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # Connect to the GPIO pins
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(6, GPIO.OUT)  # LED1 on pin 6
        GPIO.setup(5, GPIO.OUT)  # LED2 on pin 5
        GPIO.setup(23, GPIO.OUT) # LED3 on pin 23
        GPIO.setup(24, GPIO.OUT) # LED4 on pin 24

        # PWM setup
        self.pwm_led1 = GPIO.PWM(6, 100)  # PWM on pin 6 at 100Hz
        self.pwm_led1.start(0)  # Start PWM with duty cycle 0
       
        self.pwm_led2 = GPIO.PWM(5, 100)  # PWM on pin 5 at 100Hz
        self.pwm_led2.start(0)  # Start PWM with duty cycle 0
       
        self.pwm_led3 = GPIO.PWM(23, 100)  # PWM on pin 23 at 100Hz
        self.pwm_led3.start(0)  # Start PWM with duty cycle 0
       
        self.pwm_led4 = GPIO.PWM(24, 100)  # PWM on pin 24 at 100Hz
        self.pwm_led4.start(0)  # Start PWM with duty cycle 0
       
        # Initial LED intensities
        self.led_intensity = 0
        self.led_intensity2 = 0

        # Connect signals and slots
        self.ButtonLed1.clicked.connect(self.changeColorBlue)
        self.ButtonLed1.clicked.connect(self.toggle_led1)
        self.SliderLED1.valueChanged.connect(self.change_intensity1)
       
        self.ButtonLed2.clicked.connect(self.changeColorOrange)
        self.ButtonLed2.clicked.connect(self.toggle_led2)
        self.SliderLED2.valueChanged.connect(self.change_intensity2)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Punto 2"))
        self.label_4.setText(_translate("Dialog", "2024 - 1"))
        self.label_7.setText(_translate("Dialog", "Ingeniería Mecatrónica"))
        self.label.setText(_translate("Dialog", "Algoritmos de Robótica "))
        self.label_3.setText(_translate("Dialog", "Andrés Felipe Romero Medina"))
        self.label_2.setText(_translate("Dialog", "Nicolas Mejia Muñoz"))
        self.ButtonLed1.setText(_translate("Dialog", "LED 1"))
        self.ButtonLed2.setText(_translate("Dialog", "LED 2"))

    def changeColorBlue(self):
        if GPIO.input(6) == GPIO.LOW:
            self.ButtonLed1.setStyleSheet("color: orange")
        else:
            self.ButtonLed1.setStyleSheet("color: black")

    def changeColorOrange(self):
        if GPIO.input(5) == GPIO.LOW:
            self.ButtonLed2.setStyleSheet("color: blue")
        else:
            self.ButtonLed2.setStyleSheet("color: black")

    def toggle_led1(self):
        if self.led_intensity == 0:
            self.led_intensity = 100
        else:
            self.led_intensity = 0
        self.pwm_led1.ChangeDutyCycle(self.led_intensity)
           
    def toggle_led2(self):
        if self.led_intensity2 == 0:
            self.led_intensity2 = 100
        else:
            self.led_intensity2 = 0
        self.pwm_led2.ChangeDutyCycle(self.led_intensity2)

    def change_intensity1(self, value):
        self.led_intensity = value
        self.pwm_led3.ChangeDutyCycle(self.led_intensity)
   
    def change_intensity2(self, value):
        self.led_intensity2 = value
        self.pwm_led4.ChangeDutyCycle(self.led_intensity2)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())