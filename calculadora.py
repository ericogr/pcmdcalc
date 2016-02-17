#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from math import sqrt as sq
from math import log2 as l2
from operacoes import *

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
	operacoes = Operacoes()

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

	############################
	# meta dados das operacoes #
	############################
	meta_operacoes = {
		'+': {
			'operadores': 2,
			'funcao': operacoes.adicao
		},
		'-': {
			'operadores': 2,
			'funcao': operacoes.subtracao
		},
		'*': {
			'operadores': 2,
			'funcao': operacoes.multiplicacao
		},
		'/': {
			'operadores': 2,
			'funcao': operacoes.divisao
		},
		'pw': {
			'operadores': 2,
			'funcao': operacoes.power
		},
		'sq': {
			'operadores': 1,
			'funcao': operacoes.square
		},
		'l2': {
			'operadores': 1,
			'funcao': operacoes.log2
		}
	}

	#############
	# main loop #
	#############

	while True:
		leitura = input('>>>')

		operacao = meta_operacoes.get(leitura)

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