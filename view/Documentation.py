from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QWidget, QMessageBox, QLineEdit
import os

class DocuTab(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.setObjectName("self")
        self.resize(598, 404)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.docViewLabel = QtWidgets.QLabel(self)
        self.docViewLabel.setStyleSheet(" background-color : rgb(184, 208, 228); color : black")
        self.docViewLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.docViewLabel.setObjectName("docViewLabel")
        self.verticalLayout.addWidget(self.docViewLabel)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.docSearchEdit = QtWidgets.QLineEdit(self)
        self.docSearchEdit.setObjectName("docSearchEdit")
        self.horizontalLayout_2.addWidget(self.docSearchEdit)
        self.docSearchButton = QtWidgets.QPushButton(self)
        self.docSearchButton.setText("")
        self.docSearchButton.setObjectName("docSearchButton")
        self.horizontalLayout_2.addWidget(self.docSearchButton)
        self.horizontalLayout_2.setStretch(0, 4)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.docList = QtWidgets.QListWidget(self)
        self.docList.setObjectName("docList")
        self.verticalLayout.addWidget(self.docList)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.docDetLabel = QtWidgets.QLabel(self)
        self.docDetLabel.setStyleSheet(" background-color : rgb(184, 208, 228); color : black")
        self.docDetLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.docDetLabel.setObjectName("docDetLabel")
        self.gridLayout.addWidget(self.docDetLabel, 0, 0, 1, 3)


        self.doc_name_label = QtWidgets.QLabel(self)
        self.doc_name_label.setStyleSheet(" background-color : rgb(184, 208, 228); color : black")
        self.doc_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.doc_name_label.setObjectName("docDetView")
        self.doc_name_label.setFixedHeight(24)
        self.gridLayout.addWidget(self.doc_name_label, 1, 0, 1, 1)
        self.doc_name = QtWidgets.QLineEdit(self)
        self.doc_name.setObjectName("docDetView")
        self.doc_name.setFixedHeight(24)
        self.gridLayout.addWidget(self.doc_name, 1, 1, 1, 1)

        self.docDetView = QtWidgets.QTextEdit(self)
        self.docDetView.setObjectName("docDetView")
        self.gridLayout.addWidget(self.docDetView, 2, 0, 1, 3)
        self.horizontalLayout.addLayout(self.gridLayout)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 4)

        self.saveButton = QtWidgets.QPushButton()##############  Save Button
        self.saveButton.setObjectName("SaveButton")
        self.saveButton.clicked.connect(self.save_button_click)
        self.gridLayout.addWidget(self.saveButton, 1, 2, 1, 1)

        self.saveButton.setEnabled(True)

        self.docList.itemClicked.connect(self.document_click)
        self.docSearchButton.clicked.connect(self.new_button_click)

        self.path = os.getcwd() + "/Documentation"

        self.retranslateUi(self)

        self.add_menu_options()

        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("self", "Form"))
        self.docViewLabel.setText(_translate("self", "Document view"))
        __sortingEnabled = self.docList.isSortingEnabled()
        self.docList.setSortingEnabled(False)
        self.docList.setSortingEnabled(__sortingEnabled)
        self.doc_name_label.setText(_translate("self", "Document Name"))
        self.docDetLabel.setText(_translate("self", "Detailed Document view"))
        self.saveButton.setText(_translate("Dialog", "Save"))
        self.docSearchButton.setText(_translate("Dialog", "New"))

    def new_button_click(self):
        self.doc_name.setReadOnly(False)
        self.saveButton.setEnabled(True)
        self.docDetView.clear()
        self.doc_name.clear()

    def save_button_click(self):

        if self.doc_name.text() == "":
            QMessageBox.question(self, 'PyQt5 message', "Please type a file name.")
            return

        file_path=self.path+"/"+str(self.doc_name.text())+".txt"

        if os.path.exists(file_path):
            okPressed = QMessageBox.question(self, 'PyQt5 message', "Overwrite exising file?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if not okPressed:
                return

        f = open(file_path, "w+")
        f.write(self.docDetView.toPlainText())
        f.close()

    def add_menu_options(self):
        self.docs = []
        self.docList.clear()
        for dirpath, dirnames, filenames in os.walk(self.path):
            for fname in filenames:
                self.docs.append(fname[:-4])
                self.docList.addItem(fname[:-4])

    def document_click(self, item):
        self.doc_name.setReadOnly(True)
        file_path=self.path+"/"+str(item.text())+".txt"
        self.doc_name.setText(str(item.text()))
        f = open(file_path, "r")
        document = f.read()
        self.docDetView.setPlainText(document)
        f.close()
