import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# Parámetros de la señal
sampling_rate = 1000  # Frecuencia de muestreo
T = 1.0 / sampling_rate  # Periodo de muestreo
L = 1000  # Número de muestras
t = np.linspace(0.0, L * T, L, endpoint=False)  # Vector de tiempo

# Generar una señal compuesta por varias ondas sinusoidales
f1, f2, f3 = 50, 120, 180  # Frecuencias de las ondas
signal = np.sin(2.0 * np.pi * f1 * t) + 0.5 * np.sin(2.0 * np.pi * f2 * t) + 0.2 * np.sin(2.0 * np.pi * f3 * t)

# Aplicar la Transformada de Fourier
yf = fft(signal)
xf = fftfreq(L, T)[:L//2]  # Frecuencias correspondientes

# Gráfica de la señal original
plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title("Señal compuesta (dominio del tiempo)")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")

# Gráfica de las frecuencias tras la transformada de Fourier
plt.subplot(2, 1, 2)
plt.plot(xf, 2.0/L * np.abs(yf[:L//2]))
plt.title("Transformada de Fourier (dominio de la frecuencia)")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Amplitud")

plt.tight_layout()
plt.show()
