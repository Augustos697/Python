'''Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira'''
import math
val = float(input('Escreva um número:'))
print('A porção inteira de {} é {}'.format(val,math.trunc(val)))