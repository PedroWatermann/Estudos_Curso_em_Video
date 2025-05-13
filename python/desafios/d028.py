## Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou
# perdeu.

from random import randint
from time import sleep

r = randint(0, 5)
n = int(input('Descubra o número!\nDigite um número entre 0 e 5: '))

print('Pensando...')
sleep(2)

if n == r:
    print('Parabéns, você acertou!')
else:
    print('Que pena, você errou! Eu pensei no {}.'.format(r))