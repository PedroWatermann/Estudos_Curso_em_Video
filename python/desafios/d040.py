## Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
# conforme a média atingida: - média abaixo de 5,0: reprovado; - media entre 5,0 e 6,9: recuperação; - média 7,
# 0 ou superior: aprovado

n1 = float(input('Digite a 1ª nota: '))
n2 = float(input('Digite a 2ª nota: '))
m = (n1 + n2) / 2

if m < 5.0:
    print('REPROVADO!')
elif m < 7.0:
    print('RECUPERAÇÃO!')
else:
    print('APROVADO!')