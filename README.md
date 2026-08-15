1. Validar la version de python antes de iniciar el proceso python --version
2. instalar el Pyside6 con -m pip install PySide6 (esto de sebe instalar en el equipo ya que en proceso en linea no funcionaria)
3. validar que se reconoce el archivo image_processor python -c "from core.image_processor import cargar_imagen; print('image_processor funciona correctamente')"
4. Validar la instalacion de Pillow python -c "from PIL import image; print('Pillow esta instalado correctamente')
5. en caso de no tener el pillow instalado proceder a descargarlo con python -m pip install pillow
6. Validar que toma la imagen corretamente con python -c "from core.image_processor import cargar_imagen; imagen=cargar_imagen('assets/test/images.jpg'); print('Imagen cargada:', imagen.size)"
7. validaciones:
- python -c "from core.image_processor import cargar_imagen, redimensionar_imagen, reducir_colores; imagen=cargar_imagen('assets/test/images.jpg'); nueva=redimensionar_imagen(imagen, 50, 50); imegn=reducir_colores(imagen, 20);  print('Colores reducidos correctamente'); print('Modo:', imagen.mode)"
- python -c "from core.image_processor import cargar_imagen, redimensionar_imagen; imagen=cargar_imagen('assets/test/images.jpg'); nueva=redimensionar_imagen(imagen, 50, 50); print('nuevo tamaño:', nueva.size)"
- python -c "from core.image_processor import cargar_imagen, redimensionar_imagen; imagen=cargar_imagen('assets/test/images.jpg'); nueva=redimensionar_imagen(imagen, 50, 50); print('nuevo tamaño:' nueva.size)"
- python -c "from core.image_processor import cargar_imagen, obtener_dimensiones; imagen=cargar_imagen('assets/test/images.jpg'); print('Dimensiones:', obtener_dimensiones(imagen))"
- python -c "from core.image_processor import cargar_imagen, redimensionar_imagen, reducir_colores, obtener_colores; imagen=cargar_imagen('assets/test/images.jpg'); nueva=redimensionar_imagen(imagen, 50, 50); imagen=reducir_colores(imagen, 20); colores=obtener_colores(imagen);  print('Cantidad de colores encontrados:', len(colores)); print('Colores:', colores)"
- 