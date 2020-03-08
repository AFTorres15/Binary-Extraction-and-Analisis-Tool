from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CommentView(object):
    def setupUi(self, parent):
        parent.setObjectName("Form")
        self.move_to_center(parent)
        self.gridLayout = QtWidgets.QGridLayout(parent)
        self.gridLayout.setObjectName("gridLayout")
        self.saveButton = QtWidgets.QPushButton(parent)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout.addWidget(self.saveButton, 1, 1, 1, 1)
        self.clearButton = QtWidgets.QPushButton(parent)
        self.clearButton.setObjectName("clearButton")
        self.gridLayout.addWidget(self.clearButton, 1, 2, 1, 1)
        self.commentEdit = QtWidgets.QPlainTextEdit(parent)
        self.commentEdit.setObjectName("commentEdit")
        self.gridLayout.addWidget(self.commentEdit, 0, 0, 1, 3)

        self.retranslateUi(parent)
        QtCore.QMetaObject.connectSlotsByName(parent)

    def retranslateUi(self, parent):
        _translate = QtCore.QCoreApplication.translate
        parent.setWindowTitle(_translate("Form", "Comment view"))
        self.saveButton.setText(_translate("Form", "Save"))
        self.clearButton.setText(_translate("Form", "Clear"))

    def move_to_center(self, parent):
        ag = QtWidgets.QDesktopWidget().availableGeometry()
        sg = QtWidgets.QDesktopWidget().screenGeometry()

        width = ag.width() / 5
        height = ag.height() / 4

        parent.resize(width, height)

        widget = parent.geometry()
        x = (ag.width() - widget.width()) / 2
        y = (ag.height() - widget.height()) / 2
        parent.move(x, y)