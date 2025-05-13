## Faça um programa que leia o peso de cinco pessoas. Mostre qual foi o maior e o menor peso lidos.

ma = 0
me = 0
for c in range(0, 5):
    peso = float(input('Digite seu peso: '))

    if c == 0:
        ma = me = peso

    if peso > ma:
        ma = peso
    if peso < me:
        me = peso
print('Maior: {} \nMenor: {}'.format(ma, me))