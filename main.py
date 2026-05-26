historico = []
while True:

    print("\n===== FUEL TRACKER =====")
    print("1 - Registrar abastecimento")
    print("2 - Ver histórico")
    print("3 - Ver consumo médio")
    print("4 - Sair")

    op = input("Escolha uma opção: ")

    if op == "1":

        km = float(input("Km rodados: "))
        litros = float(input("Litros abastecidos: "))
        valor = float(input("Valor pago: "))

    dados = {
        "km": km,
        "litros": litros,
        "valor": valor
    }

    historico.append(dados)

    print("Abastecimento registrado!")
    if op == "4":
        print("Encerrando programa...")
        break

    else:
        print("Opção inválida")
