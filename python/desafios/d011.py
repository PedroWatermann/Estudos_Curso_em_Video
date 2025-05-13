## Faça um programa que leia a altura e a largura de uma parede em metros, calcule sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m^2.

h = float(input('Digite a altura da parede, em metros (m): '))
l = float(input('Digite a largura da parede, em metros (m): '))
a = h * l
q = a / 2
print('Serão necessários {} litros de tinta.'.format(q))