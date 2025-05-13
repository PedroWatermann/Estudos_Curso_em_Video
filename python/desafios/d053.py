## Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite uma frase (sem acentos): '))
fr = frase.replace(' ', '')
tamanho = len(fr)
f = ''
for c in range(tamanho - 1, -1, -1):
    f += fr[c]

if fr.lower() == f.lower():
    print('Palíndromo!')
else:
    print('Não palíndromo.')