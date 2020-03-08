from PyQt5.QtWidgets import QWidget, QInputDialog, QLineEdit
from PyQt5.QtCore import Qt
from controllers.Static import Static
from controllers.Dynamic import Dynamic
from view.CommentView import  *
from view.OutputFieldView import *
from model.ProjectPOI import ProjectPOI
from controllers import DataService as DS
from model.Projects import Project
from model.ProjectPOI import ProjectPOI
import mongoengine, json
from model.POI import Function, Var, String, POI
from model import ProjectPOI
from controllers import PluginDataService as dbHandler
from model.POI import import_ProjectPOI
from controllers import ProjectRunManager as PRM
#from jinja2 import Environment, FileSystemLoader

class AnalysisTab(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.poi_types = ['Function','String']
        self.tab = self.parent()
        self.terminal = QtWidgets.QTextEdit(self)
        self.setObjectName("self")
        self.resize(919, 728)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.outputButton = QtWidgets.QPushButton(self)
        self.outputButton.setObjectName("outputButton")
        self.gridLayout.addWidget(self.outputButton, 1, 8, 1, 1)
        self.outputButton.hide()
        self.saRunButton = QtWidgets.QPushButton(self)
        self.saRunButton.setObjectName("saRunButton")
        self.gridLayout.addWidget(self.saRunButton, 1, 1, 1, 1)
        self.daRunButton = QtWidgets.QPushButton(self)
        self.daRunButton.setObjectName("daRunButton")
        self.gridLayout.addWidget(self.daRunButton, 1, 5, 1, 1)
        self.daLabel = QtWidgets.QLabel(self)
        self.daLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.daLabel.setObjectName("daLabel")
        self.gridLayout.addWidget(self.daLabel, 1, 3, 1, 2)
        self.daStopButton = QtWidgets.QPushButton(self)
        self.daStopButton.setObjectName("daStopButton")
        self.gridLayout.addWidget(self.daStopButton, 1, 6, 1, 1)
        self.saLabel = QtWidgets.QLabel(self)
        self.saLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.saLabel.setObjectName("saLabel")
        self.gridLayout.addWidget(self.saLabel, 1, 0, 1, 1)
        self.poiTypeLabel = QtWidgets.QLabel(self)
        self.poiTypeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.poiTypeLabel.setObjectName("poiTypeLabel")
        self.gridLayout.addWidget(self.poiTypeLabel, 2, 0, 1, 1)
        self.pluginLabel = QtWidgets.QLabel(self)
        self.pluginLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pluginLabel.setObjectName("pluginLabel")
        self.gridLayout.addWidget(self.pluginLabel, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 7, 1, 1)
        self.commentButton = QtWidgets.QPushButton(self)
        self.commentButton.setObjectName("commentButton")
        self.gridLayout.addWidget(self.commentButton, 2, 8, 1, 1)
        self.commentButton.hide()
        self.poiTypeMenu = QtWidgets.QComboBox(self)
        self.poiTypeMenu.setObjectName("poiTypeMenu")
        self.gridLayout.addWidget(self.poiTypeMenu, 2, 1, 1, 4)
        self.changing_plugin = False
        self.pluginMenu = QtWidgets.QComboBox(self)
        self.pluginMenu.setObjectName("pluginMenu")
        self.gridLayout.addWidget(self.pluginMenu, 0, 1, 1, 4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        self.runsMenu = QtWidgets.QComboBox(self)
        self.runsMenu.setObjectName("runsMenu")
        self.gridLayout.addWidget(self.runsMenu, 0, 8, 1, 1)
        self.runsLabel = QtWidgets.QLabel(self)
        self.runsLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.runsLabel.setObjectName("runsLabel")
        self.gridLayout.addWidget(self.runsLabel, 0, 7, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.poiLabel = QtWidgets.QLabel(self)
        self.poiLabel.setStyleSheet("background-color : rgb(184, 208, 228); color : black")
        self.poiLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.poiLabel.setObjectName("poiLabel")
        self.verticalLayout_4.addWidget(self.poiLabel)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.searchEdit = QtWidgets.QLineEdit(self)
        self.searchEdit.setObjectName("searchEdit")
        self.horizontalLayout_2.addWidget(self.searchEdit)
        self.searchButton = QtWidgets.QPushButton(self)
        self.searchButton.setText("")
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout_2.addWidget(self.searchButton)
        self.horizontalLayout_2.setStretch(0, 4)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.poiList = QtWidgets.QListWidget(self)
        self.poiList.setObjectName("poiList")
        self.verticalLayout_4.addWidget(self.poiList)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.detPOILabel = QtWidgets.QLabel(self)
        self.detPOILabel.setStyleSheet("background-color : rgb(184, 208, 228); color : black")
        self.detPOILabel.setAlignment(QtCore.Qt.AlignCenter)
        self.detPOILabel.setObjectName("detPOILabel")
        self.verticalLayout_6.addWidget(self.detPOILabel)
        self.detPOIList = QtWidgets.QTableWidget(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.detPOIList.sizePolicy().hasHeightForWidth())
        self.detPOIList.setSizePolicy(sizePolicy)
        self.detPOIList.setRowCount(0)
        self.detPOIList.setColumnCount(2)
        self.detPOIList.setObjectName("detPOIList")
        self.detPOIList.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.detPOIList.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.detPOIList.horizontalHeader().hide()
        self.detPOIList.verticalHeader().hide()
        self.detPOIList.resizeRowsToContents()
        self.detPOIList.resizeColumnsToContents()
        self.verticalLayout_6.addWidget(self.detPOIList)
        self.consoleLabel = QtWidgets.QLabel(self)
        self.consoleLabel.setStyleSheet("background-color : rgb(184, 208, 228); color : black")
        self.consoleLabel.setObjectName("consoleLabel")
        self.verticalLayout_6.addWidget(self.consoleLabel)
        self.terminal.setObjectName("terminal")
        self.verticalLayout_6.addWidget(self.terminal)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 4)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.connect_buttons()
        self.add_menu_options()

    def init_project(self):
        try:
            self.runsMenu.currentIndexChanged.disconnect(self.load_project_run)
            self.pluginMenu.currentIndexChanged.disconnect(self.load_plugin_data)
            self.pluginMenu.currentIndexChanged.disconnect(self.load_project_run)
        except TypeError: #when not cennected
            pass

        self.project_name = self.tab.project_name

        self.load_plugins()


        self.load_project_run()

        self.runsMenu.setCurrentIndex(self.run)
        self.runsMenu.currentIndexChanged.connect(self.load_project_run)
        self.pluginMenu.currentIndexChanged.connect(self.load_plugin_data)
        self.pluginMenu.currentIndexChanged.connect(self.load_project_run)

    def load_plugins(self, i=0):
        if self.changing_plugin:
            return

        plugins = dbHandler.getAllPlugins()
        self.pluginMenu.clear()
        self.plugin_names = []
        for plugin in plugins:
            self.plugin_names.append(plugin)
            self.pluginMenu.addItem(plugin)
        self.plugin_name = self.plugin_names[i]
        self.load_plugin_data()

    def load_plugin_data(self):
        try:
            self.runsMenu.currentIndexChanged.disconnect(self.load_project_run)
        except TypeError: #when not cennected
            pass

        self.plugin_name = self.pluginMenu.currentText()

        self.plugin_pois = dict()
        self.plugin_pois['Function'] = []
        self.plugin_pois['String'] = []
        for poi in dbHandler.getPluginPOI(self.plugin_name):
            for poi_type in self.poi_types:
                if poi.type == poi_type:
                    self.plugin_pois[poi_type].append(poi.to_dict())

        self.runsMenu.clear()
        self.run = DS.get_runs(self.project_name, self.pluginMenu.currentText())-1
        runs = [str(run) for run in range(self.run+1)[1:]]
        self.runsMenu.addItems(runs)
        self.runsMenu.currentIndexChanged.connect(self.load_project_run)

    def load_project_content(self):
        self.r2Static = Static(self.tab.binary_path, self.plugin_pois)
        if DS.getProject(self.project_run_id) is None:
            return

        for poi in DS.getAllPois(self.project_run_id):
            if poi.type.lower() == "function":
                _poi = Function(poi.name)
                for _projectpoi in poi.data:
                    _var = Var(_projectpoi.name, _projectpoi.type)
                    _var.content['value'] = _projectpoi.data
                    _poi.content['parameters'].append(_var)
                _poi.content['calls'] = poi.calls
                _return = Var()
                _return.importFromDatabase(poi.returnV)
                _poi.content['return'] = _return
                self.r2Static.content['Function'].append(_poi)
            elif poi.type.lower() == "string":
                _poi = String(poi.name)
                _poi.importFromDatabase(poi)
                self.r2Static.content['String'].append(_poi)
            else:
                continue

        self.poiList.addItems(self.r2Static.getPOINames())
        for i in range(len(self.r2Static.getPOINames())):
            list_item = self.poiList.item(i)
            item = self.r2Static.getPOI(list_item.text())

            if type(item) == Function:
                if item.check:
                    list_item.setCheckState(Qt.Checked)
                else:
                    list_item.setCheckState(Qt.Unchecked)

    def load_project_run(self):
        self.pois = []
        self.first = 0
        self.poiList.clear()
        self.detPOIList.clear()
        self.terminal.clear()

        self.project_run_id = PRM.name_to_database(self.project_name, self.pluginMenu.currentText(),self.runsMenu.currentText())

        self.daRunButton.setDisabled(True)
        self.daStopButton.setDisabled(True)
        self.saRunButton.setDisabled(False)

        self.load_project_content()



    def new_project_run(self):
        try:
            self.runsMenu.currentIndexChanged.disconnect(self.load_project_run)
        except TypeError: #when not cennected
            pass

        self.pois = []
        self.first = 0
        if self.tab.binary_path == None:
            return
        self.poiList.clear()
        self.detPOIList.clear()
        self.terminal.clear()

        self.run += 1
        self.project_run_id = PRM.name_to_database(self.project_name, self.pluginMenu.currentText(),self.run)
        self.runsMenu.addItem(str(self.run))
        self.daRunButton.setDisabled(True)
        self.daStopButton.setDisabled(True)
        self.saRunButton.setDisabled(False)

        DS.createProject(self.project_run_id, None, self.tab.binary_path, None)
        self.r2Static = Static(self.tab.binary_path, self.plugin_pois)

        self.runsMenu.currentIndexChanged.connect(self.load_project_run)

    def retranslateUi(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("self", "Form"))
        self.outputButton.setText(_translate("self", "Output Field"))
        self.saRunButton.setText(_translate("self", "Run"))
        self.daRunButton.setText(_translate("self", "Run"))
        self.daLabel.setText(_translate("self", "Dynamic Analysis"))
        self.daStopButton.setText(_translate("self", "Stop"))
        self.saLabel.setText(_translate("self", "Static Analysis"))
        self.poiTypeLabel.setText(_translate("self", "Points of Interest Type"))
        self.pluginLabel.setText(_translate("self", "Plugin"))
        self.commentButton.setText(_translate("self", "Comment"))
        self.runsLabel.setText(_translate("self", "Runs"))
        self.poiLabel.setText(_translate("self", "Points of Interest View"))
        self.detPOILabel.setText(_translate("self", "Detailed Points of Interest View"))
        self.consoleLabel.setText(_translate("self", "Console"))

        self.daRunButton.setDisabled(True)
        self.daStopButton.setDisabled(True)

    def add_menu_options(self):
        self.poiTypeMenu.addItem("All")
        self.poiTypeMenu.addItem("Strings")
        self.poiTypeMenu.addItem("Functions")
        self.poiTypeMenu.currentTextChanged.connect(self.poiTypeMenu_click)

    def poiTypeMenu_click(self, currentText):
        self.poiList.clear()

        if currentText == "Strings":
            self.poiList.addItems(self.r2Static.getStringNames())
            len = self.r2Static.getStringNames().__len__()
        if currentText == "Functions":
            self.poiList.addItems(self.r2Static.getFunctionNames())
            len = self.r2Static.getFunctionNames().__len__()
        if currentText == "All":
            self.poiList.addItems(self.r2Static.getPOINames())
            len = self.r2Static.getPOINames().__len__()

        for i in range(len):
            list_item = self.poiList.item(i)
            item = self.r2Static.getPOI(list_item.text())

            if type(item) == Function:
                if item.check:
                    list_item.setCheckState(Qt.Checked)
                else:
                    list_item.setCheckState(Qt.Unchecked)

    def connect_buttons(self):
        self.saRunButton.clicked.connect(self.static_run)
        self.daRunButton.clicked.connect(self.dynamic_run)
        self.daStopButton.clicked.connect(self.dynamic_stop)
        self.poiList.itemClicked.connect(self.poi_click)
        #self.poiList.itemChanged.connect(self.item_check_change)
        self.commentButton.clicked.connect(self.show_comment_view)
        self.outputButton.clicked.connect(self.show_output_view)

        self.searchEdit.textChanged.connect(self.search)

    def update_pois(self):
        try:
            if self.r2Static is not None:
                self.poiList.clear()
                self.poiList.addItems(self.r2Static.getPOINames())
        except AttributeError:
            pass

    def static_run(self):
        try:
            self.runsMenu.currentIndexChanged.disconnect(self.load_project_run)
            self.pluginMenu.currentIndexChanged.disconnect(self.load_plugin_data)
            self.pluginMenu.currentIndexChanged.disconnect(self.load_project_run)
        except TypeError: #when not cennected
            pass

        self.setDisabled(True)
        self.saRunButton.setDisabled(True)

        self.new_project_run()
        self.first = 0
        self.pois = []
        self.load_plugin_data()
        self.r2Static.message.connect(self.write)
        self.r2Static.finished.connect(self.static_finished)
        self.r2Static.add_poi.connect(self.save_poi)
        self.r2Static.add_function.connect(self.save_function)
        self.r2Static.start()

    def save_function(self, fpoi):
        self.pois.append(fpoi.name)
        item = QtWidgets.QListWidgetItem(fpoi.name)
        item.setCheckState(Qt.Checked)
        self.poiList.addItem(item)

        project = DS.getProject(self.project_run_id)
        project.projectFunctions.append(fpoi)
        project.save()

    def save_poi(self, ppoi):
        self.pois.append(ppoi.name)
        item = QtWidgets.QListWidgetItem(ppoi.name)
        self.poiList.addItem(item)

        project = DS.getProject(self.project_run_id)
        project.projectPOI.append(ppoi)
        project.save()

    def static_finished(self):
        self.setDisabled(False)
        self.r2Static.message.disconnect(self.write)
        self.r2Static.finished.disconnect(self.static_finished)
        self.r2Static.add_poi.disconnect(self.save_poi)
        self.r2Static.add_function.disconnect(self.save_function)

        self.runsMenu.currentIndexChanged.connect(self.load_project_run)
        self.pluginMenu.currentIndexChanged.connect(self.load_plugin_data)
        self.pluginMenu.currentIndexChanged.connect(self.load_project_run)

        self.daRunButton.setDisabled(False)
        for poi in self.r2Static.content['Function']:
            _poi_data = poi.toProjectPoi()
            poi_data = DS.getPOI(poi.content['name'])
            if poi_data != None:
                ProjectPOI.transferPOI(poi_data, _poi_data)
        DS.getProject(self.project_run_id).save()

    def add_poi(self, poi_name):
        self.pois.append(poi_name)
        item = QtWidgets.QListWidgetItem(name)
        #item.setCheckState(Qt.Checked)
        self.poiList.addItem(item)

    def poi_click(self, item):
        poi = self.r2Static.getPOI(item.text())
        poi.check = item.checkState()

        self.detPOIList.clear()
        function = self.r2Static.getPOI(item.text()).getInfo()
        self.detPOIList.setRowCount(len(function))
        self.set_table_info(function)
        #self.detPOIList.addItems(self.r2Static.getPOI(item.text()).getInfo())

    def static_stop(self):
        self.daRunButton.setDisabled(False)


    def dynamic_run(self):
        try:
            self.r2Dynamic.stop()
        except AttributeError:
            pass

        self.r2Dynamic = Dynamic()
        # add functionality to make sure dynamic run doesnt break project
        self.tab.setStyleSheet("background-color : rgb(242, 224, 224); color : black")
        self.runInstanceButton = QtWidgets.QPushButton("Dynamic Run instance running..",self)
        self.runInstanceButton.setObjectName("runInstanceButton")
        self.gridLayout.addWidget(self.runInstanceButton, 1, 7, 1, 1)


        self.runInstanceButton.setStyleSheet("background-color : rgb(255, 0, 0)")
        self.runInstanceButton.setDisabled(True)

        self.daRunButton.setDisabled(True)
        self.daStopButton.setDisabled(False)
        self.saRunButton.setDisabled(True)

        text, okPressed = QInputDialog.getText(self, "Get text", "Input Arguments", QLineEdit.Normal, "")
        self.r2Dynamic.args = text
        self.r2Dynamic.import_static(self.r2Static.getContent())
        if not self.first:
            self.first = 1
        self.r2Dynamic.start()

    def write(self, text):
        self.terminal.insertPlainText(text)

    def dynamic_stop(self):
        self.runInstanceButton.setVisible(False)
        self.tab.setStyleSheet("")
        self.r2Dynamic.stop()
        self.poiList.clear()
        self.poiList.addItems(self.r2Static.getPOINames())

        self.daRunButton.setDisabled(False)
        self.daStopButton.setDisabled(True)
        self.saRunButton.setDisabled(False)

    def search(self):
        self.poiList.clear()
        pois = []
        currentText = self.poiTypeMenu.currentText()
        if currentText == "Strings":
            pois = (self.r2Static.getStringNames())
        elif currentText == "Functions":
            pois = (self.r2Static.getFunctionNames())
        elif currentText == "All":
            pois = (self.r2Static.getPOINames())

        search_text = self.searchEdit.text()
        if search_text != '':
            pois = [poi for poi in pois if poi.__contains__(search_text)]

        self.poiList.addItems(pois)

        for i in range(self.poiList.__len__()):
            list_item = self.poiList.item(i)
            item = self.r2Static.getPOI(list_item.text())

            if type(item) == Function:
                if item.check:
                    list_item.setCheckState(Qt.Checked)
                else:
                    list_item.setCheckState(Qt.Unchecked)


    def add_an_item(self, name):
        item = QtWidgets.QListWidgetItem(name)
        item.setCheckState(Qt.Checked)
        self.poiList.addItem(item)

    def add_items(self, names):
        for name in names:
            item = QtWidgets.QListWidgetItem(name)
            item.setCheckState(Qt.Checked)
            self.poiList.addItem(item)

    def show_comment_view(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_CommentView()
        self.ui.setupUi(self.window)
        self.window.show()

    def show_output_view(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_OutputField()
        jinga_POI = self.getPOIForOutput()

        self.ui.setupUi(self.window, jinga_POI)
        self.window.show()

    def set_table_info(self, function):
        i = 0
        for field, info in function.items():
            if type(info) is list:
                self.add_list(i, field, info)
                i += 1
            else:
                self.add_table_row(i, field, str(info))
                i += 1

    def add_list(self, row, field, list):
        isDict = False
        infoStr = ""
        for item in list:
            self.write(str(type(item)))
            if(type(item) is dict):
                infoStr += self.add_dict(item) + "\n \n"
                isDict = True
            elif type(item) is Var:
                infoStr += self.add_dict(item.getInfo(" ")) + "\n \n"
                isDict = True
            else:
                infoStr += str(item) + ", "

        if isDict:
            infoStr = infoStr.rstrip('\n')
        else:
            infoStr = infoStr[0:len(infoStr) - 2]
        self.detPOIList.verticalHeader().setSectionResizeMode(row, QtWidgets.QHeaderView.ResizeToContents)
        self.add_table_row(row, field, infoStr)

    def add_dict(self, dict):
        infoStr = ""
        for field, info in dict.items():
            infoStr += str(field) + ": " + str(info) + "\n"
        infoStr = infoStr.rstrip('\n')
        return infoStr

    def add_table_row(self, row, field, value):
        fieldItem = QtWidgets.QTableWidgetItem()
        valueItem = QtWidgets.QTableWidgetItem()

        fieldItem.setText(field)
        valueItem.setText(value)

        self.detPOIList.setItem(row, 0, fieldItem)
        self.detPOIList.setItem(row, 1, valueItem)

    def getPOIForOutput(self):
        poi_dic = []

        self.poiList.clear()
        self.poiList.addItems(self.r2Static.getPOINames())
        len = self.r2Static.getPOINames().__len__()

        for i in range(len):
            list_item = self.poiList.item(i)
            # print(list_item)
            item = self.r2Static.getPOI(list_item.text())
            #print(item)
            functionsDictionary = self.r2Static.getPOI(list_item.text()).getInfo()
            # print(functionsDictionary)
            poi_dic.append((functionsDictionary))

        return poi_dic
