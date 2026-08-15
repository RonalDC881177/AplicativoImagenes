class Pattern:
    """
    Representa un patrón generado a partir de una imagen.
    """

    def __init__(self, ancho, alto, matriz_colores):
        """
        Inicializa un patrón.
        """
        self.ancho = ancho
        self.alto = alto
        self.matriz_colores = matriz_colores

    def obtener_color(self, x, y):
        """
        Obtiene el índice de color de una casilla del patrón.
        """
        return self.matriz_colores[y][x]

    @classmethod
    def desde_imagen(cls, ruta, ancho, alto, cantidad_colores):
        """
        Crea un patrón a partir de una imagen.
        """
        from core.image_processor import procesar_imagen

        matriz = procesar_imagen(
            ruta,
            ancho,
            alto,
            cantidad_colores
        )

        return cls(ancho, alto, matriz)

    def total_casillas(self):
        """
        Devuelve la cantidad total de casillas del patrón.
        """
        return self.ancho * self.alto

    def contar_colores(self):
        """
        Cuenta cuántas casillas utiliza cada color.
        """
        conteo = {}

        for fila in self.matriz_colores:
            for indice in fila:
                if indice in conteo:
                    conteo[indice] += 1
                else:
                    conteo[indice] = 1

        return conteo