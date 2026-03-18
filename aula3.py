#Exercício 1: Identificando um Erro de Sintaxe

#print("Olá, mundo!"
#O erro ocorreu porque não ouve o fechamento dela, O correto seria print("Olá, mundo")


#Exercício 2: Lidando com um NameError

#print(nome)
#O erro acontece aqui porque não foi declarado nenhuma variável antes do print, então não tem de onde ele pegar os dados
# o certo seria assim:
# nome = "João"
# print(nome)


# Exercício 3: Erro de Tipagem (TypeError)

# def somar(a, b):
#     return a + b

# resultado = somar(10, "5")
# print(resultado)

#O erro aqui é que ele tenta somar uma string com um int, isso acaba dando um erro de tipagem (typeError)
#O certo seria assim:

# def somar(a, b):
#     return a + b

# try:
#     resultado = somar(10, "5")
#     print(resultado)

# except TypeError:
#     print("Erro de tipagem")

#Exercício 4: Corrigindo um Erro de Índice (IndexError)

# numeros = [10, 20, 30]
# indice = int(input("Digite um índice para acessar a lista: ")) 

# print(numeros[indice])

#O codigo está correto, mas não tem nenhum aviso quando o usuario digita um valor maior que o da lista, fazendo o codigo parar
#O certo seria assim:

# try:
#     numeros = [10, 20, 30]
#     indice = int(input("Digite um índice para acessar a lista: ")) 
#     print(numeros[indice])

# except IndexError:
#     print("Índice fora dos limites da lista")

#Caso o usuario coloque um limite maior que o da lista ele ira mostrar essa mensagem

#Exercício 5: Tratando Múltiplos Erros ao Mesmo Tempo

# def dividir(a, b):
#     return a / b

# num1 = input("Digite o primeiro número: ")
# num2 = input("Digite o segundo número: ")

# resultado = dividir(int(num1), int(num2))
# print(f"Resultado: {resultado}")

#Os erros que esse codigo pode gerar são que o usuario pode colocar alguma string e que ele pode tentar dividir por zero (que não é possivel)

#poderiamos fazer assim:

# def dividir(a, b):
#     return a / b

# try:
#     num1 = input("Digite o primeiro número: ")
#     num2 = input("Digite o segundo número: ")

#     resultado = dividir(int(num1), int(num2))
#     print(f"Resultado: {resultado}")

# except ValueError:
#     print("Erro: digite apenas números!")

# except ZeroDivisionError:
#     print("Erro: não é possível dividir por zero!")

#Com esse codigo indentifica se o usuario colocou alguma letra (string) ou tentou dividir por zero, se caso ocorra, ele manda uma mensagem


#Exercício 6: Erro ao Trabalhar com Dicionários

# dados = {
#     "nome": "Isaac ",
#     "idade": 25,
#     "cidade": "São Paulo"
# }

# chave = input("Digite a chave que deseja acessar: ")

# print(f"O valor da chave '{chave}' é: {dados[chave]}")

#O codigo 

