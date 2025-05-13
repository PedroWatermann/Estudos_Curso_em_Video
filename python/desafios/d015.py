## Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa, por dia, R$ 60,00 e R$ 0.15 por Km rodado.

km = float(input('Quantos Km o carro rodou? '))
d = int(input('Quantos dias ele ficou alugado? '))
print('O valor a ser pago é R${:.2f}'.format(km * 0.15 + d * 60))