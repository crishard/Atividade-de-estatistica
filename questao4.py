import numpy as np

intervalos = [(7, 18), (18, 31), (31, 42), (42, 54), (54, 66), (66, 78), (78, 90)]
frequencias = [6, 10, 13, 8, 5, 6, 2]

# a) Amplitude total
amplitude_total = intervalos[-1][1] - intervalos[0][0]

# b) Ponto médio do terceiro intervalo
terceiro_intervalo = intervalos[2]
ponto_medio_terceiro_intervalo = np.mean(terceiro_intervalo)

# c) Comprimento dos intervalos
comprimento_intervalo1 = intervalos[0][1] - intervalos[0][0]
comprimento_intervalo2 = intervalos[1][1] - intervalos[1][0]
comprimento_intervalo3 = intervalos[2][1] - intervalos[2][0]
comprimento_intervalo4 = intervalos[3][1] - intervalos[3][0]
comprimento_intervalo5 = intervalos[4][1] - intervalos[4][0]
comprimento_intervalo6 = intervalos[5][1] - intervalos[5][0]
comprimento_intervalo7 = intervalos[6][1] - intervalos[6][0]

# d) Porcentagem de internautas que gastam acima de 42 minutos
frequencias_acima_42 = sum(frequencias[3:])
total_frequencias = sum(frequencias)
porcentagem_acima_42 = (frequencias_acima_42 / total_frequencias) * 100

# e) Valor modal, mediano e médio

# Modal
moda_intervalo = intervalos[np.argmax(frequencias)]
moda = np.mean(moda_intervalo)

# Mediana
frequencias_acumuladas = np.cumsum(frequencias)
mediana_posicao = total_frequencias / 2
for i, freq_acum in enumerate(frequencias_acumuladas):
    if freq_acum >= mediana_posicao:
        intervalo_mediana = intervalos[i]
        break
mediana = np.mean(intervalo_mediana)

# Média
pontos_medios = [np.mean(intervalo) for intervalo in intervalos]
media = np.average(pontos_medios, weights=frequencias)

print(f"Amplitude total: {amplitude_total} minutos")
print(f"Ponto médio do terceiro intervalo: {ponto_medio_terceiro_intervalo} minutos")
print(f"Comprimento dos intervalos: {comprimento_intervalo1, comprimento_intervalo2, comprimento_intervalo3, comprimento_intervalo4, comprimento_intervalo5, comprimento_intervalo6, comprimento_intervalo7} minutos")
print(f"Porcentagem de internautas que gastam acima de 42 minutos: {porcentagem_acima_42:.2f}%")
print(f"Moda: {moda} minutos")
print(f"Mediana: {mediana} minutos")
print(f"Média: {media:.2f} minutos")
