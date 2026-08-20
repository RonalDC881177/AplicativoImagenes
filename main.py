import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtWidgets import QFileDialog


class VentanaPrincipal(QMainWindow):
    """
    Ventana principal de PATRONADOR.
    """

    def __init__(self):
        super().__init__()

        # Título de la ventana
        self.setWindowTitle("PATRONADOR")

        # Tamaño inicial de la ventana
        self.resize(1000, 700)

        # Botón para seleccionar una imagen
        self.boton_seleccionar = QPushButton("Seleccionar imagen", self)

        # Posición y tamaño del botón
        self.boton_seleccionar.setGeometry(20, 20, 180, 40)

        # Conectamos el botón con la función seleccionar_imagen
        self.boton_seleccionar.clicked.connect(self.seleccionar_imagen)

    def seleccionar_imagen(self):
        """
        Abre una ventana para seleccionar una imagen.
        """

        ruta, _ = QFileDialog.getOpenFileName(
            self,
            "Seleccionar imagen",
            "",
            "Imágenes (*.jpg *.jpeg *.png *.bmp)"
        )

        # Comprobamos si el usuario seleccionó una imagen
        if ruta:
            print("Imagen seleccionada:", ruta)


# Punto de entrada de la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = VentanaPrincipal()
    ventana.show()

    sys.exit(app.exec())