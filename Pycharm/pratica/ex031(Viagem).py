"""Desenvolva um programa que pergunte a distancia de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por KM para viagens de até 200Km e R$0,45 para viagens mais longas"""


via = int(input('Sua viagem é de quantos Km ?'))

if via <= 200:
    print(f'Você vai pagar R${via*0.50} pela viagem inteira, boa viagem')
elif via > 200:
    print(f'Você vai pagar R${via*0.45} pela viagem inteira, boa viagem')
