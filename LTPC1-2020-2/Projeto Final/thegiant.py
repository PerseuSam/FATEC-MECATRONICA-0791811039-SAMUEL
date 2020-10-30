#------------------------------------------- CASO 1 -------------------------------------------
#------------------------------------- AQUI É PARA PAGAR --------------------------------------
#CORRIGIR POSSIVEIS DEFEITOS

#1 ; DAVI ; 1500 ; 5155

def pagar(): 

  malandragem = True
  while malandragem:
    recebedor = input("Para quem você deseja pagar?(Davi) ").title() ##ATENÇÃO #Aqui é para inserir o usuário que vai receber
    valor = int(input("Insira o valor(1500): "))
    QR_code = input("Insira o QR Code: ")
    print(QR_code) #não mostrar para o usuário

    marcar = 0
    posicao = 0
    primeira_posicao = 0
    segunda_posicao = 0
    terceira_posicao = 0
    recebedor_QR = 0
    valor_QR = 0
    posicao_do_pontoEvirgula = 0
    while posicao < len(QR_code):
      if QR_code[posicao] == ";":
        marcar += 1
        posicao_do_pontoEvirgula = posicao
        if marcar == 1:
          primeira_posicao = posicao_do_pontoEvirgula
        if  marcar == 2:
          segunda_posicao = posicao_do_pontoEvirgula
          recebedor_QR = (QR_code[(primeira_posicao + 2) : (segunda_posicao - 1)]).title()
          print(recebedor_QR) #não mostrar para o usuário

        if marcar == 3:
          terceira_posicao = posicao_do_pontoEvirgula
          valor_QR = int(QR_code[(segunda_posicao + 2) : (terceira_posicao - 1)])
          print(valor_QR) #não mostrar para o usuário
      posicao = posicao + 1

    if recebedor == um_nome or recebedor != recebedor_QR:
      print("Algo deu errado")
      print("Tente novamente")
    elif valor != valor_QR:
      print("Valor informado diferente do QR Code")
      print("Tente novamente")

    posicao_recebedor = nomes.index(recebedor) ##ATENÇÃO
    print(saldo) #não mostrar para o usuário
        
    if (saldo[ID] - valor) >= 0:
      saldo[ID] -= valor
      saldo[posicao_recebedor] += valor
      print("Transação efetuada\n", "Seu saldo atual é: R$", saldo[ID])
      print(saldo)#não mostrar para o usuário
      malandragem = False
    else:
      print("Saldo insuficiente")
      print("Seu saldo é de: ", "R$ ",saldo[ID])
      print("Tente novamente")
      #Perguntar se quer tentar novamente
      #COLOCAR OPÇÃO SAIR E OPÇÃO REPETIR COM OUTRO VALOR
   












#------------------------------------------- CASO 2 -------------------------------------------
#----------------------------- AQUI É PARA RECEBER (GERAR QR CODE) ----------------------------
#CORRIGIR POSSIVEIS DEFEITOS

def receber():
  
  um_nome.upper()
  valor = int(input("Gerar QR Code de qual valor? "))
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

PR = True
while PR:
  print("Para realizar pagamento - Digite 'P'")
  print("Para receber - Digite 'R'")
  escolha = 0
  escolha = input("Opção: ").upper()

  if escolha == "P":
    PR = False
    print("Você escolheu P")#(CASO 1)      #APAGAR
    pagar()
  elif escolha == "R":
    PR = False
    print("Você escolheu R")#(CASO 2)      #APAGAR
    receber()
  else:
    print("Opção inválida")
    print("Tente Novamente")
