def mostre_menu():
    print("1-  VER CARDAPIO")
    print("2-  FAZER PEDIDO")
    print("3-  VER CONTA")
    print("4-   SAIR")

while True:
    mostre_menu()
    opção = input("Escolha uma opção: ")
    match opção: 
        case "1":
            print("-----cardapio-----")
            print("pizza - $35")
            print("hamburger - $35")
            print("Refrigerante - $10")
            print("o que deseja pedir? ")
            print("pizza - $35")
            print("refrigerante - $10")
        case "1":
            print("-----cardapio-----")
            print("pizza - $35")
            print("hamburger - $35")
            print("Refrigerante - $10")
            print("o que deseja pedir? ")
            print("pizza - $35")
            print("refrigerante - $10")
            pedido = input("escolha")

            match pedido:
                case "1":
                    conta += 20
                    print("Pedido selecionado: Pizza")
                case "2":
                    conta += 20
                    print("Pedido selecionado: Hamburguer")
                case "3":
                    print(f"\nO valor da conta: r$ {conta}")
                case "4":
                    print("O brigado por nos visitar")
                    break
                case _:
                    print("volte ao menu")

