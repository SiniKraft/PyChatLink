import sys
import nathlib as nlib

from PySide2.QtGui import QIcon, QPixmap, Qt
from PySide2.QtWidgets import QMainWindow, QMessageBox, QApplication
from ui_server_selecter import Ui_MainWindow as Ui_ServerSelecter


class ServerSelecter(QMainWindow, Ui_ServerSelecter):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.connect_to_server)

    def connect_to_server(self):
        if self.radioButton.isChecked():  # = default server button
            s = nlib.get_json_from_url("https://raw.githubusercontent.com/SiniKraft/PyChatLink/master/server-info.json")
            if s["online"]:
                ip = s["ip"]
            else:
                showerror(s["msg"], self, "Le serveur est hors-ligne !")
        else:
            ip = str(self.lineEdit_2.text())
        print(ip)


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
    win = ServerSelecter()
    win.show()
    sys.exit(app.exec_())
