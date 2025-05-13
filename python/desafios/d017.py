## Faça um programa que leia o comprimento dos catetos de um triângulo retângulo, calcule e mostre o valor da
# hipotenusa.

from math import pow, sqrt, hypot

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
print('O valor da hipotenusa é {}'.format(sqrt(pow(co, 2) + pow(ca, 2))))
print('O valor da hipotenusa é {}'.format((co ** 2 + ca ** 2) ** (1 / 2)))
print('O valor da hipotenusa é {}'.format(hypot(co, ca)))
