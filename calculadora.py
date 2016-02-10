print("""
	Calculadora com pilha
		Digite o valor e ENTER para adicionar na pilha
		Utilize +, -, * e / para as 4 operações matemáticas básicas
""")

leitura = ''
valor = 0
pilha = []

def adicao(a, b):
	return a + b

def subtracao(a, b):
	return a - b

def multiplicacao(a, b):
	return a * b

def divisao(a, b):
	return a / b

def imprime_pilha(pilha):
	for i, p in enumerate(pilha):
		print('{0}: {1}'.format(i, p))

operacoes = {
	'+': adicao,
	'-': subtracao,
	'*': multiplicacao,
	'/': divisao
}

while True:
	leitura = input('>>>')

	if not leitura:
		break

	operacao = operacoes.get(leitura)

	if operacao:
		valor = operacao(pilha.pop(), pilha.pop())
		pilha.append(valor)
	else:
		valor = float(leitura)
		pilha.append(valor)

	imprime_pilha(pilha)