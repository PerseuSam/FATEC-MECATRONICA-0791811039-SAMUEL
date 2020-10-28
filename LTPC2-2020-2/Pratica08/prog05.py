personagens = {"dps": [] , "healer": [], "support": [], "tank": []}

continuar = True

while continuar:

  nome = input("Qual o nome do personagem:")
  classe = input("Qual a classe do personagem:").lower()

  if classe in personagens.keys():
    personagens[classe].append(nome)

  else:
    print("Classe de personagem invalida!")

  print("\n", personagens)
  continuar = input("\nAdicionar mais personagens?(s/n)") == "s"

print("Porcentagens Relativas:")

for categoria in personagens.keys():
  porcentagem = (len(personagens[categoria])/len(personagens))*100
  print("Categoria:", categoria, " - ", porcentagem)
  if porcentagem == 25:
    print("equipe balanceada")
  else:
    print("equipe desbalanceada")



print("\nPersonagens:")
for categoria in personagens.keys():
  print("Classe de Personagem:", categoria.capitalize())
  for nome_de_personagem in personagens[categoria]:
    print(nome_de_personagem)
  print('-------')

