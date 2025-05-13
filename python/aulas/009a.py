frase = 'Pedro Augusto dos Santos Watermann'
print('\n' + frase)
print(frase[3])
print(frase[1:15])
print(frase[1:15:2])
print(frase[1::3])
print(frase[::4])
print("""opcao 1
opcao 2
opcao 3""")
print(frase.count('o'))
print(frase.upper().count('G'))
print(len(frase))

frase = '        Pedro Augusto dos Santos Watermann        '
print('\n' + frase)
print(len(frase))
print(len(frase.strip()))
print(frase.replace('dos', 'ASDlsdhfvb'))
print(frase)
print('Pedro' in frase)
print(frase.find('Watermann'))
print(frase.find('augusto'))
print(frase.lower().find('santos'))

print(frase.split())
dividido = frase.split()
print(dividido[0])
print(dividido[2][2])
