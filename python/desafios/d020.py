## O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um
# programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

nomes = input('Preciso que digite o nome deles novamente, separados por espaços: ').split()
shuffle(nomes)
print('A ordem será {}!'.format(nomes))