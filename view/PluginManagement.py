from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget, QMessageBox, QErrorMessage
from controllers import PluginDataService as dbHandler
from controllers.PluginXMLHandler import PluginXMLHandler

class PluginTab(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.setObjectName("Form")
        self.resize(660, 472)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pluginLayout = QtWidgets.QVBoxLayout()
        self.pluginLayout.setObjectName("pluginLayout")
        self.pluginViewLabel = QtWidgets.QLabel(self)
        self.pluginViewLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.pluginViewLabel.setObjectName("pluginViewLabel")
        self.pluginViewLabel.setStyleSheet("background-color : rgb(184, 208, 228); color : black")
        self.pluginLayout.addWidget(self.pluginViewLabel)
        self.pluginListView = QtWidgets.QListWidget(self)
        self.pluginListView.setObjectName("pluginListView")
        self.pluginLayout.addWidget(self.pluginListView)
        self.pluginNewButton = QtWidgets.QPushButton(self)
        self.pluginNewButton.setObjectName("pluginNewButton")
        self.pluginLayout.addWidget(self.pluginNewButton)
        self.horizontalLayout.addLayout(self.pluginLayout)
        self.detPluginLayout = QtWidgets.QVBoxLayout()
        self.detPluginLayout.setObjectName("detPluginLayout")
        self.detPluginLabel = QtWidgets.QLabel(self)
        self.detPluginLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.detPluginLabel.setObjectName("detPluginLabel")
        self.detPluginLabel.setStyleSheet("background-color : rgb(184, 208, 228); color : black")
        self.detPluginLayout.addWidget(self.detPluginLabel)
        self.detPluginGridLayout = QtWidgets.QGridLayout()
        self.detPluginGridLayout.setObjectName("detPluginGridLayout")
        self.pluginStructButton = QtWidgets.QPushButton(self)
        self.pluginStructButton.setObjectName("pluginStructButton")
        self.pluginStructButton.hide()
        self.detPluginGridLayout.addWidget(self.pluginStructButton, 0, 2, 1, 1)
        self.pluginStructEdit = QtWidgets.QLineEdit(self)
        self.pluginStructEdit.setObjectName("pluginStructEdit")
        self.pluginStructEdit.hide()
        self.detPluginGridLayout.addWidget(self.pluginStructEdit, 0, 1, 1, 1)
        self.pluginStructLabel = QtWidgets.QLabel(self)
        self.pluginStructLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pluginStructLabel.setObjectName("pluginStructLabel")
        self.detPluginGridLayout.addWidget(self.pluginStructLabel, 0, 0, 1, 1)
        self.pluginDelButton = QtWidgets.QPushButton(self)
        self.pluginDelButton.setObjectName("pluginDelButton")
        self.detPluginGridLayout.addWidget(self.pluginDelButton, 6, 0, 1, 1)
        self.pluginSaveButton = QtWidgets.QPushButton(self)
        self.pluginSaveButton.setObjectName("pluginSaveButton")
        self.detPluginGridLayout.addWidget(self.pluginSaveButton, 6, 2, 1, 1)
        self.pluginOutputLabel = QtWidgets.QLabel(self)
        self.pluginOutputLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pluginOutputLabel.setObjectName("pluginOutputLabel")
        self.detPluginGridLayout.addWidget(self.pluginOutputLabel, 3, 0, 1, 1)
        self.pluginNameLabel = QtWidgets.QLabel(self)
        self.pluginNameLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pluginNameLabel.setObjectName("pluginNameLabel")
        self.detPluginGridLayout.addWidget(self.pluginNameLabel, 1, 0, 1, 1)
        self.pluginOutputMenu = QtWidgets.QComboBox(self)
        self.pluginOutputMenu.setObjectName("pluginOutputMenu")
        self.pluginOutputMenu.hide()
        self.detPluginGridLayout.addWidget(self.pluginOutputMenu, 3, 1, 1, 1)
        self.pluginDescLabel = QtWidgets.QLabel(self)
        self.pluginDescLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.pluginDescLabel.setObjectName("pluginDescLabel")
        self.detPluginGridLayout.addWidget(self.pluginDescLabel, 2, 0, 1, 1)
        self.pluginPOIEdit = QtWidgets.QListWidget(self)
        self.pluginPOIEdit.setObjectName("pluginPOIEdit")
        self.detPluginGridLayout.addWidget(self.pluginPOIEdit, 4, 1, 1, 1)
        self.pluginLabelEdit = QtWidgets.QLineEdit(self)
        self.pluginLabelEdit.setObjectName("pluginLabelEdit")
        self.detPluginGridLayout.addWidget(self.pluginLabelEdit, 1, 1, 1, 1)
        self.pluginDescEdit = QtWidgets.QPlainTextEdit(self)
        self.pluginDescEdit.setObjectName("pluginDescEdit")
        self.detPluginGridLayout.addWidget(self.pluginDescEdit, 2, 1, 1, 1)
        self.pluginPOILabel = QtWidgets.QLabel(self)
        self.pluginPOILabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.pluginPOILabel.setObjectName("pluginPOILabel")
        self.detPluginGridLayout.addWidget(self.pluginPOILabel, 4, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.detPluginGridLayout.addItem(spacerItem, 5, 0, 1, 1)
        self.detPluginGridLayout.setRowStretch(0, 0)
        self.detPluginLayout.addLayout(self.detPluginGridLayout)
        self.detPluginLayout.setStretch(1, 1)
        self.horizontalLayout.addLayout(self.detPluginLayout)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.errorMsg = QErrorMessage()

        self.connect_functionalities()
        self.load_plugins()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pluginViewLabel.setText(_translate("Form", "Plugin view"))
        self.pluginNewButton.setText(_translate("Form", "New"))
        self.detPluginLabel.setText(_translate("Form", "Detailed Plugin view"))
        self.pluginDelButton.setText(_translate("Form", "Delete"))
        self.pluginSaveButton.setText(_translate("Form", "Save"))
        self.pluginOutputLabel.setText(_translate("Form", "Default Output Field"))
        self.pluginOutputLabel.hide()
        self.pluginNameLabel.setText(_translate("Form", "Plugin Name"))
        self.pluginDescLabel.setText(_translate("Form", "Plugin Description"))
        self.pluginPOILabel.setText(_translate("Form", "Points of Interests"))

    def connect_functionalities(self):
        self.pluginSaveButton.setDisabled(True)
        self.pluginDelButton.setDisabled(True)
        self.pluginListView.itemClicked.connect(self.select_plugin)
        self.pluginNewButton.clicked.connect(self.add_new_plugin)
        self.pluginSaveButton.clicked.connect(self.save_plugin)
        self.pluginDelButton.clicked.connect(self.delete_plugin)

        self.pluginLabelEdit.textChanged.connect(self.text_changed)
        self.pluginDescEdit.textChanged.connect(self.text_changed)

    def load_plugins(self):
        plugins = dbHandler.getAllPlugins()
        self.plugins = []
        for plugin in plugins:
            self.plugins.append(plugin) # local list of plugins
            self.pluginListView.addItem(plugin)

    def select_plugin(self, item):
        self.hide_import()
        self.pluginDelButton.setDisabled(False)
        self.pluginOutputMenu.clear()
        self.pluginPOIEdit.clear()
        plugin = dbHandler.getPlugin(item.text())
        self.pluginLabelEdit.setText(item.text())
        self.pluginDescEdit.setPlainText(plugin.description)
        allPOI = plugin.pluginPOI
        for poi in allPOI:
            self.pluginPOIEdit.addItem(poi.name)

        allOutput = None
        #for output in allOutput:
            #self.pluginOutputMenu.addItem(output)

        self.pluginSaveButton.setDisabled(True)


    def save_plugin(self):
        # Check if saving existing plugin
        if self.pluginListView.currentItem() and self.pluginListView.currentItem().isSelected():
            name = self.pluginLabelEdit.text()
            desc = self.pluginDescEdit.toPlainText()
            plugin = self.pluginListView.currentItem().text()
            updatedPlugin = dbHandler.updatePlugin(plugin, name, desc)
            self.pluginListView.currentItem().setText(updatedPlugin)
            self.pluginSaveButton.setEnabled(False)
        else: # Else create new plugin
            name = self.pluginLabelEdit.text()
            desc = self.pluginDescEdit.toPlainText()

            # Check that name is not empty
            if not name:
                self.errorMsg.showMessage("Please provide a name.")
                self.pluginNameLabel.setStyleSheet("color : red")
                return

            # Check that another project with the same name doesn't already exist
            for plugin in self.plugins:
                if plugin.__eq__(name):
                    self.errorMsg.showMessage("A project with the same name already exists.")
                    self.pluginLabelEdit.setStyleSheet("color : red")
                    return

            self.pluginLabelEdit.setStyleSheet("color : black")

            dbHandler.createPlugin("", "", name, desc, None)

            item = QtWidgets.QListWidgetItem(name)
            self.pluginListView.addItem(item)
            self.pluginListView.setCurrentItem(item)

            # Add to local list as well

            self.pluginSaveButton.setEnabled(False)


    def add_new_plugin(self):
        self.pluginSaveButton.setEnabled(True)
        item = self.pluginListView.currentItem()
        if item:
            item.setSelected(False)
        self.clear_fields()

    def delete_plugin(self):
        item = self.pluginListView.currentItem()
        name = self.pluginLabelEdit.text()
        if item and name:
            reply = QMessageBox.question(self, "Delete plugin", "Are you sure you want to delete this plugin?", QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                dbHandler.deletePlugin(name)
                self.pluginListView.takeItem(self.pluginListView.currentRow())
                self.clear_fields()
        else:
            return

    def clear_fields(self):
        self.pluginLabelEdit.clear()
        self.pluginDescEdit.clear()
        self.pluginOutputMenu.clear()
        self.pluginPOIEdit.clear()

    # Enables the save button if any edit fields are updated
    def text_changed(self):
        self.pluginSaveButton.setDisabled(False)

    def hide_import(self):
        self.pluginStructLabel.hide()
        self.pluginStructEdit.hide()
        self.pluginStructButton.hide()

    def show_import(self):
        self.pluginStructLabel.show()
        self.pluginStructEdit.show()
        self.pluginStructButton.show()
