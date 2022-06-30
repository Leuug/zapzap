import sys
import os
import zapzap
from zapzap.controllers.SingleApplication import SingleApplication
from zapzap.controllers.main_window import MainWindow
from PyQt6.QtCore import QStandardPaths
from PyQt6.QtGui import QFont, QFontDatabase

def main():
    #os.environ['QT_QPA_PLATFORM'] = 'xcb'

    app = SingleApplication(zapzap.__appid__, sys.argv)
    app.setApplicationName(zapzap.__appname__)
    app.setApplicationVersion(zapzap.__version__)
    app.setDesktopFileName(zapzap.__desktopid__)
    app.setOrganizationDomain(zapzap.__domain__)

    QFontDatabase.addApplicationFont(zapzap.font_path)
    app.setStyle('Fusion')
    app.setFont(QFont("SegoeUI"))

    # garante que teremos o diretório tmp para as fotos dos usuários utilizados nas notificações
    path = QStandardPaths.writableLocation(
        QStandardPaths.StandardLocation.AppLocalDataLocation)+'/tmp'
    if not os.path.exists(path):
        os.makedirs(path)

    window = MainWindow(app)
    app.setWindow(window)
    app.setActivationWindow(window)
    window.loadSettings()
    
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
