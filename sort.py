
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_sortWindow(object):
    def setupUi(self, sortWindow):
        sortWindow.setObjectName("sortWindow")
        sortWindow.resize(308, 345)
        self.centralwidget = QtWidgets.QWidget(sortWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sort_alogrithms = QtWidgets.QComboBox(self.centralwidget)
        self.sort_alogrithms.setGeometry(QtCore.QRect(70, 10, 141, 22))
        self.sort_alogrithms.setObjectName("sort_alogrithms")
        self.sort_alogrithms.addItem("")
        self.sort_alogrithms.setItemText(0, "Sorting algorithms")
        self.sort_alogrithms.addItem("")
        self.sort_alogrithms.addItem("")
        self.sort_alogrithms.addItem("")
        self.sort_alogrithms.addItem("")
        self.sort_alogrithms.addItem("")
        self.sort_alogrithms.addItem("")
        self.sort_alogrithms.addItem("")
        self.sort_alogrithms.addItem("")
        self.sort_alogrithms.addItem("")
        self.sort_alogrithms.addItem("")
        self.sort_alogrithms.addItem("")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(70, 40, 141, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(90, 70, 70, 17))
        self.checkBox.setObjectName("checkBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(70, 150, 111, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 100, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 230, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(70, 190, 141, 21))
        self.lineEdit.setObjectName("lineEdit")
        sortWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(sortWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 308, 21))
        self.menubar.setObjectName("menubar")
        sortWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(sortWindow)
        self.statusbar.setObjectName("statusbar")
        sortWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.get_data)

        self.retranslateUi(sortWindow)
        QtCore.QMetaObject.connectSlotsByName(sortWindow)
    def get_data(self):
        x = self.sort_alogrithms.currentText()
        y = self.comboBox.currentText()


    def retranslateUi(self, sortWindow):
        _translate = QtCore.QCoreApplication.translate
        sortWindow.setWindowTitle(_translate("sortWindow", "MainWindow"))
        self.sort_alogrithms.setItemText(1, _translate("sortWindow", "Insertion Sort"))
        self.sort_alogrithms.setItemText(2, _translate("sortWindow", "Merge Sort"))
        self.sort_alogrithms.setItemText(3, _translate("sortWindow", "Selection Sort"))
        self.sort_alogrithms.setItemText(4, _translate("sortWindow", "Bubble Sort"))
        self.sort_alogrithms.setItemText(5, _translate("sortWindow", "Quick Sort"))
        self.sort_alogrithms.setItemText(6, _translate("sortWindow", "Counting Sort"))
        self.sort_alogrithms.setItemText(7, _translate("sortWindow", "Heap Sort"))
        self.sort_alogrithms.setItemText(8, _translate("sortWindow", "Cycle Sort"))
        self.sort_alogrithms.setItemText(9, _translate("sortWindow", "Radix Sort"))
        self.sort_alogrithms.setItemText(10, _translate("sortWindow", "Shell Sort"))
        self.sort_alogrithms.setItemText(11, _translate("sortWindow", "Bucket Sort"))
        self.comboBox.setItemText(0, _translate("sortWindow", "Ascend / Descend"))
        self.comboBox.setItemText(1, _translate("sortWindow", "Ascending"))
        self.comboBox.setItemText(2, _translate("sortWindow", "Descending"))
        self.checkBox.setText(_translate("sortWindow", "Multi sort"))
        self.comboBox_2.setItemText(0, _translate("sortWindow", "Searching algorithms"))
        self.comboBox_2.setItemText(1, _translate("sortWindow", "Linear Search"))
        self.comboBox_2.setItemText(2, _translate("sortWindow", "Binary Search"))
        self.comboBox_2.setItemText(3, _translate("sortWindow", "Jump Search"))
        self.pushButton.setText(_translate("sortWindow", "Sort"))
        self.pushButton_2.setText(_translate("sortWindow", "Search"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    sortWindow = QtWidgets.QMainWindow()
    ui = Ui_sortWindow()
    ui.setupUi(sortWindow)
    sortWindow.show()
    sys.exit(app.exec_())
