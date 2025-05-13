## Tuplas são IMUTÁVEIS
lanche = 'Hamburger', 'Suco', 'Pizza', 'Pudim'
print(lanche)
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-2:])

for c in lanche:
    print(f'Eu vou comer {c}.')
print('Comi pra caramba!\n')

for c in range(0, len(lanche)):
    print(lanche[c])

for pos, c in enumerate(lanche):
    print(f'Eu vou comer {c} na posicao {pos}.')

print(f'\n{sorted(lanche)}\n')

a = 2, 5, 4
b = 5, 8, 1, 2
c = a + b
print(c)
print(len(c))
print(c.count(5))
print(c.index(8))
print(c.index(5, 1))

pessoa = 'Pedro', 17, 'M', 64.3
print(pessoa)
del pessoa
print(pessoa)