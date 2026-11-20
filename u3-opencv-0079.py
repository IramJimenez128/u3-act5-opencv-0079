import cv2
import os
print("+-+-+-+ 2. Lectura de imagenes +-+-+-+")
# Leer la imagen del archivo
image = cv2.imread( 'torrepisa.jpg' ) 
# Mostrar la imagen en una ventana
cv2.imshow( 'Imagen original Iram Jimenez 0079' , image) 
# Esperar a que se presione una tecla y cerrar la ventana
cv2.waitKey(0) 
print("+-+-+-+ 3. Conversión entre espacios de color +-+-+-+")
# Cargar la imagen
image = cv2.imread( 'torrepisa.jpg' ) 
# Convertir a escala de grises
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
# Guardar la imagen en escala de grises
cv2.imshow( 'Escala de grises Iram Jimenez 0079' , gray_image) 
cv2.waitKey(0) 
# Cargar la imagen
image = cv2.imread( 'torrepisa.jpg' ) 
# Redimensionar la imagen a 300x200
resized_image = cv2.resize(image, (300, 200)) 
# Guardar la imagen redimensionada
cv2.imshow( 'Imagen mas grande Iram Jimenez 0079' , resized_image) 
cv2.waitKey(0) 

# Cargar la imagen
image = cv2.imread('torrepisa.jpg') 
# Obtener la altura y el ancho de la imagen
(h, w) = image.shape[:2] 
# Definir el centro de la imagen
center = (w // 2, h // 2) 
#
matrix = cv2.getRotationMatrix2D(center, 90, 1.0) 
# Realizar la rotación
rotated_image = cv2.warpAffine(image, matrix, (w, h)) 
# Guardar la imagen rotada
cv2.imshow( 'Imagen rotada Iram Jimenez 0079' , rotated_image) 
cv2.waitKey(0) 

# Cargar la imagen
image = cv2.imread( 'torrepisa.jpg' ) 
# Aplicar desenfoque gaussiano
blured_image = cv2.GaussianBlur(image, (15, 15), 0) 
# Guardar la imagen desenfocada
cv2.imshow( 'Imagen difuminada Iram Jimenez 0079' , blured_image) 
cv2.waitKey(0) 

# Cargar la imagen
image = cv2.imread( 'torrepisa.jpg' ) 
# Convertir a escala de grises
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
# Aplicar el detector de bordes Canny
edges = cv2.Canny(gray_image, 100 , 200 ) 
# Guardar la imagen de bordes
cv2.imshow( 'Bordes Iram Jimenez 0079' , edges) 
cv2.waitKey(0) 

# Cargar la imagen
image = cv2.imread( 'torrepisa.jpg' ) 
# Dibujar un rectángulo
cv2.rectangle(image, ( 50 , 50 ), ( 200 , 200 ), ( 255 , 0 , 0 ), 3 ) 
# Agregar texto a la imagen
cv2.putText(image, 'Iram Jimenez 0079' , ( 60 , 40 ), cv2.FONT_HERSHEY_SIMPLEX, 1 , ( 0 , 255 , 0 ), 2 ) 
# Guardar la imagen de salida
cv2.imshow( 'Cuadro y texto Iram Jimenez 0079' , image) 
cv2.waitKey(0) 

# Obtener la ruta exacta donde está este archivo .py
carpeta_actual = os.path.dirname(os.path.abspath(__file__))
ruta_imagen = os.path.join(carpeta_actual, 'torrepisa.jpg')

# Cargar la imagen usando la ruta completa
image = cv2.imread(ruta_imagen, 0)

# Verificar si realmente cargó
if image is None:
  print(f'ERROR: No se encontró la imagen en: {ruta_imagen}')
  print('Revisa que el nombre y la extensión (.jpg, .png, .jpeg) sean exactos.')
else:
  # Aplicar umbralización
  _, thresh_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

  # Guardar en la misma carpeta
  ruta_salida = os.path.join(carpeta_actual, 'threshold_image.jpg')
  cv2.imwrite(ruta_salida, thresh_image)

  # Mostrar la imagen
  cv2.imshow('Umbralizacion Iram Jimenez 0079', thresh_image)
  cv2.waitKey(0)

# Obtener ruta segura de la carpeta del script
carpeta_actual = os.path.dirname(os.path.abspath(__file__))
ruta_imagen = os.path.join(carpeta_actual, 'torrepisa.jpg')
# Cargar la imagen
image = cv2.imread(ruta_imagen)
# Convertir la imagen a escala de grises
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Encontrar bordes
edges = cv2.Canny(gray_image, 100, 200)
# Encontrar contornos (AQUÍ ESTABA EL DETALLE: agregar ", _")
contours, _ = cv2.findContours(
    edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)
# Dibujar contornos en la imagen original
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
# Guardar y mostrar la imagen de salida con contornos
ruta_salida = os.path.join(carpeta_actual, 'contornos_torrepisa.jpg')
cv2.imwrite(ruta_salida, image)
cv2.imshow('Contornos Iram Jimenez 0079', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

