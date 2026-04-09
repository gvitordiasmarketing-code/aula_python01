#CRIAÇÃO DO DICIONÁRIO
aluno = {}
#ENTRADA DE DADOS
aluno["Nome"] = input("Digite o nome do aluno: ")
aluno["curso"] = input("Digite o curso do aluno: ")
aluno["nota"] = float(input("Digite a nota do aluno: "))

#SAÍDA DE DADOS
print(f"O Nome do aluno é : {aluno["Nome"]}")
print(f"O curso do aluno é : {aluno["curso"]}")
print("Agprovado" if aluno["nota"] >= 18 else "reprovado")
