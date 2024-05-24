import numpy as np

dados = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 10, 10, 10]

media = np.mean(dados)
a = sum(dados)

diferencas = [abs(x - media) for x in dados]


desvio_medio = np.mean(diferencas)

variancia = np.var(dados)

desvio_padrao = np.std(dados)

print(media)
print("Desvio médio:", desvio_medio)
print("Variância:", variancia)
print("Desvio-padrão:", desvio_padrao)
