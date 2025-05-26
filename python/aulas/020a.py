def soma(a, b):
    print(a + b)

def contador(*num):
    print(len(num), ' números')

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

# Programa principal
a = 4
b = 5
s = a + b
print(s)
soma(4, 5)
soma(b = 7, a = 1)

contador(1, 2, 3, 4)
contador(2, 3, 0)

valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)