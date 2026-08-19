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
        Devuelve cuantas casillas utilizan un color especifico
        """
        conteo = self.contar_colores()
        return conteo.get(indice, 0)
    
    def colores_utilizados(self):
        """
        Devuelve los indices de los colores utilizados en el patron.
        """
        conteo = self.contar_colores()
        return list(conteo.keys())
    
    def obtener_color_rgb(self, indice):
        """
        Devuelve el color RGB correspondiente a un indice.
        """
        return self.paleta_rgb[indice]
    
    def informacion_colores(self):
        """
        Devuelve informacion basica de los colores utilizados.
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
        Devuelve la informacion de una casilla del patron.
        """
        
        indice = self.obtener_color(x, y)
        rgb = self.obtener_color_rgb(indice)
        
        return{
            "x": x,
            "y": y,
            "indice": indice,
            "rgb": rgb
        }
        