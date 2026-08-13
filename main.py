import sys
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PATRONADOR")
        self.setGeometry(100, 100, 800, 500)

        texto = QLabel("Aplicacion de patrones funcionando")

        self.setCentralWidget(texto)

app = QApplication(sys.argv)

ventana = MainWindow()
ventana.show()

sys.exit(app.exec())