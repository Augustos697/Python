"""Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto"""
preco = float(input('Quanto custa o produto:'))
desconto = preco*(5/100)
print('O produto que valia R${} com o desconto de 5% é R${} '.format(preco, preco-desconto))