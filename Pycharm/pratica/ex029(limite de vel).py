"""Escreva um programa aque leia a velocidade de um carro
se ele ultrapassar 80KM/h, mostre uma mensagem dizendo que ele foi multado.
a multa vai custar R$8,00 por cada Km acima do limite"""

velc = int(input('Quantos Km estava o carro?'))
ult = 80
if velc > ult:
    print(f'Você passou do limite de velocidade vai pagar uma multa de R${8*(velc-ult)}')
else:
    print(f'Continue dirigindo com segurança')