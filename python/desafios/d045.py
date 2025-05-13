## Crie um programa que faça o computador jogar Jokenpô com você

from random import randint as r
from format import formatColor as f

p = int(input('Escolha uma opção: \n[ 1 ] Pedra \n[ 2 ] Papel \n[ 3 ] Tesoura \nQual a opção? '))
m = r(1, 3)

if p == m:
    print('{}Empate!'.format(f(text='s')))
else:
    if p == 1:
        if m == 2:
            print('{}Você perdeu!'.format(f(text='r')))
        else:
            print('{}Você ganhou!'.format(f(text='g')))
    elif p == 2:
        if m == 3:
            print('{}Você perdeu!'.format(f(text='r')))
        else:
            print('{}Você ganhou!'.format(f(text='g')))
    else:
        if m == 1:
            print('{}Você perdeu!'.format(f(text='r')))
        else:
            print('{}Você ganhou!'.format(f(text='g')))