## Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de
# conversão: 1 - binário; 2 - octal; 3 - hexadecimal

from format import formatColor as f

num = int(input('{}Digite um número inteiro: {}'.format(f(text='c'), f())))
base = int(input('{}Escolha uma base para conversão:{}\n {}1 - Binário{}\n {}2 - Octal{}\n {}3 Hexadecimal{}\n'.format(
    f(text='m'), f(), f(back='y'), f(), f(back='g'), f(), f(back='s'), f())))
if base == 1:
    print('{} em binário é {} {} {}.'.format(num, f(2, 'y', 'w'), bin(num), f()))
elif base == 2:
    print('{} em octal é {} {} {}.'.format(num, f(2, 'g', 'w'), oct(num), f()))
elif base == 3:
    print('{} em hexadecimal é {} {} {}.'.format(num, f(2, 's', 'w'), hex(num), f()))