import numpy as np
import matplotlib.pyplot as plt

dados = [154, 120, 132, 150, 231, 150, 105, 230, 240, 80, 48, 190,
         99, 205, 198, 210, 110, 100, 312, 250, 105, 150, 153, 60, 180]

# Número de observações
n = len(dados)

# a) Número de classes e amplitude
k = 6
amplitude = (max(dados) - min(dados)) / k
print(amplitude)
print(f'Número de classes: {k}')
print(f'Amplitude de cada classe: {amplitude:.2f}')

# b) Média, variância e desvio-padrão
media = np.mean(dados)
variancia = np.var(dados, ddof=0)
desvio_padrao = np.std(dados, ddof=0)

print(f'Média: {media:.2f}')
print(f'Variância: {variancia:.2f}')
print(f'Desvio-padrão: {desvio_padrao:.2f}')

# c) Histograma
plt.hist(dados, bins=k, edgecolor='black')
plt.xlabel('Consumo de Energia (kWh)')
plt.ylabel('Frequência')
plt.title('Histograma do Consumo de Energia')
plt.grid(True)
plt.show()
