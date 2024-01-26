from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QFont






class Ui_MainWindow_Mp(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(956, 744)
        MainWindow.setStyleSheet("*{\n"
"    background-color: rgb(53, 53, 53);\n"
"    color: #ffffff;\n"
"}\n"
"#playlistView{\n"
"    background-image: url(./pics/bc8.jpg);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center center;\n"
"}\n"
"#menuFIle{\n"
"    background-color: #2a82da;\n"
"    color: white;\n"
"}\n"
"#menuBar{\n"
"    background-image: url(./pics/video-bg.jpg);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center center;\n"
"    color: white;\n"
"}\n"
"#menuTools{\n"
"    background-color: #2a82da;\n"
"    color: white;\n"
"}\n"
"/******************* Perv Btn ***********************/\n"
"#previousButton{\n"
"    border-radius: 30px;\n"
"    padding: 10px;\n"
"    background-color: rgb(255, 172, 251);\n"
"}\n"
"#previousButton:hover{\n"
"    border-radius: 30px;\n"
"    padding: 10px;\n"
"    background-color: rgb(232, 194, 255);\n"
"}\n"
"#previousButton:pressed{\n"
"    border-radius: 30px;\n"
"    padding: 10px;\n"
"    background-color: rgb(203, 99, 255);\n"
"}\n"
"/*************************************************/\n"
"/******************* Play Btn ***********************/\n"
"#playButton{\n"
"    border-radius: 30px;\n"
"    padding: 10px;\n"
"    background-color: rgb(203, 99, 255);\n"
"}\n"
"#playButton:hover{\n"
"    border-radius: 30px;\n"
"    padding: 10px;\n"
"    background-color: rgb(255, 99, 159);\n"
"}\n"
"#playButton:pressed{\n"
"    border-radius: 30px;\n"
"    padding: 10px;\n"
"    background-color: rgb(255, 55, 152);\n"
"}\n"
"/*************************************************/\n"
"/******************* Pause Btn ***********************/\n"
"#pauseButton{\n"
"    border-radius: 30px;\n"
"    padding: 10px;\n"
"    background-color: rgb(203, 99, 255);\n"
"}\n"
"#pauseButton:hover{\n"
"    border-radius: 30px;\n"
"    padding: 10px;\n"
"    background-color: rgb(255, 99, 159);\n"
"}\n"
"#pauseButton:pressed{\n"
"    border-radius: 30px;\n"
"    padding: 10px;\n"
"    background-color: rgb(255, 55, 152);\n"
"}\n"
"/*************************************************/\n"
"/******************* Stop Btn ***********************/\n"
"#stopButton{\n"
"    border-radius: 30px;\n"
"    padding: 10px;\n"
"    background-color: rgb(203, 99, 255);\n"
"}\n"
"#stopButton:hover{\n"
"    border-radius: 30px;\n"
"    padding: 10px;\n"
"    background-color: rgb(255, 99, 159);\n"
"}\n"
"#stopButton:pressed{\n"
"    border-radius: 30px;\n"
"    padding: 10px;\n"
"    background-color: rgb(255, 55, 152);\n"
"}\n"
"/*************************************************/\n"
"/******************* Next Btn ***********************/\n"
"#nextButton{\n"
"    border-radius: 30px;\n"
"    padding: 10px;\n"
"    background-color: rgb(255, 172, 251);\n"
"}\n"
"#nextButton:hover{\n"
"    border-radius: 30px;\n"
"    padding: 10px;\n"
"    background-color: rgb(232, 194, 255);\n"
"}\n"
"#nextButton:pressed{\n"
"    border-radius: 30px;\n"
"    padding: 10px;\n"
"    background-color: rgb(203, 99, 255);\n"
"}\n"
"/*************************************************/\n"
"/******************* View Btn ***********************/\n"
"#viewButton{\n"
"    border-radius: 30px;\n"
"    padding: 10px;\n"
"    background-color: rgb(255, 172, 251);\n"
"}\n"
"#viewButton:hover{\n"
"    border-radius: 30px;\n"
"    padding: 10px;\n"
"    background-color: rgb(232, 194, 255);\n"
"}\n"
"#viewButton:pressed{\n"
"    border-radius: 30px;\n"
"    padding: 10px;\n"
"    background-color: rgb(203, 99, 255);\n"
"}\n"
"#playlistView{\n"
"   color: #000;"
"}\n"
)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        font = QFont()
        font.setBold(True)
        font.setFamily("Vazir")
        font.setPointSize(16)
        self.playlistView = QtWidgets.QListView(self.centralWidget)
        self.playlistView.setAcceptDrops(True)
        self.playlistView.setProperty("showDropIndicator", True)
        self.playlistView.setDragDropMode(QtWidgets.QAbstractItemView.DropOnly)
        self.playlistView.setDefaultDropAction(QtCore.Qt.CopyAction)
        self.playlistView.setAlternatingRowColors(True)
        self.playlistView.setUniformItemSizes(True)
        self.playlistView.setObjectName("playlistView")
        self.playlistView.setFont(font)
        self.verticalLayout.addWidget(self.playlistView)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.currentTimeLabel = QtWidgets.QLabel(self.centralWidget)
        self.currentTimeLabel.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setFamily("Vazir")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.currentTimeLabel.setFont(font)
        self.currentTimeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.currentTimeLabel.setObjectName("currentTimeLabel")
        self.horizontalLayout_4.addWidget(self.currentTimeLabel)
        self.timeSlider = QtWidgets.QSlider(self.centralWidget)
        self.timeSlider.setMinimum(0)
        self.timeSlider.setMaximum(100)
        self.timeSlider.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.timeSlider.setStyleSheet("")
        self.timeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.timeSlider.setObjectName("timeSlider")
        self.horizontalLayout_4.addWidget(self.timeSlider)
        self.totalTimeLabel = QtWidgets.QLabel(self.centralWidget)
        self.totalTimeLabel.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setFamily("Vazir")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.totalTimeLabel.setFont(font)
        self.totalTimeLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.totalTimeLabel.setObjectName("totalTimeLabel")
        self.horizontalLayout_4.addWidget(self.totalTimeLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.previousButton = QtWidgets.QPushButton(self.centralWidget)
        self.previousButton.setMinimumSize(QtCore.QSize(80, 60))
        self.previousButton.setMaximumSize(QtCore.QSize(80, 60))
        self.previousButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.previousButton.setStatusTip("")
        self.previousButton.setWhatsThis("")
        self.previousButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./pics/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.previousButton.setIcon(icon)
        self.previousButton.setIconSize(QtCore.QSize(40, 40))
        self.previousButton.setObjectName("previousButton")
        self.horizontalLayout_5.addWidget(self.previousButton)
        self.playButton = QtWidgets.QPushButton(self.centralWidget)
        self.playButton.setMinimumSize(QtCore.QSize(80, 60))
        self.playButton.setMaximumSize(QtCore.QSize(80, 60))
        self.playButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.playButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./pics/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playButton.setIcon(icon1)
        self.playButton.setIconSize(QtCore.QSize(40, 40))
        self.playButton.setObjectName("playButton")
        self.horizontalLayout_5.addWidget(self.playButton)
        self.pauseButton = QtWidgets.QPushButton(self.centralWidget)
        self.pauseButton.setMinimumSize(QtCore.QSize(80, 60))
        self.pauseButton.setMaximumSize(QtCore.QSize(80, 60))
        self.pauseButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pauseButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./pics/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pauseButton.setIcon(icon2)
        self.pauseButton.setIconSize(QtCore.QSize(40, 40))
        self.pauseButton.setObjectName("pauseButton")
        self.horizontalLayout_5.addWidget(self.pauseButton)
        self.stopButton = QtWidgets.QPushButton(self.centralWidget)
        self.stopButton.setMinimumSize(QtCore.QSize(80, 60))
        self.stopButton.setMaximumSize(QtCore.QSize(80, 60))
        self.stopButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stopButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./pics/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopButton.setIcon(icon3)
        self.stopButton.setIconSize(QtCore.QSize(40, 40))
        self.stopButton.setObjectName("stopButton")
        self.horizontalLayout_5.addWidget(self.stopButton)
        self.nextButton = QtWidgets.QPushButton(self.centralWidget)
        self.nextButton.setMinimumSize(QtCore.QSize(80, 60))
        self.nextButton.setMaximumSize(QtCore.QSize(80, 60))
        self.nextButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nextButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("./pics/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextButton.setIcon(icon4)
        self.nextButton.setIconSize(QtCore.QSize(40, 40))
        self.nextButton.setObjectName("nextButton")
        self.horizontalLayout_5.addWidget(self.nextButton)
        self.viewButton = QtWidgets.QPushButton(self.centralWidget)
        self.viewButton.setMinimumSize(QtCore.QSize(80, 60))
        self.viewButton.setMaximumSize(QtCore.QSize(80, 60))
        self.viewButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.viewButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("./pics/video.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.viewButton.setIcon(icon5)
        self.viewButton.setIconSize(QtCore.QSize(40, 40))
        self.viewButton.setCheckable(True)
        self.viewButton.setObjectName("viewButton")
        self.horizontalLayout_5.addWidget(self.viewButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setText("")
        existpix = QPixmap("./pics/volume.png")
        resizedpixmap = existpix.scaled(40, 40)
        self.label.setPixmap(resizedpixmap)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.volumeSlider = QtWidgets.QSlider(self.centralWidget)
        self.volumeSlider.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.volumeSlider.setMinimum(0)
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setProperty("value", 100)
        self.volumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.volumeSlider.setObjectName("volumeSlider")
        self.horizontalLayout_5.addWidget(self.volumeSlider)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 956, 42))
        font = QtGui.QFont()
        font.setFamily("Vazir")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.menuBar.setFont(font)
        self.menuBar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menuBar.setMouseTracking(True)
        self.menuBar.setObjectName("menuBar")
        self.menuFIle = QtWidgets.QMenu(self.menuBar)
        self.menuFIle.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menuFIle.setObjectName("menuFIle")
        self.menuTools = QtWidgets.QMenu(self.menuBar)
        self.menuTools.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menuTools.setObjectName("menuTools")
        MainWindow.setMenuBar(self.menuBar)
        self.open_file_action = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Vazir")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.open_file_action.setFont(font)
        self.open_file_action.setObjectName("open_file_action")
        self.actionClear_Play_List = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Vazir")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.actionClear_Play_List.setFont(font)
        self.actionClear_Play_List.setObjectName("actionClear_Play_List")
        self.actionOpen_Folder = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Vazir")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.actionOpen_Folder.setFont(font)
        self.actionOpen_Folder.setObjectName("actionOpen_Folder")
        self.menuFIle.addAction(self.open_file_action)
        self.menuFIle.addAction(self.actionOpen_Folder)
        self.menuTools.addAction(self.actionClear_Play_List)
        self.menuBar.addAction(self.menuFIle.menuAction())
        self.menuBar.addAction(self.menuTools.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YAR Media PLayer"))
        self.currentTimeLabel.setText(_translate("MainWindow", "0:00"))
        self.totalTimeLabel.setText(_translate("MainWindow", "0:00"))
        self.menuFIle.setTitle(_translate("MainWindow", "FIle"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.open_file_action.setText(_translate("MainWindow", "Open File..."))
        self.actionClear_Play_List.setText(_translate("MainWindow", "Clear Play List"))
        self.actionOpen_Folder.setText(_translate("MainWindow", "Open Folder..."))