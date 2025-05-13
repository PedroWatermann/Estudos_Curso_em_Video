## Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis
# sobre ela.

import format as f

algo = input('{}Digite algo: {}'.format(f.formatColor(7, 's', 'r'), f.formatColor()))
print(type(algo))
print(algo.isalnum())
print(algo.isalpha())
print(algo.isascii())
print(algo.isdigit())
print(algo.islower())
print(algo.isspace())
print(algo.istitle())
print(algo.isupper())
print(algo.isdecimal())
print(algo.isnumeric())
print(algo.isprintable())
print(algo.isidentifier())
