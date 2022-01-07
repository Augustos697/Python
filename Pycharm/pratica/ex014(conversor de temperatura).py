'''Escreva um programa  que converta uma temperatura digitada em °C E CONVERTA PARA °F'''
cel = float(input('Qual a temperaturas em celsius:'))
fah = (cel*1.8)+32
print('{} °C é igual a {}°F'.format(cel,fah))