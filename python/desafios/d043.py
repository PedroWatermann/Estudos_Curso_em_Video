## Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu imc e mostre seu status, de acordo com
# a tabela abaixo: - < 18,5: abaixo do peso; - < 25: peso ideal; - < 30: sobrepeso; - < 40 obesidade; - > 40:
# obesidade mórbida

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / altura ** 2

if imc < 15.5:
    print('Abaixo do peso.', imc)
elif imc < 25:
    print('Peso ideal.', imc)
elif imc < 30:
    print('Sobrepeso.', imc)
elif imc < 40:
    print('Obesidade.', imc)
else:
    print('Obesidade mórbida.', imc)