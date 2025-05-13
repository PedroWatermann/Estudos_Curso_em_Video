for c in range(0, 6):
    print(c, ' - Oi')
print('Fim\n')

for c in range(6, 0, -1):
    print(c, ' - Oi')
print('Fimn\n')

for c in range(0, 6, 2):
    print(c, ' - Oi')
print('Fim\n')

inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
for c in range(inicio, fim, passo):
    print(c)
print('\n')

s = 0
for c in range(0, 4):
    n = int(input('Digite um número: '))
    s += n
print('A somatória dos números é {}.'.format(s))