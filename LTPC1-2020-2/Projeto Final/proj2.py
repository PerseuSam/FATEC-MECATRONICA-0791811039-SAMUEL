nomes = ["Julia", "Davi", "Diego"]
e_mails = ["ju@gmail", "davi@gmail", "ego@gmail"]
senhas = ["1234", "2345", "3456"]
saldo = [1000, 250, 3000]

#ACESSO

repetir = True
while repetir:

  um_nome = input("Coloque seu nome: ").title()
  senha = input("Coloque sua senha: ")

  if um_nome in nomes:
    ID = nomes.index(um_nome) # MOSTRA A POSIÇÃO DA PALAVRA DENTRO DA LISTA
    print(ID)#não mostra para o usuário
    if senha in senhas[ID]:#CORRIGIR, se eu aperto "enter" na senha, ele aparece "Acesso autorizado"
      print("Acesso autorizado")
      repetir = False
    else:
      print("Senha ou nome incorreto")
      print("Tente novamente\n")
  else:
    print("Senha ou nome incorreto")
    print("Tente novamente\n")

print("deu bom")#não mostra para o usuário

#AQUI É PARA PAGAR
#CORRIGIR POSSIVEIS DEFEITOS
#TENTAR FAZER ISSO UMA FUNÇÃO (def) PARA QUE SEJA DECIDIDO QUAL DELAS IR ATRAVÉS DE UM "if"
 
malandragem = True
while malandragem:
  pagador = input("QR Code aqui, nome: ").title()
  if pagador == um_nome:
    print("Impossivel pagar para si mesmo")
    #COLOCAR OPÇÃO SAIR
  else:
    recebedor= nomes.index(pagador)
    print(saldo)#não mostra para o usuário
    valor = int(input("Digite um valor: "))

    if (saldo[ID] - valor) >= 0:
      saldo[ID] -= valor
      saldo[recebedor] += valor
      print("Transação efetuada\n", "Seu saldo atual é: R$", saldo[ID])
      print(saldo)#não mostra para o usuário
      malandragem = False
    else:
      print("saldo insuficiente")
      print("Seu saldo é de: ", "R$ ",saldo[ID])
      #COLOCAR OPÇÃO SAIR E OPÇÃO REPETIR COM OUTRO VALOR
      malandragem = False


#AQUI É PARA RECEBER (GERAR QR CODE)
#CORRIGIR POSSIVEIS DEFEITOS
#TENTAR FAZER ISSO UMA FUNÇÃO (def) PARA QUE SEJA DECIDIDO QUAL DELAS IR ATRAVÉS DE UM "if"










