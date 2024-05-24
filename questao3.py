import numpy as np
import pandas as pd
from scipy import stats

x_i = np.array([-4, -3, -2, -1, 0, 1, 2, 3, 4])
f_i = np.array([60, 120, 180, 200, 240, 190, 160, 90, 30])

somatorio_fi = sum(f_i)
print(f"Somatório de: {somatorio_fi:.2f}")

# a) Cálculo das medidas

# Média
media = np.average(x_i, weights=f_i)

# Variância
variancia = np.average((x_i - media) ** 2, weights=f_i)

# Desvio padrão
desvio_padrao = np.sqrt(variancia)

# Mediana
data = []
for value, freq in zip(x_i, f_i):
    data.extend([value] * freq)
data = np.array(data)
mediana = np.median(data)


# b) Justificativa para a melhor medida de tendência central


print(f"Média: {media:.2f}")
print(f"Variância: {variancia:.2f}")
print(f"Desvio Padrão: {desvio_padrao:.2f}")
print(f"Mediana: {mediana:.2f}")

