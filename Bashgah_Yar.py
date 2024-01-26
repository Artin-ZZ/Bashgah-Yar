## Import All Global Libs Here ##
import sys, sqlite3, hashlib, os, secrets, re
import pandas as pd
from sqlalchemy import create_engine
from PyQt5.QtGui import QIntValidator, QFont, QIcon
from PyQt5 import QtGui, QtCore
from sqlite3 import Error
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
## Local Libs ##
from Update.Structure.GYM_UI import Gym_Ui
from Update.Structure.Media_Pl_Ui import Ui_MainWindow_Mp
from MERCFRM_Driver import ManageRequests
from Update.Structure.Note_Pad_Ui import Root_Npad
from Update.Structure.Sales_Form_UI import SalesForm
from Update.Root.Settings.config import ADMIN_DB_FILE, MEMBER_DB_FILE, SALES_DB_FILE
from Update.Root.Settings.Helpers import randomSEC_KEY
from MADFRM_Driver import ManageMembers
from AMDFRM_Driver import ManageAdmins



class ROOT(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        # Set the window icon
        icon = QIcon('pics/main1.png')
        self.setWindowIcon(icon)
        ## Setting Up Our Ui:
        self.ui = Gym_Ui()
        self.ui.setupUi(self)
        ## Now We have To Set up The Other buttons Of Our Ui File:
        ##----------- Login Page Index No: 0 ---------------##
        self.ui.ablg_btn.clicked.connect(self.about_me_small)
        self.ui.forgpass_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.reg_btn.clicked.connect(self.regAdmin)
        self.ui.submit_btn.clicked.connect(self.loginBtn)
        ##----------- Home Page Index No: 1 ---------------##
        self.ui.hm.clicked.connect(self.alertHo)
        self.ui.btn1.clicked.connect(self.addMembers)
        self.ui.btn2.clicked.connect(self.addAdmins)
        self.ui.btn3.clicked.connect(self.notePad)
        self.ui.btn4.clicked.connect(self.infoBackUp)
        self.ui.btn5.clicked.connect(self.salesp)
        self.ui.btn6.clicked.connect(self.manageReqs)
        self.ui.btn7.clicked.connect(self.media_pl)
        self.ui.btn8.clicked.connect(self.about_me_big)
        self.ui.btn9.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        ##----------- Forgot Password Page Index No: 2 ---------------##
        self.ui.forg_usrnm.clicked.connect(self.forgotUserName)
        self.ui.confirm_btn.clicked.connect(self.confirm_see_results)
        self.ui.back_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        ##----------- Admin Page Index No: 3 ---------------##
        self.ui.hm_3.clicked.connect(self.alertHo)
        self.ui.btn1_3.clicked.connect(self.addMembers)
        self.ui.btn3_3.clicked.connect(self.notePad)
        self.ui.btn4_3.clicked.connect(self.salesp)
        self.ui.btn6_3.clicked.connect(self.manageReqs)
        self.ui.btn5_3.clicked.connect(self.media_pl)
        self.ui.btn7_3.clicked.connect(self.about_me_big)
        self.ui.btn9_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
                
    ## CLOSE EVENT ##
    def closeEvent_dg(self, event):
        # Display a confirmation dialog when closing the window
        reply = QMessageBox.question(
            self,
            'هشدار خروج',
            'آیا می خواهید از برنامه خارج شوید؟',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()  # Close the window
        else:
            event.ignore()  # Keep the window open
    
    
    
    
         
    ## Query Data Bind:
    def query(self, sql: str, data_bind: list = []):

        # Check required params
        if not sql:
            # Raise error
            raise Exception("You must provide the required parameters: ['sql']")

        # Try to query to the database
        try:
            # Return the query result
            self.c.execute(sql, data_bind)

            return self.c

        # Catch error
        except Error as e:
            # Raise error
            raise Exception(e)
    
    def userNameChek(self, username):
        self.con = sqlite3.connect(ADMIN_DB_FILE)
        self.c = self.con.cursor()
        sql = """
            SELECT * FROM admininfo
            WHERE username = ?;
        """
        data = [username]
        if self.query(sql, data).fetchone():
            return self.query(sql, data).fetchone()
        else:
            return False
    
    def isIdValid(self, id):
        self.con = sqlite3.connect(ADMIN_DB_FILE)
        self.c = self.con.cursor()
        sql = """
            SELECT * FROM admininfo
            WHERE identity_id = ?;
        """
        data = [id]
        if self.query(sql, data).fetchone():
            return self.query(sql, data).fetchone()
        else:
            return False
    
                
    ### Button Functions ###
    ## Alert Support ##
    def alertSup(self):
        QMessageBox.warning(QMessageBox(),"یادآوری"," شما در صفحه پشتیبانی هستید")
        
    ## Alert Home ##
    def alertHo(self):
        QMessageBox.warning(QMessageBox(),"یادآوری"," شما در صفحه خانه هستید")
        
    ## about me small ##
    def about_me_small(self):
        QMessageBox.information(QMessageBox(),"در باره برنامه","برنامه باشگاه یار ورژن 1.2.0  \nساخته وتوسعه یافته توسط artinZZ")
        
    ## Register Admin ##
    def regAdmin(self):
        dlg = RegAdminDialog()
        dlg.exec_()
    
    ## Frog USERNAME ##
    def forgotUserName(self):
        dlg = RetriveUsernm()
        dlg.exec_()
    
    def media_pl(self):
        self.window1 = Media_Player()
        if self.window1.isVisible():
            self.window1.show()
        else:
            self.window1.hide()
    
    ## Manage Requests ##
    def manageReqs(self):
        self.window1 = ManageRequests()
        if self.window1.isVisible():
            self.window1.hide()
        else:
            self.window1.show()

    ## Forgot Password Btn ##
    def confirm_see_results(self):
        icon = QIcon('pics/main1.png')
        self.setWindowIcon(icon)
        
        uname = self.ui.usrnm_txt.text()
        ID = self.ui.ID_txt.text()
        
        if not uname or not ID:
            QMessageBox.warning(self, "هشدار", "همه فیلد ها را پرکنید")
            return
        
        try:
            self.con = sqlite3.connect(ADMIN_DB_FILE)
            self.c = self.con.cursor()
            result = self.c.execute("SELECT * FROM admininfo WHERE username = ? AND identity_id = ?", (uname,ID))
            row = result.fetchone()
            
            if row and self.userNameChek(username=uname) and self.isIdValid(id=ID):
                self.ui.usrnm_txt.clear()
                self.ui.ID_txt.clear()
                dlg = ResetPassword()
                dlg.exec_()
            else:
                QMessageBox.warning(self, 'خطا', 'مدیر / ادمین مورد نظر پیدا نشد یا وجود ندارد یا اطلاعات وارد شده نادرست است')
                self.ui.usrnm_txt.clear()
                self.ui.ID_txt.clear()
        except Exception as e:
            QMessageBox.warning(self, 'خطا', f'خطا در جستجو: {str(e)}')
            self.ui.usrnm_txt.clear()
            self.ui.ID_txt.clear()

    ##Log In Btn ##
    def loginBtn(self):
        username = self.ui.usernm_txt.text()
        entered_password = self.ui.passw_txt.text()
        
        
        
        try:
            # Connect to the SQLite database.
            conn = sqlite3.connect(ADMIN_DB_FILE)
            cursor = conn.cursor()
            
            # Query the database to retrieve the hashed password and role.
            cursor.execute("SELECT password, role, salt FROM admininfo WHERE username=?", (username,))
            result = cursor.fetchone()
            
            if not username or not entered_password:
                QMessageBox.warning(QMessageBox(),"هشدار","تمام فیلد هارا پر کنید")
                
                
            else:
                if result:
                    hashed_password_db, role, salt_db = result
                    entered_password_bytes = entered_password.encode('utf-8')

                    # Concatenate the entered password and salt, then hash them
                    entered_password_hash = hashlib.sha256(entered_password_bytes + salt_db).hexdigest()

                    if entered_password_hash == hashed_password_db:
                        if role == 'مدیر(مربی)':
                            self.ui.usernm_txt.clear()
                            self.ui.passw_txt.clear()
                            self.ui.stackedWidget.setCurrentIndex(1)  # Index 1 for CEO panel
                            
                        elif role == 'ادمین':
                            self.ui.usernm_txt.clear()
                            self.ui.passw_txt.clear()
                            self.ui.stackedWidget.setCurrentIndex(3)  # Index 3 for Admin panel
                        else:
                            QMessageBox.warning(self, 'منع دسترسی', 'شما دسترسی های لازم را برای ورود به سیستم ندارید')
                            self.ui.usernm_txt.clear()
                            self.ui.passw_txt.clear()
                    else:
                        QMessageBox.warning(self, 'خطا در ورود', 'نام کاربری یا رمز عبور اشتباه است')
                        self.ui.usernm_txt.clear()
                        self.ui.passw_txt.clear()
                else:
                    QMessageBox.warning(self, 'خطا در ورود', 'نام کاربری یا رمز عبور اشتباه است')
                    self.ui.usernm_txt.clear()
                    self.ui.passw_txt.clear()

            conn.close()

        except sqlite3.Error as e:
            QMessageBox.warning(self, 'خطا', f'خطا در ورود: {str(e)}')
            self.ui.usernm_txt.clear()
            self.ui.passw_txt.clear()
            
            
    
    ## Add Members ##
    def addMembers(self):
        self.window1 = ManageMembers()
        if self.window1.isVisible():
            self.window1.hide()
        else:
            self.window1.show()
    
    ## Add Admins ##
    def addAdmins(self):
        self.window1 = ManageAdmins()
        if self.window1.isVisible():
            self.window1.hide()
        else:
            self.window1.show()
    
    ## Note Pad ##
    def notePad(self):
        self.window1 = Root_Npad()
        if self.window1.isVisible():
            self.window1.show()
        else:
            self.window1.hide()

    
    ## Edit Admind ##
    def infoBackUp(self):
        dlg = INFOBUP()
        dlg.exec_()
    
    ## Edit Members ##
    def salesp(self):
        dlg = SalesP()
        dlg.exec_()
        
    ## About Me Big ##
    def about_me_big(self):
        dlg = About_App()
        dlg.exec_()


#### Sport Program page ####
class SalesP(QDialog):
    def __init__(self, *args, **kwargs) -> None:
        super(SalesP, self).__init__(*args, **kwargs)
        
        self.saui = SalesForm()
        self.saui.setupUi(self)
        
        ### Main Window ###
        self.setWindowTitle("ثبت درخواست جدید")
        icon = QIcon('pics/newreq.png')
        self.setWindowIcon(icon)
        
        ### Window Buttns Setup ###
        self.saui.submitbtn.clicked.connect(self.submitFormAction)
        self.saui.closebtn.clicked.connect(self.close)
            
            
        # Creating The Data Base
        self.conn = sqlite3.connect(SALES_DB_FILE)
        self.c = self.conn.cursor()
        self.c.execute("""
        CREATE TABLE IF NOT EXISTS salesinfo (
            id INTEGER NOT NULL PRIMARY KEY,
            date VARCHAR(150) NOT NULL,
            fullname VARCHAR(150) NOT NULL,
            req_subject VARCHAR(255) NOT NULL,
            req_item VARCHAR(255) NOT NULL,
            price FLOAT NOT NULL,
            saleno VARCHAR(255) NOT NULL UNIQUE,
            adrs TEXT NOT NULL,
            phone INTEGER NOT NULL,
            req_stat VARCHAR(100) NOT NULL,
            regerfnm VARCHAR(150) NOT NULL,
            read_user BOOLEAN DEFAULT False
        );""")
        self.c.close()
        
    
    def submitFormAction(self):
        date = self.saui.date_txt.text()
        fullname = self.saui.fname_txt.text()
        req_subject = self.saui.weandhe_txt.text()
        req_item = self.saui.workoutd_txt.text()
        pricetag = self.saui.price_tag_txt.text()
        salenum = self.saui.saleno_txt.text()
        adrs = self.saui.movename_txt.text()
        phone = self.saui.phone_txt.text()
        reqstat = self.saui.reqstat_txt.itemText(self.saui.reqstat_txt.currentIndex())
        regername = self.saui.regerfname_txt.text()
        
            
        ### Hide DB Files After Creating For More Security ###
        # Check if the file exists
        if os.path.exists(SALES_DB_FILE):
            try:
                # Set the file as hidden
                os.system(f'attrib +h "{SALES_DB_FILE}"')
                print("Every Thing Works Fine")
            except Exception as e:
                print(f"Error hiding {SALES_DB_FILE}: {e}")
        else:
            print("There IS Some Error Contact Support.")
            
        if not date or not fullname or not req_subject or not req_item or not pricetag or not salenum or not adrs or not phone or not reqstat or not regername:
            QMessageBox.warning(self, 'هشدار', 'لطفاً تمام فیلدها را پر کنید')
            return
        
        try:
            self.conn = sqlite3.connect(SALES_DB_FILE)
            self.c = self.conn.cursor()
            self.c.execute(
                "INSERT INTO salesinfo(date, fullname, req_subject, req_item, price, saleno, adrs, phone, req_stat, regerfnm) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (date, fullname, req_subject, req_item, pricetag, salenum, adrs, phone, reqstat, regername))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(self, 'موفقیت آمیز', 'درخواست با موفقیت ثبت شد')
            self.close()
        except sqlite3.Error as e:
            QMessageBox.warning(self, 'خطا', f'خطا در ثبت درخواست: {str(e)}')
        
        
        
#### Retrive UserName ###
class RetriveUsernm(QDialog):
    def __init__(self, *args, **kwargs) -> None:
        super(RetriveUsernm, self).__init__(*args, **kwargs)
        
        # Window Font #
        font = QFont()
        font.setBold(True)
        font.setPointSize(16)
        font.setFamily("Vazir")
        
        # Main Window #
        self.setWindowTitle("بازیابی نام کاربری")
        icon = QIcon('pics/reset.png')
        self.setWindowIcon(icon)
        self.setFixedWidth(500)
        self.setFixedHeight(300)
        self.setFont(font)
        self.setObjectName("mainusrres")
        self.setStyleSheet("\n"
            "#mainusrres{\n"
            "    background-image: url(./pics/bc.png);\n"
            "    background-repeat: no-repeat;\n"
            "    background-position: center center;\n"
            "}\n"
            "#idinput{\n"
            "    background: transparent;\n"
            "    border: none;\n"
            "    border-bottom: 5px solid lime;\n"
            "    padding: 10px;\n"
            "    color: #000;\n"
            "}\n"
            "#confBtn{\n"
            "    background-image: url(./pics/btn_login4.png);\n"
            "    background-repeat: no-repeat;\n"
            "    background-position: center center;\n"
            "    padding: 20px;\n"
            "    border-radius: 30px;\n"
            "}\n"
            "#confBtn:hover{\n"
            "    background-image: url(./pics/btn_login3.png);\n"
            "    background-repeat: no-repeat;\n"
            "    background-position: center center;\n"
            "    padding: 20px;\n"
            "    border-radius: 30px;\n"
            "}\n"
            "#confBtn:pressed{\n"
            "    background-image: url(./pics/btn_login2.png);\n"
            "    background-repeat: no-repeat;\n"
            "    background-position: center center;\n"
            "    padding: 20px;\n"
            "    border-radius: 30px;\n"
            "}\n")
        
        layout = QVBoxLayout()
        
        self.id_input = QLineEdit()
        id_hide_conf = self.id_input
        id_hide_conf.setEchoMode(QLineEdit.Password)
        self.id_input.setPlaceholderText("کدملی خود را وارد کنید")
        self.id_input.setObjectName("idinput")
        
        self.confbtn = QPushButton()
        self.confbtn.setText("تایید")
        self.confbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.confbtn.setObjectName("confBtn")
        self.confbtn.clicked.connect(self.conf_Action)
        
        self.setLayout(layout)
        layout.addWidget(self.id_input)
        layout.addWidget(self.confbtn)
    
    def conf_Action(self):
        idpromt = self.id_input.text()
        
        if not idpromt:
            QMessageBox.warning(self, 'هشدار', "کادر مورد نظر را پر بکنید")
            
        else:
            try:
                self.conn = sqlite3.connect(ADMIN_DB_FILE)
                self.c = self.conn.cursor()
                result = self.c.execute("SELECT * FROM admininfo WHERE identity_id = ?", (idpromt,))
                row = result.fetchone()
                if row:
                    result_str = (
                        f"| نام و نام خانوادگی : {row[1]}\n"
                        f"| کدملی : {row[6]}\n"
                        f"| نام کاربری : {row[7]}\n"
                    )
                    QMessageBox.information(self, f"Admin : {row[1]}", result_str)
                else:
                    QMessageBox.warning(self, 'هشدار', 'مدیر / ادمین مورد نظر پیدا نشد یا وجود ندارد')
                self.close()
            except Exception as e:
                QMessageBox.warning(self, 'خطا', f'خطا در بازیابی: {str(e)}')

#### Reset Password Page ####
class ResetPassword(QDialog):
    def __init__(self, *args, **kwargs) -> None:
        super(ResetPassword, self).__init__(*args, **kwargs)
        
        # Window Font #
        font = QFont()
        font.setBold(True)
        font.setPointSize(16)
        font.setFamily("Vazir")
        
        # Main Window #
        self.setWindowTitle("بازیابی رمزعبور")
        icon = QIcon('pics/reset.png')
        self.setWindowIcon(icon)
        self.setFixedWidth(500)
        self.setFixedHeight(500)
        self.setFont(font)
        self.setObjectName("mainresp")
        self.setStyleSheet("\n"
        "#mainresp{\n"
            "    background-image: url(./pics/bc.png);\n"
            "    background-repeat: no-repeat;\n"
            "    background-position: center center;\n"
            "}\n"
            "#okbtn{\n"
            "    background-image: url(./pics/btn_login4.png);\n"
            "    background-repeat: no-repeat;\n"
            "    background-position: center center;\n"
            "    padding: 20px;\n"
            "    border-radius: 30px;\n"
            "}\n"
            "#okbtn:hover{\n"
            "    background-image: url(./pics/btn_login3.png);\n"
            "    background-repeat: no-repeat;\n"
            "    background-position: center center;\n"
            "    padding: 20px;\n"
            "    border-radius: 30px;\n"
            "}\n"
            "#okbtn:pressed{\n"
            "    background-image: url(./pics/btn_login2.png);\n"
            "    background-repeat: no-repeat;\n"
            "    background-position: center center;\n"
            "    padding: 20px;\n"
            "    border-radius: 30px;\n"
            "}\n"
            "#pass_input_txt{\n"
            "    background: transparent;\n"
            "    border: none;\n"
            "    border-bottom: 5px solid lime;\n"
            "    padding: 10px;\n"
            "    color: #000;\n"
            "}\n"
            "#pass_input_confirm_txt{\n"
            "    background: transparent;\n"
            "    border: none;\n"
            "    border-bottom: 5px solid lime;\n"
            "    padding: 10px;\n"
            "    color: #000;\n"
            "}\n"
            "#uname{\n"
            "    background: transparent;\n"
            "    border: none;\n"
            "    border-bottom: 5px solid lime;\n"
            "    padding: 10px;\n"
            "    color: #000;\n"
            "}\n"
            )
        
        layout = QVBoxLayout()
        
        self.pass_input = QLineEdit()
        self.pass_input.setPlaceholderText("رمزعبور جدید را وارد کنید")
        pass_hide = self.pass_input
        pass_hide.setEchoMode(QLineEdit.Password)
        self.pass_input.setObjectName("pass_input_txt")
        
        self.pass_input_confirm = QLineEdit()
        pass_hide_conf = self.pass_input_confirm
        pass_hide_conf.setEchoMode(QLineEdit.Password)
        self.pass_input_confirm.setPlaceholderText("تایید رمزعبور جدید")
        self.pass_input_confirm.setObjectName("pass_input_confirm_txt")
        
        self.uname = QLineEdit()
        self.uname.setPlaceholderText("نام کاربری")
        self.uname.setObjectName("uname")
        
        self.ok_btn = QPushButton()
        self.ok_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ok_btn.setText("اعمال رمز جدید")
        self.ok_btn.setObjectName("okbtn")
        self.ok_btn.clicked.connect(self.confAction)
        
        self.setLayout(layout)
        layout.addWidget(self.uname)
        layout.addWidget(self.pass_input)
        layout.addWidget(self.pass_input_confirm)
        layout.addWidget(self.ok_btn)
    
    ## Hash Password Function ##
    def hash_password(self, password, salt):
        # Encode the provided password as bytes
        password_bytes = password.encode('utf-8')
        # Combine the password and salt, then hash them
        hashed_password = hashlib.sha256(password_bytes + salt).hexdigest()
        return hashed_password
    
    def is_valid_password(self, password):
        # Define the regex pattern for a valid password
        # This pattern enforces the following rules:
        # - At least 8 characters long
        # - Contains at least one lowercase letter
        # - Contains at least one uppercase letter
        # - Contains at least one digit
        # - Contains at least one special character (e.g., !@#$%^&*)
        pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
        
        # Use re.match to check if the password matches the pattern
        if re.match(pattern, password):
            return True
        else:
            return False

    ## Confirm Button ##
    def confAction(self):
        pass_input = self.pass_input.text()
        confirm_pass_input = self.pass_input_confirm.text()
        username = self.uname.text()
        
        try:
            if not pass_input or not confirm_pass_input:
                QMessageBox.warning(self, 'هشدار', 'لطفاً تمام فیلدها را پر کنید')
                return
            
            elif pass_input != confirm_pass_input:
                QMessageBox.warning(self, "هشدار", "رمزعبور و تایید رمزعبور باهم مطابقت ندارد")
                self.pass_input.clear()
                self.pass_input_confirm.clear()
                self.uname.clear()
                return
                
            
            elif not self.is_valid_password(confirm_pass_input):
                QMessageBox.warning(self, "هشدار", "رمزعبور باید 8 کاراکتر یا بیشتر و باید حداقل دارای یک حرف کوچک و بزرگ و یک عدد و یک کاراکتر خاص(@ $ ! % * ? &) باشد")
                self.pass_input.clear()
                self.pass_input_confirm.clear()
                self.uname.clear()
                return
            
        except sqlite3.Error as e:
            QMessageBox.warning(self, 'خطا', f'خطا در ثبت نام ادمین / مدیر: {str(e)}')

        # Retrieve the salt from the database
        try:
            with sqlite3.connect(ADMIN_DB_FILE) as conn:
                cursor = conn.cursor()
                # Execute the query to retrieve the salt
                cursor.execute("SELECT salt FROM admininfo WHERE username=?", (username,))
                salt_db = cursor.fetchone()
                if salt_db:
                    salt_db = salt_db[0]  # Extract the salt from the result
                    # Hash the password using the retrieved salt
                    hashed_password = self.hash_password(confirm_pass_input, salt_db)

                    UPDATE = "UPDATE admininfo SET password=?, salt=? WHERE username=?"

                    try:
                        if pass_input == confirm_pass_input:
                            with sqlite3.connect(ADMIN_DB_FILE) as conn:
                                cursor = conn.cursor()
                                cursor.execute(UPDATE, (hashed_password, salt_db, username))
                                conn.commit()
                            QMessageBox.information(self, "موفقیت", "رمزعبور با موفقیت تغییر یافت")
                            self.uname.clear()
                            self.pass_input.clear()
                            self.pass_input_confirm.clear()
                        else:
                            QMessageBox.warning(QMessageBox(),"خطا","رمز عبور و تایید رمزعبور مطابقت ندارد")
                            self.uname.clear()
                            self.pass_input.clear()
                            self.pass_input_confirm.clear()
                    except sqlite3.Error as e:
                        QMessageBox.critical(self, "خطا", f"خطا در به‌روزرسانی اطلاعات: {str(e)}")
                        self.uname.clear()
                        self.pass_input.clear()
                        self.pass_input_confirm.clear()
                else:
                    QMessageBox.warning(self, "هشدار", "مدیر / ادمین با این نام وجود ندارد.")
                    self.uname.clear()
                    self.pass_input.clear()
                    self.pass_input_confirm.clear()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "خطا", f"خطا در اتصال به دیتابیس: {str(e)}")
            self.uname.clear()
            self.pass_input.clear()
            self.pass_input_confirm.clear()
        
    
#### INFO BACKUP CLASS ####
class INFOBUP(QDialog):
    def __init__(self, *args, **kwargs):
        super(INFOBUP, self).__init__(*args, **kwargs)
        
        # Window Font #
        font = QFont()
        font.setBold(True)
        font.setPointSize(16)
        font.setFamily("Vazir")
                
        # Main Window #
        self.setWindowTitle("پشتیبان گیری از اطلاعات")
        icon = QIcon('pics/bup.png')
        self.setWindowIcon(icon)
        self.setFixedWidth(500)
        self.setFixedHeight(300)
        self.setFont(font)
        self.setObjectName("mainp")
        self.setStyleSheet("\n"
            "#mainp{\n"
            "    background-image: url(./pics/bc.png);\n"
            "    background-repeat: no-repeat;\n"
            "    background-position: center center;\n"
            "}\n"
            "#aad{\n"
            "    background-image: url(./pics/btn_login4.png);\n"
            "    background-repeat: no-repeat;\n"
            "    background-position: center center;\n"
            "    padding: 20px;\n"
            "    border-radius: 30px;\n"
            "}\n"
            "#aad:hover{\n"
            "    background-image: url(./pics/btn_login3.png);\n"
            "    background-repeat: no-repeat;\n"
            "    background-position: center center;\n"
            "    padding: 20px;\n"
            "    border-radius: 30px;\n"
            "}\n"
            "#aad:pressed{\n"
            "    background-image: url(./pics/btn_login2.png);\n"
            "    background-repeat: no-repeat;\n"
            "    background-position: center center;\n"
            "    padding: 20px;\n"
            "    border-radius: 30px;\n"
            "}\n"
            "#mmd{\n"
            "    background-image: url(./pics/btn_login4.png);\n"
            "    background-repeat: no-repeat;\n"
            "    background-position: center center;\n"
            "    padding: 20px;\n"
            "    border-radius: 30px;\n"
            "}\n"
            "#mmd:hover{\n"
            "    background-image: url(./pics/btn_login3.png);\n"
            "    background-repeat: no-repeat;\n"
            "    background-position: center center;\n"
            "    padding: 20px;\n"
            "    border-radius: 30px;\n"
            "}\n"
            "#mmd:pressed{\n"
            "    background-image: url(./pics/btn_login2.png);\n"
            "    background-repeat: no-repeat;\n"
            "    background-position: center center;\n"
            "    padding: 20px;\n"
            "    border-radius: 30px;\n"
            "}\n"
            "#sla{\n"
            "    background-image: url(./pics/btn_login4.png);\n"
            "    background-repeat: no-repeat;\n"
            "    background-position: center center;\n"
            "    padding: 20px;\n"
            "    border-radius: 30px;\n"
            "}\n"
            "#sla:hover{\n"
            "    background-image: url(./pics/btn_login3.png);\n"
            "    background-repeat: no-repeat;\n"
            "    background-position: center center;\n"
            "    padding: 20px;\n"
            "    border-radius: 30px;\n"
            "}\n"
            "#sla:pressed{\n"
            "    background-image: url(./pics/btn_login2.png);\n"
            "    background-repeat: no-repeat;\n"
            "    background-position: center center;\n"
            "    padding: 20px;\n"
            "    border-radius: 30px;\n"
            "}\n")
        
        # Buttons #
        self.aadbtn = QPushButton()
        self.aadbtn.setText("پشتیبان گیری اطلاعات ادمین ها")
        self.aadbtn.setObjectName("aad")
        self.aadbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.aadbtn.clicked.connect(self.aadAccept)
        
        self.mmdbtn = QPushButton()
        self.mmdbtn.setText("پشتیبان گیری اطلاعات اعضا")
        self.mmdbtn.setObjectName("mmd")
        self.mmdbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mmdbtn.clicked.connect(self.mmdAccept)
        
        self.sladbtn = QPushButton()
        self.sladbtn.setText("پشتیبان گیری اطلاعات درخواست ها")
        self.sladbtn.setObjectName("sla")
        self.sladbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sladbtn.clicked.connect(self.slaAccept)
        
        layout = QVBoxLayout()
        
        
        self.setLayout(layout)
        layout.addWidget(self.aadbtn)
        layout.addWidget(self.mmdbtn)
        layout.addWidget(self.sladbtn)
        
        
    def aadAccept(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_dialog = QFileDialog.getSaveFileName(self, "پشتیبان گیری ادمین ها", "", "Excel Files (*.xlsx)", options=options)
        file_path = file_dialog[0]

        if file_path:
            engineA = create_engine(f"sqlite:///{ADMIN_DB_FILE}")
            df = pd.read_sql_table("admininfo", con=engineA)
            new_df = pd.DataFrame(df)
            new_df.to_excel(file_path, index=False)

    def mmdAccept(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_dialog = QFileDialog.getSaveFileName(self, "پشتیبان گیری اعضا", "", "Excel Files (*.xlsx)", options=options)
        file_path = file_dialog[0]

        if file_path:
            engineM = create_engine(f"sqlite:///{MEMBER_DB_FILE}")
            df = pd.read_sql_table("membersinfo", con=engineM)
            new_df = pd.DataFrame(df)
            new_df.to_excel(file_path, index=False)
            
    def slaAccept(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_dialog = QFileDialog.getSaveFileName(self, "پشتیبان گیری درخواست ها", "", "Excel Files (*.xlsx)", options=options)
        file_path = file_dialog[0]

        if file_path:
            engineM = create_engine(f"sqlite:///{SALES_DB_FILE}")
            df = pd.read_sql_table("salesinfo", con=engineM)
            new_df = pd.DataFrame(df)
            new_df.to_excel(file_path, index=False)
            
            
            
            
            
            
#### ABOUT APP DIALOG ####
class About_App(QDialog):
    def __init__(self, *args, **kwargs):
        super(About_App, self).__init__(*args, **kwargs)
        
        # Window Font #
        font = QFont()
        font.setBold(True)
        font.setPointSize(16)
        font.setFamily("Vazir")
        
        
        # Main Window #
        self.setWindowTitle("درباره برنامه")
        icon = QIcon('pics/info.png')
        self.setWindowIcon(icon)
        self.setFixedWidth(750)
        self.setFixedHeight(600)
        self.setFont(font)
        
        
        QBtn = QDialogButtonBox.Ok
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        
        layout = QVBoxLayout()
        
        lbl_pic = QLabel()
        lbl_pic.setObjectName("lblpic")
        lbl_pic.setStyleSheet("\n"
            "#lblpic{\n"
            "    background-image: url(pics/gym_info.png);\n"
            "    background-repeat: no-repeat;\n"
            "    background-position: center center;\n"
            "}\n")
        
        layout.addWidget(lbl_pic)

        layout.addWidget(self.buttonBox)
        self.setLayout(layout)


#### REGISTER ADMINS ####
class RegAdminDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(RegAdminDialog, self).__init__(*args, **kwargs)
        
        # Window Font #
        font = QFont()
        font.setBold(True)
        font.setPointSize(16)
        font.setFamily("Vazir")
        
        # Main Window #
        self.setWindowTitle("ثبت نام ادمین")
        icon = QIcon('pics/add.png')
        self.setWindowIcon(icon)
        self.setFixedWidth(800)
        self.setFixedHeight(800)
        self.setFont(font)
        self.setObjectName("mainp")
        self.setStyleSheet("\n"
            "#mainp{\n"
            "    background-image: url(./pics/login_bg.jpg);\n"
            "    background-repeat: no-repeat;\n"
            "    background-position: center center;\n"
            "}\n"
            "#confbtn{\n"
            "    background-image: url(./pics/btn_login4.png);\n"
            "    background-repeat: no-repeat;\n"
            "    background-position: center center;\n"
            "    border-radius: 30px;\n"
            "    padding: 20px;\n"
            "}\n"
            "#confbtn:hover{\n"
            "    background-image: url(./pics/btn_login3.png);\n"
            "    background-repeat: no-repeat;\n"
            "    background-position: center center;\n"
            "    border-radius: 30px;\n"
            "    padding: 20px;\n"
            "}\n"
            "#confbtn:pressed{\n"
            "    background-image: url(./pics/btn_login2.png);\n"
            "    background-repeat: no-repeat;\n"
            "    background-position: center center;\n"
            "    border-radius: 30px;\n"
            "    padding: 20px;\n"
            "}\n"
            "#fname_txt{\n"
            "    background: transparent;\n"
            "    border: none;\n"
            "    border-bottom: 5px solid lime;\n"
            "    padding: 10px;\n"
            "    color: #000;\n"
            "}\n"
            "#age_txt{\n"
            "    background: transparent;\n"
            "    border: none;\n"
            "    border-bottom: 5px solid lime;\n"
            "    padding: 10px;\n"
            "    color: #000;\n"
            "}\n"
            "#phn_txt{\n"
            "    background: transparent;\n"
            "    border: none;\n"
            "    border-bottom: 5px solid lime;\n"
            "    padding: 10px;\n"
            "    color: #000;\n"
            "}\n"
            "#role_txt{\n"
            "    background: transparent;\n"
            "    border: none;\n"
            "    border-bottom: 5px solid lime;\n"
            "    padding: 10px;\n"
            "    color: #000;\n"
            "}\n"
            "#controlk_txt{\n"
            "    background: transparent;\n"
            "    border: none;\n"
            "    border-bottom: 5px solid lime;\n"
            "    padding: 10px;\n"
            "    color: #000;\n"
            "}\n"
            "#id_txt{\n"
            "    background: transparent;\n"
            "    border: none;\n"
            "    border-bottom: 5px solid lime;\n"
            "    padding: 10px;\n"
            "    color: #000;\n"
            "}\n"
            "#usr_txt{\n"
            "    background: transparent;\n"
            "    border: none;\n"
            "    border-bottom: 5px solid lime;\n"
            "    padding: 10px;\n"
            "    color: #000;\n"
            "}\n"
            "#pass_txt{\n"
            "    background: transparent;\n"
            "    border: none;\n"
            "    border-bottom: 5px solid lime;\n"
            "    padding: 10px;\n"
            "    color: #000;\n"
            "}\n"
            "#adrs_txt{\n"
            "    background: transparent;\n"
            "    border: none;\n"
            "    border-bottom: 5px solid lime;\n"
            "    padding: 10px;\n"
            "    color: #000;\n"
            "}\n"
            )

        # Creating The Data Base
        self.conn = sqlite3.connect(ADMIN_DB_FILE)
        self.c = self.conn.cursor()
        self.c.execute("""
        CREATE TABLE IF NOT EXISTS admininfo (
            id INTEGER NOT NULL PRIMARY KEY,
            full_name VARCHAR(60) NOT NULL,
            age INTEGER NOT NULL,
            phone_number INTEGER NOT NULL UNIQUE,
            role VARCHAR(100) NOT NULL,
            cont_key VARCHAR(255) NOT NULL UNIQUE,
            identity_id INTEGER NOT NULL UNIQUE,
            username VARCHAR(255) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL UNIQUE,
            adrs TEXT NOT NULL,
            salt BLOB,
            read_user BOOLEAN DEFAULT False
        );""")
        self.c.close()

        self.QBtn = QPushButton()
        self.QBtn.setText("تایید")
        self.QBtn.setObjectName("confbtn")
        self.QBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.QBtn.clicked.connect(self.addAdmin)

        layout = QVBoxLayout()

        self.nameinput = QLineEdit()
        self.nameinput.setObjectName("fname_txt")
        self.nameinput.setPlaceholderText("نام و نام خانوادگی خود را وارد کنید")
        layout.addWidget(self.nameinput)

        self.age = QLineEdit()
        self.age.setObjectName("age_txt")
        self.age.setPlaceholderText("سن خود را وارد کنید")
        onlyInt = QIntValidator()
        onlyInt.setRange(0,10)
        self.age.setValidator(onlyInt)
        layout.addWidget(self.age)

        self.phonenumber = QLineEdit()
        self.phonenumber.setObjectName("phn_txt")
        self.phonenumber.setPlaceholderText("شماره تماس خود را وارد کنید")
        self.phonenumber.setInputMask("99999999999")
        layout.addWidget(self.phonenumber)
        
        # Create a combo box
        self.role = QComboBox(self)
        self.role.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.role.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.role.setObjectName("role_txt")
        self.role.addItem("مدیر(مربی)")
        self.role.addItem("ادمین")
        layout.addWidget(self.role)
        
        self.control_key = QLineEdit(randomSEC_KEY())
        self.control_key.setObjectName("controlk_txt")
        onlyInt = QIntValidator()
        self.control_key.setValidator(onlyInt)
        self.control_key.setReadOnly(True)
        layout.addWidget(self.control_key)
        
        self.identityid = QLineEdit()
        self.identityid.setObjectName("id_txt")
        self.identityid.setPlaceholderText("کدملی خود را وارد کنید")
        onlyInt = QIntValidator()
        onlyInt.setRange(0,1000000000)
        self.identityid.setValidator(onlyInt)
        layout.addWidget(self.identityid)

        self.usernm = QLineEdit()
        self.usernm.setObjectName("usr_txt")
        self.usernm.setPlaceholderText("یک نام کاربری را انتخاب و وارد کنید")
        layout.addWidget(self.usernm)
        
        self.passw = QLineEdit()
        self.passw.setObjectName("pass_txt")
        self.passw.setPlaceholderText("یک رمز را انتخاب و وارد کنید")
        passw_hide = self.passw
        passw_hide.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.passw)
        
        self.addrs = QLineEdit()
        self.addrs.setObjectName("adrs_txt")
        self.addrs.setPlaceholderText("آدرس خانه خود را وارد کنید(خلاصه وار)")
        layout.addWidget(self.addrs)
        

        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def hash_password(self):
        salt = secrets.token_hex(16)
        password = self.passw.text().encode('utf-8')  # Extract text and encode it
        salt = salt.encode('utf-8')  # Encode the salt
        # Combine the password and salt, then hash them
        hashed_password = hashlib.sha256(password + salt).hexdigest()
        return hashed_password, salt
    
    def is_valid_username(self, username):
        # Define the regular expression pattern
        pattern = r'^[a-zA-Z_][a-zA-Z0-9_]{4,29}$'
        
        # Use re.match to check if the username matches the pattern\
        if re.match(pattern, username):
            return True
        else:
            return False
        
    def is_valid_password(self, password):
        # Define the regex pattern for a valid password
        # This pattern enforces the following rules:
        # - At least 8 characters long
        # - Contains at least one lowercase letter
        # - Contains at least one uppercase letter
        # - Contains at least one digit
        # - Contains at least one special character (e.g., !@#$%^&*)
        pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
        
        # Use re.match to check if the password matches the pattern
        if re.match(pattern, password):
            return True
        else:
            return False
    
    def addAdmin(self):
        # Get data from input fields
        full_name = self.nameinput.text()
        age = self.age.text()
        phone_number = self.phonenumber.text()
        Role = self.role.itemText(self.role.currentIndex())
        controlk = self.control_key.text()
        identity_id = self.identityid.text()
        username = self.usernm.text()
        passw = self.passw.text()
        addrs = self.addrs.text()

        # Check if the file exists
        if os.path.exists(ADMIN_DB_FILE):
            try:
                # Set the file as hidden
                os.system(f'attrib +h "{ADMIN_DB_FILE}"')
                print("Everything Works Fine")
            except Exception as e:
                print(f"Error Operation Terminated: {e}")
        else:
            print("There IS Some Error Contact Support.")

        try:
            age = int(age)
            phone_number = int(phone_number)
            identity_id = int(identity_id)
        except ValueError:
            QMessageBox.warning(self, 'هشدار', 'لطفاً سن، شماره تماس، و کدملی را به صورت عددی وارد کنید')
            return
        
        try:
            if not full_name or not age or not phone_number or not Role or not identity_id or not username or not passw or not addrs:
                QMessageBox.warning(self, 'هشدار', 'لطفاً تمام فیلدها را پر کنید')
                return
            
            elif not self.is_valid_password(passw):
                QMessageBox.warning(self, "هشدار", "رمزعبور باید 8 کاراکتر یا بیشتر و باید حداقل دارای یک حرف کوچک و بزرگ و یک عدد و یک کاراکتر خاص(@ $ ! % * ? &) باشد")
                return
            
            elif not self.is_valid_username(username):
                QMessageBox.warning(self, "هشدار", "نام کاربری باید بین 5 تا 30 کاراکتر باشد و ترکیبی از حروف اعداد انگلیسی و آندرلاین باشد")
                return
            
        except sqlite3.Error as e:
            QMessageBox.warning(self, 'خطا', f'خطا در ثبت نام ادمین / مدیر: {str(e)}')
            
            
        try:
            with sqlite3.connect(ADMIN_DB_FILE) as conn:
                c = conn.cursor()
                if Role == "مدیر(مربی)":
                    c.execute("SELECT * FROM admininfo WHERE role='مدیر(مربی)'")
                    existing_ceo = c.fetchone()
                    if existing_ceo:
                        QMessageBox.critical(QMessageBox(), "خطای ثبت", "خطای نقض قوانین: فقط یک مدیر می تواند وجود داشته باشد")
                        return

                hashed_password, salt = self.hash_password()

                c.execute(
                    "INSERT INTO admininfo(full_name, age, phone_number, role, cont_key, identity_id, username, password, adrs, salt)"
                    "VALUES (?,?,?,?,?,?,?,?,?,?)",
                    (full_name, age, phone_number, Role, controlk, identity_id, username, hashed_password, addrs, salt))
                conn.commit()

            QMessageBox.information(self, 'موفقیت آمیز', 'ادمین / مدیر با موفقیت ثبت شد')
            self.close()
        except sqlite3.Error as e:
            QMessageBox.warning(self, 'خطا', f'خطا در ثبت نام ادمین / مدیر: {str(e)}')


### Media Player Class ###
##############################################################################################
def hhmmss(ms):
    # s = 1000
    # m = 60000
    # h = 360000
    s = round(ms / 1000)
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)
    return ("%d:%02d:%02d" % (h, m, s)) if h else ("%d:%02d" % (m, s))

class ViewerWindow(QMainWindow):
    state = pyqtSignal(bool)

    def closeEvent(self, e):
        # Emit the window state, to update the viewer toggle button.
        self.state.emit(False)

class PlaylistModel(QAbstractListModel):
    def __init__(self, playlist, *args, **kwargs):
        super(PlaylistModel, self).__init__(*args, **kwargs)
        self.playlist = playlist

    def data(self, index, role):
        if role == Qt.DisplayRole:
            media = self.playlist.media(index.row())
            return media.canonicalUrl().fileName()

    def rowCount(self, index):
        return self.playlist.mediaCount()

class Media_Player(QMainWindow, Ui_MainWindow_Mp):
    def __init__(self, *args, **kwargs):
        super(Media_Player, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.player = QMediaPlayer()
        

        self.player.error.connect(self.erroralert)
        self.player.play()
        

        # Setup the playlist.
        self.playlist = QMediaPlaylist()
        self.player.setPlaylist(self.playlist)

        # Add viewer for video playback, separate floating window.
        self.viewer = ViewerWindow(self)
        self.viewer.setWindowFlags(self.viewer.windowFlags() | Qt.WindowStaysOnTopHint)
        self.viewer.setMinimumSize(QSize(480, 360))
        self.viewer.setWindowTitle("Video Show")

        videoWidget = QVideoWidget()
        self.viewer.setCentralWidget(videoWidget)
        self.player.setVideoOutput(videoWidget)

        # Connect control buttons/slides for media player.
        self.playButton.pressed.connect(self.player.play)
        self.pauseButton.pressed.connect(self.player.pause)
        self.stopButton.pressed.connect(self.player.stop)
        self.volumeSlider.valueChanged.connect(self.player.setVolume)

        self.viewButton.toggled.connect(self.toggle_viewer)
        self.viewer.state.connect(self.viewButton.setChecked)

        self.previousButton.pressed.connect(self.playlist.previous)
        self.nextButton.pressed.connect(self.playlist.next)

        self.model = PlaylistModel(self.playlist)
        self.playlistView.setModel(self.model)
        self.playlist.currentIndexChanged.connect(self.playlist_position_changed)
        selection_model = self.playlistView.selectionModel()
        selection_model.selectionChanged.connect(self.playlist_selection_changed)

        self.player.durationChanged.connect(self.update_duration)
        self.player.positionChanged.connect(self.update_position)
        self.timeSlider.valueChanged.connect(self.player.setPosition)

        self.open_file_action.triggered.connect(self.open_file)
        self.actionOpen_Folder.triggered.connect(self.open_folder)
        self.actionClear_Play_List.triggered.connect(self.clearPlayList)

        self.setAcceptDrops(True)

        self.show()
    
    
    def clearPlayList(self):
        self.playlist.clear()
    
    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls():
            e.acceptProposedAction()
            
    def dropEvent(self, e):
        for url in e.mimeData().urls():
            self.playlist.addMedia(QMediaContent(url))

        self.model.layoutChanged.emit()

        if self.player.state() != QMediaPlayer.PlayingState:
            i = self.playlist.mediaCount() - len(e.mimeData().urls())
            self.playlist.setCurrentIndex(i)
            self.player.play()

    def open_file(self):
        path, _ = QFileDialog.getOpenFileName(
            self,
            "Open file",
            "",
            "mp3 Audio (*.mp3);;mp4 Video (*.mp4);;Movie files (*.mov);;All files (*.*)",
        )

        if path:
            self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile(path)))

        self.model.layoutChanged.emit()


    def open_folder(self):
        folder_path = QFileDialog.getExistingDirectory(
            self,
            "Open Folder",
            "",
            QFileDialog.ShowDirsOnly | QFileDialog.ReadOnly,
        )

        if folder_path:
            self.playlist.clear()
            self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile(folder_path)))
            self.model.layoutChanged.emit()

            media_files = [
                QUrl.fromLocalFile(folder_path + "/" + file)
                for file in os.listdir(folder_path)
                if file.lower().endswith((".mp3", ".mp4", ".ogg", ".flac", ".mkv"))
            ]

            for media_file in media_files:
                self.playlist.addMedia(QMediaContent(media_file))

            self.player.play()

    def update_duration(self, duration):
        self.timeSlider.setMaximum(duration)

        if duration >= 0:
            self.totalTimeLabel.setText(hhmmss(duration))

    def update_position(self, position):
        if position >= 0:
            self.currentTimeLabel.setText(hhmmss(position))

        self.timeSlider.blockSignals(True)
        self.timeSlider.setValue(position)
        self.timeSlider.blockSignals(False)

    def playlist_selection_changed(self, ix):
        i = ix.indexes()[0].row()
        self.playlist.setCurrentIndex(i)

    def playlist_position_changed(self, i):
        if i > -1:
            ix = self.model.index(i)
            self.playlistView.setCurrentIndex(ix)

    def toggle_viewer(self, state):
        if state:
            self.viewer.show()
        else:
            self.viewer.hide()

    def erroralert(self, *args):
        print(args)

##############################################################################################

######################
# Runs The Whole App #
######################
if __name__ == "__main__":
    app = QApplication([])
    root = ROOT()
    root.show()
    sys.exit(app.exec())