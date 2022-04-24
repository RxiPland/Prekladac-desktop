from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_hlavni_menu(object):


    def setupUi(self, MainWindow):


        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(630, 480)
        font = QtGui.QFont()
        font.setFamily("Arial")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(40, 60, 381, 161))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")


        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(40, 290, 381, 161))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.plainTextEdit_2.setFont(font)
        self.plainTextEdit_2.setReadOnly(True)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")


        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(450, 60, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")


        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 22, 101, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setCheckable(True)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(180, 252, 101, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setCheckable(True)


        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(450, 410, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")


        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(460, 140, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")

        
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(300, 252, 121, 31))
        self.pushButton_6.setObjectName("pushButton_6")

        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(300, 22, 121, 31))
        self.pushButton_7.setObjectName("pushButton_7")


        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(450, 320, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(40, 30, 121, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")


        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(40, 260, 121, 21))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")


        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Překladač"))
        self.plainTextEdit.setPlaceholderText(_translate("MainWindow", "Zde zadejte text k přeložení..."))
        self.plainTextEdit_2.setPlaceholderText(_translate("MainWindow", "Přeložený text..."))
        self.pushButton.setText(_translate("MainWindow", "Přeložit"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Čeština"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Angličtina"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Němčina"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Slovenština"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Ukrajinština"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Španělština"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Francouzština"))
        self.comboBox.setItemText(7, _translate("MainWindow", "Italština"))
        self.comboBox.setItemText(8, _translate("MainWindow", "Ruština"))
        self.comboBox.setItemText(9, _translate("MainWindow", "Polština"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Čeština"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Angličtina"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Němčina"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Slovenština"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "Ukrajinština"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "Španělština"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "Francouzština"))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "Italština"))
        self.comboBox_2.setItemText(8, _translate("MainWindow", "Ruština"))
        self.comboBox_2.setItemText(9, _translate("MainWindow", "Polština"))
        self.pushButton_2.setText(_translate("MainWindow", "Poslechnout"))
        self.pushButton_3.setText(_translate("MainWindow", "Poslechnout"))
        self.pushButton_4.setText(_translate("MainWindow", "Vymazat"))
        self.pushButton_5.setText(_translate("MainWindow", "Uložit aktuální\nvýběr jazyků"))
        self.checkBox.setText(_translate("MainWindow", " Automaticky přehrát\n zvuk překladu"))
        self.pushButton_6.setText(_translate("MainWindow", "Kopírovat překlad"))
        self.pushButton_7.setText(_translate("MainWindow", "Vložit ze schránky"))