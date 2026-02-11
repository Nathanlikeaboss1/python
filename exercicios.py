# Exercício 1.1 - Calculadora de IMC
'''peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso / (altura ** 2)
print(f"Seu IMC é: {imc:.2f}")'''

# Exercício 1.2 - Conversor de Temperatura
'''celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 1.8) + 32
print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}")'''

# Exercício 1.3 - Calculadora de Desconto
'''preco_original = float(input("Digite o preço original do produto: "))
desconto = float(input("Digite a porcentagem de desconto: ")) / 100
preco_final = preco_original - (preco_original * desconto)
print(f"O preço final do produto com desconto é: R${preco_final:.2f}")'''

# Exercício 1.4 - Idade em Dias
'''idade = int(input("Digite sua idade em anos: "))
idade_em_dias = idade * 365
print(f"Sua idade em dias é: {idade_em_dias} dias")'''

# Exercício 1.5 - Conversor de Moedas
'''reais = float(input("Digite o valor em reais: "))
cotacao_dolar = float(input("Digite a cotação do dólar: "))
dolares = reais / cotacao_dolar
print(f"O valor em dólares é: {dolares:.2f}")'''

# Exercício 1.6 - Calculadora de Combustível
'''distancia = float(input("Digite a distância km: "))
consumo = float(input("Digite o consumo do veículo (km/litro): "))
litros_gastos = distancia / consumo
print(f"Você precisará de {litros_gastos:.2f} litros de combustível para percorrer {distancia} km.")'''

# Exercício 1.7 - Média de Três Notas
'''nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
print(f"A média das três notas é: {media:.2f}")'''

#Exercício 1.8 - Área de um Terreno
'''largura = float(input("Digite a largura do terreno em metros: "))
comprimento = float(input("Digite o comprimento do terreno em metros: "))
area = largura * comprimento
print(f"A área do terreno é: {area:.2f} metros quadrados")'''

# Exercício 1.9 - Salário Líquido
'''salario_bruto = float(input("Digite o salário bruto: "))
desconto_inss = salario_bruto * 0.11
salario_liquido = salario_bruto - desconto_inss
print(f"O salário líquido é: {salario_liquido:.2f}")'''

# Exercício 1.10 - Troco
'''valor_compra = float(input("Digite o valor da compra: "))
valor_pago = float(input("Digite o valor pago: "))
troco = valor_pago - valor_compra
print(f"O troco a ser devolvido é: ${troco:.2f}")'''

# Exercício 2.1 - Par ou Ímpar
'''numero_inteiro = int(input("Digite um número inteiro: "))
if numero_inteiro % 2 == 0:
    print(f"O número {numero_inteiro} é par.")
else:    
    print(f"O número {numero_inteiro} é ímpar.")'''
    
# Exercício 2.2 - Aprovação por Nota
'''nota = float(input("Digite a nota do aluno (0-10): "))
if nota >= 7:
    print("Aprovado")
elif 5 <= nota < 7:
    print("Recuperação")
else:    
    print("Reprovado")'''
    
    
# Exercício 2.3 - Desconto por Valor
'''valor_compra = float(input("Digite o valor da compra: "))
if valor_compra > 100:
    desconto = valor_compra * 0.10
    valor_final = valor_compra - desconto
    print(f"Desconto de 10% aplicado. Valor final: ${valor_final:.2f}")
else:    
    print(f"Valor da compra: ${valor_compra:.2f}. Sem desconto aplicado.")'''
    
    
# Exercício 2.4 - Classificação de Idade
'''idade = int(input("Digite a idade da pessoa: "))
if idade <= 12:
    print("Criança")
elif idade <= 17:
    print("Adolescente")
elif idade <= 59:
    print("Adulto")
else:
    print("Idoso")'''
    
# Exercício 2.5 - Verificação de Senha
'''senha = input("Digite a senha: ")
if senha == "python123":
    print("Acesso permitido")
else:    
    print("Senha incorreta")'''
    
