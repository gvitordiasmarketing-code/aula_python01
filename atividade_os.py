import subprocess 
import os

def executar_comando(comando):
    try:
        resultado = subprocess.run(comando, shell=True)
    except Exception as e:
       print("Erro ao executar comando")

def criar_pasta():   
    executar_comando("mkdir nova_pasta")

def copiar_arquivo():   
    executar_comando("copy arquivo.txt destino.txt ")

def gerenciador_tarefas():   
    executar_comando("tasklist")

def exibe_informações():   
    executar_comando("systeminfo")

def renomear_arquivo():   
    executar_comando("move arquivo.txt pasta//")

def testar_rede():   
    executar_comando("ping google.com")

def deletar_arquivo():   
    executar_comando("del arquivo.txt")

def finalizar_processo():   
    executar_comando("taskkill /f /im notepad.exe")

def mudar_diretório():   
    executar_comando("C:\\Users")

def listar_arquivos():   
    executar_comando("dir")

def menu():
    while True:
        print("=============CRIADO POR GABRIEL==================")
        print("1 - CRIAR PASTA")
        print("2 - COPIAR ARQUIVO")
        print("3 - GERENCIADOR TAREFAS")
        print("4 - EXIBIR INFORMAÇÕES")
        print("5 - RENOMEAR ARQUIVOS")
        print("6 - TESTAR REDE")
        print("7 - DELETAR ARQUIVO")
        print("8 - FINALIZAR PROCESSO")
        print("9 - MUDAR DIREÓRIO")
        print("10 - LISTAR ARQUIVOS")
        print("0 - SAINDO")
      
        opcao = str(input("Escolha: "))

        match opcao:
            case "1":
                criar_pasta()
            case "2":
                copiar_arquivo()
        
            case "3":
                gerenciador_tarefas()
        
            case "4":
                exibe_informações()

            case "5":
                 renomear_arquivo()

            case "6":
                 testar_rede()

            case "7":
                 testar_rede()

            case "8":
                 testar_rede()

            case "9":
                 testar_rede()

            case "10":
                 testar_rede()
                 break
            case _:
                print("eita caba sabido!!!")
if __name__ == "__main__":
   menu()

        
    