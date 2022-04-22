import sys
import nathlib as nlib

from PySide2.QtGui import QIcon, QPixmap, Qt
from PySide2.QtWidgets import QMainWindow, QMessageBox, QApplication, QTableWidgetItem
from ui_server_selecter import Ui_MainWindow as Ui_ServerSelecter
from ui_chat import Ui_MainWindow as Ui_Chat


class ServerSelecter(QMainWindow, Ui_ServerSelecter):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.connect_to_server)

    def connect_to_server(self):
        ip = ""
        if self.radioButton.isChecked():  # = default server button
            s = {}
            try:
                s = nlib.get_json_from_url("https://raw.githubusercontent.com/SiniKraft/PyChatLink/master/"
                                           "server-info.json")
            except Exception as e:
                showerror("Erreur : " + str(e), self)
            if s != {}:
                if s["online"]:
                    ip = s["ip"]
                else:
                    showerror(s["msg"], self, "Le serveur est hors-ligne !")
        else:
            ip = str(self.lineEdit_2.text())
        if ip != "":
            pass  # ip is set so show login window now !


class Chat(QMainWindow, Ui_Chat):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("PyChatLink")

        self.commandLinkButton.clicked.connect(self.send_action)

    def send_action(self):
        msg = str(self.lineEdit.text())
        self.lineEdit.clear()
        self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
        self.tableWidget.setVerticalHeaderItem(self.tableWidget.rowCount() - 1, QTableWidgetItem("Pseudo"))
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 0, QTableWidgetItem(msg))


def showerror(_msg, _win=None, title="PyChatLink - Une erreur est survenue."):
    msg = QMessageBox(_win)
    msg.setWindowIcon(QIcon(QPixmap(":/images/SiniKraft-STORE-icon.png")))
    msg.setWindowTitle(title)
    msg.setIcon(QMessageBox.Critical)
    msg.setText(_msg)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()


if __name__ == "__main__":
    args = sys.argv
    args.append("--enable-smooth-scrolling")
    app = QApplication(args)
    app.setAttribute(Qt.AA_DisableWindowContextHelpButton)
    # win = ServerSelecter()
    win = Chat()
    win.show()
    sys.exit(app.exec_())
