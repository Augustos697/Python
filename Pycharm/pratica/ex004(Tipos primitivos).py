"""Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele """
algo = input('Digite alguma coisa:')
print("É um número ou alfabetico ?",algo.isalnum())
print("É alfabético",algo.isalpha())
print("esta em letras minúsculas?",algo.islower())
print("É decimal?",algo.isdecimal())
print("Está em letras maiúsculas?", algo.isupper())