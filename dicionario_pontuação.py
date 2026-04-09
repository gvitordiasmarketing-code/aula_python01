#CRIAÇÃO DO DICIONÁRIO
jogador = {}
pontos = {}

#ENTRADA DE DADOS
for i in range(3):
  nome = input("digite o nome: ") #chave
  pontuação = input("informe os pontos iniciais: ") #valor

  jogador[nome] = pontuação
for jogador[nome], pontuação in jogador.items():
    print(f"{jogador[nome]} | {pontuação}")
    if nome in jogador:
       print("jogador encontrado")
    else:
       print("jogador não encontrado")
       for jogador[nome], pontos in jogador.items():
          print(f"{jogador[nome]} | {pontos}")
