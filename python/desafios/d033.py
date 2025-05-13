## Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = float(input('Digite um número: '))
n3 = float(input('Digite outro número: '))
n2 = float(input('Digite um outro número: '))

if n1 > n2:
    if n1 > n3:
        print('{} é o maior número'.format(n1), end=' e ')
        if n2 > n3:
            print('{} é o menor número'.format(n3))
        else:
            print('{} é o menor número'.format(n2))
    else:
        print('{} é o maior número e {} é o menor número.'.format(n3, n2))
else:
    if n2 > n3:
        print('{} é o maior número e {} é o menor número.'.format(n2, n1))
    else:
        print('{} é o maior número e {} é o menor número.'.format(n3, n1))
