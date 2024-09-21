import numpy as np
import matplotlib.pyplot as plt

# Definir la función que genera una serie de Fourier para una onda cuadrada
def square_wave_approx(t, n_terms):
    wave = np.zeros_like(t)
    for n in range(1, n_terms + 1, 2):  # Solo usamos términos impares
        wave += (4 / np.pi) * (1 / n) * np.sin(n * t)
    return wave

# Parámetros
t = np.linspace(0, 2 * np.pi, 1000)  # Tiempo
n_terms = [1, 3, 5, 11]  # Diferentes aproximaciones (más términos)

# Gráficas
plt.figure(figsize=(10, 8))
for i, n in enumerate(n_terms):
    plt.subplot(len(n_terms), 1, i + 1)
    plt.plot(t, square_wave_approx(t, n))
    plt.title(f'Aproximación de Onda Cuadrada con {n} términos')
    plt.ylim(-1.5, 1.5)
    plt.grid(True)

plt.tight_layout()
plt.show()
