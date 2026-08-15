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
    Redimensionar una imagen al tamaño indicado
    """
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

    

    
    
    


    