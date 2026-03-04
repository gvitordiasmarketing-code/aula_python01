gabriel = {"arroz", "feijão", "macarrão", "ovos", "batata doce"}
tiago = {"carne", "linguiça", "tomate", "pimentão", "cebola"}
Heitor = {"farofa", "bacon", "frango", "batatinha", "alface"}
Maria = {"Maça", "Banana", "Abacate", "Cenoura", "Agrião"}

comum = gabriel.intersection(gabriel,tiago,Heitor,Maria)
print(comum)

total = gabriel.union(gabriel,tiago,Heitor,Maria)
print(total)
print(len(total))
