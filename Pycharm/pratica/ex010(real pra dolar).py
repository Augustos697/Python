"""Crie um programa que leia quanto dinheiro uma pessoa tem carteira e mostre quantos dólares ela pode comprar"""
real = float(input('Quanto dinheiro você tem ?'))
dolar = 5
if real/dolar == 1:
    print('Com {} você pode ter {} dolar'.format(real, real / dolar))
else:
    print('Com {} você pode ter {} dolares'.format(real, real/dolar))