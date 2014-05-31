import urllib2

def leArquivo():
	url = "https://files.nyu.edu/jeb21/public/jeb/orlib/files/pmed1.txt"
	dados = []
	matriz = []

	for line in urllib2.urlopen(url):
		dados.append(line.strip().strip('\n').split(' '))

	return dados

def criaMatriz():

	dados = leArquivo()
	cabecalho = dados.pop(0)
	tamanhoDaMatriz = int(cabecalho[0])
	numeroDeCentros = int(cabecalho[2])

	valorMaximo = 0

	matriz = []
	for i in range(tamanhoDaMatriz):
		matriz.append([])
		for j in range(tamanhoDaMatriz):
			matriz[i].append(None)

	for line in dados:

		x = int(line[0]) - 1
		y = int(line[1]) - 1
		valor = int(line[2])

		matriz[x][y] = valor
		matriz[y][x] = valor

		if valor > valorMaximo:
			valorMaximo = valor

	valorMaximo *= 10

	return matriz, numeroDeCentros, valorMaximo