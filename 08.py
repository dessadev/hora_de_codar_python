# Escreva um programa para ler 3 valores e escrever a soma dos 2 maiores. Solicita os três valores ao usuário

print("Digite o primeiro valor: ")
valor1 = float(input())

print("Digite o segundo valor: ")
valor2 = float(input())

print("Digite o terceiro valor: ")
valor3 = float(input())

valores = [valor1, valor2, valor3]
valores.sort(reverse=True)  

soma_dos_maiores = valores[0] + valores[1]

print("A soma dos dois maiores valores é:", soma_dos_maiores)
