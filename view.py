# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 771)
        MainWindow.setMinimumSize(QtCore.QSize(700, 771))
        MainWindow.setMaximumSize(QtCore.QSize(700, 771))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MenuLabel = QtWidgets.QLabel(self.centralwidget)
        self.MenuLabel.setGeometry(QtCore.QRect(260, 10, 131, 51))
        self.MenuLabel.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.MenuLabel.setFont(font)
        self.MenuLabel.setObjectName("MenuLabel")
        self.PhoRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.PhoRadioButton.setGeometry(QtCore.QRect(100, 100, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.PhoRadioButton.setFont(font)
        self.PhoRadioButton.setObjectName("PhoRadioButton")
        self.PhoButtonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.PhoButtonGroup.setObjectName("PhoButtonGroup")
        self.PhoButtonGroup.addButton(self.PhoRadioButton)
        self.ShawarmaRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.ShawarmaRadioButton.setGeometry(QtCore.QRect(400, 100, 221, 20))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.ShawarmaRadioButton.setFont(font)
        self.ShawarmaRadioButton.setObjectName("ShawarmaRadioButton")
        self.PhoButtonGroup.addButton(self.ShawarmaRadioButton)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 290, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.WaterRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.WaterRadioButton.setGeometry(QtCore.QRect(210, 290, 100, 20))
        self.WaterRadioButton.setObjectName("WaterRadioButton")
        self.SpiceButtonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.SpiceButtonGroup.setObjectName("SpiceButtonGroup")
        self.SpiceButtonGroup.addButton(self.WaterRadioButton)
        self.CokeRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.CokeRadioButton.setGeometry(QtCore.QRect(330, 290, 100, 20))
        self.CokeRadioButton.setObjectName("CokeRadioButton")
        self.SpiceButtonGroup.addButton(self.CokeRadioButton)
        self.PepsiRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.PepsiRadioButton.setGeometry(QtCore.QRect(460, 290, 111, 21))
        self.PepsiRadioButton.setObjectName("PepsiRadioButton")
        self.SpiceButtonGroup.addButton(self.PepsiRadioButton)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 350, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.Tips1Button = QtWidgets.QRadioButton(self.centralwidget)
        self.Tips1Button.setGeometry(QtCore.QRect(230, 350, 100, 20))
        self.Tips1Button.setObjectName("Tips1Button")
        self.DrinkButtonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.DrinkButtonGroup.setObjectName("DrinkButtonGroup")
        self.DrinkButtonGroup.addButton(self.Tips1Button)
        self.Tips2Button = QtWidgets.QRadioButton(self.centralwidget)
        self.Tips2Button.setGeometry(QtCore.QRect(340, 350, 100, 20))
        self.Tips2Button.setObjectName("Tips2Button")
        self.DrinkButtonGroup.addButton(self.Tips2Button)
        self.Tips3Button = QtWidgets.QRadioButton(self.centralwidget)
        self.Tips3Button.setGeometry(QtCore.QRect(430, 350, 100, 20))
        self.Tips3Button.setObjectName("Tips3Button")
        self.DrinkButtonGroup.addButton(self.Tips3Button)
        self.receiptLabel = QtWidgets.QLabel(self.centralwidget)
        self.receiptLabel.setGeometry(QtCore.QRect(180, 380, 291, 211))
        self.receiptLabel.setObjectName("receiptLabel")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 611, 121, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 611, 121, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.Beefbutton1 = QtWidgets.QRadioButton(self.centralwidget)
        self.Beefbutton1.setGeometry(QtCore.QRect(130, 130, 100, 20))
        self.Beefbutton1.setObjectName("Beefbutton1")
        self.ConButtonGroup1 = QtWidgets.QButtonGroup(MainWindow)
        self.ConButtonGroup1.setObjectName("ConButtonGroup1")
        self.ConButtonGroup1.addButton(self.Beefbutton1)
        self.PorkButton = QtWidgets.QRadioButton(self.centralwidget)
        self.PorkButton.setGeometry(QtCore.QRect(130, 160, 100, 20))
        self.PorkButton.setObjectName("PorkButton")
        self.ConButtonGroup1.addButton(self.PorkButton)
        self.ChickenButton1 = QtWidgets.QRadioButton(self.centralwidget)
        self.ChickenButton1.setGeometry(QtCore.QRect(130, 190, 100, 20))
        self.ChickenButton1.setObjectName("ChickenButton1")
        self.ConButtonGroup1.addButton(self.ChickenButton1)
        self.BeefButton2 = QtWidgets.QRadioButton(self.centralwidget)
        self.BeefButton2.setGeometry(QtCore.QRect(430, 130, 100, 20))
        self.BeefButton2.setObjectName("BeefButton2")
        self.ConButtonGroup2 = QtWidgets.QButtonGroup(MainWindow)
        self.ConButtonGroup2.setObjectName("ConButtonGroup2")
        self.ConButtonGroup2.addButton(self.BeefButton2)
        self.ChickenButton2 = QtWidgets.QRadioButton(self.centralwidget)
        self.ChickenButton2.setGeometry(QtCore.QRect(430, 160, 100, 20))
        self.ChickenButton2.setObjectName("ChickenButton2")
        self.ConButtonGroup2.addButton(self.ChickenButton2)
        self.MildButton1 = QtWidgets.QRadioButton(self.centralwidget)
        self.MildButton1.setGeometry(QtCore.QRect(200, 240, 51, 16))
        self.MildButton1.setObjectName("MildButton1")
        self.MediumButton1 = QtWidgets.QRadioButton(self.centralwidget)
        self.MediumButton1.setGeometry(QtCore.QRect(300, 240, 81, 16))
        self.MediumButton1.setObjectName("MediumButton1")
        self.SpicyButton1 = QtWidgets.QRadioButton(self.centralwidget)
        self.SpicyButton1.setGeometry(QtCore.QRect(430, 240, 61, 21))
        self.SpicyButton1.setObjectName("SpicyButton1")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 240, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GroupProject"))
        self.MenuLabel.setText(_translate("MainWindow", "Menu"))
        self.PhoRadioButton.setText(_translate("MainWindow", "Pho ($12.99)"))
        self.ShawarmaRadioButton.setText(_translate("MainWindow", "Shawarma (15.00)"))
        self.label_2.setText(_translate("MainWindow", "Drinks"))
        self.WaterRadioButton.setText(_translate("MainWindow", "Water (Free)"))
        self.CokeRadioButton.setText(_translate("MainWindow", "Coke ($0.99)"))
        self.PepsiRadioButton.setText(_translate("MainWindow", " Pepsi ($0.99)"))
        self.label_3.setText(_translate("MainWindow", "Tips"))
        self.Tips1Button.setText(_translate("MainWindow", "10%"))
        self.Tips2Button.setText(_translate("MainWindow", "15%"))
        self.Tips3Button.setText(_translate("MainWindow", "20%"))
        self.receiptLabel.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.pushButton_2.setText(_translate("MainWindow", "Clear"))
        self.Beefbutton1.setText(_translate("MainWindow", "Beef "))
        self.PorkButton.setText(_translate("MainWindow", "Pork "))
        self.ChickenButton1.setText(_translate("MainWindow", "Chicken"))
        self.BeefButton2.setText(_translate("MainWindow", "Beef"))
        self.ChickenButton2.setText(_translate("MainWindow", "Chicken"))
        self.MildButton1.setText(_translate("MainWindow", "Mild"))
        self.MediumButton1.setText(_translate("MainWindow", "Medium"))
        self.SpicyButton1.setText(_translate("MainWindow", "Spicy"))
        self.label.setText(_translate("MainWindow", "Spice"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
