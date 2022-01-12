"""Faça um programa que leia uma frase pelo teclado e mostre
-Quantas vezes aparece  letra A
-Em que posição ela aparecce a primeira vez
- Em que posição ela aparece a ultima vez"""
frase = input('Escreva uma frase:')
print(f"{frase.upper().count('A')}")
print(f"{frase.upper().find('A') +1}")
espacos = frase.strip().count(" ")
if " " in frase:
    posicao = int(frase.upper().strip().rfind('A'))

    print(f"{posicao-espacos+1}")
else:
    print(f"{frase.upper().rfind('A')}")