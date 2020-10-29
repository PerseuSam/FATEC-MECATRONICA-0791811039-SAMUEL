nomes = ["Julia", "Davi", "Diego"]
e_mails = ["ju@gmail", "davi@gmail", "ego@gmail"]
senhas = ["1234", "2345", "3456"]
saldo = [1000, 250, 3000]


repetir = True
while repetir:

  um_nome = input("Coloque seu nome: ").title()
  senha = input("Coloque sua senha: ")

  if um_nome in nomes:
    ID = nomes.index(um_nome) # MOSTRA A POSIÇÃO DA PALAVRA DENTRO DA LISTA
    print(ID)#não mostra para o usuário
    if senha in senhas[ID]:#CORRIGIR
      print("Acesso autorizado")
      repetir = False
    else:
      print("Senha ou nome incorreto")
      print("Tente novamente\n")
  else:
    print("Senha ou nome incorreto")
    print("Tente novamente\n")

print("deu bom")#não mostra para o usuário

um_nome = input("QR Code aqui, nome: ")
recebedor= nomes.index(um_nome)

print(saldo)#não mostra para o usuário
valor = int(input("Digite um valor: "))

if (saldo[ID] - valor) >= 0:
  saldo[ID] -= valor
  saldo[recebedor] += valor
  print(saldo[ID])
  print(saldo)#não mostra para o usuário
else:
  print("saldo insuficiente")
  print("Seu saldo é de: ", "R$ ",saldo[ID])
