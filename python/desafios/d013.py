## Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

salario = float(input('Digite o valor do salário: R$ '))
print('O novo salário será R$ {:.2f}.'.format(salario + salario * 0.15))