import sys
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtGui import QPixmap, QImage


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(391, 458)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 30, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 90, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 50, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(210, 10, 151, 81))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("TALLER2\IMAGENES\ecci.jpg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 120, 371, 31))
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 160, 371, 281))
        self.widget.setObjectName("widget")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # Conectar la señal del botón a la función select_image
        self.pushButton.clicked.connect(self.select_image)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "PUNTO5"))
        self.label_4.setText(_translate("Dialog", "Ingeniería Mecatrónica"))
        self.label_5.setText(_translate("Dialog", "2024-1"))
        self.label_3.setText(_translate("Dialog", "Algoritmos de Robótica"))
        self.label.setText(_translate("Dialog", "Nicolas Mejia Muñoz"))
        self.label_2.setText(_translate("Dialog", "Andrés Felipe Romero Medina"))
        self.pushButton.setText(_translate("Dialog", "Buscar Imagen"))

    def select_image(self):
        file_dialog = QtWidgets.QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(None, "Seleccionar imagen", "", "Image Files (*.png *.jpg *.bmp)")
        if file_path:
            image = cv2.imread(file_path)
            contours = self.find_contours(image)
            self.display_image(image, contours)

    def find_contours(self, image):
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, threshold = cv2.threshold(gray_image, 240, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        return contours

    def display_image(self, image, contours):
        cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

        # Convertir la imagen de OpenCV a QPixmap para mostrarla en el widget
        height, width, channel = image.shape
        bytes_per_line = 3 * width
        q_img = QImage(image.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        pixmap = QPixmap(q_img)

        # Crear una etiqueta y establecer la imagen en el widget
        label = QLabel(self.widget)
        label.setPixmap(pixmap)
        label.setGeometry(0, 0, width, height)
        label.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
