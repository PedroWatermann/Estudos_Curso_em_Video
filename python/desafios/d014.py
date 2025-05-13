## Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.

c = float(input('Digite um temperatura em graus celcius (ºC): '))
print('{}ºC correspondem a {}ºF.'.format(c, 9 * c / 5 + 32))