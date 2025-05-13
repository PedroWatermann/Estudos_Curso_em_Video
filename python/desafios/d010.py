## Crie um programa que leia quanto de dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# US$ 1,00 = R$ 3,27

valor = float(input('Quanto de dinheiro você tem na carteira?\nR$ '))
print('Você pode comprar US$ {:.2f}'.format(valor / 3.27))