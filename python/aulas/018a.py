from mimetypes import guess_all_extensions

from pygame.examples.blend_fill import data_dir

pessoas = [['Pedro', 17], ['Maria', 18], ['Ana', 18]]
print(pessoas)
print(pessoas[1][1])
print(pessoas[2][0])
print(pessoas[1])

teste = []
teste.append('Gustavo')
teste.append(40)
galera = list()
# galera.append(teste)
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')

del galera
galera = list()
dado = list()
for c in range(0, 3):
    dado.append((str(input('Nome: '))))
    dado.append(int(input('Idade: ')))
    # galera.append(dado)
    galera.append(dado[:])
    dado.clear()
print(galera)

totMai = totMen = 0
for p in galera:
    if p[1] >= 21:
        print('É maior de idade.')
        totMai += 1
    else:
        print('É menor de idade.')
        totMen += 1
print(f'Temos {totMai} maiores e {totMen} menores de idade.')