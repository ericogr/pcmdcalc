#!/usr/bin/env python3

from math import sqrt as sq
from math import log2 as l2

def main():
	print("""
		Calculadora com pilha
			Digite o valor e ENTER para adicionar na pilha
			Utilize +, -, * e / para as 4 operações matemáticas básicas
			Utilize sq, l2 para raiz quadrada e log2
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
		return comando == 'exit' or comando == 'quit' or comando == 'q'

	def iscomandolimpar(comando):
		comando = comando.strip().lower()
		return comando == 'cls' or comando == 'clear'

	def isnumber(number):
		numero = number.replace('.', '', 1)

		if (number.startswith('-')):
			return numero.replace('-', '', 1).isdigit()

		return numero.isdigit()

	#############
	# operacoes #
	#############
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

	#############
	# main loop #
	#############

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
			if not leitura:
				continue
			elif iscomandosair(leitura):
				break
			elif iscomandolimpar(leitura):
				pilha.clear()
			elif isnumber(leitura):
				valor = float(leitura)
				pilha.append(valor)
			else:
				print('valor invalido: \'{0}\''.format(leitura))

		imprimepilha(pilha)

if __name__  == '__main__':
	main()