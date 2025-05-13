## Crie um script Python que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas de acordo com o valor digitado

import format as f

nome = input('Qual é o seu nome?\n')
print("Olá, {}".format(f.formatColor(text='r')) + nome + '{}! Prazer em te conhecer!'.format(f.formatColor()))
