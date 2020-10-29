nomes = ["Julia", "Davi", "Diego"]
e_mails = ["ju@gmail", "davi@gmail", "ego@gmail"]
senhas = ["2312", "4782", "3572"]

um_nome = input("Coloque seu nome: ")
senha = input("Coloque sua senha: ")

elemento = nomes.index(um_nome) # MOSTRA A POSIÇÃO DA PALAVRA DENTRO DA LISTA
print(elemento)


if um_nome in nomes:
  if senha in senhas[elemento]:
    print("Acesso autorizado")
  else:
    print("Senha ou nome incorreto")




#elemento = nomes.index(um_nome) # MOSTRA A POSIÇÃO DA PALAVRA DENTRO DA LISTA
#print(elemento)

print("Adeus")

