def menu():
    print("=======================")
    print("     CALCULADORA")
    print("=======================")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")
    print("=======================")
    print("Escolha uma operação:")
# code para calcular a soma, subtração, multiplicação e divisão de dois números
def calculadora():
    while True:
        menu()
        opcao = input("Digite o número da operação desejada: ")
        if opcao == '5':
            print("Saindo...")
            break
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        if opcao == '1':
            print("Resultado:", num1 + num2)
        elif opcao == '2':
            print("Resultado:", num1 - num2)
        elif opcao == '3':
            print("Resultado:", num1 * num2)
        elif opcao == '4':
            if num2 != 0:
                print("Resultado:", num1 / num2)
            else:
                print("Erro: Divisão por zero não é permitida.")
        else:
            print("Opção inválida.")
calculadora()
