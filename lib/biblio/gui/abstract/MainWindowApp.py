import numpy as np

from PIL import Image

from PyQt5.QtWidgets import QMainWindow

from biblio.gui.abstract.MainWindowAppBase import Ui_MainWindow


class MainWindowApp(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindowApp, self).__init__(parent)
        self.setupUi(self)

        self.abstract_image = None
        self.abstract_text = None

        # Connect GUI element signals to slots.
        self.btn_process.clicked.connect(self.btn_process_clicked)
        self.txt_abstract.textChanged.connect(self.txt_abstract_changed)

    def btn_process_clicked(self):
        img_array = np.random.rand(100,100,3) * 255
        self.abstract_image = Image.fromarray(img_array.astype('uint8')).convert('RGBA')

    def txt_abstract_changed(self):
        self.abstract_text = self.txt_abstract.toPlainText()
