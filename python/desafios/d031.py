## Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$ 0,
# 50 por KM para viagens até 200Km e R$ 0,45 para viagens mais longas.

dist = float(input('Digite a distância percorrida em quilômetros: '))
valor = dist * 0.5 if dist <= 200 else dist * 0.45
print('O valor da viagem é: R${:.2f}'.format(valor))
