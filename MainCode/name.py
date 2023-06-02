from PyQt5 import QtCore, QtGui, QtWidgets
import face_dataset


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(493, 180)
        Form.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.inp_name = QtWidgets.QLabel(Form)
        self.inp_name.setGeometry(QtCore.QRect(40, 50, 131, 31))
        self.inp_name.setStyleSheet("background-color: rgb(132, 132, 132);\n"
                                    "font: 12pt \"Times New Roman\";\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border-color: rgb(255, 255, 255);")
        self.inp_name.setAlignment(QtCore.Qt.AlignCenter)
        self.inp_name.setObjectName("inp_name")
        self.name_text = QtWidgets.QLineEdit(Form)
        self.name_text.setGeometry(QtCore.QRect(180, 50, 271, 31))
        self.name_text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                     "color: rgb(0, 0, 0);\n"
                                     "font: 12pt \"Times New Roman\";")
        self.name_text.setObjectName("name_text")

        self.Cont = QtWidgets.QPushButton(Form)
        self.Cont.setGeometry(QtCore.QRect(190, 110, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.Cont.setFont(font)
        self.Cont.setStyleSheet("color:rgb(255, 255, 255);\n"
                                "background-color: rgb(132, 132, 132)")
        self.Cont.setObjectName("Cont")

        self.Cont.clicked.connect(
            lambda: face_dataset.dataset(name=self.name_text.text()))
        self.Cont.clicked.connect(lambda: Form.close())

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.inp_name.setText(_translate("Form", "Enter Name:"))
        self.Cont.setText(_translate("Form", "Continue"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
