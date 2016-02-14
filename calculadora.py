from math import sqrt as sq
from math import log2 as l2

print("""
	Calculadora com pilha
		Digite o valor e ENTER para adicionar na pilha
		Utilize +, -, * e / para as 4 operações matemáticas básicas
""")

leitura = ''
valor = 0
pilha = []

#############
# operações #
#############
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

def square(a):
	return sq(a)

def log2(a):
	return l2(a)

############
# diversos #
############
def imprimepilha(pilha):
	for i, p in enumerate(pilha):
		print('{0}: {1}'.format(i, p))

def iscomandosair(comando):
	comando = comando.strip().lower()
	return comando == 'exit' or comando == 'sair' or comando == 's'

def isnumber(number):
	return number.replace('.', '', 1).isdigit()

operacoes = {
	'+': {
		'operadores': 2,
		'funcao': adicao
	},
	'-': {
		'operadores': 2,
		'funcao': subtracao
	},
	'*': {
		'operadores': 2,
		'funcao': multiplicacao
	},
	'/': {
		'operadores': 2,
		'funcao': divisao
	},
	'pw': {
		'operadores': 2,
		'funcao': power
	},
	'sq': {
		'operadores': 1,
		'funcao': square
	},
	'l2': {
		'operadores': 1,
		'funcao': log2
	}
}

while True:
	leitura = input('>>>')

	operacao = operacoes.get(leitura)

	if operacao:
		operadores = operacao.get('operadores')

		if len(pilha) >= operadores:
			funcao = operacao.get('funcao')

			valor = funcao(*pilha[-operadores:])
			pilha = pilha[0:len(pilha) - operadores]
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