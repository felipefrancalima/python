# Funções para as operações básicas
def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro! Divisão por zero."

# Menu de opções
print("Selecione a operação:")
print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

# Receber a escolha do usuário
escolha = input("Digite sua escolha (1/2/3/4): ")

# Receber os números do usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Realizar a operação correspondente
if escolha == '1':
    print(f"{num1} + {num2} = {soma(num1, num2)}")
elif escolha == '2':
    print(f"{num1} - {num2} = {subtracao(num1, num2)}")
elif escolha == '3':
    print(f"{num1} * {num2} = {multiplicacao(num1, num2)}")
elif escolha == '4':
    print(f"{num1} / {num2} = {divisao(num1, num2)}")
else:
    print("Opção inválida!")
#