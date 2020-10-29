nomes = ["Julia", "Davi", "Diego"]
e_mails = ["ju@gmail", "davi@gmail", "ego@gmail"]
senhas = ["2312", "4782", "3572"]


repetir = True
while repetir:

  um_nome = input("Coloque seu nome: ")
  senha = input("Coloque sua senha: ")

  ID = nomes.index(um_nome) # MOSTRA A POSIÇÃO DA PALAVRA DENTRO DA LISTA
  print(ID)


  if um_nome in nomes:
    if senha in senhas[ID]:
      print("Acesso autorizado")
      repetir = False
    else:
      print("Senha ou nome incorreto")
      print("Tente novamente\n")




#elemento = nomes.index(um_nome) # MOSTRA A POSIÇÃO DA PALAVRA DENTRO DA LISTA
#print(elemento)

print("Adeus")

