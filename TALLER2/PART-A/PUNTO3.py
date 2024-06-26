
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import numpy as np
import matplotlib.pyplot as plt

class Ui_Python3(object):
    def setupUi(self, Python3):
        Python3.setObjectName("Python3")
        Python3.resize(471, 317)
        self.label_2 = QtWidgets.QLabel(Python3)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Python3)
        self.label_4.setGeometry(QtCore.QRect(10, 90, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_8 = QtWidgets.QLabel(Python3)
        self.label_8.setGeometry(QtCore.QRect(270, 20, 131, 81))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("TALLER2\IMAGENES\ecci.jpg"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label = QtWidgets.QLabel(Python3)
        self.label.setGeometry(QtCore.QRect(10, 10, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Python3)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(Python3)
        self.label_7.setGeometry(QtCore.QRect(10, 30, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.comboBox = QtWidgets.QComboBox(Python3)
        self.comboBox.setGeometry(QtCore.QRect(10, 120, 181, 22))
        self.comboBox.setObjectName("comboBox")
        self.create_function_selector()
        self.comboBox.currentIndexChanged.connect(self.upd_robot)
        
        self.graphicsView = QtWidgets.QGraphicsView(Python3)
        self.graphicsView.setGeometry(QtCore.QRect(210, 110, 256, 192))
        self.graphicsView.setObjectName("graphicsView")
        self.scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        
        
        
        self.texto1 = QtWidgets.QLabel(Python3)
        self.texto1.setGeometry(QtCore.QRect(10, 160, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.texto1.setFont(font)
        self.texto1.setText("")
        self.texto1.setObjectName("texto1")
        self.texto2 = QtWidgets.QLabel(Python3)
        self.texto2.setGeometry(QtCore.QRect(10, 190, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.texto2.setFont(font)
        self.texto2.setText("")
        self.texto2.setObjectName("texto2")
        self.texto3 = QtWidgets.QLabel(Python3)
        self.texto3.setGeometry(QtCore.QRect(10, 220, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.texto3.setFont(font)
        self.texto3.setText("")
        self.texto3.setObjectName("texto3")

        self.retranslateUi(Python3)
        QtCore.QMetaObject.connectSlotsByName(Python3)

    def create_function_selector(self):
        self.comboBox.addItems(["Robot Cartesiano", "Robot Esférico", "Robot Cilíndrico"])

    def upd_robot(self):
        # Obtener los valores ingresados
        function_index = self.comboBox.currentIndex()
        # Crear datos para graficar
        
        if function_index == 0:  # Robot Cartesiano
            self.texto1.setText("3 articulaciones")
            self.texto2.setText("   3 Prismáticas")
            self.texto3.setText("   ")
            # Carga y muestra el diagrama cinemático del robot cartesiano
            pixmap = QtGui.QPixmap("TALLER2\IMAGENES\ROBOTCARTESIANO.jpg")
            self.scene.clear()
            self.scene.addPixmap(pixmap)
        elif function_index == 1:  # Robot Esférico
            self.texto1.setText("3 articulaciones")
            self.texto2.setText("   2 Rotacionales")
            self.texto3.setText("   1 Prismática")
            # Carga y muestra el diagrama cinemático del robot cartesiano
            pixmap = QtGui.QPixmap("TALLER2\IMAGENES\ROBOTESFERICO.jpg")
            self.scene.clear()
            self.scene.addPixmap(pixmap)
        elif function_index == 2:  # Robot Cilíndrico
            self.texto1.setText("3 articulaciones")
            self.texto2.setText("   1 Rotacional")
            self.texto3.setText("   2 Prismáticas")
            # Carga y muestra el diagrama cinemático del robot cartesiano
            pixmap = QtGui.QPixmap("TALLER2\IMAGENES\ROBOTCILINDRICO.jpg")
            self.scene.clear()
            self.scene.addPixmap(pixmap)
    

    def retranslateUi(self, Python3):
        _translate = QtCore.QCoreApplication.translate
        Python3.setWindowTitle(_translate("Python3", "Python3"))
        self.label_2.setText(_translate("Python3", "Nicolas Mejia Muñoz"))
        self.label_4.setText(_translate("Python3", "2024 - 1"))
        self.label.setText(_translate("Python3", "Algoritmos de Robótica "))
        self.label_3.setText(_translate("Python3", "Andrés Felipe Romero Medina"))
        self.label_7.setText(_translate("Python3", "Ingeniería Mecatrónica"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Python3 = QtWidgets.QDialog()
    ui = Ui_Python3()
    ui.setupUi(Python3)
    Python3.show()
    sys.exit(app.exec_())
