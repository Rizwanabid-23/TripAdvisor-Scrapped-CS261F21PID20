
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_filterWindow(object):
    def setupUi(self, filterWindow):
        filterWindow.setObjectName("filterWindow")
        filterWindow.resize(260, 241)
        self.centralwidget = QtWidgets.QWidget(filterWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 150, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(40, 40, 141, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 110, 141, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        filterWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(filterWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 260, 21))
        self.menubar.setObjectName("menubar")
        filterWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(filterWindow)
        self.statusbar.setObjectName("statusbar")
        filterWindow.setStatusBar(self.statusbar)

        self.retranslateUi(filterWindow)
        QtCore.QMetaObject.connectSlotsByName(filterWindow)

    def retranslateUi(self, filterWindow):
        _translate = QtCore.QCoreApplication.translate
        filterWindow.setWindowTitle(_translate("filterWindow", "MainWindow"))
        self.label.setText(_translate("filterWindow", "Show items starting with:"))
        self.label_2.setText(_translate("filterWindow", "Show items ending  with:"))
        self.pushButton.setText(_translate("filterWindow", "Search"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    filterWindow = QtWidgets.QMainWindow()
    ui = Ui_filterWindow()
    ui.setupUi(filterWindow)
    filterWindow.show()
    sys.exit(app.exec_())
