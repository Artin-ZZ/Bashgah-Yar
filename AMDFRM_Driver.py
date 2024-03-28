# Import the required libraries and modules
# For working with SQLite databases
import sqlite3
# For various operating system-related tasks
import os ,secrets ,hashlib
# For accessing system-specific parameters and functions
import re
# PyQt5 library modules
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import *
# Additional PyQt5 modules
from PyQt5 import QtCore
from PyQt5 import QtGui
## Local Libs ##
from Update.Root.Settings.config import MAIN_DB_FILE
from Update.Root.Settings.Helpers import randomSEC_KEY






class ManageAdmins(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(ManageAdmins, self).__init__(*args, **kwargs)
        
        ### Hide DB Files After Creating For More Security ###
        # Check if the file exists
        if os.path.exists(MAIN_DB_FILE):
            try:
                # Set the file as hidden
                os.system(f'attrib +h "{MAIN_DB_FILE}"')
                print("Every Thing Works Fine")
            except Exception as e:
                print(f"Error Operation Terminated: {e}")
        else:
            print("There IS Some Error Contact Support.")
        
        # Creating The Data Base
        self.conn = sqlite3.connect(MAIN_DB_FILE)
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
        
        ### Page Font ###
        font = QFont()
        font.setBold(True)
        font.setPointSize(10)
        font.setFamily("Vazir")
        ## main Window: The database Table That user Sees ##
        file_menu = self.menuBar().addMenu("&File")
        self.setWindowTitle("مدیریت ادمین ها")
        icon = QIcon('pics/mng_admin.png')
        self.setWindowIcon(icon)
        self.setMinimumSize(800, 800)
        self.setFont(font)

        self.tableWidget = QTableWidget()
        self.setCentralWidget(self.tableWidget)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setColumnCount(10)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.tableWidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tableWidget.setHorizontalHeaderLabels(("ردیف", "نام و نام خانوادگی", "سن", "شماره تماس", "نقش / سمت","کلید کنترل","کد ملی", "نام کاربری", "گذرواژه","آدرس منزل"))
        
        
        toolbar = QToolBar()
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        statusbar = QStatusBar()
        self.setStatusBar(statusbar)
        btn_ac_adduser = QAction(QIcon("pics/add.png"), "ثبت ادمین جدید", self)
        btn_ac_adduser.triggered.connect(self.insert)
        btn_ac_adduser.setStatusTip("ثبت ادمین جدید")
        toolbar.addAction(btn_ac_adduser)
        
        btn_ac_editadmin = QAction(QIcon("pics/edit1.png"), "ویرایش ادمین ها", self)
        btn_ac_editadmin.triggered.connect(self.editAdmins)
        btn_ac_editadmin.setStatusTip("ویرایش ادمین ها")
        toolbar.addAction(btn_ac_editadmin)

        btn_ac_refresh = QAction(QIcon("pics/refresh.png"),"تاره سازی",self)
        btn_ac_refresh.triggered.connect(self.loaddata)
        btn_ac_refresh.setStatusTip("تاره سازی")
        toolbar.addAction(btn_ac_refresh)

        btn_ac_search = QAction(QIcon("pics/search.png"), "جست وجو", self)
        btn_ac_search.triggered.connect(self.search)
        btn_ac_search.setStatusTip("جست وجو")
        toolbar.addAction(btn_ac_search)

        btn_ac_delete = QAction(QIcon("pics/trash.png"), "حذف", self)
        btn_ac_delete.triggered.connect(self.delete)
        btn_ac_delete.setStatusTip("حذف ادمین")
        toolbar.addAction(btn_ac_delete)

        adduser_action = QAction(QIcon("pics/add.png"),"ثبت ادمین جدید", self)
        adduser_action.triggered.connect(self.insert)
        file_menu.addAction(adduser_action)
        
        editadmin_action = QAction(QIcon("pics/edit1.png"), "ویرایش ادمین ها", self)
        editadmin_action.triggered.connect(self.editAdmins)
        editadmin_action.setStatusTip("Add Student")
        file_menu.addAction(editadmin_action)

        searchuser_action = QAction(QIcon("pics/search.png"), "جست و جو ادمین", self)
        searchuser_action.triggered.connect(self.search)
        file_menu.addAction(searchuser_action)

        deluser_action = QAction(QIcon("pics/trash.png"), "حذف", self)
        deluser_action.triggered.connect(self.delete)
        file_menu.addAction(deluser_action)

    def loaddata(self):
        self.connection = sqlite3.connect(MAIN_DB_FILE)
        query = "SELECT * FROM admininfo;"
        result = self.connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number,QTableWidgetItem(str(data)))
        self.connection.close()

    def handlePaintRequest(self, printer):
        document = QTextDocument()
        cursor = QTextCursor(document)
        model = self.table.model()
        table = cursor.insertTable(model.rowCount(), model.columnCount())
        for row in range(table.rows()):
            for column in range(table.columns()):
                cursor.insertText(model.item(row, column).text())
                cursor.movePosition(QTextCursor.NextCell)
        document.print_(printer)

    def insert(self):
        dlg = InsertDialog()
        dlg.exec_()

    def delete(self):
        dlg = DeleteDialog()
        dlg.exec_()

    def search(self):
        dlg = SearchDialog()
        dlg.exec_()
    
    def editAdmins(self):
        dlg = EditAdminDialog()
        dlg.exec_()
                   
    
    

class InsertDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(InsertDialog, self).__init__(*args, **kwargs)
        
        font = QFont()
        font.setBold(True)
        font.setPointSize(14)
        font.setFamily("Vazir")

        
        self.setWindowTitle("ثبت نام ادمین")
        self.setObjectName("maininsert")
        icon = QIcon('pics/add.png')
        self.setWindowIcon(icon)
        self.setFixedWidth(800)
        self.setFixedHeight(800)
        self.setFont(font)
        self.setStyleSheet("\n"
            "#maininsert{\n"
            "    background-image: url(./pics/1.jpg);\n"
            "    background-repeat: no-repeat;\n"
            "    background-position: center center;\n"
            "}\n"
            "#reg_btn_a{\n"
            "    background-image: url(./pics/btn_login3.png);\n"
            "    background-repeat: no-repeat;\n"
            "    background-position: center center;\n"
            "    border-radius: 30px;\n"
            "    padding: 20px;\n"
            "}\n"
            "#reg_btn_a:hover{\n"
            "    background-image: url(./pics/btn_login4.png);\n"
            "    background-repeat: no-repeat;\n"
            "    background-position: center center;\n"
            "    border-radius: 30px;\n"
            "    padding: 20px;\n"
            "}\n"
            "#reg_btn_a:pressed{\n"
            "    background-image: url(./pics/btn_login2.png);\n"
            "    background-repeat: no-repeat;\n"
            "    background-position: center center;\n"
            "    border-radius: 30px;\n"
            "    padding: 20px;\n"
            "}\n"
            "#name_txt{\n"
            "    background: transparent;\n"
            "    border: none;\n"
            "    border-bottom: 5px solid rgb(5, 152, 250);\n"
            "    padding: 10px;\n"
            "    color: #000;\n"
            "}\n"
            "#agee_txt{\n"
            "    background: transparent;\n"
            "    border: none;\n"
            "    border-bottom: 5px solid rgb(5, 152, 250);\n"
            "    padding: 10px;\n"
            "    color: #000;\n"
            "}\n"
            "#phone_txt{\n"
            "    background: transparent;\n"
            "    border: none;\n"
            "    border-bottom: 5px solid rgb(5, 152, 250);\n"
            "    padding: 10px;\n"
            "    color: #000;\n"
            "}\n"
            "#role_txt{\n"
            "    background: transparent;\n"
            "    border: none;\n"
            "    border-bottom: 5px solid rgb(5, 152, 250);\n"
            "    padding: 10px;\n"
            "    color: #000;\n"
            "}\n"
            "#contkey{\n"
            "    background: transparent;\n"
            "    border: none;\n"
            "    border-bottom: 5px solid rgb(5, 152, 250);\n"
            "    padding: 10px;\n"
            "    color: #000;\n"
            "}\n"
            "#id_txt{\n"
            "    background: transparent;\n"
            "    border: none;\n"
            "    border-bottom: 5px solid rgb(5, 152, 250);\n"
            "    padding: 10px;\n"
            "    color: #000;\n"
            "}\n"
            "#usr_txt{\n"
            "    background: transparent;\n"
            "    border: none;\n"
            "    border-bottom: 5px solid rgb(5, 152, 250);\n"
            "    padding: 10px;\n"
            "    color: #000;\n"
            "}\n"
            "#pass_txt{\n"
            "    background: transparent;\n"
            "    border: none;\n"
            "    border-bottom: 5px solid rgb(5, 152, 250);\n"
            "    padding: 10px;\n"
            "    color: #000;\n"
            "}\n"
            "#adrs_txt{\n"
            "    background: transparent;\n"
            "    border: none;\n"
            "    border-bottom: 5px solid rgb(5, 152, 250);\n"
            "    padding: 10px;\n"
            "    color: #000;\n"
            "}\n")
        
        self.QBtn = QPushButton()
        self.QBtn.setText("تایید")
        self.QBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.QBtn.setObjectName("reg_btn_a")

        layout = QVBoxLayout()

        self.nameinput = QLineEdit()
        self.nameinput.setObjectName("name_txt")
        self.nameinput.setPlaceholderText("نام و نام خانوادگی خود را وارد کنید")
        layout.addWidget(self.nameinput)

        self.age = QLineEdit()
        self.age.setObjectName("agee_txt")
        self.age.setPlaceholderText("سن خود را وارد کنید")
        onlyInt = QIntValidator()
        onlyInt.setRange(0,10)
        self.age.setValidator(onlyInt)
        layout.addWidget(self.age)

        self.phonenumber = QLineEdit()
        self.phonenumber.setObjectName("phone_txt")
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
        self.control_key.setObjectName("contkey")
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
        
        self.username = QLineEdit()
        self.username.setObjectName("usr_txt")
        self.username.setPlaceholderText("یک نام کاربری را انتخاب و وارد کنید")
        layout.addWidget(self.username)
        
        self.passw = QLineEdit()
        self.passw.setPlaceholderText("یک رمزعبور انتخاب و وارد کنید")
        self.passw.setObjectName("pass_txt")
        layout.addWidget(self.passw)
        
        self.addrs = QLineEdit()
        self.addrs.setObjectName("adrs_txt")
        self.addrs.setPlaceholderText("آدرس خانه خود را وارد کنید(خلاصه وار)")
        layout.addWidget(self.addrs)
        
        
        
        self.QBtn.clicked.connect(self.addAdmin)
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
        username = self.username.text()
        passw = self.passw.text()
        addrs = self.addrs.text()

        # Check if the file exists
        if os.path.exists(MAIN_DB_FILE):
            try:
                # Set the file as hidden
                os.system(f'attrib +h "{MAIN_DB_FILE}"')
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
            with sqlite3.connect(MAIN_DB_FILE) as conn:
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
    


class SearchDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(SearchDialog, self).__init__(*args, **kwargs)
        
        font = QFont()
        font.setBold(True)
        font.setPointSize(14)
        font.setFamily("Vazir")

    
        self.setWindowTitle("جست و جو ادمین ها")
        icon = QIcon('pics/search.png')
        self.setWindowIcon(icon)
        self.setFixedWidth(500)
        self.setFixedHeight(200)
        self.setFont(font)
        self.setObjectName("mainserp")
        self.setStyleSheet("\n"
            "#sch_txt{\n"
            "    background: transparent;\n"
            "    border: none;\n"
            "    border-bottom: 5px solid lime;\n"
            "    padding: 10px;\n"
            "    color: #000;\n"
            "}\n"
            "#mainserp{\n"
            "    background-image: url(./pics/bc.png);\n"
            "    background-repeat: no-repeat;\n"
            "    background-position: center center;\n"
            "}\n"
            "#srch_btn_a{\n"
            "    background-image: url(./pics/btn_login4.png);\n"
            "    background-repeat: no-repeat;\n"
            "    background-position: center center;\n"
            "    border-radius: 30px;\n"
            "    padding: 20px;\n"
            "}\n"
            "#srch_btn_a:hover{\n"
            "    background-image: url(./pics/btn_login3.png);\n"
            "    background-repeat: no-repeat;\n"
            "    background-position: center center;\n"
            "    border-radius: 30px;\n"
            "    padding: 20px;\n"
            "}\n"
            "#srch_btn_a:pressed{\n"
            "    background-image: url(./pics/btn_login2.png);\n"
            "    background-repeat: no-repeat;\n"
            "    background-position: center center;\n"
            "    border-radius: 30px;\n"
            "    padding: 20px;\n"
            "}\n")
        
        
        self.QBtn = QPushButton()
        self.QBtn.setText("تایید")
        self.QBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.QBtn.setObjectName("srch_btn_a")
        self.QBtn.clicked.connect(self.searchUser)
        layout = QVBoxLayout()

        self.searchinput = QLineEdit()
        self.searchinput.setObjectName("sch_txt")
        self.searchinput.setPlaceholderText("نام و نام خانوادگی(به صورت کامل )")
        layout.addWidget(self.searchinput)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def searchUser(self):
        fname = self.searchinput.text()
        if not fname:
            QMessageBox.warning(self, 'هشدار', "کادر مورد نظر را پر بکنید")
        else:
            try:
                self.conn = sqlite3.connect(MAIN_DB_FILE)
                self.c = self.conn.cursor()
                result = self.c.execute("SELECT * FROM admininfo WHERE full_name = ?", (fname,))
                row = result.fetchone()
                if row:
                    result_str = (
                        f"| ردیف : {row[0]}\n"
                        f"| نام و نام خانوادگی : {row[1]}\n"
                        f"| سن : {row[2]}\n"
                        f"| شماره تماس : {row[3]}\n"
                        f"| سمت / نقش : {row[4]}\n"
                        f"| کدملی : {row[6]}\n"
                        f"| نام کاربری : {row[7]}\n"
                        f"| آدرس منزل : {row[9]}\n"
                    )
                    QMessageBox.information(self, f"َAdmin : {row[1]}", result_str)
                else:
                    QMessageBox.warning(self, 'هشدار', 'مدیر / ادمین مورد نظر پیدا نشد یا وجود ندارد')
                self.close()
            except Exception as e:
                QMessageBox.warning(self, 'خطا', f'خطا در جستجو: {str(e)}')
    

class DeleteDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(DeleteDialog, self).__init__(*args, **kwargs)
        
        font = QFont()
        font.setBold(True)
        font.setPointSize(14)
        font.setFamily("Vazir")

        

        self.setWindowTitle("حذف ادمین")
        icon = QIcon('pics/trash.png')
        self.setWindowIcon(icon)
        self.setFixedWidth(500)
        self.setFixedHeight(200)
        self.setFont(font)
        self.setObjectName("delp")
        self.setStyleSheet("\n"
            "#delp{\n"
            "    background-image: url(./pics/bc.png);\n"
            "    background-repeat: no-repeat;\n"
            "    background-position: center center;\n"
            "}\n"
            "#del_btn{\n"
            "   background-color: rgb(255, 0, 0);\n"
            "   border-radius: 30px;\n"
            "   padding: 20px;\n"
            "}\n"
            "#del_btn:hover{\n"
            "   background-color: rgb(250, 102, 102);\n"
            "   border-radius: 30px;\n"
            "   padding: 20px;\n"
            "}\n"
            "#del_btn:pressed{\n"
            "   background-color: rgb(255, 81, 33);\n"
            "   border-radius: 30px;\n"
            "   padding: 20px;\n"
            "}\n"
            "#del_txt{\n"
            "    background: transparent;\n"
            "    border: none;\n"
            "    border-bottom: 5px solid lime;\n"
            "    padding: 10px;\n"
            "    color: #000;\n"
            "}\n"
            )
        
        
        
        self.QBtn = QPushButton()
        self.QBtn.setText("حذف")
        self.QBtn.setObjectName("del_btn")
        self.QBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.QBtn.clicked.connect(self.deleteUser)
        
        
        layout = QVBoxLayout()

        self.deleteinput = QLineEdit()
        self.deleteinput.setObjectName("del_txt")
        self.deleteinput.setPlaceholderText("کلید کنترل : ")
        layout.addWidget(self.deleteinput)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)


    def deleteUser(self):
        delrol = self.deleteinput.text()
        if not delrol:
            QMessageBox.warning(self, 'هشدار', "کادر مورد نظر را پر بکنید")
        else:
            try:
                self.conn = sqlite3.connect(MAIN_DB_FILE)
                self.c = self.conn.cursor()
                self.c.execute("DELETE FROM admininfo WHERE cont_key = ?", (delrol,))
                self.conn.commit()
                self.c.close()
                self.conn.close()
                if self.c.rowcount > 0:
                    QMessageBox.information(self, 'موفقیت آمیز', 'مدیر / ادمین با موفقیت حذف شد')
                else:
                    QMessageBox.warning(self, 'هشدار', 'مدیر / ادمین مورد نظر حذف نشد یا وجود ندارد')
                self.close()
            except sqlite3.Error as e:
                QMessageBox.warning(self, 'خطا', f'خطا در حذف مدیر / ادمین: {str(e)}')




class EditAdminDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(EditAdminDialog, self).__init__(*args, **kwargs)
        
        
        ### Page Font ###
        font = QFont()
        font.setBold(True)
        font.setPointSize(14)
        font.setFamily("Vazir")
        
         ### Main Window ###
        self.setWindowTitle("ویرایش ادمین ها")
        icon = QIcon('pics/edit1.png')
        self.setWindowIcon(icon)
        self.setFont(font)
        self.setObjectName("mainenp")
        self.setStyleSheet("\n"
            "#mainenp{\n"
            "    background-image: url(./pics/1.jpg);\n"
            "    background-repeat: no-repeat;\n"
            "    background-position: center center;\n"
            "}\n"               
            "#edit_btn_a{\n"
            "    background-image: url(./pics/btn_login3.png);\n"
            "    background-repeat: no-repeat;\n"
            "    background-position: center center;\n"
            "   border-radius: 30px;\n"
            "   padding: 20px;\n"
            "}\n"
            "#edit_btn_a:hover{\n"
            "    background-image: url(./pics/btn_login4.png);\n"
            "    background-repeat: no-repeat;\n"
            "    background-position: center center;\n"
            "   border-radius: 30px;\n"
            "   padding: 20px;\n"
            "}\n"
            "#edit_btn_a:pressed{\n"
            "    background-image: url(./pics/btn_login2.png);\n"
            "    background-repeat: no-repeat;\n"
            "    background-position: center center;\n"
            "   border-radius: 30px;\n"
            "   padding: 20px;\n"
            "}\n"
            
            "#close_btn_a{\n"
            "   background-color: rgb(255, 0, 0);\n"
            "   border-radius: 30px;\n"
            "   padding: 20px;\n"
            "}\n"
            "#close_btn_a:hover{\n"
            "   background-color: rgb(250, 102, 102);\n"
            "   border-radius: 30px;\n"
            "   padding: 20px;\n"
            "}\n"
            "#close_btn_a:pressed{\n"
            "   background-color: rgb(255, 81, 33);\n"
            "   border-radius: 30px;\n"
            "   padding: 20px;\n"
            "}\n"
            "#roll_txt{\n"
            "    background: transparent;\n"
            "    border: none;\n"
            "    border-bottom: 5px solid rgb(5, 152, 250);\n"
            "    padding: 10px;\n"
            "    color: #000;\n"
            "}\n"
            "#fname_txt{\n"
            "    background: transparent;\n"
            "    border: none;\n"
            "    border-bottom: 5px solid rgb(5, 152, 250);\n"
            "    padding: 10px;\n"
            "    color: #000;\n"
            "}\n"
            "#age_txt{\n"
            "    background: transparent;\n"
            "    border: none;\n"
            "    border-bottom: 5px solid rgb(5, 152, 250);\n"
            "    padding: 10px;\n"
            "    color: #000;\n"
            "}\n"
            "#phn_txt{\n"
            "    background: transparent;\n"
            "    border: none;\n"
            "    border-bottom: 5px solid rgb(5, 152, 250);\n"
            "    padding: 10px;\n"
            "    color: #000;\n"
            "}\n"
            "#role_txt{\n"
            "    background: transparent;\n"
            "    border: none;\n"
            "    border-bottom: 5px solid rgb(5, 152, 250);\n"
            "    padding: 10px;\n"
            "    color: #000;\n"
            "}\n"
            "#id_txt{\n"
            "    background: transparent;\n"
            "    border: none;\n"
            "    border-bottom: 5px solid rgb(5, 152, 250);\n"
            "    padding: 10px;\n"
            "    color: #000;\n"
            "}\n"
            "#uname_txt{\n"
            "    background: transparent;\n"
            "    border: none;\n"
            "    border-bottom: 5px solid rgb(5, 152, 250);\n"
            "    padding: 10px;\n"
            "    color: #000;\n"
            "}\n"
            "#pass_txt{\n"
            "    background: transparent;\n"
            "    border: none;\n"
            "    border-bottom: 5px solid rgb(5, 152, 250);\n"
            "    padding: 10px;\n"
            "    color: #000;\n"
            "}\n"
            "#adrs_txt{\n"
            "    background: transparent;\n"
            "    border: none;\n"
            "    border-bottom: 5px solid rgb(5, 152, 250);\n"
            "    padding: 10px;\n"
            "    color: #000;\n"
            "}\n"
        )
        self.setFixedWidth(800)
        self.setFixedHeight(800)
        
        
        
        ### Main Window Components ###
        self.editbtn = QPushButton()
        self.editbtn.setText("اعمال تغییرات")
        self.editbtn.setFont(font)
        self.editbtn.setObjectName("edit_btn_a")
        self.editbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.editbtn.clicked.connect(self.editAdmin)
        
        self.closeBtn = QPushButton()
        self.closeBtn.setText("بستن")
        self.closeBtn.setFont(font)
        self.closeBtn.setObjectName("close_btn_a")
        self.closeBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.closeBtn.clicked.connect(self.close)
        
        layout = QVBoxLayout()
        
        self.rollided = QLineEdit()
        self.rollided.setObjectName("roll_txt")
        self.rollided.setPlaceholderText("شماره ردیف ادمین مورد نظر را وارد کنید")
        
        self.full_nameed = QLineEdit()
        self.full_nameed.setObjectName("fname_txt")
        self.full_nameed.setPlaceholderText("ویرایش نام و نام خانوادگی")
        
        self.ageed = QLineEdit()
        self.ageed.setObjectName("age_txt")
        self.ageed.setPlaceholderText("ویرایش سن(تا دو رقم بدون اعشار)")
        onlyInt = QIntValidator()
        onlyInt.setRange(0,10)
        self.ageed.setValidator(onlyInt)
        
        self.phonenumed = QLineEdit()
        self.phonenumed.setObjectName("phn_txt")
        self.phonenumed.setPlaceholderText("ویرایش شماره تماس(فقط از اعداد استفاده کنید)")
        self.phonenumed.setInputMask("99999999999")
        
        self.roleed = QLineEdit()
        self.roleed.setObjectName("role_txt")
        self.roleed.setPlaceholderText("ویرایش سمت")
        
        self.IDed = QLineEdit()
        self.IDed.setObjectName("id_txt")
        self.IDed.setPlaceholderText("ویرایش کدملی(فقط از اعداد استفاده کنید)")
        onlyInt = QIntValidator()
        onlyInt.setRange(0,1000000000)
        self.IDed.setValidator(onlyInt)
        
        self.usrnmed = QLineEdit()
        self.usrnmed.setObjectName("uname_txt")
        self.usrnmed.setPlaceholderText("ویرایش نام کاربری")
        
        self.passwed = QLineEdit()
        self.passwed.setObjectName("pass_txt")
        self.passwed.setPlaceholderText("ویرایش رمز عبور")
        
        self.adrsed = QLineEdit()
        self.adrsed.setObjectName("adrs_txt")
        self.adrsed.setPlaceholderText("ویرایش آدرس منزل")
        
        
        layout.addWidget(self.rollided)
        layout.addWidget(self.full_nameed)
        layout.addWidget(self.ageed)
        layout.addWidget(self.phonenumed)
        layout.addWidget(self.roleed)
        layout.addWidget(self.IDed)
        layout.addWidget(self.usrnmed)
        layout.addWidget(self.passwed)
        layout.addWidget(self.adrsed)
        layout.addWidget(self.editbtn)
        layout.addWidget(self.closeBtn)
        self.setLayout(layout)
    
    
    def hash_password(self, password):
        salt = secrets.token_hex(16)
        password = self.passwed.text().encode('utf-8')  # Encode the provided password
        salt = salt.encode('utf-8')  # Encode the salt
        # Combine the password and salt, then hash them
        hashed_password = hashlib.sha256(password + salt).hexdigest()
        return hashed_password, salt
    
    def editAdmin(self):
        
        ### Hide DB Files After Creating For More Security ###
        # Check if the file exists
        if os.path.exists(MAIN_DB_FILE):
            try:
                # Set the file as hidden
                os.system(f'attrib +h "{MAIN_DB_FILE}"')
                print("Every Thing Works Fine")
            except Exception as e:
                print(f"Error Operation Terminated: {e}")
        else:
            print("There IS Some Error Contact Support.")
            
        roll_id = self.rollided.text()
        fname = self.full_nameed.text()
        age = self.ageed.text()
        phone = self.phonenumed.text()
        Role = self.roleed.text()
        id_num = self.IDed.text()
        usrname = self.usrnmed.text()
        passw_ed = self.passwed.text()
        adrsed = self.adrsed.text()
        
        if not roll_id or not fname  or not age or not Role or not id_num or not usrname or not passw_ed or not adrsed:
            QMessageBox.warning(self, "هشدار", "همه فیلدها باید پر شوند.")
            return

        try:
            age = int(age)
            phone = int(phone)
            id_num = int(id_num)
        except ValueError:
            QMessageBox.warning(self, "هشدار", "سن، شماره تماس، و کدملی باید اعداد صحیح باشند.")
            return

        # Hash the password before updating the database
        hashed_password, _ = self.hash_password(passw_ed)
        
        UPDATE_ALL = """UPDATE admininfo SET full_name=?, age=?, phone_number=?, role=? ,identity_id=?, username=?, password=?, adrs=? WHERE id=?"""

        
        try:
            with sqlite3.connect(MAIN_DB_FILE) as conn:
                cursor = conn.cursor()
                cursor.execute(UPDATE_ALL, (fname, age, phone, Role, id_num, usrname, hashed_password, adrsed, roll_id))
                conn.commit()
            QMessageBox.information(self, "موفقیت", "اطلاعات با موفقیت به‌روزرسانی شد.")
        except sqlite3.Error as e:
            QMessageBox.critical(self, "خطا", f"خطا در به‌روزرسانی اطلاعات: {str(e)}")