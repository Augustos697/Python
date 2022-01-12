"""escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão
1 para binário
2 para octal
3 para hexadecimal"""


num = int(input('Escreva um número:'))
escolha = int(input('''converter em: 
 [1]-Binário
 [2]-octal
 [3]-hexadecimal
 '''))
if escolha == 1:
    print(f'{num} = {bin(num)}')
elif escolha == 2:
    print(f'{num} = {oct(num)} ')
elif escolha == 3:
    print(f'{num} = {hex(num)}')