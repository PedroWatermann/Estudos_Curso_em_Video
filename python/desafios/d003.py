## Crie um programa que leia dois números e mostre a soma entre eles.

import format as f

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
print(n1, '+', n2, '={}'.format(f.formatColor(text='m')), n1 + n2, '{}'.format(f.formatColor()))
