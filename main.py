from PyQt5.QtWidgets import *
from controller import *


def main():
    app = QApplication([])
    window = Controller()
    window.show()
    app.exec_()
#I did something

if __name__ == '__main__':
    main()
