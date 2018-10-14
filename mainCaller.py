#!/usr/bin/env python3
from mainWindow import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore
import sys
import os
import sqlite3
from sqlite3 import Error

class mainWindowController(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(mainWindowController, self).__init__()
        self.setupUi(self)
        self.database = os.path.join(os.path.dirname(os.path.abspath(__file__)), "database.db")
        self.conn = self.create_connection(self.database)
        if self.conn is not None:
            self.cur = self.conn.cursor()
            self.cur.execute("SELECT * FROM albums")
         
            rows = self.cur.fetchall()
         
            self.tableWidget.setRowCount(len(rows))
            self.tableWidget.setColumnCount(3)
            self.tableWidget_2.setRowCount(len(rows))
            self.tableWidget_2.setColumnCount(3)

            for i in range(0, len(rows)):
                self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(rows[i][0])))
                self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(rows[i][1])))
                self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(rows[i][2])))

                self.tableWidget_2.setItem(i, 0, QtWidgets.QTableWidgetItem(str(rows[i][0])))
                self.tableWidget_2.setItem(i, 1, QtWidgets.QTableWidgetItem(str(rows[i][1])))
                self.tableWidget_2.setItem(i, 2, QtWidgets.QTableWidgetItem(str(rows[i][2])))
            self.tableWidget.setVisible(False)
            for i in range(self.tableWidget.horizontalHeader().count()):
                self.tableWidget.horizontalHeader().setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
            self.tableWidget.show()
            self.tableWidget.setVisible(True)

            self.tableWidget_2.setVisible(False)
            for i in range(self.tableWidget_2.horizontalHeader().count()):
                self.tableWidget_2.horizontalHeader().setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
            self.tableWidget_2.show()
            self.tableWidget_2.setVisible(True)
             
    def create_connection(self,db_file):
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)
     
        return None
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = mainWindowController()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()