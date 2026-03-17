#Desafio: Criar um programa de caixa eletrônico simples que permita ao usuário depositar dinheiro, sacar dinheiro e verificar o extrato.
# saldo = 0.0
# extrato = []

# while True:
#     print("\nCAIXA ELETRÔNICO")
#     print("1 - Depositar dinheiro")
#     print("2 - Sacar dinheiro")
#     print("3 - Extrato")
#     print("4 - Sair")

#     escolha = input("Escolha uma opção: ")

#     if escolha == '1':
#         valor = float(input("Digite o valor a ser depositado: "))
#         if valor > 0:
#             saldo += valor
#             extrato.append(f"Depósito: +R${valor:.2f}")
#             print("Depósito realizado!")
#         else:
#             print("Valor inválido.")

#     elif escolha == '2':
#         valor = float(input("Digite o valor do saque: "))

#         if valor <= 0:
#             print("Valor inválido.")
#         elif valor > saldo:
#             print("Saldo insuficiente.")
#         else:
#             saldo -= valor
#             extrato.append(f"Saque: -R${valor:.2f}")
#             print("Saque realizado!")

#     elif escolha == '3':
#         print("\n--- EXTRATO ---")

#         if len(extrato) == 0:
#             print("Sem movimentações")
#         else:
#             for item in extrato:
#                 print(item)

#         print(f"Saldo: R${saldo:.2f}")

#     elif escolha == '4':
#         break

#     else:
#         print("Opção inválida.")

#Desafio: Criar uma calculadora simples que permita ao usuário realizar operações de soma, subtração, multiplicação e divisão.

class calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def soma(self):
        return self.num1 + self.num2
    
    def subtracao(self):
        return self.num1 - self.num2

    def multiplicacao(self):
        return self.num1 * self.num2

    def divisao(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Divisão por zero não é permitida."


def menu():
    print("\nBem-vindo à calculadora simples!")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Histórico")
    print("6 - Limpar Histórico")
    print("7 - Sair")
    return input("Digite a opção: ")


def main():
    historico = []  

    while True:
        opcao = menu()

        if opcao == '1':
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            calc = calculadora(num1, num2)
            resultado = calc.soma()

            historico.append(f"{num1} + {num2} = {resultado}")
            print(f"Resultado: {resultado}")

        elif opcao == '2':
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            calc = calculadora(num1, num2)
            resultado = calc.subtracao()

            historico.append(f"{num1} - {num2} = {resultado}")
            print(f"Resultado: {resultado}")

        elif opcao == '3':
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            calc = calculadora(num1, num2)
            resultado = calc.multiplicacao()

            historico.append(f"{num1} * {num2} = {resultado}")
            print(f"Resultado: {resultado}")

        elif opcao == '4':
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                calc = calculadora(num1, num2)
                resultado = calc.divisao()

                historico.append(f"{num1} / {num2} = {resultado}")
                print(f"Resultado: {resultado}")

            except ValueError:
                print("Entrada inválida. Por favor, digite números válidos.")

        elif opcao == '5':
            print("\n--- HISTÓRICO ---")

            if not historico:
                print("Nenhuma operação realizada.")
            else:
                for item in historico:
                    print(item)

        elif opcao == '6':
            print("\n--- HISTÓRICO ---")

            historico.clear()
            print("Histórico limpo.")

            

        elif opcao == '7':
            print("Encerrando...")
            break

        else:
            print("Opção inválida.")


main()

# import requests 

# resposta = requests.get("https://parallelum.com.br/fipe/api/v1/carros/marcas")

# print("Status da Requisição:", resposta.status_code)
# print("Resposta da API", resposta.json())
