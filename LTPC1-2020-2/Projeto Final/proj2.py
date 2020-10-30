#------------------------------------------- CASO 1 -------------------------------------------
#------------------------------------- AQUI É PARA PAGAR --------------------------------------
#CORRIGIR POSSIVEIS DEFEITOS

def pagar(): 

  malandragem = True
  while malandragem:
    pagador = input("QR Code aqui, nome: ").title() ##ATENÇÃO #Aqui é para inserir o usuário que vai receber 
    #Aqui é para inserir o QR code (e eu vou ter que dar um jeito do programa entender)
    if pagador == um_nome: ##ATENÇÃO
      print("Impossivel pagar para si mesmo")
      #COLOCAR OPÇÃO SAIR
    else:
      recebedor = nomes.index(pagador) ##ATENÇÃO
      print(saldo) #não mostrar para o usuário
      valor = int(input("Digite um valor: ")) #Aqui é para inserir o valor

      if (saldo[ID] - valor) >= 0:
        saldo[ID] -= valor
        saldo[recebedor] += valor
        print("Transação efetuada\n", "Seu saldo atual é: R$", saldo[ID])
        print(saldo)#não mostrar para o usuário
        malandragem = False
      else:
        print("saldo insuficiente")
        print("Seu saldo é de: ", "R$ ",saldo[ID])
        #COLOCAR OPÇÃO SAIR E OPÇÃO REPETIR COM OUTRO VALOR
        malandragem = False




#------------------------------------------- CASO 2 -------------------------------------------
#----------------------------- AQUI É PARA RECEBER (GERAR QR CODE) ----------------------------
#CORRIGIR POSSIVEIS DEFEITOS

def receber():

  ID = nomes.index(um_nome)
  um_nome.upper()
  valor = int(input("Gerar Qr Code de qual valor? "))
  import random
  n_aleatorio = (random.randrange(1000, 9999))

  print("Seu QR Code é:", ID,";", um_nome.upper(),";", valor,";", n_aleatorio)




#------------------------------------------ INICIO --------------------------------------------

nomes = ["Julia", "Davi", "Diego"]
e_mails = ["ju@gmail", "davi@gmail", "ego@gmail"]
senhas = ["1234", "2345", "3456"]
saldo = [1000, 250, 3000]

#------------------------------------------ ACESSO --------------------------------------------

repetir = True
while repetir:

  um_nome = input("Coloque seu nome: ").title()
  senha = input("Coloque sua senha: ")

  if um_nome in nomes:
    ID = nomes.index(um_nome) # MOSTRA A POSIÇÃO DA PALAVRA DENTRO DA LISTA
    print(ID)#não mostrar para o usuário
    if senha in senhas[ID]:#CORRIGIR, se eu aperto "enter" na senha, ele aparece "Acesso autorizado"
      print("Acesso autorizado")
      repetir = False
    else:
      print("Senha ou nome incorreto") 
      print("Tente novamente\n")
  else:
    print("Senha ou nome incorreto")
    print("Tente novamente\n")

#------------------------ ESCOLHA ENTRE PAGAR OU RECEBER(GERAR QR CODE) -----------------------

RP = True
while RP:
  print("Para realizar pagamento - Digite 'P'")
  print("Para receber - Digite 'R'")
  escolha = 0
  escolha = input("Opção: ").upper()

  if escolha == "P":
    RP = False
    print("Vc escolheu P")#(CASO 1)      #APAGAR
    pagar()
  elif escolha == "R":
    RP = False
    print("Vc escolheu R")#(CASO 2)      #APAGAR
    receber()
  else:
    print("Opção inválida")
    print("Tente Novamente")



