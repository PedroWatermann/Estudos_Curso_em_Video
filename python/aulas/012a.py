nome = str(input('Qual é seu nome?\n'))

if nome == 'Pedro':
    print('Que nome bonito!')
elif nome == 'Ana':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Jéssica Maria Marcia Paulão':
    print('Que belo nome feminino!')
else:
    print('Seu nome é normal! ')

print('Tenha um bom dia, {}!'.format(nome))