"""Faça um programa que leia um ano qualquer e mostre se ele é bissexto"""

anob = int(input('Escreva um ano: '))
if anob % 4 == 0 or anob % 100 !=0 or  anob % 400 == 0:
    print('é um ano bissexto')
else:
    print('Não é um ano bissexto')
