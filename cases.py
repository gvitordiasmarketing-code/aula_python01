escolha = int(input("Informe um numero de 1 a 7 para escolher o dia na semana:"))


match escolha:
    case 1:
        print("Segunda")
    case 2:
        print("Terça")
    case 3:
        print("Quarta")
    case 4:
        print("Quinta")
    case 5:
        print("Sexta")
    case 6:
        print("Sábado")
    case 7:
        print("Domingo")
    case _:
        print("vc e o enéas desta geração!!")

