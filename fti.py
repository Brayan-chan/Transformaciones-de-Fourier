import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft2, fftshift
from skimage import data

# Cargar una imagen de ejemplo
image = data.camera()

# Aplicar la Transformada de Fourier
fft_image = fft2(image)
fft_image_shifted = fftshift(fft_image)  # Centrar el cero de frecuencia

# Mostrar la imagen original y su espectro de Fourier
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Imagen Original')

plt.subplot(1, 2, 2)
plt.imshow(np.log(np.abs(fft_image_shifted)), cmap='gray')
plt.title('Transformada de Fourier')

plt.show()
