def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('Fim!')

def somar(a = 0, b = 0, c = 0):
    print(a + b + c)

def funcao():
    n1 = 4
    global n2
    n2 = 0
    print(f'n1 dentro vale {n1}')
    print(f'n2 dentro vale {n2}')

def soma(a = 0, b = 0, c = 0):
    return a + b + c


help(contador)

somar(1, 2, 3)
somar(1, 2)
somar(1)
somar()

n1 = 9
n2 = 10
print(f'n1 fora vale {n1}')
print(f'n2 fora vale {n2}')
funcao()
print(f'n2 fora vale {n2}')

r1 = soma(4, 3, 2)
print(f'{r1} e {soma(1, 2)}')