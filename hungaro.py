def transpoeMatriz(matriz):
	return [list(i) for i in zip(*matriz)]

def find(linha):
	posicao = [i for i, x in enumerate(linha) if x == 0]
	return posicao

def etapa1(matriz):
	for linha in matriz:
		elementoMinimo = min(linha)
		for elemento in linha:
			x = matriz.index(linha)
			y = linha.index(elemento)
			matriz[x][y] = elemento - elementoMinimo
	return matriz



def etapa2(matriz):
	matrizTransposta = transpoeMatriz(matriz)
	matriz = transpoeMatriz( etapa1(matrizTransposta) )
	return matriz

def etapa3(matriz, matrizDeCustos):
	custoTotal = 0
	for linha in matriz:
		x = matriz.index(linha)
		posicoes = find(linha)
		if len(posicoes) == 1:
			y = posicoes[0] 
			print x, matrizDeCustos[x][y]
			custoTotal += matrizDeCustos[x][y]
		else:
			for y in posicoes:
				matrizT = transpoeMatriz(matriz)
				if matrizT[y].count(0) == 1:
					print x, matrizDeCustos[x][y]
					custoTotal += matrizDeCustos[x][y]
					continue
	print "Custo total: ", custoTotal




matrizDeCustos = [[15, 10, 9], [9, 15, 10], [10, 12, 8]]
matriz = [[15, 10, 9], [9, 15, 10], [10, 12, 8]]

matriz = etapa1(matriz)
print matriz
matriz = etapa2(matriz)
print matriz
etapa3(matriz, matrizDeCustos)
