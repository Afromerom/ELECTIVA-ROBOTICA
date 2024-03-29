import RPi.GPIO as GPIO
import time
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 155)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(10, 30, 191, 21))
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
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(240, 10, 151, 81))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("TALLER2/IMAGENES/ecci.jpg"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
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
        self.label_5.setGeometry(QtCore.QRect(50, 120, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.estado = QtWidgets.QLabel(Dialog)
        self.estado.setGeometry(QtCore.QRect(260, 110, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.estado.setFont(font)
        self.estado.setObjectName("estado")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # Configurar el modo de los pines
        GPIO.setmode(GPIO.BCM)

        # Definir el pin de entrada
        self.pin_entrada = 19

        # Configurar el pin de entrada como una entrada
        GPIO.setup(self.pin_entrada, GPIO.IN)

        # Iniciar el hilo para leer el estado del GPIO
        self.read_gpio_thread = QtCore.QThread()
        self.worker = GpioReader(self.pin_entrada)
        self.worker.moveToThread(self.read_gpio_thread)
        self.read_gpio_thread.started.connect(self.worker.read_gpio)
        self.worker.state_changed.connect(self.update_estado_label)
        self.read_gpio_thread.start()

    def update_estado_label(self, estado):
        if estado == GPIO.HIGH:
            self.estado.setText("<font color='red'>ALTO</font>")
        else:
            self.estado.setText("<font color='blue'>BAJO</font>")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Punto 4"))
        self.label_3.setText(_translate("Dialog", "Andrés Felipe Romero Medina"))
        self.label.setText(_translate("Dialog", "Algoritmos de Robótica "))
        self.label_7.setText(_translate("Dialog", "Ingeniería Mecatrónica"))
        self.label_2.setText(_translate("Dialog", "Nicolas Mejia Muñoz"))
        self.label_4.setText(_translate("Dialog", "2024 - 1"))
        self.label_5.setText(_translate("Dialog", "Estado de la entrada"))

class GpioReader(QtCore.QObject):
    state_changed = QtCore.pyqtSignal(int)

    def __init__(self, pin):
        super().__init__()
        self.pin = pin

    @QtCore.pyqtSlot()
    def read_gpio(self):
        try:
            while True:
                # Leer el estado del pin de entrada
                estado = GPIO.input(self.pin)
                self.state_changed.emit(estado)
                # Esperar un tiempo antes de volver a leer el estado
                time.sleep(0.1)

        except KeyboardInterrupt:
            # Limpiar los pines GPIO
            GPIO.cleanup()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())