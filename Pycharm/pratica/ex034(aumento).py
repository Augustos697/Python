"""Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
Para salários superiores  a R$ 1.250,00, calcule um aumento de 10%
Para os inferiores ou iguais, o aumento é de 15%"""
sal = int(input('Qual o seu salário ?'))
if sal > 1250:
    print(f'Você vai receber um aumento de 10%, seu salário vai ser de {sal+(sal*10/100)} ')
elif sal < 1250:
    print(f'Você vai receber um aumento de 15%, seu salário vai ser de {sal+(sal*15/100)} ')