## Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. Mostre
    # A média de idade do grupo.
    # Qual é o nome do homem mais velho.
    # Quantas mulheres tem menos de 20 anos.

media = qtde = idade = 0
nome = ''

for c in range(0, 4):
    n = str(input('Qual é seu nome: '))
    i = int(input('Qual sua idade: '))
    s = str(input('Qual seu sexo: '))

    if c == 0:
        idade = i
        nome = n

    if s.lower() == 'm':
        if i > idade:
            nome = n
    elif s.lower() == 'f':
        if i < 20:
            qtde += 1

    media += i

print(f'\nMédia idade: {media / 4} \nNome velho: {nome} \nQuantidade: {qtde}')