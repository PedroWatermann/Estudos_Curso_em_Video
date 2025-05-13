## Desenvolva um programa que leia o primeiro termo e a razão de uma PA. Mostre os 10 primeiros termos dessa progressão.

p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
for c in range(1, 11):
    print('{:>2}º termo: {}'.format(c, p + (c - 1) * r))