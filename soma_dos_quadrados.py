import numpy as np

dados = [33.21, 42.13, 38.27, 41.81, 26.73, 38.69, 39.85, 40.02, 27.71, 36.54, 46.54, 
         44.68, 37.83, 40.50, 26.01, 47.01, 31.56, 42.77, 41.84, 12.83, 41.30, 39.70, 
         20.87, 42.23, 27.81, 31.85, 34.47, 30.59]

media = np.mean(dados)

soma_dos_quadrados = sum((x - media) ** 2 for x in dados)
variancia_manual = soma_dos_quadrados / len(dados)

variancia_np = np.var(dados, ddof=0)
print(soma_dos_quadrados)
