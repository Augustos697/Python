"""Faça um progrma que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²"""
alt = int(input('Qual a altura ? '))
lar = int(input('Qual a largura ?'))
area = alt*lar
tinta = area/2
print('uma parede com {}m² vai precisar  de {}L tinta'.format(area, tinta))