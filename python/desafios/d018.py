## Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

import math

a = int(input('Digite o valor de um ângulo: '))
print('Seno: {:.2f} \nCosseno: {:.2f} \nTangente: {:.2f}'.format(math.sin(math.radians(a)), math.cos(math.radians(a)),
                                                     math.tan(math.radians(a))))