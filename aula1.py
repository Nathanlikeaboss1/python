#exemplo 1
# nome = "Maria"
# idade = 25
# altura = 1.65
# estudante = True

# print("Nome:", nome)
# print("Idade:", idade)
# print("Altura:", altura)
# print("É Estudante?", estudante)

# Exemplo 2
# preco = 50.00
# quantidade = 3
# total = preco * quantidade

# print(f"Preço unitário: R$ , {preco}")
# print(f"Quantidade: {quantidade}")
# print(f"Total: R$ {total}")

# # Exercicio 1
# nome = input("Digite seu nome: ")
# idade = input("Digite sua idade: ")
# futuro = int(idade) + 10

# print("Em 10 anos você terá : " + str(futuro) + " anos")

# Exercicio 2
# nome = input("Digite seu nome: ")
# idade = input("Digite sua idade: ")
# ano = input("Digite o ano no futuro para saber sua idade: ")
# anoAtual = int(2026)

# futuro = (int(ano) - int(anoAtual)) + int(idade)
# print(f"Em {ano}, você terá {futuro} anos.")

# Exercicio 3
# idade = 18

# if idade >= 18:
#     print("Você é maior de idade.")
# else:
#     print("Você é menor de idade.")

# Exercicio 4
# idade = int(input("Digite sua idade: "))
# anoAtual = int(2026)
# anosRestantes = 65 - idade
# aposentadoria = anoAtual + anosRestantes
# maiorIdade = 18
# anoMaiorIdade = anoAtual + (maiorIdade - idade)

# if idade >= 18:
#     print("Você é maior de idade e se aposentará em", aposentadoria)
# else:
#     print("Você é menor de idade e terá 18 em", anoMaiorIdade)

# # # Exercicio 5
# # nota = int(input("Digite sua nota: "))

# if nota >= 7:
#     print("Aprovado")
# elif nota >= 5:
#     print("Recuperação")
# else:
#      print("Reprovado")

# temperatura = float(input("Digite a temparatura em Celsius: "))

# if temperatura >= 30:
#     print("Está quente!")
# elif temperatura >= 16 and temperatura < 30:
#     print("Está agradável.")
# else:
#     print("Está frio!")

for i in range(1,6):
    print("Número:", i)
