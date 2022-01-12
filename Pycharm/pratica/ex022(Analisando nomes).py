"""Crie um programa que leia o nome completo de uma pessoa e mostre
- O nome com todas as letras maiúsculas
-O nome com todas Minúculas
-Quantas letras ao todo(sem considerar espaços)
- Quantas letras tem o primeiro nome """
nome = input("Qual o seu nome ?")
print(f"Seu nome em letras maiúculas fica: {nome.upper()}")
print(f"Seu nome em letras minúsculas fica: {nome.lower()}")
print(f"Seu nome tem {len(nome)} letras")
print(f"Seu primeiro nome é {nome.split()[0]}")