## Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
# superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite seu salário: R$'))

if salario > 1250.00:
    print('Com o reajuste, seu novo salário será de R${}'.format(salario + salario * 0.1))
else:
    print('Com o reajuste, seu novo salário será de R${}'.format(salario + salario * 0.15))