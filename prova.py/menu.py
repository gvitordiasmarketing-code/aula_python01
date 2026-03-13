menu = ()
escolha = ()

print("======[MENU]======")
print("voce é 22?")
print("1 - sim")
print("2 - não")
print("3 - sair do menu")

escolha = input("selecione uma opção")
match escolha:
    case "1":
        print("sim")
    case"2":
        print("não")
    case _:
        print("sair do menu")
        


