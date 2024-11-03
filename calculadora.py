def adicao(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 == 0:
        return "Erro: Divisão por zero não é permitida."
    return num1 / num2

def obter_numero(mensagem):
    while True:
        valor = input(mensagem)
        try:
            return float(valor)  # Pode ser convertido para inteiro ou float
        except ValueError:
            print("Erro: Entrada inválida. Por favor, insira um número válido.")

def calculadora():
    operacoes = {
        '1': adicao,
        '2': subtracao,
        '3': multiplicacao,
        '4': divisao,
    }

    historico = []

    while True:
        print("\nEscolha uma operação:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Ver histórico")
        print("6. Sair")

        operacao = input("Digite o número da operação (1/2/3/4/5/6): ")

        if operacao == '6':
            print("Saindo...")
            break

        if operacao == '5':
            if historico:
                print("\nHistórico de operações:")
                for item in historico:
                    print(item)
            else:
                print("Nenhuma operação realizada até agora.")
            continue

        if operacao in operacoes:
            num1 = obter_numero("Digite o primeiro número: ")
            num2 = obter_numero("Digite o segundo número: ")

            resultado = operacoes[operacao](num1, num2)
            historico.append(f"{num1} {['+', '-', '*', '/'][int(operacao)-1]} {num2} = {resultado}")

            print(f"O resultado é: {resultado}")

        else:
            print("Operação inválida.")

# Executar a calculadora
if __name__ == "__main__":
    calculadora()

