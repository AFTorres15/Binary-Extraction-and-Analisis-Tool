#!/usr/bin/env python3
# coding: utf-8

import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTabWidget, QVBoxLayout
from PyQt5.QtGui import QIcon
from view import Project, Analysis, PluginManagement, POI, Documentation

app = None


class App(QMainWindow):

    def __init__(self):
        super(QMainWindow, self).__init__()
        # Initialize window size
        self.title = 'BEAT'
        screen = app.primaryScreen()
        size = screen.size()
        self.width = size.width() / 1.5
        self.height = size.height() / 1.5
        self.left = (size.width() - self.width) / 2
        self.top = (size.height() - self.height) / 2
        # File menu initialize
        self.init_ui("BEAT")

        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)
        self.show()

    # This adds a menu bar on top of our table widget
    # Has option to exit from file menu
    def init_ui(self, title):
        self.setWindowTitle(title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        main_menu = self.menuBar()
        file_menu = main_menu.addMenu('File')

        exit_button = QAction(QIcon('exit24.png'), 'Exit', self)
        exit_button.setShortcut('Ctrl+Q')
        exit_button.setStatusTip('Exit application')
        exit_button.triggered.connect(self.close)
        file_menu.addAction(exit_button)


# Table Widget Class handles tabs
class MyTableWidget(QWidget):
    binary_path = None
    project_name = None

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.project_tab = Project.ProjectTab()  # Took off parent
        self.analysis_tab = Analysis.AnalysisTab(self)
        self.plugin_tab = PluginManagement.PluginTab(self)
        self.points_of_interest_tab = POI.POITab(self)
        self.documentation_tab = Documentation.DocuTab(self)
        self.tabs.resize(600, 400)

        # Add tabs
        self.tabs.addTab(self.project_tab, "Project")
        self.tabs.addTab(self.analysis_tab, "Analysis")
        self.analysis_tab.setDisabled(True)
        self.tabs.addTab(self.plugin_tab, "Plugin Management")
        self.tabs.addTab(self.points_of_interest_tab, "Point of Interest")
        self.tabs.addTab(self.documentation_tab, "Documentation")

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

        # connect signals
        self.project_tab.window_name.connect(self.set_new_window_title)
        self.project_tab.name.connect(self.save_name)
        self.project_tab.path.connect(self.project_to_analysis)
        self.tabs.currentChanged.connect(self.on_change)

    @pyqtSlot(str)
    def save_name(self, name):
        self.project_name = name

    @pyqtSlot(str)
    def set_new_window_title(self, title):
        self.parent().setWindowTitle(title)

    @pyqtSlot(str)
    def project_to_analysis(self, project):
        QTabWidget.setCurrentIndex(self.tabs, 1)
        self.analysis_tab.setDisabled(False)
        self.binary_path = project
        self.analysis_tab.init_project()

    def on_change(self):
        if self.tabs.currentIndex() == 3:
            self.points_of_interest_tab.clear()
            self.points_of_interest_tab.load_info()

    def disable_tabs(self):
        self.project_tab.setDisabled(True)
        self.plugin_tab.setDisabled(True)
        self.points_of_interest_tab.setDisabled(True)
        self.documentation_tab.setDisabled(True)

    def enable_tabs(self):
        self.project_tab.setDisabled(False)
        self.plugin_tab.setDisabled(False)
        self.points_of_interest_tab.setDisabled(False)
        self.documentation_tab.setDisabled(False)


# MAIN
if __name__ == '__main__':
    app = QApplication(sys.argv)
    print('len', len(sys.argv))
    ex = App()
    sys.exit(app.exec_())
