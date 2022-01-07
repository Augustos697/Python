"""Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento"""
salario = float(input('Qual o seu salário atual ?'))
aumento = salario*(15/100)
print('Você vai ter um aumento de 15%, ganhará R${}'.format(salario+aumento))