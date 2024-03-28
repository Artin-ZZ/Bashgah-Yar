import os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import *

class Root_Npad(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Root_Npad, self).__init__(*args, **kwargs)
        self.file_path = None
        layout = QVBoxLayout()
        self.editor = QPlainTextEdit()
            
        self.resize(900, 700)
        ## Setup The Qtext Edit
        ## If none, we haven't got a file open yet (or creating new).
        self.path = None

        layout.addWidget(self.editor)

        container = QWidget()
        font = QFont()
        font.setBold(True)
        font.setFamily('Vazir')
        font.setPointSize(16)
        container.setFont(font)
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.status = QStatusBar()
        self.setStatusBar(self.status)

        file_toolbar = QToolBar("File")
        file_toolbar.setIconSize(QSize(30, 30))
        self.addToolBar(file_toolbar)
        file_menu = self.menuBar().addMenu("&File")

        open_file_action = QAction(QIcon(os.path.join('pics/NotePadIcons', 'blue-folder-open-document.png')), "Open File...", self)
        open_file_action.setStatusTip("Open File")
        open_file_action.triggered.connect(self.file_open)
        open_file_action.setShortcut(QKeySequence.StandardKey.Open)
        file_menu.addAction(open_file_action)
        file_toolbar.addAction(open_file_action)

        save_file_action = QAction(QIcon(os.path.join('pics/NotePadIcons', 'disk.png')), "Save", self)
        save_file_action.setStatusTip("Save Current Page")
        save_file_action.triggered.connect(self.file_save)
        save_file_action.setShortcut(QKeySequence.StandardKey.Save)
        file_menu.addAction(save_file_action)
        file_toolbar.addAction(save_file_action)

        saveas_file_action = QAction(QIcon(os.path.join('pics/NotePadIcons', 'disk--pencil.png')), "Save As...", self)
        saveas_file_action.setStatusTip("Save Current Page To Specified File")
        saveas_file_action.triggered.connect(self.file_saveas)
        file_menu.addAction(saveas_file_action)
        file_toolbar.addAction(saveas_file_action)

        print_action = QAction(QIcon(os.path.join('pics/NotePadIcons', 'printer.png')), "Print...", self)
        print_action.setStatusTip("Print current page")
        print_action.triggered.connect(self.file_print)
        file_menu.addAction(print_action)
        file_toolbar.addAction(print_action)

        edit_toolbar = QToolBar("Tools")
        edit_toolbar.setIconSize(QSize(30, 30))
        self.addToolBar(edit_toolbar)
        edit_menu = self.menuBar().addMenu("&Tools")

        undo_action = QAction(QIcon(os.path.join('pics/NotePadIcons', 'arrow-curve-180-left.png')), "Undo", self)
        undo_action.setStatusTip("Undo last change")
        undo_action.triggered.connect(self.editor.undo)
        edit_menu.addAction(undo_action)

        redo_action = QAction(QIcon(os.path.join('pics/NotePadIcons', 'arrow-curve.png')), "Redo", self)
        redo_action.setStatusTip("Redo last change")
        redo_action.triggered.connect(self.editor.redo)
        edit_toolbar.addAction(redo_action)
        edit_menu.addAction(redo_action)

        edit_menu.addSeparator()

        cut_action = QAction(QIcon(os.path.join('pics/NotePadIcons', 'scissors.png')), "Cut", self)
        cut_action.setStatusTip("Cut selected text")
        cut_action.triggered.connect(self.editor.cut)
        edit_toolbar.addAction(cut_action)
        edit_menu.addAction(cut_action)

        copy_action = QAction(QIcon(os.path.join('pics/NotePadIcons', 'document-copy.png')), "Copy", self)
        copy_action.setStatusTip("Copy selected text")
        copy_action.triggered.connect(self.editor.copy)
        edit_toolbar.addAction(copy_action)
        edit_menu.addAction(copy_action)

        paste_action = QAction(QIcon(os.path.join('pics/NotePadIcons', 'clipboard-paste-document-text.png')), "Paste", self)
        paste_action.setStatusTip("Paste from clipboard")
        paste_action.triggered.connect(self.editor.paste)
        edit_toolbar.addAction(paste_action)
        edit_menu.addAction(paste_action)

        select_action = QAction(QIcon(os.path.join('pics/NotePadIcons', 'selection-input.png')), "Select all", self)
        select_action.setStatusTip("Select all text")
        select_action.triggered.connect(self.editor.selectAll)
        edit_menu.addAction(select_action)

        edit_menu.addSeparator()

        wrap_action = QAction(QIcon(os.path.join('pics/NotePadIcons', 'arrow-continue.png')), "Wrap text to window", self)
        wrap_action.setStatusTip("Toggle wrap text to window")
        wrap_action.setCheckable(True)
        wrap_action.setChecked(True)
        wrap_action.triggered.connect(self.edit_toggle_wrap)
        edit_menu.addAction(wrap_action)

        help_toolbar = QToolBar("Help")
        help_toolbar.setIconSize(QSize(30, 30))
        self.addToolBar(help_toolbar)
        edit_menu = self.menuBar().addMenu("&Help")

        ab_dv_action = QAction(QIcon(os.path.join('pics/NotePadIcons', 'question.png')), "در باره سازنده", self)
        ab_dv_action.setStatusTip("در باره سازنده")
        ab_dv_action.triggered.connect(self._about_dev_info)
        edit_menu.addAction(ab_dv_action)

        edit_menu.addSeparator()
        




        self.update_title()
        self.show()

    def dialog_critical(self, s):
        dlg = QMessageBox(self)
        dlg.setText(s)
        dlg.setIcon(QMessageBox.Critical)
        dlg.show()

    def file_open(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open")
        if path:
            try:
                with open(path, "r") as file:
                    self.editor.setPlainText(file.read())
                self.file_path = path
            except Exception as e:
                self.dialog_critical(f"Error opening file: {str(e)}")

    def file_save(self):
        if self.file_path is None:
            self.file_saveas()
        else:
            try:
                with open(self.file_path, "w") as file:
                    file.write(self.editor.toPlainText())
                self.editor.document().setModified(False)
            except Exception as e:
                self.dialog_critical(f"Error saving file: {str(e)}")

    def file_saveas(self):
        try:
            path, _ = QFileDialog.getSaveFileName(self, "Save As")
            if path:
                with open(path, "w") as file:
                    file.write(self.editor.toPlainText())
                self.file_path = path
                self.editor.document().setModified(False)
        except Exception as e:
            self.dialog_critical(f"Error saving file: {str(e)}")
    
    
        except:
            QMessageBox.warning(QMessageBox(), "Warning", "Save The File In A Direction!")
    
    def file_print(self):
        dlg = QPrintDialog()
        if dlg.exec_():
            self.editor.print_(dlg.printer())
    
    def update_title(self):
        self.setWindowTitle("%s - Smart Note" % (os.path.basename(self.path) if self.path else "Untitled"))
    
    def edit_toggle_wrap(self):
        self.editor.setLineWrapMode(1 if self.editor.lineWrapMode() == 0 else 0)

    def _about_dev_info(self):
        dlg = AboutDialog()
        dlg.exec_()
        
    def closeEvent(self,event):
                reply = QMessageBox.question(self,'هشدار بستن یادداشت ها','اگر یادداشت خود ذخیره نکرده باشید یادداشت شما حذف می شود آیا مایلید از یادداشت ها خارج شوید؟',QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
                
                if reply == QMessageBox.Yes :
                    self.close()
                else :
                    try:
                        event.ignore()
                    except AttributeError:
                        pass


    # Rest of your Root_Npad class methods here...

class AboutDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(AboutDialog, self).__init__(*args, **kwargs)
        
        font = QFont()
        font.setBold(True)
        font.setPointSize(12)
        font.setFamily("Vazir")
        
        self.setFixedWidth(650)
        self.setFixedHeight(500)
        self.setFont(font)

        QBtn = QDialogButtonBox.Ok
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()


        title = QLabel("About Creator :")
        font = title.font()
        font.setPointSize(20)
        title.setFont(font)

        lbl_pic = QLabel()
        pixmap = QPixmap('pics/NotePadIcons/About_notes.png')
        pixmap = pixmap.scaledToWidth(500)
        lbl_pic.setPixmap(pixmap)
        lbl_pic.setFixedHeight(400)

        layout.addWidget(title)

        layout.addWidget(QLabel("Version 4.0.2"))
        layout.addWidget(lbl_pic)

        layout.addWidget(self.buttonBox)
        self.setLayout(layout)