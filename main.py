import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QFileDialog,
    QLabel
)

from models.pattern import Pattern


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

        # Aquí guardaremos el patrón generado
        self.patron = None

        # Botón para seleccionar una imagen
        self.boton_seleccionar = QPushButton(
            "Seleccionar imagen",
            self
        )

        # Posición y tamaño del botón
        self.boton_seleccionar.setGeometry(
            20, 20, 180, 40
        )

        # Conectamos el botón con la función
        self.boton_seleccionar.clicked.connect(
            self.seleccionar_imagen
        )

        # Texto para mostrar el estado
        self.etiqueta_estado = QLabel(
            "No se ha seleccionado ninguna imagen.",
            self
        )

        self.etiqueta_estado.setGeometry(
            20, 80, 500, 30
        )

    def seleccionar_imagen(self):
        """
        Permite seleccionar una imagen y crear el patrón.
        """

        ruta, _ = QFileDialog.getOpenFileName(
            self,
            "Seleccionar imagen",
            "",
            "Imágenes (*.jpg *.jpeg *.png *.bmp)"
        )

        # Si el usuario canceló la selección
        if not ruta:
            return

        print("Imagen seleccionada:", ruta)

        # Crear el patrón utilizando nuestro código existente
        self.patron = Pattern.desde_imagen(
            ruta,
            50,
            50,
            20
        )

        # Mostrar información en la terminal
        print("Patrón creado correctamente")
        print("Total de casillas:", self.patron.total_casillas())
        print("Colores utilizados:", self.patron.colores_utilizados())

        # Actualizar el estado de la interfaz
        self.etiqueta_estado.setText(
            "Imagen procesada correctamente."
        )


# Punto de entrada de la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = VentanaPrincipal()
    ventana.show()

    sys.exit(app.exec())