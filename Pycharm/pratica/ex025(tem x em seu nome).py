"""Crie um program que leioa o nome de uma pessoa e diga se ela tem silva no nome"""
nome = input('Qual seu nome?')
if "SILVA" in nome.upper():
    print('Seu nome tem Silva')
else:
    print('Seu nome não tem Silva')