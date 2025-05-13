## Elabore um programa que calcule o valor a ser cobrado por um produto, considerando o seu preço normal e condição
# de pagamento: - a vista dinheiro/cheque: 10% desconto; a vista cartão: 5% desconto; em até 2x cartão: normal; 3x ou
# mais cartão: 20% juros

preco = float(input('Preço das compras: R$'))
pgto = int(input('FORMAS DE PAGAMENTO\n[ 1 ] À vista dinheiro/cheque \n[ 2 ] À vista cartão \n[ 3 ] 2x no cartão \n[ 4 ] +3x no cartão \nQual é a opção?'))

if pgto == 1:
    print('Valor final: R$', preco - preco * 0.1)
elif pgto == 2:
    print('Valor final: R$', preco - preco * 0.05)
elif pgto == 3:
    print('Valor final: R$', preco)
elif pgto == 4:
    int(input('Quantas vezes?'))
    print('Valor final: R$', preco + preco * 0.2)