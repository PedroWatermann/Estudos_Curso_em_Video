## Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados

num = '{:0>4}'.format(input('Digite um número de 0 a 9999: '))
u = int(num) // 1 % 10
d = int(num) // 10 % 10
c = int(num) // 100 % 10
m = int(num) // 1000 % 10
print('{} milhar(es) \n{} centena(s) \n{} dezena(s) \n{} unidade(s)'.format(num[0],num[1], num[2], num[3]))
print('\n{} milhar(es) \n{} centena(s) \n{} dezena(s) \n{} unidade(s)'.format(m, c, d, u))