from view import *
from PyQt5.QtWidgets import *


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.PhoRadioButton.setChecked(True)
        self.MildButton1.setChecked(True)
        self.WaterRadioButton.setChecked(True)
        self.Tips1Button.setChecked(True)



        self.pushButton.clicked.connect(lambda: self.submit())
        self.pushButton_2.clicked.connect(lambda: self.clear())
    def submit(self):
        tip = 0.00
        if self.ShawarmaRadioButton.isChecked():
            # self.BeefButton2.setHidden(False)
            # self.ChickenButton2.setHidden(False)
            if self.BeefButton2.isChecked() or self.ChickenButton2.isChecked():
                if self.MildButton1.isChecked() or self.MediumButton1.isChecked() or self.SpicyButton1():
                    if self.Tips1Button.isChecked():
                        tip = 0.10
                    elif self.Tips2Button.isChecked():
                        tip = 0.15
                    elif self.Tips3Button.isChecked():
                        tip = 0.20
                    tax = 15.00 * 0.1
                    total_tip = (15.00 + tax) * tip
                    total_bill = 15.00 + tax + total_tip
                    self.receiptLabel.setText(f"\t Receipt \n Shawarma: \t\t$15.00 \n meat: \t\t\t$1.99 \n spice: mild, medium, spicy \n tax:\t\t\t${tax:.2f} \n total tip:\t\t\t${total_tip:.2f} \n total bill:\t\t${total_bill:.2f}")

    def clear(self):
        self.receiptLabel("")

