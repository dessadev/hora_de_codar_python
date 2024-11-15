# Escreva um programa para ler 3 valores e escrever o maior deles, solicita os três valores ao usuário

print("Digite o primeiro valor: ")
valor1 = float(input())

print("Digite o segundo valor: ")
valor2 = float(input())

print("Digite o terceiro valor: ")
valor3 = float(input())

maior = valor1

if valor2 > maior:
    maior = valor2

if valor3 > maior:
    maior = valor3

print("O maior valor é:", maior)
