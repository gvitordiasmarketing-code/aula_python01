workshop1 ={"Ana", "Bruna", "Cleuza", "Dafine", "Elena","Ana"}
workshop2 ={"Alice","Brenda", "Caio", "Douglas", "Caio","vitor"}

participantes_a = set(workshop1)
participantes_b = set(workshop2)

print(f"Participantes do evento 1: {participantes_a}")
print(f"Participantes do evento 2: {participantes_b}")

todos_participantes = participantes_a.union(participantes_b)
print(f"toal de participantes: {todos_participantes}\n")
print(len (todos_participantes))