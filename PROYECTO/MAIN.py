

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(634, 566)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(220, 10, 181, 101))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("PROYECTO\IMAGENES\ecci.jpg"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 90, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
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
        self.label_7.setGeometry(QtCore.QRect(10, 30, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.servo1 = QtWidgets.QSlider(Dialog)
        self.servo1.setGeometry(QtCore.QRect(80, 190, 171, 22))
        self.servo1.setOrientation(QtCore.Qt.Horizontal)
        self.servo1.setObjectName("servo1")
        self.valor1 = QtWidgets.QLabel(Dialog)
        self.valor1.setGeometry(QtCore.QRect(270, 190, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.valor1.setFont(font)
        self.valor1.setText("")
        self.valor1.setObjectName("valor1")
        self.servo1_2 = QtWidgets.QSlider(Dialog)
        self.servo1_2.setGeometry(QtCore.QRect(80, 220, 171, 22))
        self.servo1_2.setOrientation(QtCore.Qt.Horizontal)
        self.servo1_2.setObjectName("servo1_2")
        self.valor1_2 = QtWidgets.QLabel(Dialog)
        self.valor1_2.setGeometry(QtCore.QRect(270, 220, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.valor1_2.setFont(font)
        self.valor1_2.setText("")
        self.valor1_2.setObjectName("valor1_2")
        self.servo1_3 = QtWidgets.QSlider(Dialog)
        self.servo1_3.setGeometry(QtCore.QRect(80, 250, 171, 22))
        self.servo1_3.setOrientation(QtCore.Qt.Horizontal)
        self.servo1_3.setObjectName("servo1_3")
        self.valor1_3 = QtWidgets.QLabel(Dialog)
        self.valor1_3.setGeometry(QtCore.QRect(270, 250, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.valor1_3.setFont(font)
        self.valor1_3.setText("")
        self.valor1_3.setObjectName("valor1_3")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 140, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 190, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(20, 220, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(20, 250, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(20, 290, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.PICK_D = QtWidgets.QPushButton(Dialog)
        self.PICK_D.setGeometry(QtCore.QRect(120, 290, 71, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PICK_D.setFont(font)
        self.PICK_D.setObjectName("PICK_D")
        self.PLACE_D = QtWidgets.QPushButton(Dialog)
        self.PLACE_D.setGeometry(QtCore.QRect(200, 290, 71, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PLACE_D.setFont(font)
        self.PLACE_D.setObjectName("PLACE_D")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(320, 150, 22, 181))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.line.setFont(font)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(10, 320, 321, 31))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(350, 130, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(360, 190, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(360, 230, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(360, 270, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(360, 140, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(Dialog)
        self.label_17.setGeometry(QtCore.QRect(10, 130, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.GO_D = QtWidgets.QPushButton(Dialog)
        self.GO_D.setGeometry(QtCore.QRect(430, 300, 71, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.GO_D.setFont(font)
        self.GO_D.setObjectName("GO_D")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(350, 320, 241, 31))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_18 = QtWidgets.QLabel(Dialog)
        self.label_18.setGeometry(QtCore.QRect(10, 340, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(Dialog)
        self.label_19.setGeometry(QtCore.QRect(30, 350, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.START_D = QtWidgets.QPushButton(Dialog)
        self.START_D.setGeometry(QtCore.QRect(90, 390, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.START_D.setFont(font)
        self.START_D.setObjectName("START_D")
        self.line_4 = QtWidgets.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(10, 420, 321, 31))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(Dialog)
        self.line_5.setGeometry(QtCore.QRect(320, 340, 22, 81))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.line_5.setFont(font)
        self.line_5.setLineWidth(1)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.DISP = QtWidgets.QWidget(Dialog)
        self.DISP.setGeometry(QtCore.QRect(350, 340, 271, 211))
        self.DISP.setObjectName("DISP")
        self.POS_X = QtWidgets.QTextEdit(Dialog)
        self.POS_X.setGeometry(QtCore.QRect(470, 180, 111, 31))
        self.POS_X.setObjectName("POS_X")
        self.POS_Y = QtWidgets.QTextEdit(Dialog)
        self.POS_Y.setGeometry(QtCore.QRect(470, 220, 111, 31))
        self.POS_Y.setObjectName("POS_Y")
        self.POS_Z = QtWidgets.QTextEdit(Dialog)
        self.POS_Z.setGeometry(QtCore.QRect(470, 260, 111, 31))
        self.POS_Z.setObjectName("POS_Z")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "PROYECTO"))
        self.label_3.setText(_translate("Dialog", "Andrés Felipe Romero Medina"))
        self.label_4.setText(_translate("Dialog", "2024 - 1"))
        self.label_2.setText(_translate("Dialog", "Nicolas Mejia Muñoz"))
        self.label.setText(_translate("Dialog", "Algoritmos de Robótica "))
        self.label_7.setText(_translate("Dialog", "Ingeniería Mecatrónica"))
        self.label_5.setText(_translate("Dialog", "MANUAL"))
        self.label_6.setText(_translate("Dialog", "ART 1"))
        self.label_9.setText(_translate("Dialog", "ART 2"))
        self.label_10.setText(_translate("Dialog", "ART 3"))
        self.label_11.setText(_translate("Dialog", "Gripper →"))
        self.PICK_D.setText(_translate("Dialog", "PICK"))
        self.PLACE_D.setText(_translate("Dialog", "PLACE"))
        self.label_12.setText(_translate("Dialog", "MODO: "))
        self.label_13.setText(_translate("Dialog", "POSICIÓN X"))
        self.label_14.setText(_translate("Dialog", "POSICIÓN Y"))
        self.label_15.setText(_translate("Dialog", "POSICIÓN Z"))
        self.label_16.setText(_translate("Dialog", "SEMI - AUTOMÁTICO"))
        self.label_17.setText(_translate("Dialog", "MODO: "))
        self.GO_D.setText(_translate("Dialog", "GO!"))
        self.label_18.setText(_translate("Dialog", "MODO: "))
        self.label_19.setText(_translate("Dialog", "AUTOMÁTICO"))
        self.START_D.setText(_translate("Dialog", "START!"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
