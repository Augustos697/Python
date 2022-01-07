"""Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor"""
val = int(input('Escolha um número:'))
print('O número {} tem como antecessor {} e sucessor {}'.format(val,val-1,val+1))