from PyQt5 import QtCore, QtGui, QtWidgets
import name
import face_train
import face_recog

class Ui_Main(object):
    def open_form(self):
        self.window = QtWidgets.QWidget()
        self.ui = name.Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(530, 339)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        Main.setFont(font)
        Main.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setObjectName("centralwidget")
        self.Label = QtWidgets.QLabel(self.centralwidget)
        self.Label.setGeometry(QtCore.QRect(120, 20, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        self.Label.setFont(font)
        self.Label.setStyleSheet("background-color: rgb(132, 132, 132);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        self.Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Label.setObjectName("Label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(50, 80, 181, 201))
        self.frame.setStyleSheet("background-color: rgb(132, 132, 132);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 161, 181))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/Users/KIIT/Desktop/astitva/images.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.Register_Face = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.open_form())
        self.Register_Face.setGeometry(QtCore.QRect(290, 130, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.Register_Face.setFont(font)
        self.Register_Face.setStyleSheet("background-color: rgb(132, 132, 132);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        self.Register_Face.setObjectName("Register_Face")
        self.Recognition = QtWidgets.QPushButton(self.centralwidget)
        self.Recognition.setGeometry(QtCore.QRect(290, 200, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.Recognition.setFont(font)
        self.Recognition.setStyleSheet("background-color: rgb(132, 132, 132);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        self.Recognition.setObjectName("Recognition")

        self.Recognition.clicked.connect(lambda:face_train.train())
        self.Recognition.clicked.connect(lambda:face_recog.face_recog())

        Main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 530, 22))
        self.menubar.setObjectName("menubar")
        Main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Main)
        self.statusbar.setObjectName("statusbar")
        Main.setStatusBar(self.statusbar)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "MainWindow"))
        self.Label.setText(_translate("Main", "Face Recognition"))
        self.Register_Face.setText(_translate("Main", "Register Face"))
        self.Recognition.setText(_translate("Main", "Recognition"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    ui = Ui_Main()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())
