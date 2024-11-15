# Escreva um programa que leia um valor informado pelo usuário e diga se o valor informado é positivo, negativo ou zero.

print("Digite um valor: ")
valor = float(input())

if valor > 0:
    print("O valor é positivo.")
elif valor < 0:
    print("O valor é negativo.")
else:
    print("O valor é zero.")
