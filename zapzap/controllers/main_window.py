from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QMoveEvent, QDesktopServices
from PyQt6.QtCore import QUrl
from PyQt6 import uic
import zapzap
from zapzap.controllers.about import About


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        uic.loadUi(zapzap.abs_path+'/view/main_window.ui', self)

        self.openDialog = None

        self.actionReload_Service.triggered.connect(self.reload_Service)
        self.actionAbout_Zapzap.triggered.connect(self.openAbout_Zapzap)
        
        self.actionLearn_More.triggered.connect(lambda: QDesktopServices.openUrl(
            QUrl('https://github.com/rafatosta/zapzap')))
        self.actionChangelog.triggered.connect(lambda: QDesktopServices.openUrl(
            QUrl('https://github.com/rafatosta/zapzap/releases')))
        self.actionSupport.triggered.connect(lambda: QDesktopServices.openUrl(
            QUrl('https://github.com/rafatosta/zapzap/issues')))

    def reload_Service(self):
        print('f5')

    def openAbout_Zapzap(self):
        self.openDialog = About(self)
        self.openDialog.show()

    def moveEvent(self, a0: QMoveEvent) -> None:
        if self.openDialog != None:
            self.openDialog.centerPos()
        return super().moveEvent(a0)
