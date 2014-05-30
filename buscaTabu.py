from random import randrange

def pegaCusto(matriz, centros):
	custo = 0
	for i in range(len(matriz)):
		menor = valorMaximo
		for c in centros:
			if i == c:
				menor = 0
				continue
			if matriz[c][i] != None and i != c and i not in centros:
				if matriz[c][i] < menor:
					menor = matriz[c][i]
		custo += menor
	return custo


def geraCentrosVizinhos(centrosAtuais, tamanhoDaMatriz):
	centrosNovos = []
	combinacaoNova = []
	for i in range(len(centrosAtuais)):
		if (centrosAtuais[i] - 1) >= 0:
			for j in range(len(centrosAtuais)):
				if i != j:
					combinacaoNova.append(centrosAtuais[j])
				else:
					combinacaoNova.append(centrosAtuais[i] - 1)

		if combinacaoNova:
			centrosNovos.append(combinacaoNova)
		combinacaoNova = []

		if (centrosAtuais[i] + 1) < tamanhoDaMatriz:
			for j in range(len(centrosAtuais)):
				if i != j:
					combinacaoNova.append(centrosAtuais[j])
				else:
					combinacaoNova.append(centrosAtuais[i] + 1)

		if combinacaoNova:
			centrosNovos.append(combinacaoNova)
		combinacaoNova = []
	return centrosNovos


def satisfazAspiracao(custoAtual, custo):
	if custo < custoAtual:
		return True
	else:
		return False


def geraCentrosIniciais(tamanhoDaMatriz, numeroDeCentros):
	centrosIniciais = []
	while len(centrosIniciais) < numeroDeCentros:
		novoCentro = randrange(0, tamanhoDaMatriz)
		if novoCentro not in centrosIniciais:
			centrosIniciais.append(novoCentro)
	return centrosIniciais


matriz = [[None, 3, None, 4, None, None, None, None, None, None, None, None, None, None, None],
		  [3, None, 5, None, None, None, 3, None, None, None, None, None, None, None, None],
		  [None, 5, None, 2, None, 8, 1, None, None, None, None, None, None, None, None],
		  [4, None, 2, None, 4, 8, None, None, None, None, None, None, None, None, None],
		  [None, None, None, 4, None, 2, None, None, None, 10, None, None, None, None, None],
		  [None, None, 8, 8, 2, None, 5, None, 1, None, None, None, None, None, None],
		  [None, 3, 1, None, None, 5, None, 5, None, None, None, 7, None, None, None],
		  [None, None, None, None, None, None, 5, None, 11, None, 7, 6, None, None, None],
		  [None, None, None, None, None, 1, None, 11, None, 8, None, None, None, None, None],
		  [None, None, None, None, 10, None, None, None, 8, None, 6, None, None, 10, None],
		  [None, None, None, None, None, None, None, 7, None, 6, None, None, 1, 15, None],
		  [None, None, None, None, None, None, 7, 6, None, None, None, None, 3, None, None],
		  [None, None, None, None, None, None, None, None, None, None, 1, 3, None, None, 14],
		  [None, None, None, None, None, None, None, None, None, 10, 15, None, None, None, 4],
		  [None, None, None, None, None, None, None, None, None, None, None, None, 14, 4, None]]

tamanhoDaMatriz = len(matriz)
valorMaximo = 100
numeroDeCentros = 3

centros = geraCentrosIniciais(tamanhoDaMatriz, numeroDeCentros)

listaTabu = []
maximoIteracoesTabu = 5
iteracoesTabu = 0

custo = 0
custoAtual = pegaCusto(matriz, centros)
melhorCustoAtual = len(matriz) * valorMaximo
melhorSolucaoAtual = centros


for x in range(1000):

	# Pega a lista de centros vizinhos
	centrosVizinhos = geraCentrosVizinhos(centros, tamanhoDaMatriz)
	print centrosVizinhos

	# Atualiza iteracoes tabu - # de iteracoes para um centro sair da lista tabu
	if listaTabu:
		iteracoesTabu += 1
		if iteracoesTabu == maximoIteracoesTabu:
			listaTabu.pop(0)
			iteracoesTabu = 0
	else:
		iteracoesTabu = 0
	print "Iteracoes tabu: ", iteracoesTabu


	# Enquanto ainda tiver opcoes na lista de vizinhos, buscar o melhor vizinho
	while centrosVizinhos:
		custo = 0
		centros = centrosVizinhos.pop(0)
		print centros

		for i in range(len(matriz)):
			menor = valorMaximo
			for c in centros:
				if i == c:
					menor = 0
					continue
				if matriz[c][i] != None and i != c and i not in centros:
					if matriz[c][i] < menor:
						menor = matriz[c][i]
			custo += menor

		print "Custo da iteracao: ", custo

		if custo <= melhorCustoAtual:
			print "Nova melhor solucao at ", centros
			melhorCustoAtual = custo
			custoAtual = custo
			melhorSolucaoAtual = centros
			centrosVizinhos = []
			listaTabu.append(centros)

		else:
			if centros not in listaTabu or satisfazAspiracao(custoAtual, custo):
				centrosVizinhos = []
				custoAtual = custo
				listaTabu.append(centros)



		print "Iteracao #", x + 1, " - melhor custo atual: ", melhorCustoAtual

print melhorCustoAtual, melhorSolucaoAtual