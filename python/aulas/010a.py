nome = input('Qual é seu nome? \n')

if nome == 'Pedro':
    print('Que nome lindo você tem!\n')
else:
    print('Seu nome é tão normal...\n')

print('Bom dia {}'.format(nome))

# --------------------------------------

n1 = int(input('Nota 1: '))
n2 = int(input('Nota 2: '))
m = (n1 + n2) / 2
print('A sua média foi {:.2f}'.format(m))
print('Parabéns!' if m >= 6.0 else 'Estude mais!')