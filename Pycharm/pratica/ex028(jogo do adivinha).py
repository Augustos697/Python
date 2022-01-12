"""Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador

o Programa deverá escrever na tela se o usuario acertou ou errou"""

import random


pc = random.randint(1,10)
humano = 0
while pc != humano:
    humano = int(input("Escolha um número de 1 a 10:"))
    if humano == pc:
        print('\033[0:32mVocê acertou\033[m')
    else:
        erros = 0
        erros += humano
        print(f'Você errou: \033[0:31m{ erros}\033[m ')


