nomes = ["Julia", "Davi", "Diego"]
e_mails = ["ju@gmail", "davi@gmail", "ego@gmail"]
senhas = ["1234", "2345", "3456"]
saldo = [1000.00, 250.00, 3000.00]


repetir = True
while repetir:

  um_nome = input("Coloque seu nome: ").title()
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

um_nome = input("QR Code aqui, nome: ")
recebedor= nomes.index(um_nome)

print(saldo)
valor = int(input("Digite um valor: "))

if (saldo[ID] - valor) > 0:
  saldo[ID] -= valor
  saldo[recebedor] += valor
  print(saldo)
else:
  print("saldo insuficiente")
