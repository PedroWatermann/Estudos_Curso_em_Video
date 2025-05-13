## Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome
# separadamente.

nc = str(input('Digite seu nome completo: '))
ncs = nc.strip().split()
qtde = len(ncs)
print('Olá, {} {}!'.format(ncs[0], ncs[qtde - 1]))