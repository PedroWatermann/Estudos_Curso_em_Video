## Desenvolva um programa que leia 6 números inteiros e soma apenas aqueles que forem pares.

s = 0
for c in range(0, 6):
    n = int(input('Digite um valor: '))
    s += n if n % 2 == 0 else 0
print('A soma é {}.'.format(s))