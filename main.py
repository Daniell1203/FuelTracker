while True:

    print("\n===== FUEL TRACKER =====")
    print("1 - Registrar abastecimento")
    print("2 - Ver histórico")
    print("3 - Ver consumo médio")
    print("4 - Sair")

    op = input("Escolha uma opção: ")

    if op == "4":
        print("Encerrando programa...")
        break

    else:
        print("Opção inválida")