"""Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome santo"""
cidade = input('Qual cidade você mora?')
if cidade.upper().split()[0] == "SANTO":
    print('Sua cidade começa com santo')
elif cidade.upper().split()[0] == "SANTOS":
    print('Sua cidade começa com o plural de santo')
else:
    print('Sua cidade não começa com santos')