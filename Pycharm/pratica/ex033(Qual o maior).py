"""Faça um programa que leia três números e mostre qual é ao maior e qual é o menor"""
n1 = int(input('Escreva o 1° número:'))
n2 = int(input('Escreva o 2° número:'))
n3 = int(input('Escreva o 3° número:'))
if n1 > n2 and n1 > n3 and n2 < n3 :
    print(f'{n1} é o maior número ')
    print(f"{n2} é o menor número")
elif n2 > n1 and n2 >n3 and n1 < n3:
    print(f"{n2} é o maior número")
    print(f"{n1} é o menor número")
else:
    print(f"{n3} é maior número")
    print(f"{n1} é menor número")