## Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'.

print('O nome começa com "SANTO"? {}'.format(str(input('Digite o nome de uma cidade: ')).split()[0].upper() == 'SANTO'))