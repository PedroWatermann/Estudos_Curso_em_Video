print("\033[1;31;43mOlá, mundo!\033[m")
print("\033[1;30;45mOlá, mundo!\033[m")
print("\033[7;30mOlá, mundo!\033[m")

a = 3
b = 5
print("Os valores são \033[32m{}\033[m e \033[31m{}\033[m.".format(a, b))

nome = "Pedro"
print("Olá! Muito prazer em te conhecer, {}{}{}!".format("\033[4;36m", nome, "\033[m"))

# Dicionário
cores = {
    'limpa': '\033[m',
    'azul': '\033[34m',
    'amarelo': '\033[43m',
    'invertido': '\033[7;40m'}
print('Olá, {}{}{}! Os números são {} {} {} e {} {} {}!'.format(cores['azul'], nome, cores['limpa'],
                                                                cores['amarelo'], a,
                                                           cores['limpa'], cores['invertido'], b, cores['limpa']))