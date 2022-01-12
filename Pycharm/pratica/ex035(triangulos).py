"""Desenvolva um programa que leia o comprimentos de três retas e diga se pode ou não formar um triângulo"""
ret1 = float(input('Escreva a primeira reta:'))
ret2 = float(input('Escreva a segunda reta:'))
ret3 = float(input('Escreva a terceira reta:'))
if ret1 + ret2 > ret3 and ret2 + ret3 > ret1 and ret3 + ret1 > ret2:
    print("Dá para forma um triângulo")
else:
    print("Não dá para formar um triângulo")