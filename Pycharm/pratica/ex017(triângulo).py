'''Faça um programa que leia o comprimento do cateto oposto e do cateeto
adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa'''
from math import sqrt
cato = float(input('Qual o valor do cateto oposto:'))
cata = float(input('Qual valor do cateto adjacente:'))
hipotenusa =  sqrt((cato**2 + cata**2))
print(hipotenusa)