from PySide2 import QtWidgets

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyConverter")
        self.setup_ui()


    def setup_ui(self):
        self.create_widgets()
        self.create_layouts()
        self.modify_widgets()
        self.add_widgets_to_layouts()
        self.setup_connections()

    def create_widgets(self):
        self.lbl_quality = QtWidgets.QLabel("Qualité:")
        self.spn_quality = QtWidgets.QSpinBox()
        self.lbl_size = QtWidgets.QLabel("Taille:")
        self.spn_size = QtWidgets.QSpinBox()
        self.lbl_dossierOut = QtWidgets.QLabel("Dossier de sortie:")
        self.le_dossierOut = QtWidgets.QLineEdit()
        self.lw_files = QtWidgets.QListWidget()
        self.btn_convert = QtWidgets.QPushButton("Conversion")
        self.lbl_dropInfo = QtWidgets.QLabel("^ Déposez les images sur l'interface")

    def modify_widgets(self):
        pass

    def create_layouts(self):
        pass

    def add_widgets_to_layouts(self):
        pass

    def setup_connections(self):
        pass
