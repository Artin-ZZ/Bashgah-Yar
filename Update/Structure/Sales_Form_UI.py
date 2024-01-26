from PyQt5 import QtCore, QtGui, QtWidgets
from Update.Root.Settings.Helpers import randomSEC_KEY_reqs


class SalesForm(object):
    def setupUi(self, MainPage):
        MainPage.setObjectName("MainPage")
        MainPage.resize(800, 800)
        MainPage.setMinimumSize(QtCore.QSize(800, 800))
        MainPage.setMaximumSize(QtCore.QSize(800, 800))
        font = QtGui.QFont()
        font.setFamily("Vazir")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        MainPage.setFont(font)
        MainPage.setLayoutDirection(QtCore.Qt.RightToLeft)
        MainPage.setStyleSheet("/*Central Widget*/\n"
"#MainPage{\n"
"    background-image: url(./pics/login_bg.jpg);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center center;\n"
"    border: none;\n"
"}\n"
"#Container{\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"/********** BUTTONS ***********/\n"
"#submitbtn{\n"
"    background-image: url(./pics/btn_login4.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center center;\n"
"    border-radius: 30px;\n"
"}\n"
"#submitbtn:hover{\n"
"    background-image: url(./pics/btn_login3.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center center;\n"
"    border-radius: 30px;\n"
"}\n"
"#submitbtn:pressed{\n"
"    background-image: url(./pics/btn_login2.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center center;\n"
"    border-radius: 30px;\n"
"}\n"
"/*****************/\n"
"#closebtn{\n"
"    background-color: rgb(255, 0, 0);\n"
"    border-radius: 30px;\n"
"    color: #fff;\n"
"}\n"
"#closebtn:hover{\n"
"    background-color: rgb(255, 115, 115);\n"
"    border-radius: 30px;\n"
"    color: #fff;\n"
"}\n"
"#closebtn:pressed{\n"
"    background-color:rgb(191, 255, 123);\n"
"    border-radius: 30px;\n"
"    color: #000;\n"
"}\n"
"/***************************** LABEL AND TEXT FIELDS *******************************/\n"
"#date_lbl{\n"
"    background-color:rgb(72, 72, 72) ;\n"
"    border-radius: 30px;\n"
"    color: #fff;\n"
"}\n"
"#date_txt{\n"
"    background: transparent;\n"
"    border: none;\n"
"    border-bottom: 5px solid lime;\n"
"}\n"
"/*****************/\n"
"#fname_lbl{\n"
"    background-color:rgb(72, 72, 72) ;\n"
"    border-radius: 30px;\n"
"    color: #fff;\n"
"}\n"
"#fname_txt{\n"
"    background: transparent;\n"
"    border: none;\n"
"    border-bottom: 5px solid lime;\n"
"}\n"
"/*****************/\n"
"#weandhe_lbl{\n"
"    background-color:rgb(72, 72, 72) ;\n"
"    border-radius: 30px;\n"
"    color: #fff;\n"
"}\n"
"#weandhe_txt{\n"
"    background: transparent;\n"
"    border: none;\n"
"    border-bottom: 5px solid lime;\n"
"}\n"
"/*****************/\n"
"#workoutd_lbl{\n"
"    background-color:rgb(72, 72, 72) ;\n"
"    border-radius: 30px;\n"
"    color: #fff;\n"
"}\n"
"#workoutd_txt{\n"
"    background: transparent;\n"
"    border: none;\n"
"    border-bottom: 5px solid lime;\n"
"}\n"
"/*****************/\n"
"#movename_lbl{\n"
"    background-color:rgb(72, 72, 72) ;\n"
"    border-radius: 30px;\n"
"    color: #fff;\n"
"}\n"
"#movename_txt{\n"
"    background: transparent;\n"
"    border: none;\n"
"    border-bottom: 5px solid lime;\n"
"}\n"
"/*****************/\n"
"#saleno_lbl{\n"
"    background-color:rgb(72, 72, 72) ;\n"
"    border-radius: 30px;\n"
"    color: #fff;\n"
"}\n"
"#saleno_txt{\n"
"    background: transparent;\n"
"    border: none;\n"
"    border-bottom: 5px solid lime;\n"
"}\n"
"/*****************/\n"
"#phone_lbl{\n"
"    background-color:rgb(72, 72, 72) ;\n"
"    border-radius: 30px;\n"
"    color: #fff;\n"
"}\n"
"#phone_txt{\n"
"    background: transparent;\n"
"    border: none;\n"
"    border-bottom: 5px solid lime;\n"
"}\n"
"/*****************/\n"
"#reqstat_lbl{\n"
"    background-color:rgb(72, 72, 72) ;\n"
"    border-radius: 30px;\n"
"    color: #fff;\n"
"}\n"
"#reqstat_txt{\n"
"    background: transparent;\n"
"    border: none;\n"
"    border-bottom: 5px solid lime;\n"
"}\n"
"/*****************/\n"
"#price_tag_lbl{\n"
"    background-color:rgb(72, 72, 72) ;\n"
"    border-radius: 30px;\n"
"    color: #fff;\n"
"}\n"
"#price_tag_txt{\n"
"    background: transparent;\n"
"    border: none;\n"
"    border-bottom: 5px solid lime;\n"
"}\n"
"/*****************/\n"
"#regerfname_lbl{\n"
"    background-color:rgb(72, 72, 72) ;\n"
"    border-radius: 30px;\n"
"    color: #fff;\n"
"}\n"
"#regerfname_txt{\n"
"    background: transparent;\n"
"    border: none;\n"
"    border-bottom: 5px solid lime;\n"
"}\n")
        self.verticalLayout = QtWidgets.QVBoxLayout(MainPage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Container = QtWidgets.QFrame(MainPage)
        self.Container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Container.setObjectName("Container")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Container)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.saleno_txt = QtWidgets.QLineEdit(self.Container)
        self.saleno_txt.setText(randomSEC_KEY_reqs())# ---> Read only
        self.saleno_txt.setMinimumSize(QtCore.QSize(300, 50))
        self.saleno_txt.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setFamily("Vazir")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.saleno_txt.setReadOnly(True)
        self.saleno_txt.setFont(font)
        self.saleno_txt.setObjectName("saleno_txt")
        self.gridLayout_2.addWidget(self.saleno_txt, 6, 1, 1, 1)
        self.saleno_lbl = QtWidgets.QLabel(self.Container)
        self.saleno_lbl.setMinimumSize(QtCore.QSize(220, 60))
        self.saleno_lbl.setMaximumSize(QtCore.QSize(220, 60))
        font = QtGui.QFont()
        font.setFamily("Vazir")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.saleno_lbl.setFont(font)
        self.saleno_lbl.setObjectName("saleno_lbl")
        self.gridLayout_2.addWidget(self.saleno_lbl, 6, 0, 1, 1)
        self.fname_txt = QtWidgets.QLineEdit(self.Container)
        self.fname_txt.setMinimumSize(QtCore.QSize(300, 50))
        self.fname_txt.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setFamily("Vazir")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.fname_txt.setFont(font)
        self.fname_txt.setObjectName("fname_txt")
        self.gridLayout_2.addWidget(self.fname_txt, 1, 1, 1, 1)
        self.workoutd_txt = QtWidgets.QLineEdit(self.Container)
        self.workoutd_txt.setMinimumSize(QtCore.QSize(300, 50))
        self.workoutd_txt.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setFamily("Vazir")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.workoutd_txt.setFont(font)
        self.workoutd_txt.setObjectName("workoutd_txt")
        self.gridLayout_2.addWidget(self.workoutd_txt, 5, 1, 1, 1)
        self.price_tag_txt = QtWidgets.QLineEdit(self.Container)
        self.price_tag_txt.setMinimumSize(QtCore.QSize(300, 50))
        self.price_tag_txt.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setFamily("Vazir")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.price_tag_txt.setFont(font)
        self.price_tag_txt.setObjectName("price_tag_txt")
        self.gridLayout_2.addWidget(self.price_tag_txt, 7, 1, 1, 1)
        self.weandhe_txt = QtWidgets.QLineEdit(self.Container)
        self.weandhe_txt.setMinimumSize(QtCore.QSize(300, 50))
        self.weandhe_txt.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setFamily("Vazir")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.weandhe_txt.setFont(font)
        self.weandhe_txt.setObjectName("weandhe_txt")
        self.gridLayout_2.addWidget(self.weandhe_txt, 3, 1, 1, 1)
        self.fname_lbl = QtWidgets.QLabel(self.Container)
        self.fname_lbl.setMinimumSize(QtCore.QSize(220, 60))
        self.fname_lbl.setMaximumSize(QtCore.QSize(220, 60))
        font = QtGui.QFont()
        font.setFamily("Vazir")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.fname_lbl.setFont(font)
        self.fname_lbl.setObjectName("fname_lbl")
        self.gridLayout_2.addWidget(self.fname_lbl, 1, 0, 1, 1)
        self.workoutd_lbl = QtWidgets.QLabel(self.Container)
        self.workoutd_lbl.setMinimumSize(QtCore.QSize(220, 60))
        self.workoutd_lbl.setMaximumSize(QtCore.QSize(220, 60))
        font = QtGui.QFont()
        font.setFamily("Vazir")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.workoutd_lbl.setFont(font)
        self.workoutd_lbl.setObjectName("workoutd_lbl")
        self.gridLayout_2.addWidget(self.workoutd_lbl, 5, 0, 1, 1)
        self.price_tag = QtWidgets.QLabel(self.Container)
        self.price_tag.setMinimumSize(QtCore.QSize(220, 60))
        self.price_tag.setMaximumSize(QtCore.QSize(220, 60))
        font = QtGui.QFont()
        font.setFamily("Vazir")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.price_tag.setFont(font)
        self.price_tag.setObjectName("price_tag_lbl")
        self.gridLayout_2.addWidget(self.price_tag, 7, 0, 1, 1)
        self.submitbtn = QtWidgets.QPushButton(self.Container)
        self.submitbtn.setMinimumSize(QtCore.QSize(300, 70))
        self.submitbtn.setMaximumSize(QtCore.QSize(300, 70))
        font = QtGui.QFont()
        font.setFamily("Vazir")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.submitbtn.setFont(font)
        self.submitbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submitbtn.setObjectName("submitbtn")
        self.gridLayout_2.addWidget(self.submitbtn, 14, 1, 1, 1)
        self.weandhe_lbl = QtWidgets.QLabel(self.Container)
        self.weandhe_lbl.setMinimumSize(QtCore.QSize(220, 60))
        self.weandhe_lbl.setMaximumSize(QtCore.QSize(220, 60))
        font = QtGui.QFont()
        font.setFamily("Vazir")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.weandhe_lbl.setFont(font)
        self.weandhe_lbl.setObjectName("weandhe_lbl")
        self.gridLayout_2.addWidget(self.weandhe_lbl, 3, 0, 1, 1)
        self.movename_lbl = QtWidgets.QLabel(self.Container)
        self.movename_lbl.setMinimumSize(QtCore.QSize(220, 60))
        self.movename_lbl.setMaximumSize(QtCore.QSize(220, 60))
        font = QtGui.QFont()
        font.setFamily("Vazir")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.movename_lbl.setFont(font)
        self.movename_lbl.setObjectName("movename_lbl")
        self.gridLayout_2.addWidget(self.movename_lbl, 8, 0, 1, 1)
        self.movename_txt = QtWidgets.QLineEdit(self.Container)
        self.movename_txt.setMinimumSize(QtCore.QSize(400, 50))
        self.movename_txt.setMaximumSize(QtCore.QSize(400, 50))
        font = QtGui.QFont()
        font.setFamily("Vazir")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.movename_txt.setFont(font)
        self.movename_txt.setObjectName("movename_txt")
        self.gridLayout_2.addWidget(self.movename_txt, 8, 1, 1, 1)
        self.phone_lbl = QtWidgets.QLabel(self.Container)
        self.phone_lbl.setMinimumSize(QtCore.QSize(250, 60))
        self.phone_lbl.setMaximumSize(QtCore.QSize(250, 60))
        font = QtGui.QFont()
        font.setFamily("Vazir")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.phone_lbl.setFont(font)
        self.phone_lbl.setObjectName("phone_lbl")
        self.gridLayout_2.addWidget(self.phone_lbl, 9, 0, 1, 1)
        self.reqstat_lbl = QtWidgets.QLabel(self.Container)
        self.reqstat_lbl.setMinimumSize(QtCore.QSize(250, 60))
        self.reqstat_lbl.setMaximumSize(QtCore.QSize(250, 60))
        font = QtGui.QFont()
        font.setFamily("Vazir")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.reqstat_lbl.setFont(font)
        self.reqstat_lbl.setObjectName("reqstat_lbl")
        self.gridLayout_2.addWidget(self.reqstat_lbl, 10, 0, 1, 1)        
        self.regerfname_lbl = QtWidgets.QLabel(self.Container)
        self.regerfname_lbl.setMinimumSize(QtCore.QSize(250, 60))
        self.regerfname_lbl.setMaximumSize(QtCore.QSize(250, 60))
        font = QtGui.QFont()
        font.setFamily("Vazir")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.regerfname_lbl.setFont(font)
        self.regerfname_lbl.setObjectName("regerfname_lbl")
        self.gridLayout_2.addWidget(self.regerfname_lbl, 11, 0, 1, 1)
        self.phone_txt = QtWidgets.QLineEdit(self.Container)
        self.phone_txt.setMinimumSize(QtCore.QSize(300, 50))
        self.phone_txt.setMaximumSize(QtCore.QSize(300, 50))
        self.phone_txt.setInputMask("99999999999")
        font = QtGui.QFont()
        font.setFamily("Vazir")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.phone_txt.setFont(font)
        self.phone_txt.setObjectName("phone_txt")
        self.gridLayout_2.addWidget(self.phone_txt, 9, 1, 1, 1)
        self.reqstat_txt = QtWidgets.QComboBox(self.Container)
        self.reqstat_txt.setMinimumSize(QtCore.QSize(300, 50))
        self.reqstat_txt.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setFamily("Vazir")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.reqstat_txt.setFont(font)
        self.reqstat_txt.setObjectName("reqstat_txt")
        self.reqstat_txt.addItem("با موفقیت انجام شد")
        self.reqstat_txt.addItem("درحال انجام شدن")
        self.reqstat_txt.addItem("وقفه در انجام")
        self.reqstat_txt.addItem("لغو شد")
        self.reqstat_txt.addItem("خطا در انجام")
        self.gridLayout_2.addWidget(self.reqstat_txt, 10, 1, 1, 1)
        self.regerfname_txt = QtWidgets.QLineEdit(self.Container)
        self.regerfname_txt.setMinimumSize(QtCore.QSize(300, 50))
        self.regerfname_txt.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setFamily("Vazir")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.regerfname_txt.setFont(font)
        self.regerfname_txt.setObjectName("regerfname_txt")
        self.gridLayout_2.addWidget(self.regerfname_txt, 11, 1, 1, 1)
        self.date_txt = QtWidgets.QLineEdit(self.Container)
        self.date_txt.setMinimumSize(QtCore.QSize(300, 50))
        self.date_txt.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setFamily("Vazir")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.date_txt.setFont(font)
        self.date_txt.setObjectName("date_txt")
        self.gridLayout_2.addWidget(self.date_txt, 0, 1, 1, 1)
        self.date_lbl = QtWidgets.QLabel(self.Container)
        self.date_lbl.setMinimumSize(QtCore.QSize(220, 60))
        self.date_lbl.setMaximumSize(QtCore.QSize(220, 60))
        font = QtGui.QFont()
        font.setFamily("Vazir")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.date_lbl.setFont(font)
        self.date_lbl.setObjectName("date_lbl")
        self.gridLayout_2.addWidget(self.date_lbl, 0, 0, 1, 1)
        self.closebtn = QtWidgets.QPushButton(self.Container)
        self.closebtn.setMinimumSize(QtCore.QSize(200, 70))
        self.closebtn.setMaximumSize(QtCore.QSize(200, 70))
        font = QtGui.QFont()
        font.setFamily("Vazir")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.closebtn.setFont(font)
        self.closebtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.closebtn.setObjectName("closebtn")
        self.gridLayout_2.addWidget(self.closebtn, 14, 0, 1, 1)
        self.verticalLayout.addWidget(self.Container)

        self.retranslateUi(MainPage)
        QtCore.QMetaObject.connectSlotsByName(MainPage)

    def retranslateUi(self, MainPage):
        _translate = QtCore.QCoreApplication.translate
        MainPage.setWindowTitle(_translate("MainPage", "Dialog"))
        self.saleno_txt.setPlaceholderText(_translate("MainPage", "شماره سفارش"))
        self.saleno_lbl.setText(_translate("MainPage", "   شماره سفارش:"))
        self.fname_txt.setPlaceholderText(_translate("MainPage", "نام و نام خانوادگی "))
        self.workoutd_txt.setPlaceholderText(_translate("MainPage", "ایتم درخواستی توسط ورزشکار"))
        self.weandhe_txt.setPlaceholderText(_translate("MainPage", "موضوع درخواست"))
        self.fname_lbl.setText(_translate("MainPage", "  نام ونام خانوادگی: "))
        self.workoutd_lbl.setText(_translate("MainPage", "   ایتم درخواستی:"))
        self.submitbtn.setText(_translate("MainPage", "ثبت درخواست"))
        self.weandhe_lbl.setText(_translate("MainPage", "  موضوع درخواست:"))
        self.movename_lbl.setText(_translate("MainPage", "   آدرس مشتری:"))
        self.movename_txt.setPlaceholderText(_translate("MainPage", "آدرس منزل مشتری"))
        self.phone_lbl.setText(_translate("MainPage", "  شماره تماس مشتری:"))
        self.phone_txt.setPlaceholderText(_translate("MainPage", "شماره تماس مشتری"))
        self.reqstat_lbl.setText(_translate("MainPage", "  وضعیت درخواست:"))
        self.reqstat_txt.setPlaceholderText(_translate("MainPage", "وضعیت درخواست"))
        self.date_txt.setPlaceholderText(_translate("MainPage", "نمونه (1402/3/14)"))
        self.date_lbl.setText(_translate("MainPage", "  تاریخ :"))
        self.closebtn.setText(_translate("MainPage", "بستن صفحه"))
        self.price_tag.setText(_translate("MainPage", " قیمت آیتم(تومان) :"))
        self.price_tag_txt.setPlaceholderText(_translate("MainPage", "قیمت آیتم درخواستی"))
        self.regerfname_lbl.setText(_translate("MainPage", " نام متصدی:"))
        self.regerfname_txt.setPlaceholderText(_translate("MainPage", "نام کامل ثبت کننده"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainPage = QtWidgets.QDialog()
#     ui = SalesForm()
#     ui.setupUi(MainPage)
#     MainPage.show()
#     sys.exit(app.exec_())
