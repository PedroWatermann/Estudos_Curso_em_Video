## Crie um programa que leia o ano de nascimento de 7 pessoas. Mostre quantas atingiram e quantas ainda não atingiram a maioridade (21 anos).
import datetime

m = 0
for c in range(0, 7):
    anoNasc = int(input('Digite se ano de nascimento: '))
    idade = datetime.date.today().year - anoNasc
    if idade >= 21:
        m += 1
print('{} atingiram e {} não atingiram.'.format(m, 7 - m))