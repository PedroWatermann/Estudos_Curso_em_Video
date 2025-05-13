## Crie um programa que leia o nome completo de uma pessoa e mostre:
# o nome com todas as letras maiúsculas
# o nome com todas as letras minúsculas
# quantas letras no total (sem considerar espaços)
# quantas letras tem no primeiro nome
from operator import length_hint

nc = input('\nDigite seu nome completo: ')

print('\nSeu nome em letras minúsculas: {}.'.format(nc.lower()))
print('Seu nome em letras maiúsculas: {}.'.format(nc.upper()))
print('Seu nome completo possui {} letras.'.format(len(''.join(nc.split()))))
print('Seu nome completo possui {} letras.'.format(len(nc) - nc.count(' ')))
print('Seu primeiro nome possui {} letras.'.format(len(nc.split()[0])))
print('Seu primeiro nome possui {} letras.'.format(nc.find(' ')))
