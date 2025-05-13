## Refaça o d035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: - equilátero:
# todos os lados iguais; - isósceles: dois lados iguais; - escaleno: todos os lados diferentes

a = float(input('Digite o valor da 1ª reta: '))
b = float(input('Digite o valor da 2ª reta: '))
c = float(input('Digite o valor da 3ª reta: '))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print('É um triângulo equilátero!')
    elif a == b or a == c or b == c:
        print('É um triângulo isósceles!')
    elif a != b != c:
        print('É um triângulo escaleno!')
else:
    print('Não é um triângulo!')