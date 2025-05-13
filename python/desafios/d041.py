## A confederação nacional de natação precisa de um programa que leia o ano de nascimento de uma atleta e mostre sua
# categoria, conforme a idade: - até 9: mirim; até 14: infantil; até 19: júnior; até 20: sênior; - acima: master
import datetime

anoNasc = int(input('Digite o ano de nascimento: '))
anoAtual = datetime.date.today().year
idade = anoAtual - anoNasc

if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Júnior')
elif idade <= 20:
    print('Sênior')
else:
    print('Master')