# Exercício 2.6 - Calculadora de Multa
'''velocidade = float(input("Digite a velocidade do veículo (km/h): "))
if velocidade > 60:
    multa = (velocidade - 60) * 5
    print(f"Você foi multado! O valor da multa é: R$ {multa:.2f}")
else:
    print("Você está dentro do limite de velocidade.")'''

# Exercício 2.7 - Maior de Dois Números
'''num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
if num1 > num2:
    print(f"O maior número é: {num1}")
elif num2 > num1:
    print(f"O maior número é: {num2}")
else:    print("Os dois números são iguais.")'''

# Exercício 2.8 - Verificação de Triangulo
'''lado1 = float(input("Digite o primeiro lado do triângulo: "))
lado2 = float(input("Digite o segundo lado do triângulo: "))
lado3 = float(input("Digite o terceiro lado do triângulo: "))
if (lado1 < lado2 + lado3) and (lado2 < lado1 + lado3) and (lado3 < lado1 + lado2):
    print("Os lados formam um triângulo.")
else:    
    print("Os lados não formam um triângulo.")'''
    
# Exercício 2.9 - Calculadora de IMC com Classificação
'''peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso / (altura ** 2)
print(f"Seu IMC é: {imc:.2f}")
if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif imc < 25:
    print("Classificação: Peso normal")
elif imc < 30:
    print("Classificação: Sobrepeso")
else:
    print("Classificação: Obesidade")'''
    
# Exercício 2.10 - Sistema de Login Simples

'''usuario = input("Digite o nome de usuário: ").lower()
senha = input("Digite a senha: ")
if usuario == "admin" and senha == "1234":
    print("Login bem-sucedido!")
else:
    print("Login falhou. Verifique seu nome de usuário e senha.")'''
    
# Exercício 3.1 - Contagem Regressiva
'''for n in range(10, -1, -1):
    print(n)'''

# Exercício 3.2 - Tabuada Personalizada
'''number = int(input("Digite um número inteiro para a contagem regressiva: "))
for n in range(10, -1, -1):
    calculate = number * n
    print(calculate)'''

# Exercício 3.3 - Soma de Números
'''numero = int(input("Digite um número inteiro: "))
for n in range(1, numero + 1):
    print(n)'''
    
# Exercício 3.4 - Números Pares
'''for n in range(1, 51):
    if n % 2 == 0:
        print(n)'''
        
# Exercício 3.5 - Contador de Negativos
'''num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
num4 = int(input("Digite o quarto número: "))
num5 = int(input("Digite o quinto número: "))
contagem_negativos = 0
for n in [num1, num2, num3, num4, num5]:
    if n < 0:
        contagem_negativos += 1
print(f"O número de valores negativos é: {contagem_negativos}")'''

# Exercício 3.6 - Média de Notas
'''nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
nota5 = float(input("Digite a quinta nota: "))
media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
print(f"A média das notas é: {media:.2f}")'''

# Exercício 3.7 - Maior Número
'''num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
num4 = float(input("Digite o quarto número: "))
num5 = float(input("Digite o quinto número: "))
maior_numero = num1
for n in [num1, num2, num3, num4, num5]:
    if n > maior_numero:
        maior_numero = n

print(f"O maior número é: {maior_numero}")'''

# Exercício 3.8 - Fatorial
'''num1 = int(input("Digite o número: "))
fatorial = 1
for n in range(num1, 0, -1):
    fatorial = fatorial * n
    print(fatorial)'''
    
# Exercício 3.9 - Desenho de Asteriscos
'''number = int(input("Digite o número de linhas para o desenho de asteriscos: "))
for n in range(number):
    print("*" * number)'''
    
# Exercício 3.10 - Verificador de Primos
'''number = int(input("Digite um número inteiro: "))
for n in range(2, number+1):
    if number % n == 0:
        print(n, "É primo")'''


'''for n in range (1,6):
    print("Número : ", n)'''

'''for i in range(1,11):
    resultado = 5 * i
    print(f"5 x {i} = {resultado}")'''

numero = int(input("Digite um número: "))
soma = 0
for n in range(1, numero+1):
    print(f"{soma} + {n} = {soma + n}")
    soma = soma + n




