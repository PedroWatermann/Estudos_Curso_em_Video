## Escreva um programa que leia dois números inteiros o compare-os, mostrando na tela uma mensagem: - O primeiro
# valor é maior; - O segundo valor é maior; - Não existe valor maior, os dois são iguais

from format import formatColor as f

n1 = int(input('{}Digite um número inteiro: {}'.format(f(text='r'), f())))
n2 = int(input('{}Digite outro número inteiro: {}'.format(f(text='b'), f())))

if n1 > n2:
    print('{}{} é maior{} que {}.'.format(f(text='r'), n1, f(), n2))
elif n1 < n2:
    print('{}{} é maior{} que {}.'.format(f(text='b'), n2, f(), n1))
else:
    print('{}Não existe valor maior,{} os dois são iguais.'.format(f(text='s'), f()))