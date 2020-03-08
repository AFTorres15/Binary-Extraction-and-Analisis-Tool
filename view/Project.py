
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget, QFileDialog, QErrorMessage, QHeaderView, QMessageBox
from PyQt5.QtCore import pyqtSignal
from controllers.Static import Static
from controllers import DataService as dbHandler
from model import MongoSetup


#
# Functionality for the Projects tab page
#
class ProjectTab(QWidget):

    r2Static = None
    window_name = pyqtSignal(str)
    path = pyqtSignal(str)
    name = pyqtSignal(str)

    def __init__(self):
        QWidget.__init__(self)
        self.projects = []
        self.setObjectName("self")
        self.resize(951, 754)
        self.horizontal_layout = QtWidgets.QHBoxLayout(self)
        self.horizontal_layout.setObjectName("horizontalLayout")
        self.vertical_layout = QtWidgets.QVBoxLayout()
        self.vertical_layout.setObjectName("verticalLayout")
        self.project_label = QtWidgets.QLabel(self)
        self.project_label.setAlignment(QtCore.Qt.AlignCenter)
        self.project_label.setObjectName("projectLabel")
        self.project_label.setStyleSheet("background-color : rgb(184, 208, 228); color : black")
        self.vertical_layout.addWidget(self.project_label)
        self.project_search = QtWidgets.QLineEdit(self)
        self.project_search.setObjectName("projectSearch")
        self.vertical_layout.addWidget(self.project_search)
        self.project_list = QtWidgets.QListWidget(self)
        self.project_list.setObjectName("projectList")
        self.vertical_layout.addWidget(self.project_list)
        self.project_new_button = QtWidgets.QPushButton(self)
        self.project_new_button.setObjectName("projectNewButton")
        self.vertical_layout.addWidget(self.project_new_button)
        self.horizontal_layout.addLayout(self.vertical_layout)

        self.error_msg = QErrorMessage()

        self.vertical_layout_2 = QtWidgets.QVBoxLayout()
        self.vertical_layout_2.setObjectName("verticalLayout_2")
        self.det_project_label = QtWidgets.QLabel(self)
        self.det_project_label.setAlignment(QtCore.Qt.AlignCenter)
        self.det_project_label.setObjectName("detProjectLabel")
        self.det_project_label.setStyleSheet("background-color : rgb(184, 208, 228); color : black")
        self.vertical_layout_2.addWidget(self.det_project_label)
        self.grid_layout_2 = QtWidgets.QGridLayout()
        self.grid_layout_2.setObjectName("gridLayout_2")
        self.project_desc_label = QtWidgets.QLabel(self)
        self.project_desc_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop |
                                             QtCore.Qt.AlignTrailing)
        self.project_desc_label.setObjectName("projectDescLabel")
        self.grid_layout_2.addWidget(self.project_desc_label, 1, 2, 1, 1)
        self.project_desc_edit = QtWidgets.QPlainTextEdit(self)
        self.project_desc_edit.setObjectName("projectDescEdit")
        self.grid_layout_2.addWidget(self.project_desc_edit, 1, 3, 1, 1)
        self.project_name_label = QtWidgets.QLabel(self)
        self.project_name_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing |
                                             QtCore.Qt.AlignVCenter)
        self.project_name_label.setObjectName("projectNameLabel")
        self.grid_layout_2.addWidget(self.project_name_label, 0, 2, 1, 1)
        self.project_name_edit = QtWidgets.QLineEdit(self)
        self.project_name_edit.setObjectName("projectNameEdit")
        self.grid_layout_2.addWidget(self.project_name_edit, 0, 3, 1, 1)
        self.project_path_edit = QtWidgets.QLineEdit(self)
        self.project_path_edit.setObjectName("projectPathEdit")
        self.grid_layout_2.addWidget(self.project_path_edit, 2, 3, 1, 1)
        self.project_prop_label = QtWidgets.QLabel(self)
        self.project_prop_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop |
                                             QtCore.Qt.AlignTrailing)
        self.project_prop_label.setObjectName("projectPropLabel")
        self.grid_layout_2.addWidget(self.project_prop_label, 3, 2, 1, 1)
        self.project_path_label = QtWidgets.QLabel(self)
        self.project_path_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing |
                                             QtCore.Qt.AlignVCenter)
        self.project_path_label.setObjectName("projectPathLabel")
        self.grid_layout_2.addWidget(self.project_path_label, 2, 2, 1, 1)
        self.project_path_button = QtWidgets.QPushButton(self)
        self.project_path_button.setObjectName("projectPathButton")
        self.grid_layout_2.addWidget(self.project_path_button, 2, 4, 1, 1)
        self.project_del_button = QtWidgets.QPushButton(self)
        self.project_del_button.setObjectName("projectDelButton")
        self.grid_layout_2.addWidget(self.project_del_button, 4, 1, 1, 1)
        self.project_save_button = QtWidgets.QPushButton(self)
        self.project_save_button.setObjectName("projectSaveButton")
        self.grid_layout_2.addWidget(self.project_save_button, 4, 4, 1, 1)
        self.project_prop_table = QtWidgets.QTableWidget(self)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.project_prop_table.sizePolicy().hasHeightForWidth())
        self.project_prop_table.setSizePolicy(size_policy)
        self.project_prop_table.setRowCount(12)
        self.project_prop_table.setColumnCount(2)
        self.project_prop_table.setObjectName("projectPropTable")
        self.project_prop_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        item = QtWidgets.QTableWidgetItem()
        self.project_prop_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.project_prop_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.project_prop_table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.project_prop_table.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.project_prop_table.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.project_prop_table.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.project_prop_table.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.project_prop_table.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.project_prop_table.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.project_prop_table.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.project_prop_table.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.project_prop_table.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.project_prop_table.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.project_prop_table.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.project_prop_table.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.project_prop_table.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.project_prop_table.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.project_prop_table.setItem(8, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.project_prop_table.setItem(9, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.project_prop_table.setItem(9, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.project_prop_table.setItem(10, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.project_prop_table.setItem(10, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.project_prop_table.setItem(11, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.project_prop_table.setItem(11, 1, item)
        self.project_prop_table.horizontalHeader().setVisible(True)
        self.project_prop_table.horizontalHeader().setDefaultSectionSize(83)
        self.project_prop_table.horizontalHeader().setStretchLastSection(False)
        self.project_prop_table.verticalHeader().setVisible(False)
        self.grid_layout_2.addWidget(self.project_prop_table, 3, 3, 1, 1)
        self.vertical_layout_2.addLayout(self.grid_layout_2)
        self.horizontal_layout.addLayout(self.vertical_layout_2)
        self.horizontal_layout.setStretch(0, 1)
        self.horizontal_layout.setStretch(1, 4)

        self.retranslate_ui(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        MongoSetup.global_init()
        self.connect_functionalities()
        self.load_projects()
        self.project_search.setPlaceholderText("Search...")

    def retranslate_ui(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("self", "Form"))
        self.project_label.setText(_translate("self", "Project view"))
        self.project_new_button.setText(_translate("self", "New"))
        self.det_project_label.setText(_translate("self", "Detailed Project view"))
        self.project_desc_label.setText(_translate("self", "Project Description"))
        self.project_name_label.setText(_translate("self", "Project Name"))
        self.project_prop_label.setText(_translate("self", "Binary File Properties"))
        self.project_path_label.setText(_translate("self", "Binary File Path"))
        self.project_path_button.setText(_translate("self", "Browse"))
        self.project_del_button.setText(_translate("self", "Delete"))
        self.project_save_button.setText(_translate("self", "Save"))
        item = self.project_prop_table.horizontalHeaderItem(0)
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText(_translate("self", "Name"))
        item = self.project_prop_table.horizontalHeaderItem(1)
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText(_translate("self", "Value"))
        __sortingEnabled = self.project_prop_table.isSortingEnabled()
        self.project_prop_table.setSortingEnabled(False)
        item = self.project_prop_table.item(0, 0)
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText(_translate("self", "OS"))
        item = self.project_prop_table.item(1, 0)
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText(_translate("self", "Binary Type"))
        item = self.project_prop_table.item(2, 0)
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText(_translate("self", "Machine"))
        item = self.project_prop_table.item(3, 0)
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText(_translate("self", "Class"))
        item = self.project_prop_table.item(4, 0)
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText(_translate("self", "Bits"))
        item = self.project_prop_table.item(5, 0)
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText(_translate("self", "Language"))
        item = self.project_prop_table.item(6, 0)
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText(_translate("self", "Canary"))
        item = self.project_prop_table.item(7, 0)
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText(_translate("self", "Crypto"))
        item = self.project_prop_table.item(8, 0)
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText(_translate("self", "Nx"))
        item = self.project_prop_table.item(9, 0)
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText(_translate("self", "Pic"))
        item = self.project_prop_table.item(10, 0)
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText(_translate("self", "Relocs"))
        item = self.project_prop_table.item(11, 0)
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText(_translate("self", "Stripped"))
        self.project_prop_table.setSortingEnabled(__sortingEnabled)

        self.project_path_edit.setReadOnly(True)

        self.hide_detailed_view()

    # Connects each button to their respective function
    def connect_functionalities(self):
        self.project_list.itemClicked.connect(self.select_project)
        self.project_list.itemDoubleClicked.connect(self.project_double_click)
        self.project_new_button.clicked.connect(self.add_new_project)
        self.project_path_button.clicked.connect(self.browse_click)
        self.project_del_button.clicked.connect(self.delete_project)
        self.project_save_button.clicked.connect(self.save_project)

        self.project_desc_edit.textChanged.connect(self.text_changed)
        self.project_name_edit.textChanged.connect(self.text_changed)
        self.project_search.textChanged.connect(self.search)

    # Load all the saved projects to the Project view
    def load_projects(self):
        names = dbHandler.getAllProjects()
        for name in names:
            self.projects.append(name)
            self.project_list.addItem(name)

    # Shows detailed view of any clicked project
    def select_project(self, item):
        self.project_name_edit.setReadOnly(True)
        title = 'BEAT - ' + item.text()
        self.window_name.emit(title)
        self.parent().setWindowTitle(title)
        self.show_detailed_view()
        self.project_path_button.hide()
        self.project_name_edit.setText(item.text())
        self.project_name_edit.setDisabled(True)
        project = dbHandler.getProject(item.text())
        self.project_desc_edit.setPlainText(project.description)
        self.project_path_edit.setText(project.path)

        properties = project.properties
        for index in range(len(properties)):
            item = QtWidgets.QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            item.setText(properties[index])
            self.project_prop_table.setItem(index, 1, item)

        self.project_save_button.setDisabled(True)

    # Double click to go to analysis tab with current project
    def project_double_click(self):
        self.name.emit(self.project_name_edit.text())
        self.path.emit(self.project_path_edit.text())

    # Prepares detailed view for creation of new project
    def add_new_project(self):
        self.project_name_edit.setDisabled(False)
        self.project_name_edit.setReadOnly(False)
        self.project_path_label.setStyleSheet("color : Black")
        self.project_name_label.setStyleSheet("color : Black")
        item = self.project_list.currentItem()
        if item:
            self.window_name.emit("Beat")
            item.setSelected(False)
            self.clear_inputs()
            for index in range(12):
                item = QtWidgets.QTableWidgetItem()
                item.setText("")
                self.project_prop_table.setItem(index, 1, item)

        self.show_detailed_view()

    # Deletes currently selected project
    def delete_project(self):
        item = self.project_list.currentItem()
        name = self.project_name_edit.text()
        if item and name:
            reply = QMessageBox.question(self, "Delete project",
                                         "Are you sure you want to delete this project?",
                                         QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                dbHandler.deleteProject(name)
                self.project_list.takeItem(self.project_list.currentRow())
                self.hide_detailed_view()
        else:
            self.hide_detailed_view()


    # Gets text from fields and saves them into a database
    def save_project(self):
        # Check if saving existing project
        if self.project_list.currentItem() and self.project_list.currentItem().isSelected():
            name = self.project_name_edit.text()
            desc = self.project_desc_edit.toPlainText()
            project = self.project_list.currentItem().text()
            updatedProject = dbHandler.updateProject(project, name, desc)
            self.project_list.currentItem().setText(updatedProject)
            self.project_save_button.setEnabled(False)
        else: # Else create new project
            name = self.project_name_edit.text()
            desc = self.project_desc_edit.toPlainText()
            path = self.project_path_edit.text()

            # Check that path is exists
            if not path:
                self.error_msg.showMessage("Please provide a binary file.")
                self.project_path_label.setStyleSheet("color : red")
                return

            properties = []
            for i in range(12):
                properties.append(self.project_prop_table.item(i, 1).text())

            self.project_path_label.setStyleSheet("color : Black")

            # Check that name is not empty
            if not name:
                self.error_msg.showMessage("Please provide a name.")
                self.project_name_label.setStyleSheet("color : red")
                return

            # Check that another project with the same name doesn't already exist
            for project in self.projects:
                if project.__eq__(name):
                    self.error_msg.showMessage("A project with the same name already exists.")
                    self.project_name_label.setStyleSheet("color : red")
                    return

            self.project_name_label.setStyleSheet("color : Black")

            dbHandler.createProject(name, desc, path, properties) # create the project

            item = QtWidgets.QListWidgetItem(name)
            self.project_list.addItem(item)
            self.project_list.setCurrentItem(item)

            # Add to local list as well

            self.project_save_button.setEnabled(False)
            self.project_path_button.hide()

    # Opens a browser window where user can select a binary to import
    def browse_click(self):
        file_path, _ = QFileDialog.getOpenFileName(self)
        self.project_path_edit.setText(file_path)
        self.r2Static = Static(file_path, [])
        info_list = self.r2Static.getFileInfo()
        for i, info in enumerate(info_list):
            item = QtWidgets.QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            item.setText(str(info))
            self.project_prop_table.setItem(i, 1, item)

        if not self.project_prop_table.item(2, 1).text().__contains__('x86'):
            self.error_msg.showMessage("File is not of type x86.")
            self.project_path_edit.clear()


    # Enables the save button if any edit fields are updated
    def text_changed(self):
        self.project_save_button.setDisabled(False)

    # Shows the detailed view
    def show_detailed_view(self):
        self.det_project_label.show()
        self.project_desc_label.show()
        self.project_desc_edit.show()
        self.project_name_label.show()
        self.project_name_edit.show()
        self.project_prop_label.show()
        self.project_prop_table.show()
        self.project_path_label.show()
        self.project_path_edit.show()
        self.project_path_button.show()
        self.project_del_button.show()
        self.project_save_button.show()

    # Hides the detailed view
    def hide_detailed_view(self):
        self.det_project_label.hide()
        self.project_desc_label.hide()
        self.project_desc_edit.hide()
        self.project_name_label.hide()
        self.project_name_edit.hide()
        self.project_prop_label.hide()
        self.project_prop_table.hide()
        self.project_path_label.hide()
        self.project_path_edit.hide()
        self.project_path_button.hide()
        self.project_del_button.hide()
        self.project_save_button.hide()

    # Clears all text on detailed view in preparation of new input
    def clear_inputs(self):
        self.project_name_edit.clear()
        self.project_desc_edit.clear()
        self.project_path_edit.clear()

    # Searches user input against the list of projects
    def search(self):
        searchText = self.project_search.text()
        if searchText == '':
            self.project_list.clear()
            self.project_list.addItems(self.projects)
        else:
            results = [project for project in self.projects if project.__contains__(searchText)]
            self.project_list.clear()
            self.project_list.addItems(results)
