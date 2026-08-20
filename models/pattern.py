class Pattern:
    """
    Representa un patrón generado a partir de una imagen.
    """

    def __init__(self, ancho, alto, matriz_colores, paleta_rgb=None):
        """
        Inicializa un patrón.
        """
        self.ancho = ancho
        self.alto = alto
        self.matriz_colores = matriz_colores
        self.paleta_rgb = paleta_rgb

    def obtener_color(self, x, y):
        """
        Obtiene el índice de color de una casilla del patrón.
        """
        if not self.posicion_valida(x, y):
            raise ValueError("La posicion esta fuera de los limites del patron")

        return self.matriz_colores[y][x]

    @classmethod
    def desde_imagen(cls, ruta, ancho, alto, cantidad_colores):
        """
        Crea un patrón a partir de una imagen.
        """
        from core.image_processor import (
            cargar_imagen,
            redimensionar_imagen,
            reducir_colores,
            crear_matriz_colores,
            obtener_paleta_rgb
        )

        imagen = cargar_imagen(ruta)
        imagen = redimensionar_imagen(imagen, ancho, alto)
        imagen = reducir_colores(imagen, cantidad_colores)

        matriz = crear_matriz_colores(imagen)
        paleta_rgb = obtener_paleta_rgb(imagen)

        return cls(ancho, alto, matriz, paleta_rgb)

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

    def cantidad_color(self, indice):
        """
        Devuelve cuántas casillas utilizan un color específico.
        """
        conteo = self.contar_colores()
        return conteo.get(indice, 0)

    def colores_utilizados(self):
        """
        Devuelve los índices de los colores utilizados en el patrón.
        """
        conteo = self.contar_colores()
        return list(conteo.keys())

    def obtener_color_rgb(self, indice):
        """
        Devuelve el color RGB correspondiente a un índice.
        """
        return self.paleta_rgb[indice]

    def informacion_colores(self):
        """
        Devuelve información básica de los colores utilizados.
        """
        colores = []

        for indice in self.colores_utilizados():
            colores.append({
                "indice": indice,
                "rgb": self.obtener_color_rgb(indice),
                "cantidad": self.cantidad_color(indice)
            })

        return colores

    def informacion_casilla(self, x, y):
        """
        Devuelve la información de una casilla del patrón.
        """
        indice = self.obtener_color(x, y)
        rgb = self.obtener_color_rgb(indice)

        return {
            "x": x,
            "y": y,
            "indice": indice,
            "rgb": rgb
        }

    def obtener_fila(self, y):
        """
        Devuelve una fila completa del patrón.
        """
        return self.matriz_colores[y]

    def obtener_columna(self, x):
        """
        Devuelve una columna completa del patrón.
        """
        columna = []

        for y in range(self.alto):
            columna.append(self.matriz_colores[y][x])

        return columna

    def posicion_valida(self, x, y):
        """
        Comprueba si una posición existe dentro del patrón.
        """
        return 0 <= x < self.ancho and 0 <= y < self.alto

    def obtener_casilla(self, x, y):
        """
        Obtiene el color de una casilla del patrón.
        """
        if not self.posicion_valida(x, y):
            return None

        return self.matriz_colores[y][x]

    def establecer_casilla(self, x, y, color_id):
        """
        Establece el color de una casilla del patrón.
        """
        if not self.posicion_valida(x, y):
            return False

        self.matriz_colores[y][x] = color_id
        return True

    def cantidad_por_color(self):
        """
        Devuelve la cantidad de casillas que utiliza cada color.
        """
        return self.contar_colores()
    

    