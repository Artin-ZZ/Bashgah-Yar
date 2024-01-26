from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *



class Gym_Ui(object):
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(1080, 882)
                font = QtGui.QFont()
                font.setFamily("Vazir")
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                MainWindow.setFont(font)
                MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
                MainWindow.setStyleSheet("/*Main Window*/\n"
        # "*{\n"
        # "    border: none;\n"
        # "    background-color: transparent;\n"
        # "}\n"
        "/*Central Widget*/\n"
        "#centralwidget{\n"
        "    background-image: url(./pics/body_bg1.jpg);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border: none;\n"
        "}\n"
        "/******* PAGE 1 *******/\n"
        "/******* LOGIN FORM *******/\n"
        "#Login{\n"
        "    background-image: url(./pics/login_bg.jpg);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border: none;\n"
        "}\n"
        "#login_form{\n"
        "    border: none;\n"
        "    border-radius: 30px;\n"
        "}\n"
        "/* Forgot Password Page */\n"
        "#forgpass{\n"
        "    background-image: url(./pics/bg_forgpass.jpg);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border: none;\n"
        "}\n"
        "#head_lbl{\n"
        "    border: none;\n"
        "    border-radius: 30px;\n"
        "    background-color: rgb(74, 74, 74);\n"
        "    color: #fff;\n"
        "    padding: 10px;\n"
        "}\n"
        "#usrnm_txt{\n"
        "    background: transparent;\n"
        "    border: none;\n"
        "    border-bottom: 5px solid lime;\n"
        "    padding: 10px;\n"
        "    color: #fff;\n"
        "}\n"
        "#ID_txt{\n"
        "    background: transparent;\n"
        "    border: none;\n"
        "    border-bottom: 5px solid lime;\n"
        "    padding: 10px;\n"
        "    color: #fff;\n"
        "}\n"
        "#confirm_btn{\n"
        "    background-image: url(./pics/btn_login4.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20p\n"
        "}\n"
        "#confirm_btn:hover{\n"
        "    background-image: url(./pics/btn_login3.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20p\n"
        "}\n"
        "#confirm_btn:pressed{\n"
        "    background-image: url(./pics/btn_login2.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20p\n"
        "}\n"
        "#forg_usrnm{\n"
        "    background: transparent;\n"
        "    text-decoration: underline;\n"
        "    color: rgb(3, 252, 252);\n"
        "}\n"
        "#forg_usrnm:hover{\n"
        "    background: transparent;\n"
        "    text-decoration: underline;\n"
        "    color: rgb(192, 33, 255);\n"
        "}\n"
        "#forg_usrnm:pressed{\n"
        "    background: transparent;\n"
        "    text-decoration: underline;\n"
        "    color: rgb(0, 0, 0);\n"
        "}\n"

        "#back_btn{\n"
        "    background-image: url(./pics/btn_login3.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20p\n"
        "}\n"
        "#back_btn:hover{\n"
        "    background-image: url(./pics/btn_login.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20p\n"
        "}\n"
        "#back_btn:pressed{\n"
        "    background-image: url(./pics/btn_login2.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20p\n"
        "}\n"
        "/* login form components*/\n"
        "#frm_lbl{\n"
        "    border: none;\n"
        "    border-radius: 30px;\n"
        "    background-color: rgb(74, 74, 74);\n"
        "    color: #fff;\n"
        "    padding: 10px;\n"
        "}\n"
        "#usernm_lbl{\n"
        "    border: none;\n"
        "    border-radius: 30px;\n"
        "    padding: 10px;\n"
        "}\n"
        "#passw_lbl{\n"
        "    border: none;\n"
        "    border-radius: 30px;\n"
        "    padding: 10px;\n"
        "}\n"
        "#usernm_txt{\n"
        "    background: transparent;\n"
        "    border: none;\n"
        "    border-bottom: 5px solid lime;\n"
        "    padding: 10px;\n"
        "}\n"
        "#textEdit{\n"
        "    background: transparent;\n"
        "    border: none;\n"
        "}\n"
        "#txt_holder{\n"
        "    background: transparent;\n"
        "    border: none;\n"
        "}\n"
        "#passw_txt{\n"
        "    background: transparent;\n"
        "    border: none;\n"
        "    border-bottom: 5px solid lime;\n"
        "    padding: 10px;\n"
        "}\n"
        "/*Log In Button*/\n"
        "#submit_btn{\n"
        "    background-image: url(./pics/btn_login4.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "}\n"
        "#submit_btn:hover{\n"
        "    background-image: url(./pics/btn_login.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "}\n"
        "#submit_btn:pressed{\n"
        "    background-image: url(./pics/btn_login2.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "}\n"
        "/*Register Button*/\n"
        "#reg_btn{\n"
        "    background-image: url(./pics/btn_login3.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "}\n"
        "#reg_btn:hover{\n"
        "    background-image: url(./pics/btn_login.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "}\n"
        "#reg_btn:pressed{\n"
        "    background-image: url(./pics/btn_login2.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "}\n"
        "/*Fogot password Button*/\n"
        "#forgpass_btn{\n"
        "    background: transparent;\n"
        "    text-decoration: underline;\n"
        "    color: rgb(255, 1, 111);\n"
        "}\n"
        "#forgpass_btn:hover{\n"
        "    background: transparent;\n"
        "    text-decoration: underline;\n"
        "    color: rgb(192, 33, 255);\n"
        "}\n"
        "#forgpass_btn:pressed{\n"
        "    background: transparent;\n"
        "    text-decoration: underline;\n"
        "    color: rgb(0, 38, 255);\n"
        "}\n"
        "/*About App Login Page Button*/\n"
        "#ablg_btn{\n"
        "    background: transparent;\n"
        "    text-decoration: underline;\n"
        "    color: rgb(0, 38, 255);\n"
        "}\n"
        "#ablg_btn:hover{\n"
        "    background: transparent;\n"
        "    text-decoration: underline;\n"
        "    color: rgb(255, 1, 111);\n"
        "}\n"
        "#ablg_btn:pressed{\n"
        "    background: transparent;\n"
        "    text-decoration: underline;\n"
        "    color: #000;\n"
        "}\n"
        "/******* PAGE 2 *******/\n"
        "/******* HOME PAGE *******/\n"
        "#h_container{\n"
        "    border: none;\n"
        "    background-color: transparent;\n"
        "}\n"
        "#side_menu{\n"
        "    border: none;\n"
        "    border-radius: 30px;\n"
        "    background-image: url(./pics/side_nav2.jpg);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: top center;\n"
        "}\n"
        "/*SIDE MENU COMPONENTS*/\n"
        "/*** Home Button ***/\n"
        "#hm{\n"
        "    background-image: url(./pics/btn_login4.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#hm:hover{\n"
        "    background-image: url(./pics/btn_login3.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#hm:pressed{\n"
        "    background-image: url(./pics/btn_login2.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "/*** Button 1 ***/\n"
        "#btn1{\n"
        "    background-image: url(./pics/btn_login.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#btn1:hover{\n"
        "    background-image: url(./pics/btn_login3.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#btn1:pressed{\n"
        "    background-image: url(./pics/btn_login2.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "/*** Button 2 ***/\n"
        "#btn2{\n"
        "    background-image: url(./pics/btn_login.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#btn2:hover{\n"
        "    background-image: url(./pics/btn_login3.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#btn2:pressed{\n"
        "    background-image: url(./pics/btn_login2.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "/*** Button 3 ***/\n"
        "#btn3{\n"
        "    background-image: url(./pics/btn_login.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#btn3:hover{\n"
        "    background-image: url(./pics/btn_login3.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#btn3:pressed{\n"
        "    background-image: url(./pics/btn_login2.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "/*** Button 4 ***/\n"
        "#btn4{\n"
        "    background-image: url(./pics/btn_login.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#btn4:hover{\n"
        "    background-image: url(./pics/btn_login3.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#btn4:pressed{\n"
        "    background-image: url(./pics/btn_login2.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "/*** Button 5 ***/\n"
        "#btn5{\n"
        "    background-image: url(./pics/btn_login.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#btn5:hover{\n"
        "    background-image: url(./pics/btn_login3.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#btn5:pressed{\n"
        "    background-image: url(./pics/btn_login2.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "/*** Button 6 ***/\n"
        "#btn6{\n"
        "    background-image: url(./pics/btn_login.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#btn6:hover{\n"
        "    background-image: url(./pics/btn_login3.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#btn6:pressed{\n"
        "    background-image: url(./pics/btn_login2.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "/*** Button 7 ***/\n"
        "#btn7{\n"
        "    background-image: url(./pics/btn_login.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#btn7:hover{\n"
        "    background-image: url(./pics/btn_login3.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#btn7:pressed{\n"
        "    background-image: url(./pics/btn_login2.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "/*** Button 8 ***/\n"
        "#btn8{\n"
        "    background-image: url(./pics/btn_login.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#btn8:hover{\n"
        "    background-image: url(./pics/btn_login3.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#btn8:pressed{\n"
        "    background-image: url(./pics/btn_login2.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "/*** Button 9 ***/\n"
        "#btn9{\n"
        "    background-color: rgb(255, 0, 0);\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#btn9:hover{\n"
        "    background-color: rgb(255, 125, 125);\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#btn9:pressed{\n"
        "    background-color: rgb(135, 157, 255);\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "/******* PAGE 3 *******/\n"
        "/******* CONTACT US PAGE *******/\n"
        "#h_container_2{\n"
        "    border: none;\n"
        "    background-color: transparent;\n"
        "}\n"
        "#side_menu_2{\n"
        "    border: none;\n"
        "    border-radius: 30px;\n"
        "    background-image: url(./pics/side_nav2.jpg);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: top center;\n"
        "}\n"
        "/*SIDE MENU COMPONENTS*/\n"
        "/*** Home Button ***/\n"
        "#hm_2{\n"
        "    background-image: url(./pics/btn_login.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#hm_2:hover{\n"
        "    background-image: url(./pics/btn_login3.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#hm_2:pressed{\n"
        "    background-image: url(./pics/btn_login2.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "/*** Button 1 ***/\n"
        "#btn1_2{\n"
        "    background-image: url(./pics/btn_login.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#btn1_2:hover{\n"
        "    background-image: url(./pics/btn_login3.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#btn1_2:pressed{\n"
        "    background-image: url(./pics/btn_login2.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "/*** Button 2 ***/\n"
        "#btn2_2{\n"
        "    background-image: url(./pics/btn_login.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#btn2_2:hover{\n"
        "    background-image: url(./pics/btn_login3.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#btn2_2:pressed{\n"
        "    background-image: url(./pics/btn_login2.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "/*** Button 3 ***/\n"
        "#btn3_2{\n"
        "    background-image: url(./pics/btn_login.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#btn3_2:hover{\n"
        "    background-image: url(./pics/btn_login3.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#btn3_2:pressed{\n"
        "    background-image: url(./pics/btn_login2.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "/*** Button 4 ***/\n"
        "#btn4_2{\n"
        "    background-image: url(./pics/btn_login.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#btn4_2:hover{\n"
        "    background-image: url(./pics/btn_login3.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#btn4_2:pressed{\n"
        "    background-image: url(./pics/btn_login2.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "/*** Button 5 ***/\n"
        "#btn5_2{\n"
        "    background-image: url(./pics/btn_login.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#btn5_2:hover{\n"
        "    background-image: url(./pics/btn_login3.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#btn5_2:pressed{\n"
        "    background-image: url(./pics/btn_login2.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "/*** Button 6 ***/\n"
        "#btn6_2{\n"
        "    background-image: url(./pics/btn_login.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#btn6_2:hover{\n"
        "    background-image: url(./pics/btn_login3.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#btn6_2:pressed{\n"
        "    background-image: url(./pics/btn_login2.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "/*** Button 7 ***/\n"
        "#btn7_2{\n"
        "    background-image: url(./pics/btn_login.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#btn7_2:hover{\n"
        "    background-image: url(./pics/btn_login3.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#btn7_2:pressed{\n"
        "    background-image: url(./pics/btn_login2.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "/*** Button 8 ***/\n"
        "#btn8_2{\n"
        "    background-image: url(./pics/btn_login4.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#btn8_2:hover{\n"
        "    background-image: url(./pics/btn_login3.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#btn8_2:pressed{\n"
        "    background-image: url(./pics/btn_login2.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "/*** Button 9 ***/\n"
        "#btn9_2{\n"
        "    background-color: rgb(255, 0, 0);\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#btn9_2:hover{\n"
        "    background-color: rgb(255, 125, 125);\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#btn9_2:pressed{\n"
        "    background-color: rgb(135, 157, 255);\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "/*** Contact Us Page Text Holder ***/\n"
        "#conus_cont{\n"
        "    background-image: url(./pics/body_bg3.jpg);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    border: none;\n"
        "}\n"
        "/**************************************************/\n"
        "/******* ADMIN PANEL *******/\n"
        "#side_menu_3{\n"
        "    border: none;\n"
        "    border-radius: 30px;\n"
        "    background-image: url(./pics/side_nav2.jpg);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: top center;\n"
        "}\n"
        "/*SIDE MENU COMPONENTS*/\n"
        "/*** Home Button ***/\n"
        "#hm_3{\n"
        "    background-image: url(./pics/btn_login4.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border-radius: 30px;\n"
        "    border: none;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#hm_3:hover{\n"
        "    background-image: url(./pics/btn_login3.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border: none;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#hm_3:pressed{\n"
        "    background-image: url(./pics/btn_login2.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border: none;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "/*** Button 1 ***/\n"
        "#btn1_3{\n"
        "    background-image: url(./pics/btn_login.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border: none;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#btn1_3:hover{\n"
        "    background-image: url(./pics/btn_login3.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border: none;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#btn1_3:pressed{\n"
        "    background-image: url(./pics/btn_login2.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border: none;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "/*** Button 2 ***/\n"
        "#btn2_3{\n"
        "    background-image: url(./pics/btn_login.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border: none;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#btn2_3:hover{\n"
        "    background-image: url(./pics/btn_login3.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border: none;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#btn2_3:pressed{\n"
        "    background-image: url(./pics/btn_login2.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border: none;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "/*** Button 3 ***/\n"
        "#btn3_3{\n"
        "    background-image: url(./pics/btn_login.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border: none;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#btn3_3:hover{\n"
        "    background-image: url(./pics/btn_login3.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border: none;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#btn3_3:pressed{\n"
        "    background-image: url(./pics/btn_login2.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border: none;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "/*** Button 4 ***/\n"
        "#btn4_3{\n"
        "    background-image: url(./pics/btn_login.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border: none;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#btn4_3:hover{\n"
        "    background-image: url(./pics/btn_login3.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border: none;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#btn4_3:pressed{\n"
        "    background-image: url(./pics/btn_login2.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border: none;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "/*** Button 5 ***/\n"
        "#btn5_3{\n"
        "    background-image: url(./pics/btn_login.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border: none;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#btn5_3:hover{\n"
        "    background-image: url(./pics/btn_login3.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border: none;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#btn5_3:pressed{\n"
        "    background-image: url(./pics/btn_login2.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border: none;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "/*** Button 6 ***/\n"
        "#btn6_3{\n"
        "    background-image: url(./pics/btn_login.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border: none;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#btn6_3:hover{\n"
        "    background-image: url(./pics/btn_login3.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border: none;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#btn6_3:pressed{\n"
        "    background-image: url(./pics/btn_login2.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border: none;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "/*** Button 7 ***/\n"
        "#btn7_3{\n"
        "    background-image: url(./pics/btn_login.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border: none;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#btn7_3:hover{\n"
        "    background-image: url(./pics/btn_login3.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border: none;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#btn7_3:pressed{\n"
        "    background-image: url(./pics/btn_login2.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border: none;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "/*** Button 8 ***/\n"
        "#btn8_3{\n"
        "    background-image: url(./pics/btn_login.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border: none;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#btn8_3:hover{\n"
        "    background-image: url(./pics/btn_login3.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border: none;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#btn8_3:pressed{\n"
        "    background-image: url(./pics/btn_login2.png);\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center center;\n"
        "    border: none;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "/*** Button 9 ***/\n"
        "#btn9_3{\n"
        "    background-color: rgb(255, 0, 0);\n"
        "    border: none;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#btn9_3:hover{\n"
        "    background-color: rgb(255, 125, 125);\n"
        "    border: none;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#btn9_3:pressed{\n"
        "    background-color: rgb(135, 157, 255);\n"
        "    border: none;\n"
        "    border-radius: 30px;\n"
        "    padding: 20px;\n"
        "    padding-left: 40px;\n"
        "    padding-Right: 40px;\n"
        "}\n"
        "#logo_holder{\n"
        "    background: transparent;\n"
        "    border: none;\n"
        "}\n")
                MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
                self.verticalLayout.setObjectName("verticalLayout")
                self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
                self.stackedWidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
                self.stackedWidget.setObjectName("stackedWidget")
                self.Login = QtWidgets.QWidget()
                self.Login.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
                self.Login.setObjectName("Login")
                self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Login)
                self.verticalLayout_2.setObjectName("verticalLayout_2")
                self.container = QtWidgets.QFrame(self.Login)
                self.container.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.container.setFrameShadow(QtWidgets.QFrame.Raised)
                self.container.setObjectName("container")
                self.formLayout = QtWidgets.QFormLayout(self.container)
                self.formLayout.setObjectName("formLayout")
                self.login_form = QtWidgets.QFrame(self.container)
                self.login_form.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.login_form.setFrameShadow(QtWidgets.QFrame.Raised)
                self.login_form.setObjectName("login_form")
                self.gridLayout = QtWidgets.QGridLayout(self.login_form)
                self.gridLayout.setObjectName("gridLayout")
                self.passw_txt = QtWidgets.QLineEdit(self.login_form)
                self.passw_txt.setMinimumSize(QtCore.QSize(400, 60))
                self.passw_txt.setMaximumSize(QtCore.QSize(400, 60))
                entered_password_hide = self.passw_txt
                entered_password_hide.setEchoMode(QLineEdit.Password)
                font = QtGui.QFont()
                font.setFamily("Vazir")
                font.setPointSize(14)
                font.setBold(True)
                font.setWeight(75)
                self.passw_txt.setFont(font)
                self.passw_txt.setLayoutDirection(QtCore.Qt.RightToLeft)
                self.passw_txt.setText("")
                self.passw_txt.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
                self.passw_txt.setObjectName("passw_txt")
                self.gridLayout.addWidget(self.passw_txt, 4, 1, 1, 1)
                self.usernm_lbl = QtWidgets.QLabel(self.login_form)
                self.usernm_lbl.setMinimumSize(QtCore.QSize(170, 0))
                self.usernm_lbl.setMaximumSize(QtCore.QSize(170, 16777215))
                font = QtGui.QFont()
                font.setFamily("Vazir")
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.usernm_lbl.setFont(font)
                self.usernm_lbl.setObjectName("usernm_lbl")
                self.gridLayout.addWidget(self.usernm_lbl, 2, 2, 1, 1)
                self.usernm_txt = QtWidgets.QLineEdit(self.login_form)
                self.usernm_txt.setMinimumSize(QtCore.QSize(400, 60))
                self.usernm_txt.setMaximumSize(QtCore.QSize(400, 60))
                font = QtGui.QFont()
                font.setFamily("Vazir")
                font.setPointSize(14)
                font.setBold(True)
                font.setWeight(75)
                self.usernm_txt.setFont(font)
                self.usernm_txt.setLayoutDirection(QtCore.Qt.RightToLeft)
                self.usernm_txt.setInputMask("")
                self.usernm_txt.setText("")
                self.usernm_txt.setCursorPosition(0)
                self.usernm_txt.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
                self.usernm_txt.setReadOnly(False)
                self.usernm_txt.setObjectName("usernm_txt")
                self.gridLayout.addWidget(self.usernm_txt, 2, 1, 1, 1)
                self.submit_btn = QtWidgets.QPushButton(self.login_form)
                font = QtGui.QFont()
                font.setFamily("Vazir")
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.submit_btn.setFont(font)
                self.submit_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.submit_btn.setObjectName("submit_btn")
                self.gridLayout.addWidget(self.submit_btn, 7, 2, 1, 1)
                self.reg_btn = QtWidgets.QPushButton(self.login_form)
                self.reg_btn.setMinimumSize(QtCore.QSize(0, 0))
                font = QtGui.QFont()
                font.setFamily("Vazir")
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.reg_btn.setFont(font)
                self.reg_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.reg_btn.setObjectName("reg_btn")
                self.gridLayout.addWidget(self.reg_btn, 8, 2, 1, 1)
                self.passw_lbl = QtWidgets.QLabel(self.login_form)
                self.passw_lbl.setMinimumSize(QtCore.QSize(240, 60))
                self.passw_lbl.setMaximumSize(QtCore.QSize(240, 60))
                font = QtGui.QFont()
                font.setFamily("Vazir")
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.passw_lbl.setFont(font)
                self.passw_lbl.setObjectName("passw_lbl")
                self.gridLayout.addWidget(self.passw_lbl, 4, 2, 1, 1)
                self.ablg_btn = QtWidgets.QPushButton(self.login_form)
                font = QtGui.QFont()
                font.setFamily("Vazir")
                font.setPointSize(16)
                font.setBold(True)
                font.setUnderline(True)
                font.setWeight(75)
                self.ablg_btn.setFont(font)
                self.ablg_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("./pics/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.ablg_btn.setIcon(icon)
                self.ablg_btn.setIconSize(QtCore.QSize(100, 50))
                self.ablg_btn.setAutoDefault(False)
                self.ablg_btn.setFlat(False)
                self.ablg_btn.setObjectName("ablg_btn")
                self.gridLayout.addWidget(self.ablg_btn, 7, 1, 1, 1)
                self.forgpass_btn = QtWidgets.QPushButton(self.login_form)
                font = QtGui.QFont()
                font.setFamily("Vazir")
                font.setPointSize(16)
                font.setBold(True)
                font.setUnderline(True)
                font.setWeight(75)
                self.forgpass_btn.setFont(font)
                self.forgpass_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.forgpass_btn.setObjectName("forgpass_btn")
                self.gridLayout.addWidget(self.forgpass_btn, 8, 1, 1, 1)
                self.frm_lbl = QtWidgets.QLabel(self.login_form)
                self.frm_lbl.setMinimumSize(QtCore.QSize(330, 60))
                self.frm_lbl.setMaximumSize(QtCore.QSize(330, 60))
                font = QtGui.QFont()
                font.setFamily("Vazir")
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.frm_lbl.setFont(font)
                self.frm_lbl.setObjectName("frm_lbl")
                self.gridLayout.addWidget(self.frm_lbl, 1, 2, 1, 1)
                self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.login_form)
                self.verticalLayout_2.addWidget(self.container, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
                self.stackedWidget.addWidget(self.Login)
                self.Home = QtWidgets.QWidget()
                self.Home.setObjectName("Home")
                self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Home)
                self.verticalLayout_3.setObjectName("verticalLayout_3")
                self.h_container = QtWidgets.QFrame(self.Home)
                self.h_container.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.h_container.setFrameShadow(QtWidgets.QFrame.Raised)
                self.h_container.setObjectName("h_container")
                self.horizontalLayout = QtWidgets.QHBoxLayout(self.h_container)
                self.horizontalLayout.setObjectName("horizontalLayout")
                self.main_body = QtWidgets.QFrame(self.h_container)
                self.main_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.main_body.setFrameShadow(QtWidgets.QFrame.Raised)
                self.main_body.setObjectName("main_body")
                self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.main_body)
                self.verticalLayout_5.setObjectName("verticalLayout_5")
                self.textEdit = QtWidgets.QTextEdit(self.main_body)
                self.textEdit.setReadOnly(True)
                self.textEdit.setObjectName("textEdit")
                self.verticalLayout_5.addWidget(self.textEdit)
                self.horizontalLayout.addWidget(self.main_body)
                self.side_menu = QtWidgets.QFrame(self.h_container)
                self.side_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.side_menu.setFrameShadow(QtWidgets.QFrame.Raised)
                self.side_menu.setObjectName("side_menu")
                self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.side_menu)
                self.verticalLayout_4.setObjectName("verticalLayout_4")
                self.hm = QtWidgets.QPushButton(self.side_menu)
                font = QtGui.QFont()
                font.setFamily("Vazir")
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.hm.setFont(font)
                self.hm.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.hm.setObjectName("hm")
                self.verticalLayout_4.addWidget(self.hm)
                self.btn1 = QtWidgets.QPushButton(self.side_menu)
                font = QtGui.QFont()
                font.setFamily("Vazir")
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.btn1.setFont(font)
                self.btn1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.btn1.setObjectName("btn1")
                self.verticalLayout_4.addWidget(self.btn1)
                self.btn2 = QtWidgets.QPushButton(self.side_menu)
                font = QtGui.QFont()
                font.setFamily("Vazir")
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.btn2.setFont(font)
                self.btn2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.btn2.setObjectName("btn2")
                self.verticalLayout_4.addWidget(self.btn2)
                self.btn3 = QtWidgets.QPushButton(self.side_menu)
                font = QtGui.QFont()
                font.setFamily("Vazir")
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.btn3.setFont(font)
                self.btn3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.btn3.setObjectName("btn3")
                self.verticalLayout_4.addWidget(self.btn3)
                self.btn4 = QtWidgets.QPushButton(self.side_menu)
                font = QtGui.QFont()
                font.setFamily("Vazir")
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.btn4.setFont(font)
                self.btn4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.btn4.setObjectName("btn4")
                self.verticalLayout_4.addWidget(self.btn4)
                self.btn5 = QtWidgets.QPushButton(self.side_menu)
                font = QtGui.QFont()
                font.setFamily("Vazir")
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.btn5.setFont(font)
                self.btn5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.btn5.setObjectName("btn5")
                self.verticalLayout_4.addWidget(self.btn5)
                self.btn6 = QtWidgets.QPushButton(self.side_menu)
                font = QtGui.QFont()
                font.setFamily("Vazir")
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.btn6.setFont(font)
                self.btn6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.btn6.setObjectName("btn5")
                self.verticalLayout_4.addWidget(self.btn6)
                self.btn7 = QtWidgets.QPushButton(self.side_menu)
                font = QtGui.QFont()
                font.setFamily("Vazir")
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.btn7.setFont(font)
                self.btn7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.btn7.setObjectName("btn7")
                self.verticalLayout_4.addWidget(self.btn7)
                self.btn8 = QtWidgets.QPushButton(self.side_menu)
                font = QtGui.QFont()
                font.setFamily("Vazir")
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.btn8.setFont(font)
                self.btn8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.btn8.setObjectName("btn8")
                self.verticalLayout_4.addWidget(self.btn8)
                self.btn9 = QtWidgets.QPushButton(self.side_menu)
                font = QtGui.QFont()
                font.setFamily("Vazir")
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.btn9.setFont(font)
                self.btn9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.btn9.setObjectName("btn9")
                self.verticalLayout_4.addWidget(self.btn9)
                self.horizontalLayout.addWidget(self.side_menu, 0, QtCore.Qt.AlignRight)
                self.verticalLayout_3.addWidget(self.h_container)
                self.stackedWidget.addWidget(self.Home)
                self.forgpass = QtWidgets.QWidget()
                self.forgpass.setObjectName("forgpass")
                self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.forgpass)
                self.verticalLayout_8.setObjectName("verticalLayout_8")
                self.frame = QtWidgets.QFrame(self.forgpass)
                self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame.setObjectName("frame")
                self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
                self.gridLayout_2.setObjectName("gridLayout_2")
                self.head_lbl = QtWidgets.QLabel(self.frame)
                self.head_lbl.setMinimumSize(QtCore.QSize(450, 100))
                self.head_lbl.setMaximumSize(QtCore.QSize(450, 100))
                font = QtGui.QFont()
                font.setFamily("Vazir")
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.head_lbl.setFont(font)
                self.head_lbl.setLayoutDirection(QtCore.Qt.RightToLeft)
                self.head_lbl.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
                self.head_lbl.setObjectName("head_lbl")
                self.gridLayout_2.addWidget(self.head_lbl, 0, 0, 1, 1)
                self.confirm_btn = QtWidgets.QPushButton(self.frame)
                self.confirm_btn.setMinimumSize(QtCore.QSize(0, 80))
                self.confirm_btn.setMaximumSize(QtCore.QSize(16777215, 80))
                font = QtGui.QFont()
                font.setFamily("Vazir")
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.confirm_btn.setFont(font)
                self.confirm_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.confirm_btn.setLayoutDirection(QtCore.Qt.RightToLeft)
                self.confirm_btn.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
                self.confirm_btn.setObjectName("confirm_btn")
                self.gridLayout_2.addWidget(self.confirm_btn, 4, 2, 1, 2)
                self.ID_txt = QtWidgets.QLineEdit(self.frame)
                self.ID_txt.setMinimumSize(QtCore.QSize(400, 70))
                self.ID_txt.setMaximumSize(QtCore.QSize(400, 70))
                entered_ID_hide = self.ID_txt
                entered_ID_hide.setEchoMode(QLineEdit.Password)
                font = QtGui.QFont()
                font.setFamily("Vazir")
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.ID_txt.setFont(font)
                self.ID_txt.setLayoutDirection(QtCore.Qt.RightToLeft)
                self.ID_txt.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
                self.ID_txt.setText("")
                self.ID_txt.setObjectName("ID_txt")
                self.gridLayout_2.addWidget(self.ID_txt, 2, 0, 1, 3)
                self.usrnm_txt = QtWidgets.QLineEdit(self.frame)
                self.usrnm_txt.setMinimumSize(QtCore.QSize(400, 70))
                self.usrnm_txt.setMaximumSize(QtCore.QSize(400, 70))
                font = QtGui.QFont()
                font.setFamily("Vazir")
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.usrnm_txt.setFont(font)
                self.usrnm_txt.setLayoutDirection(QtCore.Qt.RightToLeft)
                self.usrnm_txt.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
                self.usrnm_txt.setText("")
                self.usrnm_txt.setObjectName("usrnm_txt")
                self.gridLayout_2.addWidget(self.usrnm_txt, 1, 0, 1, 2)
                self.usrnm_lbl = QtWidgets.QLabel(self.frame)
                self.usrnm_lbl.setMinimumSize(QtCore.QSize(170, 60))
                self.usrnm_lbl.setMaximumSize(QtCore.QSize(170, 60))
                font = QtGui.QFont()
                font.setFamily("Vazir")
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.usrnm_lbl.setFont(font)
                self.usrnm_lbl.setLayoutDirection(QtCore.Qt.RightToLeft)
                self.usrnm_lbl.setStyleSheet("color: #fff;")
                self.usrnm_lbl.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
                self.usrnm_lbl.setObjectName("usrnm_lbl")
                self.gridLayout_2.addWidget(self.usrnm_lbl, 1, 2, 1, 2)
                self.forg_usrnm = QtWidgets.QPushButton(self.frame)
                self.forg_usrnm.setMinimumSize(QtCore.QSize(0, 80))
                self.forg_usrnm.setMaximumSize(QtCore.QSize(16777215, 80))
                font = QtGui.QFont()
                font.setFamily("Vazir")
                font.setPointSize(14)
                font.setBold(True)
                font.setUnderline(True)
                font.setWeight(75)
                self.forg_usrnm.setFont(font)
                self.forg_usrnm.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.forg_usrnm.setObjectName("forg_usrnm")
                self.gridLayout_2.addWidget(self.forg_usrnm, 4, 0, 1, 1)
                self.ID_lbl = QtWidgets.QLabel(self.frame)
                self.ID_lbl.setMinimumSize(QtCore.QSize(170, 60))
                self.ID_lbl.setMaximumSize(QtCore.QSize(170, 60))
                font = QtGui.QFont()
                font.setFamily("Vazir")
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.ID_lbl.setFont(font)
                self.ID_lbl.setLayoutDirection(QtCore.Qt.RightToLeft)
                self.ID_lbl.setStyleSheet("color: #fff;")
                self.ID_lbl.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
                self.ID_lbl.setObjectName("ID_lbl")
                self.gridLayout_2.addWidget(self.ID_lbl, 2, 3, 1, 1)
                self.back_btn = QtWidgets.QPushButton(self.frame)
                self.back_btn.setMinimumSize(QtCore.QSize(0, 80))
                self.back_btn.setMaximumSize(QtCore.QSize(16777215, 80))
                font = QtGui.QFont()
                font.setFamily("Vazir")
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.back_btn.setFont(font)
                self.back_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.back_btn.setObjectName("back_btn")
                self.gridLayout_2.addWidget(self.back_btn, 6, 0, 1, 1)
                self.verticalLayout_8.addWidget(self.frame, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
                self.stackedWidget.addWidget(self.forgpass)
                self.AdminP = QtWidgets.QWidget()
                self.AdminP.setObjectName("AdminP")
                self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.AdminP)
                self.verticalLayout_9.setObjectName("verticalLayout_9")
                self.body_hold = QtWidgets.QFrame(self.AdminP)
                self.body_hold.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.body_hold.setFrameShadow(QtWidgets.QFrame.Raised)
                self.body_hold.setObjectName("body_hold")
                self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.body_hold)
                self.horizontalLayout_4.setObjectName("horizontalLayout_4")
                self.logo_holder = QtWidgets.QTextEdit(self.body_hold)
                self.logo_holder.setObjectName("logo_holder")
                self.logo_holder.setReadOnly(True)
                self.horizontalLayout_4.addWidget(self.logo_holder)
                self.side_menu_3 = QtWidgets.QFrame(self.body_hold)
                self.side_menu_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.side_menu_3.setFrameShadow(QtWidgets.QFrame.Raised)
                self.side_menu_3.setObjectName("side_menu_3")
                self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.side_menu_3)
                self.verticalLayout_10.setObjectName("verticalLayout_10")
                self.hm_3 = QtWidgets.QPushButton(self.side_menu_3)
                font = QtGui.QFont()
                font.setFamily("Vazir")
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.hm_3.setFont(font)
                self.hm_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.hm_3.setObjectName("hm_3")
                self.verticalLayout_10.addWidget(self.hm_3)
                self.btn1_3 = QtWidgets.QPushButton(self.side_menu_3)
                font = QtGui.QFont()
                font.setFamily("Vazir")
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.btn1_3.setFont(font)
                self.btn1_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.btn1_3.setObjectName("btn1_3")
                self.verticalLayout_10.addWidget(self.btn1_3)
                self.btn3_3 = QtWidgets.QPushButton(self.side_menu_3)
                font = QtGui.QFont()
                font.setFamily("Vazir")
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.btn3_3.setFont(font)
                self.btn3_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.btn3_3.setObjectName("btn3_3")
                self.verticalLayout_10.addWidget(self.btn3_3)
                self.btn4_3 = QtWidgets.QPushButton(self.side_menu_3)
                font = QtGui.QFont()
                font.setFamily("Vazir")
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.btn4_3.setFont(font)
                self.btn4_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.btn4_3.setObjectName("btn4_3")
                self.verticalLayout_10.addWidget(self.btn4_3)
                self.btn5_3 = QtWidgets.QPushButton(self.side_menu_3)
                font = QtGui.QFont()
                font.setFamily("Vazir")
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.btn5_3.setFont(font)
                self.btn5_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.btn5_3.setObjectName("btn5_3")
                self.verticalLayout_10.addWidget(self.btn5_3)
                self.btn6_3 = QtWidgets.QPushButton(self.side_menu_3)
                font = QtGui.QFont()
                font.setFamily("Vazir")
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.btn6_3.setFont(font)
                self.btn6_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.btn6_3.setObjectName("btn6_3")
                self.verticalLayout_10.addWidget(self.btn6_3)
                self.btn7_3 = QtWidgets.QPushButton(self.side_menu_3)
                font = QtGui.QFont()
                font.setFamily("Vazir")
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.btn7_3.setFont(font)
                self.btn7_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.btn7_3.setObjectName("btn7_3")
                self.verticalLayout_10.addWidget(self.btn7_3)
                self.btn9_3 = QtWidgets.QPushButton(self.side_menu_3)
                font = QtGui.QFont()
                font.setFamily("Vazir")
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.btn9_3.setFont(font)
                self.btn9_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.btn9_3.setObjectName("btn9_3")
                self.verticalLayout_10.addWidget(self.btn9_3)
                self.horizontalLayout_4.addWidget(self.side_menu_3, 0, QtCore.Qt.AlignRight)
                self.verticalLayout_9.addWidget(self.body_hold)
                self.stackedWidget.addWidget(self.AdminP)
                self.verticalLayout.addWidget(self.stackedWidget)
                MainWindow.setCentralWidget(self.centralwidget)

                self.retranslateUi(MainWindow)
                self.stackedWidget.setCurrentIndex(0)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "باشگاه یار"))
                self.passw_txt.setPlaceholderText(_translate("MainWindow", "رمز خود را وارد کنید"))
                self.usernm_lbl.setText(_translate("MainWindow", "نام کاربری :"))
                self.usernm_txt.setPlaceholderText(_translate("MainWindow", "نام کاربری خود را وارد کنید"))
                self.submit_btn.setText(_translate("MainWindow", "ورود"))
                self.reg_btn.setText(_translate("MainWindow", "ثبت مدیر/ادمین جدید"))
                self.passw_lbl.setText(_translate("MainWindow", "گذرواژه / رمز عبور:"))
                self.ablg_btn.setText(_translate("MainWindow", "در باره برنامه"))
                self.forgpass_btn.setText(_translate("MainWindow", "رمز خود را فراموش کرده ام"))
                self.frm_lbl.setText(_translate("MainWindow", "به باشگاه یار خوش آمدید"))
                self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
        "<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
        "<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt; font-weight:600;\"><br /></p>\n"
        "<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt; font-weight:600;\"><br /></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"./pics/main1.png\" /></p>\n"
        "<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
                self.hm.setText(_translate("MainWindow", "خانه"))
                self.btn1.setText(_translate("MainWindow", "اعضا / جدید"))
                self.btn2.setText(_translate("MainWindow", "ادمین ها / جدید"))
                self.btn3.setText(_translate("MainWindow", "یادداشت جدید"))
                self.btn4.setText(_translate("MainWindow", "پشتیبان گیری اطلاعات"))
                self.btn5.setText(_translate("MainWindow", "ثبت درخواست"))
                self.btn6.setText(_translate("MainWindow", "مدیریت درخواست ها"))
                self.btn7.setText(_translate("MainWindow", "مدیا پلیر"))
                self.btn8.setText(_translate("MainWindow", "در باره برنامه"))
                self.btn9.setText(_translate("MainWindow", "خروج از حساب"))
                self.head_lbl.setText(_translate("MainWindow", "برای باز یابی رمز خود فرم زیر را پر کنید"))
                self.confirm_btn.setText(_translate("MainWindow", "تایید"))
                self.ID_txt.setPlaceholderText(_translate("MainWindow", "کد ملی خود را وارد کنید"))
                self.usrnm_txt.setPlaceholderText(_translate("MainWindow", "نام کاربری خود را وارد کنید"))
                self.usrnm_lbl.setText(_translate("MainWindow", " نام کاربری :"))
                self.forg_usrnm.setText(_translate("MainWindow", "نام کاربری خود را فراموش کرده ام"))
                self.ID_lbl.setText(_translate("MainWindow", " کد ملی :"))
                self.back_btn.setText(_translate("MainWindow", "بازگشت"))
                self.logo_holder.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
        "<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
        "<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt; font-weight:600;\"><br /></p>\n"
        "<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt; font-weight:600;\"><br /></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"./pics/main1.png\" /></p>\n"
        "<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
                self.hm_3.setText(_translate("MainWindow", "خانه"))
                self.btn1_3.setText(_translate("MainWindow", "اعضا / جدید"))
                self.btn3_3.setText(_translate("MainWindow", "یادداشت ها / جدید"))
                self.btn4_3.setText(_translate("MainWindow", "ثبت درخواست"))
                self.btn5_3.setText(_translate("MainWindow",  "مدیا پلیر"))
                self.btn6_3.setText(_translate("MainWindow", "مدیریت درخواست ها"))
                self.btn7_3.setText(_translate("MainWindow", "در باره برنامه"))
                self.btn9_3.setText(_translate("MainWindow", "خروج از حساب"))