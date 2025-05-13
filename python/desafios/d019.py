## Um professor quer sortear um de seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome deles e escrevendo o nome do escolhido.

from random import choice

print('O aluno que apagará o quadro será {}!'.format(choice(input('Digite o nome dos 4 alunos, separados por espaços: ').split())))
