import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats

dados = [33.21, 42.13, 38.27, 41.81, 26.73, 38.69, 39.85, 40.02, 27.71, 36.54, 46.54, 
         44.68, 37.83, 40.50, 26.01, 47.01, 31.56, 42.77, 41.84, 12.83, 41.30, 39.70, 
         20.87, 42.23, 27.81, 31.85, 34.47, 30.59]

# a) Distribuições de frequência
dados_serie = pd.Series(dados)
frequencia_absoluta = dados_serie.value_counts().sort_index()
frequencia_relativa = frequencia_absoluta / len(dados)
frequencia_acumulada = frequencia_absoluta.cumsum()
frequencia_relativa_acumulada = frequencia_relativa.cumsum()

tabela_frequencias = pd.DataFrame({
    'Frequência Absoluta': frequencia_absoluta,
    'Frequência Relativa': frequencia_relativa,
    'Frequência Acumulada': frequencia_acumulada,
    'Frequência Relativa Acumulada': frequencia_relativa_acumulada
})

# Imprimir as tabelas de frequências
print(tabela_frequencias)

# b) Histograma
plt.hist(dados, bins='auto', edgecolor='black')
plt.xlabel('Peso dos tubérculos (g)')
plt.ylabel('Frequência')
plt.title('Histograma da distribuição de pesos dos tubérculos')
plt.grid(True)

# c) Medidas de posição central e dispersão
media = np.mean(dados)
mediana = np.median(dados)
variancia = np.var(dados, ddof=0)
desvio_padrao = np.std(dados, ddof=0)

# d) Indicação das medidas no histograma
plt.axvline(media, color='r', linestyle='dashed', linewidth=1, label=f'Média: {media:.2f}')
plt.axvline(mediana, color='g', linestyle='dashed', linewidth=1, label=f'Mediana: {mediana:.2f}')
plt.legend()

plt.show()

print(f"Média: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Variância: {variancia:.2f}")
print(f"Desvio Padrão: {desvio_padrao:.2f}")
