intervalos = [(10, 22), (22, 34), (34, 46), (46, 58), (58, 70), (70, 82), (82, 94), (94, 106), (106, 118), (118, 130)]
fi = [2, 8, 12, 16, 22, 21, 15, 7, 5, 1]

pontos_medios = [(intervalo[0] + intervalo[1]) / 2 for intervalo in intervalos]
media = sum([ponto_medio * f for ponto_medio, f in zip(pontos_medios, fi)]) / sum(fi)

n = sum(fi)
posicao_mediana = n / 2
f_acumulada_anterior = 22
classe_mediana = intervalos[3]
f_classe_mediana = fi[3]
limite_inferior = intervalos[3][0]
amplitude = classe_mediana[1] - classe_mediana[0]
aaa= (((posicao_mediana - 22) * amplitude) ) / f_classe_mediana
mediana = limite_inferior + aaa
print(limite_inferior, posicao_mediana, 22, f_classe_mediana, amplitude, aaa)


indice_moda = fi.index(max(fi))
moda = intervalos[indice_moda]


print("a) Média:", media)
print("b) Mediana:", mediana,)
print("c) Moda:", moda)
