"""Faça um programa que leia um número inteiro qalquer e mostre na sua tela a tabuada"""
valor = int(input('Escolha um valor:'))
con = 0
while con != 11:
    print("{} x {} = {}".format(valor, con, valor*con))
    con += 1