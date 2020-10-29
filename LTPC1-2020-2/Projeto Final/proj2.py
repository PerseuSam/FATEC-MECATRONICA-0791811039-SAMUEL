nomes = ["Julia", "Davi", "Diego"]
e_mails = ["ju@gmail", "davi@gmail", "ego@gmail"]
senhas = ["2312", "4782", "3572"]
saldo = [1000, 250, 3000]


repetir = True
while repetir:

  um_nome = input("Coloque seu nome: ")
  senha = input("Coloque sua senha: ")

  if um_nome in nomes:
    ID = nomes.index(um_nome) # MOSTRA A POSIÇÃO DA PALAVRA DENTRO DA LISTA
    print(ID)
    if senha in senhas[ID]:
      print("Acesso autorizado")
      repetir = False
    else:
      print("Senha ou nome incorreto")
      print("Tente novamente\n")
  else:
    print("Senha ou nome incorreto")
    print("Tente novamente\n")

print("deu bom")

print(saldo)
valor = int(input("Digite um valor: "))
saldo[ID] += valor
print(saldo)
