## Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Digite um número: '))
q = 0
for c in range(n, 0, -1):
    if n % c == 0:
        q += 1
if q == 2:
    print('{} é um número primo.'.format(n))
else:
    print('{} não é um número primo.'.format(n))