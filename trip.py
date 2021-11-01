from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import csv
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QMainWindow, QApplication, QComboBox, QHBoxLayout, QPushButton, QProgressBar, QWidget
import selenium
from sort import Ui_sortWindow
from filter import Ui_filterWindow
stop_window = True
pause=False
class hotel:
    def __init__(self, name, price, reviews, rating, city, services, ranking):
        self.name = name
        self.price = price
        self.reviews = reviews
        self.rating = rating
        self.city = city
        self.services = services
        self.ranking = ranking
class WorkerThread(QThread):    
    def run(self):
            QApplication.processEvents()
            #driver = webdriver.Chrome(executable_path='C:\\Users\\rizwa\\Downloads\\chromedriver_win32\\chromedriver.exe')
            driver = webdriver.Chrome(executable_path='D:\\Driver\\chromedriver.exe')
            driver.get("https://www.tripadvisor.com/Hotels")
            content = driver.page_source
            soup = BeautifulSoup(content)
            categories = []
            categories_2 = []
            categories_3 = []
            array_list = []
            counter=0
            i = soup.find('div', attrs={'class': 'ppr_rup ppr_priv_popular_hotels'})
            j = i.find('ul', attrs={'class': 'flexCols'})
            for k in j.findAll('li', attrs={'class': 'item'}):
                get_category = k.find('a', attrs={'class': 'ui_link'})
                if (get_category):
                    get_href = get_category.get('href').replace("/Hotels-", "")
                    get_href_1 = get_href.rsplit("-", 2)[0]
                    get_href = get_href.replace(get_href_1, "")
                    get_href_2 = get_category.get('href').replace("/Hotels-", "")
                    get_href_2 = get_href_2.replace(get_href_1, "")
                    get_href_2 = get_href_2.replace("-Hotels.html", "")
                    get_href_2 = get_href_2.replace("-", "")
                    categories.append(get_href_1)
                    categories_2.append(get_href)
                    categories_3.append(get_href_2)
            while stop_window != False:
                for j in range(0, len(categories)):
                    k = 0
                    for i in range(1, 11):
                        driver.get("https://www.tripadvisor.com/Hotels-" + str(categories[j]) + "-oa" + str(k) + str(categories_2[j]))
                        k += 30
                        while pause==True:
                            counter+=1
                        city = categories_3[j]
                        content = driver.page_source
                        soup = BeautifulSoup(content)
                        for a in soup.findAll('div', attrs={'class': 'ui_column is-8 main_col allowEllipsis'}):
                            name = a.find('a', attrs={'class': 'property_title prominent'})
                            price = a.find('div', attrs={'class': 'price __resizeWatch'})
                            if price == None:
                                price = "PKR 22,000"
                            reviews = a.find('a', attrs={'class': 'review_count'})
                            if reviews == None:
                                reviews = "0"
                            rating = a.find('a', attrs={'class': 'ui_bubble_rating bubble_50'})
                            if rating == None:
                                rating = a.find('a', attrs={'class': 'ui_bubble_rating bubble_45'})
                                if rating == None:
                                    rating = a.find('a', attrs={'class': 'ui_bubble_rating bubble_40'})
                                    if rating == None:
                                        rating = a.find('a', attrs={'class': 'ui_bubble_rating bubble_35'})
                                        if rating == None:
                                            rating = a.find('a', attrs={'class': 'ui_bubble_rating bubble_30'})
                                            if rating == None:
                                                rating = a.find('a', attrs={'class': 'ui_bubble_rating bubble_25'})
                                                if rating == None:
                                                    rating = a.find('a', attrs={'class': 'ui_bubble_rating bubble_20'})
                                                    if rating == None:
                                                        rating = a.find('a', attrs={'class': 'ui_bubble_rating bubble_15'})
                                                        if rating == None:
                                                            rating = a.find('a', attrs={'class': 'ui_bubble_rating bubble_10'})
                            if rating == None:
                                rating = "0"
                            else:
                                rating = rating["alt"]
                                rating = rating.replace(' of 5 bubbles', '')
                            ranking = a.find('div', attrs={'class': 'popindex'})
                            if ranking == None:
                                ranking = "Not available"
                            services = a.find('div', attrs={'class': 'label'})
                            if services == None:
                                services = "Not available"
                            if hasattr(price, 'text'):
                                price = price.text
                            if hasattr(services, 'text'):
                                services = services.text
                            if hasattr(ranking, 'text'):
                                ranking = ranking.text
                            h = hotel(*name, price, city, rating,
                                    reviews.text, services, ranking)
                            array_list.append(h)        
                        if stop_window == False:
                            break
                    if stop_window == False:
                        break


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1005, 526)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 60, 741, 401))
        self.tableWidget.setMinimumSize(QtCore.QSize(711, 0))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 0, 131, 61))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(790, 340, 191, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(790, 410, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(770, 140, 61, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(850, 180, 61, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(850, 140, 61, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(770, 180, 61, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.ssButton = QtWidgets.QPushButton(self.centralwidget)
        self.ssButton.setGeometry(QtCore.QRect(40, 30, 21, 21))
        self.ssButton.setObjectName("ssButton")
        self.ssButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.ssButton_2.setGeometry(QtCore.QRect(150, 30, 21, 21))
        self.ssButton_2.setObjectName("ssButton_2")
        self.ssButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.ssButton_3.setGeometry(QtCore.QRect(240, 30, 21, 20))
        self.ssButton_3.setObjectName("ssButton_3")
        self.ssButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.ssButton_4.setGeometry(QtCore.QRect(326, 36, 20, 20))
        self.ssButton_4.setObjectName("ssButton_4")
        self.ssButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.ssButton_5.setGeometry(QtCore.QRect(460, 30, 21, 21))
        self.ssButton_5.setObjectName("ssButton_5")
        self.ssButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.ssButton_6.setGeometry(QtCore.QRect(530, 30, 21, 21))
        self.ssButton_6.setObjectName("ssButton_6")
        self.ssButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.ssButton_7.setGeometry(QtCore.QRect(630, 30, 20, 20))
        self.ssButton_7.setObjectName("ssButton_7")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(70, 30, 21, 21))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(270, 30, 21, 21))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(560, 30, 21, 21))
        self.pushButton_7.setObjectName("pushButton_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1005, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.clicker)
        self.pushButton_3.clicked.connect(self.break_window)
        self.pushButton_2.clicked.connect(self.pause_window)
        self.pushButton_4.clicked.connect(self.resume_window)
        self.pushButton_5.clicked.connect(self.searchWindow_1)
        self.pushButton_6.clicked.connect(self.searchWindow_1)
        self.pushButton_7.clicked.connect(self.searchWindow_1)
        self.ssButton.clicked.connect(self.sortedWindow_1)
        self.ssButton_2.clicked.connect(self.sortedWindow_1)
        self.ssButton_3.clicked.connect(self.sortedWindow_1)
        self.ssButton_4.clicked.connect(self.sortedWindow_1)
        self.ssButton_5.clicked.connect(self.sortedWindow_1)
        self.ssButton_6.clicked.connect(self.sortedWindow_1)
        self.ssButton_7.clicked.connect(self.sortedWindow_1)
        #self.prog_bar(0)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #def prog_bar(self,value):
        # self.bar = QProgressBar(self)
        #print(value)
        # self.bar.setObjectName("progressBar")
        # self.bar.setGeometry(790, 440, 191, 23)      
        # self.bar.setValue(value)
        # self.bar.show()
        #.p_bar.setObjectName("progressBar")
        #self.p_bar.setGeometry(790, 440, 191, 23)
        #self.p_bar.setValue(value)
        
        
    def clicker(self):
        global stop_window
        stop_window = True
        self.worker = WorkerThread()
        self.worker.start()
    def break_window(self):
        global stop_window
        stop_window = False
    def pause_window(self):
        global pause
        pause=True
    def resume_window(self):
        global pause
        pause=False
    def sortedWindow_1(self):
        self.sortWindow = QtWidgets.QMainWindow()
        self.ui = Ui_sortWindow()
        self.ui.setupUi(self.sortWindow)
        self.sortWindow.show()
    def searchWindow_1(self):
        self.filterWindow = QtWidgets.QMainWindow()
        self.ui = Ui_filterWindow()
        self.ui.setupUi(self.filterWindow)
        self.filterWindow.show()
    def getdata(self):
        data_array = []
        with open("C:\\Users\\Asad Mehmood\\Documents\\GitHub\\CS261F21PID20\\data.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                data_array.append(row)
        return data_array
    def loaddata(self,data_array):
        row = 0
        for i in data_array:
            data = [{"Name": i[0], "Price":i[1], "Reviews":i[2],
                     "Rating":i[3], "City":i[4], "Services":i[5], "Ranking":i[6]}]
            self.tableWidget.setRowCount(len(data_array))
            for person in data:
                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(person["Name"]))
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(person["Price"]))
                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(person["Reviews"]))
                self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(person["Rating"]))
                self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(person["City"]))
                self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(person["Services"]))
                self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(person["Ranking"]))
            row += 1

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Names"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Price"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "City"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Rating"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Review"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Services"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Ranking"))
        self.label.setText(_translate("MainWindow", "TripAdvisor"))
        self.label_2.setText(_translate("MainWindow", "Time Elapsed:"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.pushButton_2.setText(_translate("MainWindow", "Pause"))
        self.pushButton_3.setText(_translate("MainWindow", "Stop"))
        self.pushButton_4.setText(_translate("MainWindow", "Resume"))
        self.ssButton.setText(_translate("MainWindow", "S"))
        self.ssButton_2.setText(_translate("MainWindow", "S"))
        self.ssButton_3.setText(_translate("MainWindow", "S"))
        self.ssButton_4.setText(_translate("MainWindow", "S"))
        self.ssButton_5.setText(_translate("MainWindow", "S"))
        self.ssButton_6.setText(_translate("MainWindow", "S"))
        self.ssButton_7.setText(_translate("MainWindow", "S"))
        self.pushButton_5.setText(_translate("MainWindow", "F"))
        self.pushButton_6.setText(_translate("MainWindow", "F"))
        self.pushButton_7.setText(_translate("MainWindow", "F"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
