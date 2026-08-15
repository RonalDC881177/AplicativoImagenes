def cargar_imagen(ruta):
    """
    Carga una imagen desde la ruta.
    """
    from PIL import Image
    
    image = Image.open(ruta)
    return image

def obtener_dimensiones(imagen):
    """
    Obtener el ancho y alto de la imagen
    """
    return imagen.size

def redimensionar_imagen(imagen, ancho, alto):
    """
    Redimensiona una imagen al tamaño indicado.
    """
    if ancho <= 0 or alto <= 0:
        raise ValueError("El ancho y el alto deben ser mayores que cero")

    return imagen.resize((ancho, alto))

def reducir_colores(imagen, cantidad_colores):
    """
    Reducir la cantidad de colores de la imagen.
    """
    return imagen.quantize(colors=cantidad_colores)

def obtener_colores(imagen):
    """
    Obtener los colores utilizados en la imagen
    """
    colores = imagen.getcolors(imagen.width * imagen.height)
    return colores

def obtener_color_pixel(imagen, x, y):
    """
    Obtiene el color de un pixel en una posicion determinada
    """
    return imagen.getpixel((x, y))

def obtener_color_rgb(imagen, x, y):
    """
    Obtiene el color RGB de un pixel
    """
    pixel = imagen.getpixel((x, y))
    return imagen.getpalette()[
    pixel * 3: pixel * 3+3
    ]

def obtener_paleta_rgb(imagen):
    """
    obtiene todos los colores rgb de la paleta de la imagen
    """
    paleta = imagen.getpalette()
    colores = []

    for i in range(0, 20*3, 3):
        color = paleta[i:i + 3]
        colores.append(color)
    return colores

def obtener_indice_color(imagen, x, y):
    """
    Obtiene el indice de color dentro de una imagen
    """
    return imagen.getpixel((x, y))

def crear_matriz_colores(imagen):
    """
    Crea una matriz con el indice de color de cada pixel
    """
    matriz = []

    for y in range(imagen.height):
        fila = []

        for x in range(imagen.width):
            indice = obtener_indice_color(imagen, x, y)
            fila.append(indice)

        matriz.append(fila)

    return matriz

def convertir_matriz_a_rgb(imagen, matriz):
    """
    Convierte los índices de color de la matriz a valores RGB.
    """
    paleta = imagen.getpalette()
    matriz_rgb = []

    for fila in matriz:
        fila_rgb = []

        for indice in fila:
            posicion = indice * 3
            color = paleta[posicion: posicion + 3]
            fila_rgb.append(color)

        matriz_rgb.append(fila_rgb)

    return matriz_rgb

def contar_colores(matriz):
    """
    Cuenta cuántas veces aparece cada índice de color.
    """
    conteo = {}

    for fila in matriz:
        for indice in fila:
            if indice in conteo:
                conteo[indice] += 1
            else:
                conteo[indice] = 1

    return conteo

def contar_total_casillas(conteo):
    """
    Calcula el total de casillas del patrón.
    """
    return sum(conteo.values())

def obtener_rgb_por_indice(imagen, indice):
    """
    Obtiene el color RGB correspondiente a un índice de la paleta.
    """
    paleta = imagen.getpalette()
    posicion = indice * 3

    return paleta[posicion:posicion + 3]

def procesar_imagen(ruta, ancho, alto, cantidad_colores):
    """
    Procesa una imagen y genera la matriz de colores.
    """
    imagen = cargar_imagen(ruta)
    imagen = redimensionar_imagen(imagen, ancho, alto)
    imagen = reducir_colores(imagen, cantidad_colores)

    matriz = crear_matriz_colores(imagen)

    return matriz