from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QFileDialog
from jinja2 import Environment, FileSystemLoader
from os.path import expanduser
import os.path
import os

class Ui_OutputField(QWidget):
    def setupUi(self, outputField, jinga_POI):
        outputField.setObjectName("outputField")
        self.move_to_center(outputField)
        self.gridLayout = QtWidgets.QGridLayout(outputField)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(outputField)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(outputField)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.locationEdit = QtWidgets.QLineEdit(outputField)
        self.locationEdit.setObjectName("locationEdit")
        self.gridLayout.addWidget(self.locationEdit, 2, 1, 1, 2)
        self.browseButton = QtWidgets.QPushButton(outputField)
        self.browseButton.setObjectName("browseButton")
        self.gridLayout.addWidget(self.browseButton, 2, 3, 1, 1)
        self.nameEdit = QtWidgets.QLineEdit(outputField)
        self.nameEdit.setObjectName("nameEdit")
        self.gridLayout.addWidget(self.nameEdit, 0, 1, 1, 3)
        self.generateButton = QtWidgets.QPushButton(outputField)
        self.generateButton.setObjectName("generateButton")
        self.gridLayout.addWidget(self.generateButton, 3, 3, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 2)
        self.gridLayout.setColumnStretch(2, 2)
        QtCore.QMetaObject.connectSlotsByName(outputField)
        self.connect_functionalities(jinga_POI)

        self.retranslateUi(outputField)
        QtCore.QMetaObject.connectSlotsByName(outputField)

    def retranslateUi(self, outputField):
        _translate = QtCore.QCoreApplication.translate
        outputField.setWindowTitle(_translate("outputField", "Output Field view"))
        self.label.setText(_translate("outputField", "Name"))
        self.label_3.setText(_translate("outputField", "Location"))
        self.browseButton.setText(_translate("outputField", "Browse"))
        self.generateButton.setText(_translate("outputField", "Generate"))

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

    def connect_functionalities(self,jinga_POI):
        self.browseButton.clicked.connect(self.browse_click)
        if(self.generateButton.clicked.connect(self.jinga_script)):
            self.jinga_script(jinga_POI)


        # Opens a browser window where user selects where to save
    def browse_click(self):

        filePath = QFileDialog.getExistingDirectory()
        self.locationEdit.setText(filePath)

        # calls jinga script template

    def jinga_script(self,jinga_POI):
        if type(jinga_POI) is bool:
            return
        # load semantics for jing expressions

        template_dir = 'resource'
        file_loader = FileSystemLoader(template_dir)
        env = Environment(loader=file_loader)
        template = env.get_template('POI.txt')

        # render template using python dictionary cause op or any variable

        output_expression = template.render(jinga_POI=jinga_POI)

        # print to console
        # print(output_expression)
        # Juan help with name 
        firstRun = "Jinga_ouput_Network.txt"


        directory = self.locationEdit.text()

        file_path = os.path.join(directory, firstRun)
        
       
        with open(os.path.join(directory,firstRun), "w") as file:
            file.write(output_expression)

            