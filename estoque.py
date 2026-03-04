
#criação do divionário estoque
estoque = {

         "camisa":50,
         "calça":170,
         "boné":139,
         "tenis nike":400,

}
#Mostrar estoque atual
print("Estoque atual: ")
for produto, quantidade in estoque.items():
    print(f"{produto} ; {quantidade}")
#pedido dados para o usuário do sistema
nome_produto = input("\n digite o nome do produto vendido: ")
quantidade_vendida = int(input("\ninforme a quantidade vendida: "))
#Atualizar o estoque
if nome_produto in estoque:
    if quantidade_vendida <= estoque[nome_produto]:
        estoque[nome_produto] = estoque[nome_produto] - quantidade_vendida
        print("venda realizada com sucesso!")
else:
    print("Produto não encontrado")
    #ESTOQUE ATUALIZADO
    for produto
 

