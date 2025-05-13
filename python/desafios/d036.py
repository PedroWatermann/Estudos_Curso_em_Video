## Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor
# da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que
# ela não pode exceder 30% do salário ou então o empréstimo será negado.

from format import formatColor as f

valCasa = float(input('{}Digite o valor da casa: R${}'.format(f(text='g'), f())))
salComp = float(input('{}Digite o valor do seu salário: R${}'.format(f(text='b'), f())))
qtdAnos = int(input('{}Em quantos anos irá comprar: {}'.format(f(text='m'), f())))

valParcela = valCasa / qtdAnos * 12

if valParcela > salComp * 0.3:
    print('\nO empréstimo foi {} NEGADO {}! Salário insuficiente.'.format(f(2, 'w', 'r'), f()))
else:
    print('\nEmpréstimo {} APROVADO {}! Aproveite.'.format(f(2, 'w', 'g'), f()))