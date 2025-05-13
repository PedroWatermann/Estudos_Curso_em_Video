## Faça um programa que leia o ano de nascimento e informe, de acordo com sua idade: - se ele ainda vai se alistar ao
# serviço militar; - se é hora de se alistar; - se já passou do tempo do alistamento. Seu programa também deverá
# mostrar o tempo que falta ou que passou do prazo

from format import formatColor as f
import datetime

anoNasc = int(input('{}Digite o ano que você nasceu: {}'.format(f(text='m'), f())))
anoAtua = datetime.date.today().year
idade = anoAtua - anoNasc

if idade < 18:
    print('{}Você ainda se alistará ao exército.{} Faltam {}{}{} ano(s).'.format(f(text='g'), f(), f(text='g'),
                                                                               18 - idade, f()))
elif idade > 18:
    print('{}Você perdeu o prazo para se alistar ao exército.{} Se passaram {}{}{} ano(s).'.format(f(text='r'), f(),
                                                                                           f(text='r'),
                                                                               idade - 18, f()))
else:
    print('{}É hora de se alistar ao exército.{}'.format(f(text='b'), f()))