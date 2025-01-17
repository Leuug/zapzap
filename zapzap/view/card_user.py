from gettext import gettext as _
# Form implementation generated from reading ui file './zapzap/view/card_user.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_CardUser(object):
    def setupUi(self, CardUser):
        CardUser.setObjectName("CardUser")
        CardUser.resize(620, 92)
        CardUser.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(CardUser)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(CardUser)
        self.frame.setMinimumSize(QtCore.QSize(620, 0))
        self.frame.setMaximumSize(QtCore.QSize(620, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.icon = QtWidgets.QLabel(self.frame)
        self.icon.setMinimumSize(QtCore.QSize(64, 64))
        self.icon.setMaximumSize(QtCore.QSize(64, 64))
        self.icon.setText("")
        self.icon.setScaledContents(True)
        self.icon.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.icon.setObjectName("icon")
        self.horizontalLayout.addWidget(self.icon)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.name = QtWidgets.QLineEdit(self.frame)
        self.name.setEnabled(True)
        self.name.setMinimumSize(QtCore.QSize(0, 30))
        self.name.setMaximumSize(QtCore.QSize(16777215, 30))
        self.name.setText("")
        self.name.setReadOnly(False)
        self.name.setClearButtonEnabled(False)
        self.name.setObjectName("name")
        self.gridLayout_2.addWidget(self.name, 0, 0, 1, 1)
        self.key = QtWidgets.QLabel(self.frame)
        self.key.setMinimumSize(QtCore.QSize(70, 30))
        self.key.setMaximumSize(QtCore.QSize(70, 30))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        self.key.setFont(font)
        self.key.setText("")
        self.key.setObjectName("key")
        self.gridLayout_2.addWidget(self.key, 1, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.btnDisable = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDisable.sizePolicy().hasHeightForWidth())
        self.btnDisable.setSizePolicy(sizePolicy)
        self.btnDisable.setMinimumSize(QtCore.QSize(100, 30))
        self.btnDisable.setMaximumSize(QtCore.QSize(100, 30))
        self.btnDisable.setObjectName("btnDisable")
        self.gridLayout.addWidget(self.btnDisable, 0, 0, 1, 1)
        self.btnDelete = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDelete.sizePolicy().hasHeightForWidth())
        self.btnDelete.setSizePolicy(sizePolicy)
        self.btnDelete.setMinimumSize(QtCore.QSize(100, 30))
        self.btnDelete.setMaximumSize(QtCore.QSize(100, 30))
        self.btnDelete.setObjectName("btnDelete")
        self.gridLayout.addWidget(self.btnDelete, 1, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(CardUser)
        QtCore.QMetaObject.connectSlotsByName(CardUser)

    def retranslateUi(self, CardUser):
        
        CardUser.setWindowTitle(_("Form"))
        self.name.setPlaceholderText(_("Enter the user name"))
        self.btnDisable.setText(_("Disable"))
        self.btnDelete.setText(_("Delete"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CardUser = QtWidgets.QWidget()
    ui = Ui_CardUser()
    ui.setupUi(CardUser)
    CardUser.show()
    sys.exit(app.exec())
