
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget, QErrorMessage
from controllers.PluginXMLHandler import PluginXMLHandler
from controllers import PluginDataService as dbHandler

class POITab(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.setObjectName("self")
        self.resize(824, 600)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.poiLabel = QtWidgets.QLabel(self)
        self.poiLabel.setStyleSheet("background-color : rgb(184, 208, 228); color : black")
        self.poiLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.poiLabel.setObjectName("poiLabel")
        self.verticalLayout.addWidget(self.poiLabel)
        self.poiSearch = QtWidgets.QLineEdit(self)
        self.poiSearch.setObjectName("poiSearch")
        self.verticalLayout.addWidget(self.poiSearch)
        self.poiList = QtWidgets.QListWidget(self)
        self.poiList.setObjectName("poiList")
        self.verticalLayout.addWidget(self.poiList)
        self.poiNewButton = QtWidgets.QPushButton(self)
        self.poiNewButton.setObjectName("poiNewButton")
        self.verticalLayout.addWidget(self.poiNewButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.detGridLayout = QtWidgets.QGridLayout()
        self.detGridLayout.setObjectName("detGridLayout")
        self.addParametersButton = QtWidgets.QPushButton(self)
        self.addParametersButton.setObjectName("addParametersButton")
        self.detGridLayout.addWidget(self.addParametersButton, 7, 0, 1, 1)
        self.poiSizeEdit = QtWidgets.QLineEdit(self)
        self.poiSizeEdit.setObjectName("poiSizeEdit")
        self.detGridLayout.addWidget(self.poiSizeEdit, 6, 1, 1, 2)
        self.poiTypeEdit = QtWidgets.QLineEdit(self)
        self.poiTypeEdit.setObjectName("poiTypeEdit")
        self.detGridLayout.addWidget(self.poiTypeEdit, 5, 1, 1, 2)
        self.poiSizeLabel = QtWidgets.QLabel(self)
        self.poiSizeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.poiSizeLabel.setObjectName("poiSizeLabel")
        self.detGridLayout.addWidget(self.poiSizeLabel, 6, 0, 1, 1)
        self.poiNameEdit = QtWidgets.QLineEdit(self)
        self.poiNameEdit.setObjectName("poiNameEdit")
        self.detGridLayout.addWidget(self.poiNameEdit, 4, 1, 1, 2)
        self.poiTypeLabel = QtWidgets.QLabel(self)
        self.poiTypeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.poiTypeLabel.setObjectName("poiTypeLabel")
        self.detGridLayout.addWidget(self.poiTypeLabel, 5, 0, 1, 1)
        self.poiNameLabel = QtWidgets.QLabel(self)
        self.poiNameLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.poiNameLabel.setObjectName("poiNameLabel")
        self.detGridLayout.addWidget(self.poiNameLabel, 4, 0, 1, 1)
        self.poiTypeMenuLabel = QtWidgets.QLabel(self)
        self.poiTypeMenuLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.poiTypeMenuLabel.setObjectName("poiTypeMenuLabel")
        self.detGridLayout.addWidget(self.poiTypeMenuLabel, 1, 0, 1, 1)
        self.poiTypeMenu = QtWidgets.QComboBox(self)
        self.poiTypeMenu.setObjectName("poiTypeMenu")
        self.detGridLayout.addWidget(self.poiTypeMenu, 1, 1, 1, 1)
        self.poiDetLabel = QtWidgets.QLabel(self)
        self.poiDetLabel.setStyleSheet("background-color : rgb(184, 208, 228); color : black")
        self.poiDetLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.poiDetLabel.setObjectName("poiDetLabel")
        self.detGridLayout.addWidget(self.poiDetLabel, 3, 0, 1, 4)
        self.poiPluginMenu = QtWidgets.QComboBox(self)
        self.poiPluginMenu.setObjectName("poiPluginMenu")
        self.detGridLayout.addWidget(self.poiPluginMenu, 0, 1, 1, 1)
        self.poiPluginLabel = QtWidgets.QLabel(self)
        self.poiPluginLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.poiPluginLabel.setObjectName("poiPluginLabel")
        self.detGridLayout.addWidget(self.poiPluginLabel, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.detGridLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.poiDelButton = QtWidgets.QPushButton(self)
        self.poiDelButton.setObjectName("poiDelButton")
        self.horizontalLayout_3.addWidget(self.poiDelButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.poiSaveButton = QtWidgets.QPushButton(self)
        self.poiSaveButton.setObjectName("poiSaveButton")
        self.horizontalLayout_3.addWidget(self.poiSaveButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 4)

        self.retranslate_ui(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.errorMsg = QErrorMessage()

        self.init_counters()
        self.load_info()
        self.connect_functionalities()
        self.poiDelButton.setDisabled(True)
        self.poiSaveButton.setDisabled(True)
        self.poiSearch.setPlaceholderText("Search...")

        self.hide_detail_view()
        self.addParametersButton.hide()
        self.parameters = []
        self.labels1 = []
        self.types = []
        self.labels2 = []
        self.pois = []


    def retranslate_ui(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("self", "Form"))
        self.poiLabel.setText(_translate("self", "Point of Interest View"))
        self.poiNewButton.setText(_translate("self", "New"))
        self.addParametersButton.setText(_translate("self", "Add Parameters"))
        self.poiSizeLabel.setText(_translate("self", "Size"))
        self.poiTypeLabel.setText(_translate("self", "Type"))
        self.poiNameLabel.setText(_translate("self", "Name"))
        self.poiTypeMenuLabel.setText(_translate("self", "Point of Interest Type"))
        self.poiDetLabel.setText(_translate("self", "Detailed Point of Interest View"))
        self.poiPluginLabel.setText(_translate("self", "Plugin"))
        self.poiDelButton.setText(_translate("self", "Delete"))
        self.poiSaveButton.setText(_translate("self", "Save"))

    def clear(self):
        self.poiTypeMenu.clear()
        self.poiPluginMenu.clear()

    def load_info(self):
        self.poiPluginMenu.addItem("None")
        plugins = dbHandler.getAllPlugins()
        for plugin in plugins:
            self.poiPluginMenu.addItem(plugin)

        self.poiPluginMenu.setCurrentIndex(0)


    def connect_functionalities(self):
        self.poiPluginMenu.currentIndexChanged.connect(self.pluginMenuChanged)
        self.poiTypeMenu.currentIndexChanged.connect(self.typeMenuChanged)
        self.poiList.itemClicked.connect(self.select_poi)
        self.poiNewButton.clicked.connect(self.add_new_poi)
        self.poiSaveButton.clicked.connect(self.save_poi)
        self.poiDelButton.clicked.connect(self.delete_poi)
        self.addParametersButton.clicked.connect(self.add_field)
        self.poiSearch.textChanged.connect(self.search)

        self.poiNameEdit.textChanged.connect(self.text_changed)
        self.poiTypeEdit.textChanged.connect(self.text_changed)
        self.poiSizeEdit.textChanged.connect(self.text_changed)

    def select_poi(self, item):
        self.show_detail_view()
        self.remove_parameters()
        self.init_counters()

        poi = dbHandler.getPOI(self.poiPluginMenu.currentText(), item.text())

        self.poiNameEdit.setText(poi.name)
        self.poiTypeEdit.setText(poi.type)
        self.poiSizeEdit.setText(str(poi.size_return))

        allData = poi.data
        for parameter, type in allData.items():
            self.add_field_data(parameter, type)

        self.poiDelButton.setDisabled(False)
        self.poiSaveButton.setDisabled(True)

    def add_new_poi(self):
        self.poiList.setCurrentItem(None)
        if self.poiPluginMenu.currentText() == 'None':
            self.errorMsg.showMessage("Please select a plugin.")
        else:
            self.remove_parameters()
            self.show_detail_view()
            self.clearInputs()
            self.poiSaveButton.setDisabled(False)

    def save_poi(self):
        if self.poiList.currentItem() and self.poiList.currentItem().isSelected():
            pluginName = self.poiPluginMenu.currentText()
            poiName = self.poiNameEdit.text()
            type = self.poiTypeEdit.text()
            size = self.poiSizeEdit.text()
            parameters = {}
            i = 0;
            for field, paraType in zip(self.parameters, self.types):
                parameters[field.text()] = paraType.text()
                i += 1
                #parameters.append(field.text())

            if(size == ""):
                size = None
            updatedPOI = dbHandler.updatePOI(pluginName, self.poiList.currentItem().text(), poiName, type, size, parameters)
            self.poiList.currentItem().setText(updatedPOI)
            self.poiSaveButton.setEnabled(False)
        else:
            pluginName = self.poiPluginMenu.currentText()
            poiName = self.poiNameEdit.text()
            type = self.poiTypeEdit.text()
            size = self.poiSizeEdit.text()
            parameters = {}
            i = 0;
            for field, paraType in zip(self.parameters, self.types):
                parameters[field.text()] = paraType.text()
                #parameters.append(field.text())

            if(size == ""):
                size = None

            dbHandler.insertNewPOIToPlugin(pluginName, poiName, type, size, parameters)

            item = QtWidgets.QListWidgetItem(poiName)
            self.poiList.addItem(item)
            self.poiList.setCurrentItem(item)

    def delete_poi(self):
        dbHandler.deletePOI(self.poiPluginMenu.currentText(), self.poiNameEdit.text())
        self.poiList.takeItem(self.poiList.currentRow())
        self.clearInputs()
        self.hide_detail_view()

    def pluginMenuChanged(self):
        if self.poiPluginMenu.currentIndex() != -1:
            if self.poiPluginMenu.currentText() == 'None':
                self.poiList.clear()
                self.pois.clear()
                self.poiTypeMenu.clear()
                self.clearInputs()
                self.hide_detail_view()
                self.remove_parameters()
            else:
                self.poiTypeMenu.clear()
                self.poiTypeMenu.addItem("All")
                self.clearInputs()
                self.hide_detail_view()
                self.remove_parameters()
                allPoiTypes = dbHandler.getPluginPOITypes(self.poiPluginMenu.currentText())

                for type in allPoiTypes:
                    self.poiTypeMenu.addItem(type)


    def typeMenuChanged(self):
        if self.poiTypeMenu.currentText() == 'All':
            self.pois.clear()
            self.poiList.clear()
            allPoi = []
            if self.poiPluginMenu.currentText() != 'None':
                allPoi = dbHandler.getPluginPOINames(self.poiPluginMenu.currentText())

            for poi in allPoi:
                self.pois.append(poi)
                self.poiList.addItem(poi)
        else:
            if self.poiTypeMenu.currentIndex() >= 0:
                filteredList = dbHandler.getPOIFromType(self.poiPluginMenu.currentText(), self.poiTypeMenu.currentText())

                self.poiList.clear()
                self.pois.clear()
                for filter in filteredList:
                    self.pois.append(filter)
                    self.poiList.addItem(filter)

    def clearInputs(self):
        self.poiNameEdit.clear()
        self.poiSizeEdit.clear()
        self.poiTypeEdit.clear()

    # Enables the save button if any edit fields are updated
    def text_changed(self):
        _translate = QtCore.QCoreApplication.translate
        function = self.poiTypeEdit.text()
        if(function == 'Function' or function == 'function'):
            self.addParametersButton.show()
            self.poiSizeLabel.setText(_translate("self", "Return Type"))
        else:
            self.addParametersButton.hide()
            self.poiSizeLabel.setText(_translate("self", "Size"))
        self.poiSaveButton.setDisabled(False)

    def hide_detail_view(self):
        self.poiNameLabel.hide()
        self.poiSizeLabel.hide()
        self.poiTypeLabel.hide()

        self.poiNameEdit.hide()
        self.poiSizeEdit.hide()
        self.poiTypeEdit.hide()

    def show_detail_view(self):
        self.poiNameLabel.show()
        self.poiSizeLabel.show()
        self.poiTypeLabel.show()

        self.poiNameEdit.show()
        self.poiSizeEdit.show()
        self.poiTypeEdit.show()

    def remove_parameters(self):
        for field in self.parameters:
            field.clear()
            field.deleteLater()
        for label in self.labels1:
            label.deleteLater()
        for field2 in self.types:
            field2.clear()
            field2.deleteLater()
        for label2 in self.labels2:
            label2.deleteLater()

        self.parameters = []
        self.labels1 = []
        self.types = []
        self.labels2 = []

    def init_counters(self):
        self.count = 8
        self.paraCount = 1;

    def add_field(self):
        label1 = QtWidgets.QLabel(f"Parameter {self.paraCount}", self)
        label1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.detGridLayout.addWidget(label1, self.count, 0)
        field1 = QtWidgets.QLineEdit(self)
        self.detGridLayout.addWidget(field1, self.count, 1)

        label2 = QtWidgets.QLabel("Type", self)
        label2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.detGridLayout.addWidget(label2, self.count, 2)
        field2 = QtWidgets.QLineEdit(self)
        self.detGridLayout.addWidget(field2, self.count, 3)

        self.count += 1
        self.paraCount += 1
        self.labels1.append(label1)
        self.parameters.append(field1)
        self.labels2.append(label2)
        self.types.append(field2)

        field1.textChanged.connect(self.text_changed)
        field2.textChanged.connect(self.text_changed)

    def add_field_data(self, parameter, type):
        label1 = QtWidgets.QLabel(f"Parameter {self.paraCount}", self)
        label1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.detGridLayout.addWidget(label1, self.count, 0)
        field1 = QtWidgets.QLineEdit(self)
        self.detGridLayout.addWidget(field1, self.count, 1)
        field1.setText(parameter)

        label2 = QtWidgets.QLabel("Type", self)
        label2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.detGridLayout.addWidget(label2, self.count, 2)
        field2 = QtWidgets.QLineEdit(self)
        self.detGridLayout.addWidget(field2, self.count, 3)
        field2.setText(type)

        self.count += 1
        self.paraCount += 1
        self.labels1.append(label1)
        self.parameters.append(field1)
        self.labels2.append(label2)
        self.types.append(field2)

        field1.textChanged.connect(self.text_changed)
        field2.textChanged.connect(self.text_changed)

    def search(self):
        searchText = self.poiSearch.text()
        if searchText == '':
            self.poiList.clear()
            self.poiList.addItems(self.pois)
        else:
            results = [poi for poi in self.pois if poi.__contains__(searchText)]
            self.poiList.clear()
            self.poiList.addItems(results)
