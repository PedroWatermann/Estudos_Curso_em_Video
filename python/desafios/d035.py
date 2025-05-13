## Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um
# triângulo.

a = float(input('Digite o valor da 1ª reta: '))
b = float(input('Digite o valor da 2ª reta: '))
c = float(input('Digite o valor da 3ª reta: '))

if a + b > c and a + c > b and b + c > a:
    print('É um triângulo!')
else:
    print('Não é um triângulo!')