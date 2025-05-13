## Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m = float(input('Digite um valor em metros (m): '))
print('Em centímetros: {:.0f}cm \nEm milímetros: {:.0f}mm'.format(m * 100, m * 1000))