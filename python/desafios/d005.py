## Faça um programa que leia um número inteiro e mostre na tela seu sucessor e seu antecessor.

import format as f

n = int(input('Digite um número inteiro: '))
print('Seu antecessor é {}{}{} e seu sucessor é {}{}{}.'.format(f.formatColor(text='r'), n - 1, f.formatColor(), f.formatColor(text='c'), n + 1, f.formatColor()))