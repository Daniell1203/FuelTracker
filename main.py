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

    elif op == "2":

        if len(historico) == 0:
            print("Nenhum abastecimento registrado.")

        else:

            print("\n===== HISTÓRICO =====")

        for item in historico:

            print(f"\nKm rodados: {item['km']}")
            print(f"Litros: {item['litros']}")
            print(f"Valor pago: R${item['valor']}")

    elif op == "3":

        if len(historico) == 0:
         print("Sem dados.")

        else:

            soma = 0

        for item in historico:

            consumo = item["km"] / item["litros"]

            soma += consumo

        media = soma / len(historico)

        print(f"\nConsumo médio: {media:.2f} km/L")
    if op == "4":
        print("Encerrando programa...")
        break

    else:
        print("Opção inválida")
