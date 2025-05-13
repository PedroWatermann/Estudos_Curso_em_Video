## Faça um programa que leia uma frase pelo teclado e mostre:
# quantas vezes aparece a letra 'A'
# em que posição aparece a primeira vez
# em que posição ela aparece a última vez

frase = input('Digite uma frase: ').upper().strip()
print('A letra "A" aparece {} vezes. \nA primeira letra "A" está na posição {}. \nA última letra "A" está na posição '
      '{}.'.format(frase.count('A'), frase.find('A') + 1, frase.rfind('A') + 1))