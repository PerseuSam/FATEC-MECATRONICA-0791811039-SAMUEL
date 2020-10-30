#------------------------------------------- CASO 1 -------------------------------------------
#------------------------------------- AQUI É PARA PAGAR --------------------------------------
#CORRIGIR POSSIVEIS DEFEITOS

#0 ; JULIA ; 300 ; 5155

def pagar(): 

  malandragem = True
  while malandragem:
    recebedor = input("Para quem você deseja pagar?(Julia) ").title()
    valor = int(input("Insira o valor(300): "))
    QR_code = input("Insira o QR Code: ") #0 ; JULIA ; 300 ; 5155
    ID_recebedor = nomes.index(recebedor)

    marcar = 0
    posicao = 0
    primeira_posicao = 0
    segunda_posicao = 0
    terceira_posicao = 0
    ID_QR = 0
    recebedor_QR = 0
    valor_QR = 0
    posicao_do_pontoEvirgula = 0
    while posicao < len(QR_code):
      if QR_code[posicao] == ";":
        marcar += 1
        posicao_do_pontoEvirgula = posicao
        if marcar == 1:
          primeira_posicao = posicao_do_pontoEvirgula
          ID_QR = int(QR_code[: (primeira_posicao - 1)])
        if  marcar == 2:
          segunda_posicao = posicao_do_pontoEvirgula
          recebedor_QR = (QR_code[(primeira_posicao + 2) : (segunda_posicao - 1)]).title() #0 ; JULIA ; 300 ; 5155
        if marcar == 3:
          terceira_posicao = posicao_do_pontoEvirgula
          valor_QR = int(QR_code[(segunda_posicao + 2) : (terceira_posicao - 1)]) #0 ; JULIA ; 300 ; 5155
      posicao = posicao + 1


    if recebedor == um_nome or recebedor != recebedor_QR or ID_recebedor != ID_QR:
      print("Algo deu errado")
      print("Tente novamente")
    elif valor != valor_QR:
      print("Valor informado diferente do QR Code")
      print("Tente novamente")

    posicao_recebedor = nomes.index(recebedor) ##ATENÇÃO
        
    if (saldo[ID] - valor) >= 0:
      saldo[ID] -= valor
      saldo[posicao_recebedor] += valor
      print("Transação efetuada")
      print("Seu saldo atual é: R$", saldo[ID])
      malandragem = False
    else:
      print("Saldo insuficiente")
      print("Seu saldo é de: ", "R$ ",saldo[ID])
      print("Tente novamente")


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
  print("\nPara realizar pagamento - Digite 'P'")
  print("Para receber - Digite 'R'")
  print("Para sair - Digite 'SAIR'")
  escolha = 0
  escolha = input("Opção: ").upper()

  if escolha == "P":
    print("Você escolheu a opção Pagamento") #(CASO 1)
    pagar()
  elif escolha == "R":
    print("Você escolheu a opção Receber") #(CASO 2)
    receber()
  elif escolha == "SAIR":
    print("Você escolheu a opção sair") 
    print("Até breve")
    break
  else:
    print("Opção inválida")
    print("Tente Novamente")
