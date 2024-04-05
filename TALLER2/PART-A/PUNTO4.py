
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
import matplotlib.pyplot as plt

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(930, 692)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
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
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(260, 10, 131, 81))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("TALLER2\IMAGENES\ecci.jpg"))
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
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(10, 30, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalSlider1 = QtWidgets.QSlider(Dialog)
        self.horizontalSlider1.setGeometry(QtCore.QRect(140, 590, 731, 22))
        self.horizontalSlider1.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider1.setObjectName("horizontalSlider1")
        self.horizontalSlider1.valueChanged.connect(self.actualizar_valor_resistencia)
        self.horizontalSlider_2 = QtWidgets.QSlider(Dialog)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(140, 620, 731, 22))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalSlider_2.valueChanged.connect(self.actualizar_valor_capacitancia)
        self.horizontalSlider_3 = QtWidgets.QSlider(Dialog)
        self.horizontalSlider_3.setGeometry(QtCore.QRect(140, 650, 731, 22))
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.horizontalSlider_3.valueChanged.connect(self.actualizar_valor_voltaje)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 590, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(30, 620, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(30, 650, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 120, 861, 451))
        self.widget.setObjectName("widget")
        self.resistenciavalor = QtWidgets.QLabel(Dialog)
        self.resistenciavalor.setGeometry(QtCore.QRect(880, 590, 47, 13))
        self.resistenciavalor.setText("")
        self.resistenciavalor.setObjectName("resistenciavalor")
        self.capacitorvalor = QtWidgets.QLabel(Dialog)
        self.capacitorvalor.setGeometry(QtCore.QRect(870, 620, 61, 20))
        self.capacitorvalor.setText("")
        self.capacitorvalor.setObjectName("capacitorvalor")
        self.voltajevalor = QtWidgets.QLabel(Dialog)
        self.voltajevalor.setGeometry(QtCore.QRect(880, 650, 61, 20))
        self.voltajevalor.setText("")
        self.voltajevalor.setObjectName("voltajevalor")
        
        #Mostrarlo
        self.widgetLayout = QtWidgets.QVBoxLayout(self.widget)
        self.figure = plt.figure() 
        self.canvas = FigureCanvas(self.figure)
        self.widgetLayout.addWidget(self.canvas)    
        
        self.horizontalSlider1.valueChanged.connect(self.update_plot)
        self.horizontalSlider_2.valueChanged.connect(self.update_plot)
        self.horizontalSlider_3.valueChanged.connect(self.update_plot)   


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def actualizar_valor_resistencia(self, value):
        self.resistenciavalor.setText(str(value))
    
    def actualizar_valor_capacitancia(self, value):
        self.capacitorvalor.setText(str(value))
    
    def actualizar_valor_voltaje(self, value):
        self.voltajevalor.setText(str(value))
    
    
    def update_plot(self):
        resistencia = (self.horizontalSlider1.value())*1e3
        capacitancia = (self.horizontalSlider_2.value()) * 1e-6    
        voltaje = self.horizontalSlider_3.value()
        
        tiempo = np.linspace(0, 5 * resistencia * capacitancia, 1000)
        carga = voltaje * (1 - np.exp(-tiempo / (resistencia * capacitancia)))
        descarga = voltaje * np.exp(-tiempo / (resistencia * capacitancia))
        
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.plot(tiempo, carga, label="Carga")
        ax.plot(tiempo, descarga, label="Descarga")
        ax.set_xlabel("Tiempo")
        ax.set_ylabel("Voltaje")
        ax.legend()  # Agregar los paréntesis aquí para llamar a la función      
        ax.grid(True)  
        self.canvas.draw()


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Python4"))
        self.label_3.setText(_translate("Dialog", "Andrés Felipe Romero Medina"))
        self.label_4.setText(_translate("Dialog", "2024 - 1"))
        self.label_2.setText(_translate("Dialog", "Nicolas Mejia Muñoz"))
        self.label.setText(_translate("Dialog", "Algoritmos de Robótica "))
        self.label_7.setText(_translate("Dialog", "Ingeniería Mecatrónica"))
        self.label_5.setText(_translate("Dialog", "Resistencia (Ω)"))
        self.label_6.setText(_translate("Dialog", "Capacitancia (µF)"))
        self.label_9.setText(_translate("Dialog", "Voltaje (V)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
