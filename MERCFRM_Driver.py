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
from Update.Root.Settings.config import SALES_DB_FILE
from Update.Root.Settings.Helpers import randomSEC_KEY_reqs








class ManageRequests(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(ManageRequests, self).__init__(*args, **kwargs)
        
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
        
        ### Page Font ###
        font = QFont()
        font.setBold(True)
        font.setPointSize(10)
        font.setFamily("Vazir")
        ## main Window: The database Table That user Sees ##
        file_menu = self.menuBar().addMenu("&File")
        self.setWindowTitle("مدیریت درخواست ها")
        icon = QIcon('pics/newreq.png')
        self.setWindowIcon(icon)
        self.setMinimumSize(800, 800)
        self.setFont(font)

        self.tableWidget = QTableWidget()
        self.setCentralWidget(self.tableWidget)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setColumnCount(11)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.tableWidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tableWidget.setHorizontalHeaderLabels(("ردیف", "تاریخ","نام و نام خانوادگی", "موضوع درخواست", "آیتم درخواستی", "قیمت(تومان)","شماره درخواست", "آدرس منزل مشتری","شماره تماس مشتری","وضعیت درخواست","نام و نام خانوادگی متصدی"))
        
        
        toolbar = QToolBar()
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        statusbar = QStatusBar()
        self.setStatusBar(statusbar)
        btn_ac_adduser = QAction(QIcon("pics/newreq.png"), "ثبت درخواست جدید", self)
        btn_ac_adduser.triggered.connect(self.insert)
        btn_ac_adduser.setStatusTip("ثبت درخواست جدید")
        toolbar.addAction(btn_ac_adduser)
        
        btn_ac_edituser = QAction(QIcon("pics/edit1.png"), "ویرایش درخواست ها", self)
        btn_ac_edituser.triggered.connect(self.editMembers)
        btn_ac_edituser.setStatusTip("ویرایش درخواست ها")
        toolbar.addAction(btn_ac_edituser)

        btn_ac_refresh = QAction(QIcon("pics/refresh.png"),"تازه سازی",self)
        btn_ac_refresh.triggered.connect(self.loaddata)
        btn_ac_refresh.setStatusTip("تازه سازی")
        toolbar.addAction(btn_ac_refresh)

        btn_ac_search = QAction(QIcon("pics/search.png"), "جست و جو", self)
        btn_ac_search.triggered.connect(self.search)
        btn_ac_search.setStatusTip("جست و جو درخواست ها")
        toolbar.addAction(btn_ac_search)

        btn_ac_delete = QAction(QIcon("pics/trash.png"), "حذف", self)
        btn_ac_delete.triggered.connect(self.delete)
        btn_ac_delete.setStatusTip("حذف درخواست")
        toolbar.addAction(btn_ac_delete)

        adduser_action = QAction(QIcon("pics/newreq.png"),"ثبت درخواست جدید", self)
        adduser_action.triggered.connect(self.insert)
        file_menu.addAction(adduser_action)
        
        adduser_action = QAction(QIcon("pics/edit1.png"),"ویرایش درخواست", self)
        adduser_action.triggered.connect(self.editMembers)
        file_menu.addAction(adduser_action)

        searchuser_action = QAction(QIcon("pics/search.png"), "جست و جو درخواست", self)
        searchuser_action.triggered.connect(self.search)
        file_menu.addAction(searchuser_action)

        deluser_action = QAction(QIcon("pics/trash.png"), "حذف", self)
        deluser_action.triggered.connect(self.delete)
        file_menu.addAction(deluser_action)

    def loaddata(self):
        self.connection = sqlite3.connect(SALES_DB_FILE)
        query = "SELECT * FROM salesinfo;"
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
        dlg = UpdateReqs()
        dlg.exec_()


class InsertDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(InsertDialog, self).__init__(*args, **kwargs)
        
        font = QFont()
        font.setBold(True)
        font.setPointSize(14)
        font.setFamily("Vazir")
        
        self.setWindowTitle("ثبت درخواست جدید")
        icon = QIcon('pics/newreq.png')
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
            "#pricetaginp{\n"
            "    background: transparent;\n"
            "    border: none;\n"
            "    border-bottom: 5px solid rgb(5, 152, 250);\n"
            "    padding: 10px;\n"
            "    color: #000;\n"
            "}\n"
            "#reqst_txt{\n"
            "    background: transparent;\n"
            "    border: none;\n"
            "    border-bottom: 5px solid rgb(5, 152, 250);\n"
            "    padding: 10px;\n"
            "    color: #000;\n"
            "}\n"
            "#regernm_txt{\n"
            "    background: transparent;\n"
            "    border: none;\n"
            "    border-bottom: 5px solid rgb(5, 152, 250);\n"
            "    padding: 10px;\n"
            "    color: #000;\n"
            "}\n")

        self.QBtn = QPushButton()
        self.QBtn.setText("تایید")
        self.QBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.QBtn.setObjectName("reg_btn")
        self.QBtn.clicked.connect(self.adduser)

        layout = QVBoxLayout()

        self.dateinp = QLineEdit()
        self.dateinp.setObjectName("name_txt")
        self.dateinp.setPlaceholderText("تاریخ درخواست")
        layout.addWidget(self.dateinp)

        self.full_name = QLineEdit()
        self.full_name.setObjectName("age_txt")
        self.full_name.setPlaceholderText("نام و نام خانوادگی درخواست کننده")
        layout.addWidget(self.full_name)

        self.req_sub = QLineEdit()
        self.req_sub.setObjectName("phone_txt")
        self.req_sub.setPlaceholderText("موضوع درخواست")
        layout.addWidget(self.req_sub)
        
        self.req_iem = QLineEdit()
        self.req_iem.setPlaceholderText("آیتم درخواستی")
        self.req_iem.setObjectName("contk_txt")
        layout.addWidget(self.req_iem)
        
        self.pricetaginp = QLineEdit()
        self.pricetaginp.setPlaceholderText("قیمت آیتم درخواستی")
        self.pricetaginp.setObjectName("pricetaginp")
        layout.addWidget(self.pricetaginp)
        
        self.salenum = QLineEdit(randomSEC_KEY_reqs())
        self.salenum.setObjectName("idinp_txt")
        onlyInt = QIntValidator()
        self.salenum.setValidator(onlyInt)
        self.salenum.setReadOnly(True)
        layout.addWidget(self.salenum)
        
        self.adrs = QLineEdit()
        self.adrs.setObjectName("paydt_txt")
        self.adrs.setPlaceholderText("آدرس درخواست کننده")
        layout.addWidget(self.adrs)
        
        self.phone = QLineEdit()
        self.phone.setObjectName("adrs_txt")
        self.phone.setPlaceholderText("شماره تماس درخواست کننده")
        self.phone.setInputMask("99999999999")
        layout.addWidget(self.phone)
        
        self.reqst = QComboBox()
        self.reqst.setObjectName("reqst_txt")
        self.reqst.setPlaceholderText("وضعیت سفارش")
        self.reqst.addItem("با موفقیت انجام شد")
        self.reqst.addItem("درحال انجام شدن")
        self.reqst.addItem("وقفه در انجام")
        self.reqst.addItem("لغو شد")
        self.reqst.addItem("خطا در انجام")
        layout.addWidget(self.reqst)
        
        self.regernm_txt = QLineEdit()
        self.regernm_txt.setObjectName("regernm_txt")
        self.regernm_txt.setPlaceholderText("نام و نام خانوادگی متصدی")
        layout.addWidget(self.regernm_txt)
        

        layout.addWidget(self.QBtn)
        self.setLayout(layout)
        

     
    def adduser(self):
        date = self.dateinp.text()
        fullnm = self.full_name.text()
        reqsub = self.req_sub.text()
        reqitem = self.req_iem.text()
        pricetag = self.pricetaginp.text()
        saleno = self.salenum.text()
        adrss = self.adrs.text()
        phone = self.phone.text()
        regername = self.regernm_txt.text()
        reqstat = self.reqst.itemText(self.reqst.currentIndex())
        
        try:
            phone = int(phone)
            pricetag = int(pricetag)
        except ValueError:
            QMessageBox.warning(self, 'هشدار', 'لطفاً شماره تماس را به صورت عددی وارد کنید')
            return

        if not date or not fullnm or not reqsub or not reqitem or not saleno or not adrss or not phone or not reqstat or not regername:
            QMessageBox.warning(self, 'هشدار', 'لطفاً تمام فیلدها را پر کنید')
            return

        try:
            self.conn = sqlite3.connect(SALES_DB_FILE)
            self.c = self.conn.cursor()
            self.c.execute("INSERT INTO salesinfo(date, fullname, req_subject, req_item, price, saleno, adrs, phone, req_stat, regerfnm) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (date, fullnm, reqsub, reqitem, pricetag, saleno, adrss, phone, reqstat, regername))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(self, 'موفقیت آمیز', 'درخواست با موفقیت ثبت شد')
            self.close()
        except sqlite3.Error as e:
            QMessageBox.warning(self, 'خطا', f'خطا در ثبت درخواست: {str(e)}')


class SearchDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(SearchDialog, self).__init__(*args, **kwargs)
        
        font = QFont()
        font.setBold(True)
        font.setPointSize(14)
        font.setFamily("Vazir")

        self.setWindowTitle("جست و جو درخواست ها")
        icon = QIcon('pics/search.png')
        self.setWindowIcon(icon)
        self.setFixedWidth(1000)
        self.setFixedHeight(700)
        self.setObjectName("mainsspage")
        self.setFont(font)
        self.setStyleSheet("\n"
            "#mainsspage{\n"
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
        self.QBtn.clicked.connect(self.searchReqs)
        
        layout = QVBoxLayout()

        self.searchinput = QLineEdit()
        self.searchinput.setObjectName("fname_txt")
        self.searchinput.setPlaceholderText("نام و نام خانوادگی(به صورت کامل )")
        
        
        #############################################################
        self.tableWidget = QTableWidget()
        self.tableWidget.setGeometry(QtCore.QRect(120, 150, 521, 192))
        self.tableWidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(1)
        item = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Vazir")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Vazir")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Vazir")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Vazir")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Vazir")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Vazir")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Vazir")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setItem(0, 0, item)
        item = QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Vazir")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setItem(0, 1, item)
        item = QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Vazir")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setItem(0, 2, item)
        item = QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Vazir")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setItem(0, 3, item)
        item = QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Vazir")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setItem(0, 4, item)
        item = QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Vazir")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setItem(0, 5, item)
        
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText("1")
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText("نام ونام خانوادگی")
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText("تاریخ پرداخت")
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText("آیتم درخواستی")
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText("مبلغ پرداختی")
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText("نام متصدی")
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText("وضعیت درخواست")
        self.__sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        #############################################################
        
        
        layout.addWidget(self.searchinput)
        layout.addWidget(self.tableWidget)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)
    
    
    def searchReqs(self):
        fname = self.searchinput.text()
        if not fname:
            QMessageBox.warning(self, 'هشدار', "کادر مورد نظر را پر بکنید")
        else:
            try:
                # Open the database connection
                self.conn = sqlite3.connect(SALES_DB_FILE)
                self.c = self.conn.cursor()
                
                # Execute the query and fetch results
                result = self.c.execute("SELECT fullname, date, req_item, price, regerfnm, req_stat FROM salesinfo WHERE fullname = ?", (fname,))
                rows = result.fetchall()

                if rows:
                    self.tableWidget.setRowCount(len(rows))
                    self.tableWidget.setColumnCount(6)

                    for row_index, row in enumerate(rows):
                        for col_index, value in enumerate(row):
                            # Create a font
                            font = QFont()
                            font.setWeight(75)
                            font.setBold(True)
                            font.setFamily("Vazir")
                            font.setPointSize(10)

                            # Create a QTableWidgetItem with the value
                            item = QTableWidgetItem(str(value))

                            # Make the item non-editable
                            item.setFlags(item.flags() & ~Qt.ItemIsEditable)

                            # Set the font for the item
                            item.setFont(font)

                            # Set the item in the tableWidget
                            self.tableWidget.setItem(row_index, col_index, item)

                    # Restore the sorting setting
                    self.tableWidget.setSortingEnabled(self.__sortingEnabled)
                else:
                    QMessageBox.warning(self, 'هشدار', 'درخواست مورد نظر پیدا نشد یا وجود ندارد')
            except Exception as e:
                # Handle exceptions and show an error message
                QMessageBox.warning(self, 'خطا', f'خطا در جستجو: {str(e)}')
            finally:
                # Ensure the database connection is closed
                self.conn.close()
    

class DeleteDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(DeleteDialog, self).__init__(*args, **kwargs)
        
        font = QFont()
        font.setBold(True)
        font.setPointSize(14)
        font.setFamily("Vazir")
        
        self.setWindowTitle("حذف درخواست")
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
        self.deleteinput.setPlaceholderText("نام ونام خانوادگی درخواست کننده:")
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
                self.conn = sqlite3.connect(SALES_DB_FILE)
                self.c = self.conn.cursor()
                self.c.execute("DELETE FROM salesinfo WHERE fullname = ?", (delrol,))
                self.conn.commit()
                self.c.close()
                self.conn.close()
                if self.c.rowcount > 0:
                    QMessageBox.information(self, 'موفقیت آمیز', 'درخواست با موفقیت حذف شد')
                    self.close()
                else:
                    QMessageBox.warning(self, 'هشدار', 'درخواست مورد نظر حذف نشد یا وجود ندارد')
                self.close()
            except sqlite3.Error as e:
                QMessageBox.warning(self, 'خطا', f'خطا در حذف درخواست: {str(e)}')
                self.close()



class UpdateReqs(QDialog):
    def __init__(self, *args, **kwargs):
        super(UpdateReqs, self).__init__(*args, **kwargs)
        
        ### Page Font ###
        font = QFont()
        font.setBold(True)
        font.setPointSize(14)
        font.setFamily("Vazir")

        ### Main Window ###
        self.setWindowTitle("ویرایش درخواست ها")
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
            "}\n"
            "#phoning_txt{\n"
            "    background: transparent;\n"
            "    border: none;\n"
            "    border-bottom: 5px solid rgb(5, 152, 250);\n"
            "    padding: 10px;\n"
            "    color: #000;\n"
            "}\n"
            "#reqstat_txt{\n"
            "    background: transparent;\n"
            "    border: none;\n"
            "    border-bottom: 5px solid rgb(5, 152, 250);\n"
            "    padding: 10px;\n"
            "    color: #000;\n"
            "}\n")
        self.setWindowTitle("ویرایش درخواست ها")
        self.setFixedWidth(800)
        self.setFixedHeight(800)
        self.setObjectName("mainpage")
        
        ### Main Window Components ###
        self.editbtn = QPushButton()
        self.editbtn.setText("اعمال تغییرات")
        self.editbtn.setFont(font)
        self.editbtn.setObjectName("edit_btn")
        self.editbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.editbtn.clicked.connect(self.editReqs)
        
        self.closeBtn = QPushButton()
        self.closeBtn.setText("بستن")
        self.closeBtn.setFont(font)
        self.closeBtn.setObjectName("close_btn")
        self.closeBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.closeBtn.clicked.connect(self.close)
        
        layout = QVBoxLayout()
        
        self.rollid = QLineEdit()
        self.rollid.setObjectName("rollid_txt")
        self.rollid.setPlaceholderText("شماره ردیف درخواست مورد نظر را وارد کنید")
                
        self.datef = QLineEdit()
        self.datef.setObjectName("fname_txt")
        self.datef.setPlaceholderText("ویرایش تاریخ ")

        self.fname = QLineEdit()
        self.fname.setObjectName("age_txt")
        self.fname.setPlaceholderText("ویرایش نام ونام خانوادگی")
        
        self.reqsub = QLineEdit()
        self.reqsub.setObjectName("phone_txt")
        self.reqsub.setPlaceholderText("ویرایش موضوع درخواست")
        
        self.req_item = QLineEdit()
        self.req_item.setObjectName("id_txt")
        self.req_item.setPlaceholderText("ویرایش آیتم درخواستی")
        
        self.price_tag = QLineEdit()
        self.price_tag.setObjectName("paydt_txt")
        self.price_tag.setPlaceholderText("ویرایش قیمت آیتم درخواستی")

        self.addrs = QLineEdit()
        self.addrs.setObjectName("adrs_txt")
        self.addrs.setPlaceholderText("ویرایش آدرس منزل")
        
        self.phone = QLineEdit()
        self.phone.setObjectName("phoning_txt")
        self.phone.setInputMask("99999999999")
        self.phone.setPlaceholderText("ویرایش شماره تماس در خواست کننده")
        
        self.req_stat = QComboBox()
        self.req_stat.setObjectName("reqstat_txt")
        self.req_stat.addItem("با موفقیت انجام شد")
        self.req_stat.addItem("درحال انجام شدن")
        self.req_stat.addItem("وقفه در انجام")
        self.req_stat.addItem("لغو شد")
        self.req_stat.addItem("خطا در انجام")
        self.req_stat.setPlaceholderText("ویرایش وضعیت سفارش")

        layout.addWidget(self.rollid)
        layout.addWidget(self.datef)
        layout.addWidget(self.fname)
        layout.addWidget(self.reqsub)
        layout.addWidget(self.req_item)
        layout.addWidget(self.price_tag)
        layout.addWidget(self.addrs)
        layout.addWidget(self.phone)
        layout.addWidget(self.req_stat)
        layout.addWidget(self.editbtn)
        layout.addWidget(self.closeBtn)
        self.setLayout(layout)
        
    def editReqs(self):
        roll_id = self.rollid.text()
        date = self.datef.text()
        fullname = self.fname.text()
        reqsubj = self.reqsub.text()
        reqitem = self.req_item.text()
        price = self.price_tag.text()
        addrs = self.addrs.text()
        phone = self.phone.text()
        reqstat = self.req_stat.itemText(self.req_stat.currentIndex())

        if not roll_id or not date or not phone or not fullname or not addrs or not reqsubj or not reqitem or not price or not reqstat:
            QMessageBox.warning(self, "هشدار", "همه فیلدها باید پر شوند.")
            return

        try:
            roll_id = int(roll_id)
            price = int(price)
            phone = int(phone)
        except ValueError:
            QMessageBox.warning(self, "هشدار", "سن، شماره تماس، ردیف و قیمت باید عددی باشند.")
            return

        UPDATE_ALL = """UPDATE salesinfo SET date=?, fullname=?, req_subject=?, req_item=?, price=?, adrs=?, phone=?, req_stat=? WHERE id=?"""

        try:
            self.conn = sqlite3.connect(SALES_DB_FILE)
            self.c = self.conn.cursor()
            self.c.execute(UPDATE_ALL, (date, fullname, reqsubj, reqitem, price, addrs, phone, reqstat, roll_id))
            self.conn.commit()
            self.conn.close()
            QMessageBox.information(self, "موفقیت", "اطلاعات با موفقیت به‌روزرسانی شد.")
            self.close()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "خطا", f"خطا در به‌روزرسانی اطلاعات: {str(e)}")
            self.close()