## Crie um script Python que leia o dia, o mes e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada.

import format as f

dia = input('Dia = ')
mes = input('Mês = ')
ano = input('Ano = ')
print('Você nasceu no dia {}'.format(f.formatColor(style=2, text='r', back='c')) + dia + ' de ' + mes + ' de ' + ano
      + '{}. Correto?'.format(f.formatColor()))
