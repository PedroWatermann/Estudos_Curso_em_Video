## Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.

n = int(input('Digite um número inteiro: '))
print('{} é par.'.format(n) if n % 2 == 0 else '{} é ímpar.'.format(n))