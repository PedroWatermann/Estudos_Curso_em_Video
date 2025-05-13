## Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nome = input('Informe o nome do aluno: ')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
print('A média de {} é {}.'.format(nome, (n1 + n2) / 2))