# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Pipe\Desktop\INTERFACES\PUNTO1.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(366, 320)
        self.Suma = QtWidgets.QPushButton(Dialog)
        self.Suma.setGeometry(QtCore.QRect(20, 190, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Suma.setFont(font)
        self.Suma.setObjectName("Suma")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 70, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 90, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.multipli = QtWidgets.QPushButton(Dialog)
        self.multipli.setGeometry(QtCore.QRect(20, 230, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.multipli.setFont(font)
        self.multipli.setObjectName("multipli")
        self.resta = QtWidgets.QPushButton(Dialog)
        self.resta.setGeometry(QtCore.QRect(90, 190, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.resta.setFont(font)
        self.resta.setObjectName("resta")
        self.div = QtWidgets.QPushButton(Dialog)
        self.div.setGeometry(QtCore.QRect(90, 230, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.div.setFont(font)
        self.div.setObjectName("div")
        self.sin = QtWidgets.QPushButton(Dialog)
        self.sin.setGeometry(QtCore.QRect(160, 190, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.sin.setFont(font)
        self.sin.setObjectName("sin")
        self.tan = QtWidgets.QPushButton(Dialog)
        self.tan.setGeometry(QtCore.QRect(230, 190, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.tan.setFont(font)
        self.tan.setObjectName("tan")
        self.sec = QtWidgets.QPushButton(Dialog)
        self.sec.setGeometry(QtCore.QRect(300, 190, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.sec.setFont(font)
        self.sec.setObjectName("sec")
        self.csec = QtWidgets.QPushButton(Dialog)
        self.csec.setGeometry(QtCore.QRect(300, 230, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.csec.setFont(font)
        self.csec.setObjectName("csec")
        self.cos = QtWidgets.QPushButton(Dialog)
        self.cos.setGeometry(QtCore.QRect(160, 230, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.cos.setFont(font)
        self.cos.setObjectName("cos")
        self.cot = QtWidgets.QPushButton(Dialog)
        self.cot.setGeometry(QtCore.QRect(230, 230, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.cot.setFont(font)
        self.cot.setObjectName("cot")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(110, 120, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.num1 = QtWidgets.QTextBrowser(Dialog)
        self.num1.setGeometry(QtCore.QRect(90, 140, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.num1.setFont(font)
        self.num1.setObjectName("num1")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(220, 120, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.num1_2 = QtWidgets.QTextBrowser(Dialog)
        self.num1_2.setGeometry(QtCore.QRect(200, 140, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.num1_2.setFont(font)
        self.num1_2.setObjectName("num1_2")
        self.respuesta = QtWidgets.QLabel(Dialog)
        self.respuesta.setGeometry(QtCore.QRect(80, 270, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.respuesta.setFont(font)
        self.respuesta.setText("")
        self.respuesta.setObjectName("respuesta")
        self.respuesta_2 = QtWidgets.QLabel(Dialog)
        self.respuesta_2.setGeometry(QtCore.QRect(80, 290, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.respuesta_2.setFont(font)
        self.respuesta_2.setText("")
        self.respuesta_2.setObjectName("respuesta_2")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(20, 30, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(220, 20, 141, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("border-image: url(:/newPrefix/ecci.jpg);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Python-1"))
        self.Suma.setText(_translate("Dialog", "+"))
        self.label.setText(_translate("Dialog", "Algoritmos de Robótica "))
        self.label_2.setText(_translate("Dialog", "Nicolas Mejia Muñoz"))
        self.label_3.setText(_translate("Dialog", "Andrés Felipe Romero Medina"))
        self.label_4.setText(_translate("Dialog", "2024 - 1"))
        self.multipli.setText(_translate("Dialog", "*"))
        self.resta.setText(_translate("Dialog", "-"))
        self.div.setText(_translate("Dialog", "/"))
        self.sin.setText(_translate("Dialog", "sin"))
        self.tan.setText(_translate("Dialog", "tan"))
        self.sec.setText(_translate("Dialog", "sec"))
        self.csec.setText(_translate("Dialog", "csec"))
        self.cos.setText(_translate("Dialog", "cos"))
        self.cot.setText(_translate("Dialog", "cot"))
        self.label_5.setText(_translate("Dialog", "Número 1"))
        self.label_6.setText(_translate("Dialog", "Número 2"))
        self.label_7.setText(_translate("Dialog", "Ingeniería Mecatrónica"))
import logo1_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
