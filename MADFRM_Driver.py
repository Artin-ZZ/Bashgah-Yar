# Import the required libraries and modules
# For working with SQLite databases
import sqlite3
# For various operating system-related tasks
import os
# For accessing system-specific parameters and functions
import sys
# PyQt5 library modules
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import *
# Additional PyQt5 modules
from PyQt5 import QtCore
from PyQt5 import QtGui
## Local Libs And Modules ##
from Update.Root.Settings.config import MEMBER_DB_FILE
from Update.Root.Settings.Helpers import randomSEC_KEY








class ManageMembers(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(ManageMembers, self).__init__(*args, **kwargs)
        
        ### Hide DB Files After Creating For More Security ###
        # Check if the file exists
        if os.path.exists(MEMBER_DB_FILE):
            try:
                # Set the file as hidden
                os.system(f'attrib +h "{MEMBER_DB_FILE}"')
                print("Every Thing Works Fine")
            except Exception as e:
                print(f"Error hiding {MEMBER_DB_FILE}: {e}")
        else:
            print("There IS Some Error Contact Support.")
        
        # Creating The Data Base
        self.conn = sqlite3.connect(MEMBER_DB_FILE)
        self.c = self.conn.cursor()
        self.c.execute("""
        CREATE TABLE IF NOT EXISTS membersinfo (
            id INTEGER NOT NULL PRIMARY KEY,
            full_name VARCHAR(100) NOT NULL,
            age INTEGER NOT NULL,
            phone_number INTEGER NOT NULL UNIQUE, 
            Control_key VARCHAR(255) NOT NULL UNIQUE,
            identity_id INTEGER NOT NULL UNIQUE,
            address TEXT NOT NULL,
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
        self.setWindowTitle("مدیریت اعضا")
        icon = QIcon('pics/mng_members.png')
        self.setWindowIcon(icon)
        self.setMinimumSize(800, 800)
        self.setFont(font)

        self.tableWidget = QTableWidget()
        self.setCentralWidget(self.tableWidget)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.tableWidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tableWidget.setHorizontalHeaderLabels(("ردیف", "نام و نام خانوادگی", "سن", "شماره تماس", "کلید کنترل","کد ملی","آدرس منزل"))
        
        
        toolbar = QToolBar()
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        statusbar = QStatusBar()
        self.setStatusBar(statusbar)
        btn_ac_adduser = QAction(QIcon("pics/add.png"), "ثبت عضو جدید", self)
        btn_ac_adduser.triggered.connect(self.insert)
        btn_ac_adduser.setStatusTip("ثبت عضو جدید")
        toolbar.addAction(btn_ac_adduser)
        
        btn_ac_edituser = QAction(QIcon("pics/edit1.png"), "ویرایش اعضا", self)
        btn_ac_edituser.triggered.connect(self.editMembers)
        btn_ac_edituser.setStatusTip("ویرایش اعضا")
        toolbar.addAction(btn_ac_edituser)

        btn_ac_refresh = QAction(QIcon("pics/refresh.png"),"تازه سازی",self)
        btn_ac_refresh.triggered.connect(self.loaddata)
        btn_ac_refresh.setStatusTip("تازه سازی ")
        toolbar.addAction(btn_ac_refresh)

        btn_ac_search = QAction(QIcon("pics/search.png"), "جست و جو", self)
        btn_ac_search.triggered.connect(self.search)
        btn_ac_search.setStatusTip("جست و جو")
        toolbar.addAction(btn_ac_search)

        btn_ac_delete = QAction(QIcon("pics/trash.png"), "حذف", self)
        btn_ac_delete.triggered.connect(self.delete)
        btn_ac_delete.setStatusTip("حذف")
        toolbar.addAction(btn_ac_delete)

        adduser_action = QAction(QIcon("pics/add.png"),"ثبت عضو جدید", self)
        adduser_action.triggered.connect(self.insert)
        file_menu.addAction(adduser_action)
        
        adduser_action = QAction(QIcon("pics/edit1.png"),"ویرایش اعضا", self)
        adduser_action.triggered.connect(self.editMembers)
        file_menu.addAction(adduser_action)

        searchuser_action = QAction(QIcon("pics/search.png"), "جست و جو اعضا", self)
        searchuser_action.triggered.connect(self.search)
        file_menu.addAction(searchuser_action)

        deluser_action = QAction(QIcon("pics/trash.png"), "حذف", self)
        deluser_action.triggered.connect(self.delete)
        file_menu.addAction(deluser_action)

    def loaddata(self):
        self.connection = sqlite3.connect(MEMBER_DB_FILE)
        query = "SELECT * FROM membersinfo;"
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
        
    def editMembers(self):
        dlg = UpdateMembers()
        dlg.exec_()


class InsertDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(InsertDialog, self).__init__(*args, **kwargs)
        
        font = QFont()
        font.setBold(True)
        font.setPointSize(14)
        font.setFamily("Vazir")
        
        self.setWindowTitle("ثبت نام اعضا")
        icon = QIcon('pics/add.png')
        self.setObjectName("maininsertpage")
        self.setWindowIcon(icon)
        self.setFixedWidth(800)
        self.setFixedHeight(800)
        self.setFont(font)
        self.setStyleSheet("\n"
            "#maininsertpage{\n"
            "    background-image: url(./pics/1.jpg);\n"
            "    background-repeat: no-repeat;\n"
            "    background-position: center center;\n"
            "}\n" 
            "#reg_btn{\n"
            "    background-image: url(./pics/btn_login3.png);\n"
            "    background-repeat: no-repeat;\n"
            "    background-position: center center;\n"
            "    border-radius: 30px;\n"
            "    padding: 20px;\n"
            "}\n"
            "#reg_btn:hover{\n"
            "    background-image: url(./pics/btn_login4.png);\n"
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
            "#name_txt{\n"
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
            "#phone_txt{\n"
            "    background: transparent;\n"
            "    border: none;\n"
            "    border-bottom: 5px solid rgb(5, 152, 250);\n"
            "    padding: 10px;\n"
            "    color: #000;\n"
            "}\n"
            "#contk_txt{\n"
            "    background: transparent;\n"
            "    border: none;\n"
            "    border-bottom: 5px solid rgb(5, 152, 250);\n"
            "    padding: 10px;\n"
            "    color: #000;\n"
            "}\n"
            "#idinp_txt{\n"
            "    background: transparent;\n"
            "    border: none;\n"
            "    border-bottom: 5px solid rgb(5, 152, 250);\n"
            "    padding: 10px;\n"
            "    color: #000;\n"
            "}\n"
            "#paydt_txt{\n"
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

        self.QBtn = QPushButton()
        self.QBtn.setText("تایید")
        self.QBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.QBtn.setObjectName("reg_btn")
        self.QBtn.clicked.connect(self.adduser)

        layout = QVBoxLayout()

        self.nameinput = QLineEdit()
        self.nameinput.setObjectName("name_txt")
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
        self.phonenumber.setObjectName("phone_txt")
        self.phonenumber.setPlaceholderText("شماره تماس خود را وارد کنید")
        self.phonenumber.setInputMask("99999999999")
        layout.addWidget(self.phonenumber)
        
        self.ControlKey = QLineEdit(randomSEC_KEY())
        self.ControlKey.setObjectName("contk_txt")
        onlyInt = QIntValidator()
        self.ControlKey.setValidator(onlyInt)
        self.ControlKey.setReadOnly(True)
        layout.addWidget(self.ControlKey)
        
        self.identityid = QLineEdit()
        self.identityid.setObjectName("idinp_txt")
        self.identityid.setPlaceholderText("کدملی خود را وارد کنید")
        onlyInt = QIntValidator()
        onlyInt.setRange(0,1000000000)
        self.identityid.setValidator(onlyInt)
        layout.addWidget(self.identityid)
        
        self.addrs = QLineEdit()
        self.addrs.setObjectName("adrs_txt")
        self.addrs.setPlaceholderText("آدرس خانه خود را وارد کنید(خلاصه وار)")
        layout.addWidget(self.addrs)
        

        layout.addWidget(self.QBtn)
        self.setLayout(layout)
        

     
    def adduser(self):
        full_name = self.nameinput.text()
        age = self.age.text()
        phone_number = self.phonenumber.text()
        control_key = self.ControlKey.text()
        identity_id = self.identityid.text()
        addrs = self.addrs.text()

        
        ### Hide DB Files After Creating For More Security ###
        # Check if the file exists
        if os.path.exists(MEMBER_DB_FILE):
            try:
                # Set the file as hidden
                os.system(f'attrib +h "{MEMBER_DB_FILE}"')
                print("Every Thing Works Fine")
            except Exception as e:
                print(f"Error hiding {MEMBER_DB_FILE}: {e}")
        else:
            print("There IS Some Error Contact Support.")
        
        
        try:
            age = int(age)
            phone_number = int(phone_number)
            identity_id = int(identity_id)
        except ValueError:
            QMessageBox.warning(self, 'هشدار', 'لطفاً سن، شماره تماس، و کدملی را به صورت عددی وارد کنید')
            return

        if not full_name or not age or not phone_number or not control_key or not identity_id or not addrs:
            QMessageBox.warning(self, 'هشدار', 'لطفاً تمام فیلدها را پر کنید')
            return

        try:
            self.conn = sqlite3.connect(MEMBER_DB_FILE)
            self.c = self.conn.cursor()
            self.c.execute("INSERT INTO membersinfo(full_name, age, phone_number, Control_key, identity_id, address) VALUES (?, ?, ?, ?, ?, ?)",(full_name, age, phone_number, control_key, identity_id, addrs))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(self, 'موفقیت آمیز', 'عضو با موفقیت ثبت نام شد')
            self.close()
        except sqlite3.Error as e:
            QMessageBox.warning(self, 'خطا', f'خطا در ثبت نام عضو: {str(e)}')


class SearchDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(SearchDialog, self).__init__(*args, **kwargs)
        
        font = QFont()
        font.setBold(True)
        font.setPointSize(14)
        font.setFamily("Vazir")

        self.setWindowTitle("جست و جو اعضا")
        icon = QIcon('pics/search.png')
        self.setWindowIcon(icon)
        self.setFixedWidth(500)
        self.setFixedHeight(200)
        self.setObjectName("mainspage")
        self.setFont(font)
        self.setStyleSheet("\n"
            "#mainspage{\n"
            "    background-image: url(./pics/bc.png);\n"
            "    background-repeat: no-repeat;\n"
            "    background-position: center center;\n"
            "}\n"               
            "#srch_btn{\n"
            "    background-image: url(./pics/btn_login4.png);\n"
            "    background-repeat: no-repeat;\n"
            "    background-position: center center;\n"
            "    border-radius: 30px;\n"
            "    padding: 20px;\n"
            "}\n"
            "#srch_btn:hover{\n"
            "    background-image: url(./pics/btn_login3.png);\n"
            "    background-repeat: no-repeat;\n"
            "    background-position: center center;\n"
            "    border-radius: 30px;\n"
            "    padding: 20px;\n"
            "}\n"
            "#srch_btn:pressed{\n"
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
            "}\n")

        self.QBtn = QPushButton()
        self.QBtn.setText("جست و جو")
        self.QBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.QBtn.setObjectName("srch_btn")
        self.QBtn.clicked.connect(self.searchUser)
        
        layout = QVBoxLayout()

        self.searchinput = QLineEdit()
        self.searchinput.setObjectName("fname_txt")
        self.searchinput.setPlaceholderText("نام و نام خانوادگی(به صورت کامل )")
        layout.addWidget(self.searchinput)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)
        
    
    def searchUser(self):
        cont_key = self.searchinput.text()
        if not cont_key:
            QMessageBox.warning(self, 'هشدار', "کادر مورد نظر را پر بکنید")
        else:
            # try:
                self.conn = sqlite3.connect(MEMBER_DB_FILE)
                self.c = self.conn.cursor()
                result = self.c.execute("SELECT * FROM membersinfo WHERE full_name = ?", (cont_key,))
                row = result.fetchone()
                if row:
                    result_str = (
                        f"| ردیف : {row[0]}\n"
                        f"| نام و نام خانوادگی : {row[1]}\n"
                        f"| سن : {row[2]}\n"
                        f"| شماره تماس : {row[3]}\n"
                        f"| کلید کنترل : {row[4]}\n"
                        f"| کدملی : {row[5]}\n"
                        f"| آدرس منزل : {row[6]}"
                    )
                    QMessageBox.information(self, f"Membder: {row[1]}", result_str)
                else:
                    QMessageBox.warning(self, 'هشدار', 'عضو مورد نظر پیدا نشد یا وجود ندارد')
                self.close()
            # except Exception as e:
            #     QMessageBox.warning(self, 'خطا', f'خطا در جستجو: {str(e)}')
                

class DeleteDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(DeleteDialog, self).__init__(*args, **kwargs)
        
        font = QFont()
        font.setBold(True)
        font.setPointSize(14)
        font.setFamily("Vazir")
        
        self.setWindowTitle("حذف عضو")
        icon = QIcon('pics/trash.png')
        self.setObjectName("delpage")
        self.setWindowIcon(icon)
        self.setFixedWidth(500)
        self.setFixedHeight(200)
        self.setFont(font)
        self.setStyleSheet("\n"
            "#delpage{\n"
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
            "#contkey_txt{\n"
            "    background: transparent;\n"
            "    border: none;\n"
            "    border-bottom: 5px solid lime;\n"
            "    padding: 10px;\n"
            "    color: #000;\n"
            "}\n")

        self.QBtn1 = QPushButton()
        self.QBtn1.setText("حذف")
        self.QBtn1.setObjectName("del_btn")
        self.QBtn1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.QBtn1.clicked.connect(self.deleteUser)
        
        layout = QVBoxLayout()

        self.deleteinput = QLineEdit()
        self.deleteinput.setPlaceholderText("کلید کنترل:")
        self.deleteinput.setObjectName("contkey_txt")
        layout.addWidget(self.deleteinput)
        layout.addWidget(self.QBtn1)
        self.setLayout(layout)
        
    def deleteUser(self):
        delrol = self.deleteinput.text()
        if not delrol:
            QMessageBox.warning(self, 'هشدار', "کادر مورد نظر را پر بکنید")
        else:
            try:
                self.conn = sqlite3.connect(MEMBER_DB_FILE)
                self.c = self.conn.cursor()
                self.c.execute("DELETE FROM membersinfo WHERE Control_key = ?", (delrol,))
                self.conn.commit()
                self.c.close()
                self.conn.close()
                if self.c.rowcount > 0:
                    QMessageBox.information(self, 'موفقیت آمیز', 'عضو با موفقیت حذف شد')
                else:
                    QMessageBox.warning(self, 'هشدار', 'عضو مورد نظر حذف نشد یا وجود ندارد')
                self.close()
            except sqlite3.Error as e:
                QMessageBox.warning(self, 'خطا', f'خطا در حذف عضو: {str(e)}')



class UpdateMembers(QDialog):
    def __init__(self, *args, **kwargs):
        super(UpdateMembers, self).__init__(*args, **kwargs)
        
        ### Page Font ###
        font = QFont()
        font.setBold(True)
        font.setPointSize(14)
        font.setFamily("Vazir")

        ### Main Window ###
        self.setWindowTitle("ویرایش اعضا")
        icon = QIcon('pics/edit1.png')
        self.setWindowIcon(icon)
        self.setFont(font)
        self.setStyleSheet("\n"
            "#mainpage{\n"
            "    background-image: url(./pics/1.jpg);\n"
            "    background-repeat: no-repeat;\n"
            "    background-position: center center;\n"
            "}\n"
            "#edit_btn{\n"
            "    background-image: url(./pics/btn_login3.png);\n"
            "    background-repeat: no-repeat;\n"
            "    background-position: center center;\n"
            "   border-radius: 30px;\n"
            "   padding: 20px;\n"
            "}\n"
            "#edit_btn:hover{\n"
            "    background-image: url(./pics/btn_login4.png);\n"
            "    background-repeat: no-repeat;\n"
            "    background-position: center center;\n"
            "   border-radius: 30px;\n"
            "   padding: 20px;\n"
            "}\n"
            "#edit_btn:pressed{\n"
            "    background-image: url(./pics/btn_login2.png);\n"
            "    background-repeat: no-repeat;\n"
            "    background-position: center center;\n"
            "   border-radius: 30px;\n"
            "   padding: 20px;\n"
            "}\n"
            
            "#close_btn{\n"
            "   background-color: rgb(255, 0, 0);\n"
            "   border-radius: 30px;\n"
            "   padding: 20px;\n"
            "}\n"
            "#close_btn:hover{\n"
            "   background-color: rgb(250, 102, 102);\n"
            "   border-radius: 30px;\n"
            "   padding: 20px;\n"
            "}\n"
            "#close_btn:pressed{\n"
            "   background-color: rgb(255, 81, 33);\n"
            "   border-radius: 30px;\n"
            "   padding: 20px;\n"
            "}\n"
            "#rollid_txt{\n"
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
            "#phone_txt{\n"
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
            "#paydt_txt{\n"
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
        self.setWindowTitle("ویرایش اطلاعات اعضا")
        self.setFixedWidth(800)
        self.setFixedHeight(800)
        self.setObjectName("mainpage")
        
        ### Main Window Components ###
        self.editbtn = QPushButton()
        self.editbtn.setText("اعمال تغییرات")
        self.editbtn.setFont(font)
        self.editbtn.setObjectName("edit_btn")
        self.editbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.editbtn.clicked.connect(self.editUser)
        
        self.closeBtn = QPushButton()
        self.closeBtn.setText("بستن")
        self.closeBtn.setFont(font)
        self.closeBtn.setObjectName("close_btn")
        self.closeBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.closeBtn.clicked.connect(self.close)
        
        layout = QVBoxLayout()
        
        self.rollid = QLineEdit()
        self.rollid.setObjectName("rollid_txt")
        self.rollid.setPlaceholderText("شماره ردیف فرد مورد نظر را وارد کنید")
                
        self.full_name = QLineEdit()
        self.full_name.setObjectName("fname_txt")
        self.full_name.setPlaceholderText("ویرایش نام و نام خانوادگی")

        self.age = QLineEdit()
        self.age.setObjectName("age_txt")
        self.age.setPlaceholderText("ویرایش سن(تا دو رقم بدون اعشار)")
        onlyInt = QIntValidator()
        onlyInt.setRange(0,10)
        self.age.setValidator(onlyInt)
        
        self.phonenum = QLineEdit()
        self.phonenum.setObjectName("phone_txt")
        self.phonenum.setPlaceholderText("ویرایش شماره تماس(فقط از اعداد استفاده کنید)")
        self.phonenum.setInputMask("99999999999")
        
        self.ID = QLineEdit()
        self.ID.setObjectName("id_txt")
        self.ID.setPlaceholderText("ویرایش کدملی(فقط از اعداد استفاده کنید)")
        onlyInt = QIntValidator()
        onlyInt.setRange(0,1000000000)
        self.ID.setValidator(onlyInt)

        self.addrs = QLineEdit()
        self.addrs.setObjectName("adrs_txt")
        self.addrs.setPlaceholderText("ویرایش آدرس منزل")

        layout.addWidget(self.rollid)
        layout.addWidget(self.full_name)
        layout.addWidget(self.age)
        layout.addWidget(self.phonenum)
        layout.addWidget(self.ID)
        layout.addWidget(self.addrs)
        layout.addWidget(self.editbtn)
        layout.addWidget(self.closeBtn)
        self.setLayout(layout)
        
    def editUser(self):
        roll_id = self.rollid.text()
        fname = self.full_name.text()
        age = self.age.text()
        phone = self.phonenum.text()
        id_num = self.ID.text()
        addrs = self.addrs.text()

        if not roll_id or not fname or not age or not phone or not id_num or not addrs:
            QMessageBox.warning(self, "هشدار", "همه فیلدها باید پر شوند.")
            return

        try:
            age = int(age)
            phone = int(phone)
            id_num = int(id_num)
        except ValueError:
            QMessageBox.warning(self, "هشدار", "سن، شماره تماس، و کدملی باید اعداد صحیح باشند.")
            return

        UPDATE_ALL = """UPDATE membersinfo SET full_name=?, age=?, phone_number=?, identity_id=?, address=? WHERE id=?"""

        try:
            self.conn = sqlite3.connect(MEMBER_DB_FILE)
            self.c = self.conn.cursor()
            self.c.execute(UPDATE_ALL, (fname, age, phone, id_num, addrs, roll_id))
            self.conn.commit()
            self.conn.close()
            QMessageBox.information(self, "موفقیت", "اطلاعات با موفقیت به‌روزرسانی شد.")
        except sqlite3.Error as e:
            QMessageBox.critical(self, "خطا", f"خطا در به‌روزرسانی اطلاعات: {str(e)}")