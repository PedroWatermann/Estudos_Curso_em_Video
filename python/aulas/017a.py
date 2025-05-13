num = [2, 5, 9, 1, 8, 6, 0, 2]
print(num)
num[2]= 3
num.append(7)
num.sort()
num.sort(reverse=True)
len(num)
num.insert(2, 0)
num.pop()
num.pop(2)
num.remove(2)
if 4 in num:
    num.remove(4)

valores = list() # ou []
valores.append(5)
valores.append(9)
valores.append(4)
for v in valores:
    print(f'{v}...', end='')

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print(valores)

a = [2, 3, 4, 7]
b = a
print(f'Lista A: {a} \nLista B: {b}\n')
b[2] = 8
print(f'Lista A: {a} \nLista B: {b}\n')
c = a[:]
print(f'Lista A: {a} \nLista C: {c}\n')
c[2] = 0
print(f'Lista A: {a} \nLista C: {c}\n')