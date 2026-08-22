import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QFileDialog,
    QLabel,
    QTableWidget,
    QTableWidgetItem
)

from PySide6.QtGui import QColor

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

        self.boton_seleccionar.setGeometry(
            20, 20, 180, 40
        )

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

        # Tabla donde mostraremos el patrón
        self.tabla_patron = QTableWidget(
            self
        )

        self.tabla_patron.setGeometry(
            20, 120, 900, 520
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

        # Crear el patrón
        self.patron = Pattern.desde_imagen(
            ruta,
            50,
            50,
            20
        )

        print("Patrón creado correctamente")
        print(
            "Total de casillas:",
            self.patron.total_casillas()
        )

        print(
            "Colores utilizados:",
            self.patron.colores_utilizados()
        )

        # Mostrar el patrón en la tabla
        self.mostrar_patron()

        # Actualizar el estado
        self.etiqueta_estado.setText(
            "Imagen procesada correctamente."
        )

    def mostrar_patron(self):
        """
        Muestra las casillas del patrón en la tabla.
        """

        # Obtener dimensiones del patrón
        filas = 50
        columnas = 50

        # Configurar cantidad de filas y columnas
        self.tabla_patron.setRowCount(filas)
        self.tabla_patron.setColumnCount(columnas)

        # Recorrer todas las casillas
        for y in range(filas):
            for x in range(columnas):

                # Obtener el índice del color
                indice = self.patron.obtener_casilla(
                    x,
                    y
                )

                # Obtener el color RGB
                rgb = self.patron.obtener_color_rgb(
                    indice
                )

                # Crear la celda
                celda = QTableWidgetItem()

                # Aplicar el color RGB
                celda.setBackground(
                    QColor(
                        rgb[0],
                        rgb[1],
                        rgb[2]
                    )
                )

                # Colocar la celda en la tabla
                self.tabla_patron.setItem(
                    y,
                    x,
                    celda
                )

        # Ajustar tamaño de las columnas
        for x in range(columnas):
            self.tabla_patron.setColumnWidth(
                x,
                18
            )

        # Ajustar tamaño de las filas
        for y in range(filas):
            self.tabla_patron.setRowHeight(
                y,
                18
            )


# Punto de entrada de la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = VentanaPrincipal()
    ventana.show()

    sys.exit(app.exec())