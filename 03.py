#Escreva um programa em que o usuário informe o seu nome e em seguida o programa perguntará a idade do usuário. O programa deve exibir a mensagem "Olá, [NomeDoUsuario], sua idade é [idade]".

nome_do_usuario = input("Digite o seu nome: ")
idade = input("Digite a sua idade: ")

idade = int(idade)

print(f"Olá, {nome_do_usuario}, sua idade é {idade}")
