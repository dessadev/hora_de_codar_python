import math

# Retângulo
print("Digite a base do retângulo: ")
base = float(input())
print("Digite a altura: ")
altura = float(input())
print("A área do retângulo é ", base * altura)

# Quadrado
print("\nDigite um lado do quadrado: ")
lado = float(input())
print("A área do quadrado é ", lado * lado)

# Losango
print("\nDigite a diagonal maior do losango: ")
diagonal_maior = float(input())
print("Digite a diagonal menor: ")
diagonal_menor = float(input())
print("A área do losango é ", diagonal_maior * diagonal_menor / 2)

# Trapézio
print("\nDigite a base maior do trapézio: ")
base_maior = float(input())
print("Digite a base menor: ")
base_menor = float(input())
print("Digite a altura: ")
h = float(input())
print("A área do trapézio é ", (base_maior + base_menor) * h / 2)

# Paralelogramo
print("\nDigite a base do paralelogramo: ")
base = float(input())
print("Digite a altura: ")
altura = float(input())
print("A área do paralelogramo é ", base * altura)

# Triângulo
print("\nDigite a base do triângulo: ")
base = float(input())
print("Digite a altura: ")
altura = float(input())
print("A área do triângulo é ", base * altura / 2)

# Círculo
print("\nDigite o raio do círculo: ")
r2 = float(input())
print("A área do círculo é ", math.pi * r2 * r2)
