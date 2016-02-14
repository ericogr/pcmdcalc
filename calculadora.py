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

def power(a, b):
	return a ** b

def imprimepilha(pilha):
	for i, p in enumerate(pilha):
		print('{0}: {1}'.format(i, p))

def iscomandosair(comando):
	comando = comando.strip().lower()
	return comando == 'exit' or comando == 'sair' or comando == 's'

def isnumber(number):
	return number.replace('.', '', 1).isdigit()

operacoes = {
	'+': adicao,
	'-': subtracao,
	'*': multiplicacao,
	'/': divisao,
	'p': power
}

while True:
	leitura = input('>>>')

	operacao = operacoes.get(leitura)

	if operacao:
		if len(pilha) > 1:
			valor = operacao(pilha.pop(), pilha.pop())
			pilha.append(valor)
		else:
			print('pilha sem elementos para operacao')
	else:
		if iscomandosair(leitura):
			break

		if isnumber(leitura):
			valor = float(leitura)
			pilha.append(valor)
		else:
			print('valor invalido: \'{0}\''.format(leitura))

	imprimepilha(pilha)