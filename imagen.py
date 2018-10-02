import cv2

# Carga de imagen
image_path = 'av.jpg'
image = cv2.imread(image_path)

# Se guarda una copia
image_copy_path = 'copiaAV.jpg'
cv2.imwrite(image_copy_path, image)

# Se carga la copia y se convierte a escala gris
image_copy = cv2.imread(image_copy_path,0)

# Show
cv2.imshow('Original', image)
cv2.imshow('Gris', image_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()
