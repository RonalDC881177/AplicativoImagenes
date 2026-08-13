def cargar_imagen(ruta):
    """
    Carga una imagen desde la ruta.
    """
    from PIL import Image
    
    image = Image.open(ruta)
    return image


    