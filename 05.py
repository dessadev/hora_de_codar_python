#Escreva um programa em que o usuário informe dois números. Então escreva em tela o maior deles.

print("Digite o primeiro número: ")
num1 = float(input())

print("Digite o segundo número: ")
num2 = float(input())

if num1 > num2:
    print("O maior número é:", num1)
elif num2 > num1:
    print("O maior número é:", num2)
else:
    print("Os dois números são iguais.")
