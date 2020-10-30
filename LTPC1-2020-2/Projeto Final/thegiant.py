#------------------------------------------- CASO 1 -------------------------------------------
#------------------------------------- AQUI É PARA PAGAR --------------------------------------

#EXEMPLO DE QR CODE: 0 ; JULIA ; 300.0 ; 5155

def pagar(): 

  repete_pagar = True
  while repete_pagar:
    recebedor = input("Para quem você deseja pagar?(Nome completo) ").title() #Se não encontra o nome na lista, da crash
    valor = float(input("Insira o valor: "))
    QR_code = input("Insira o QR Code: ") 
    ID_recebedor = nomes.index(recebedor)
    primeiro_nome = recebedor.split()
    primeiro_nome[0].upper()

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
          recebedor_QR = (QR_code[(primeira_posicao + 2) : (segunda_posicao - 1)]).title()
        if marcar == 3:
          terceira_posicao = posicao_do_pontoEvirgula
          valor_QR = float(QR_code[(segunda_posicao + 2) : (terceira_posicao - 1)])
      posicao = posicao + 1


    if recebedor == nome_completo or primeiro_nome[0].upper() != recebedor_QR.upper() or ID_recebedor != ID_QR:
      print("Algo deu errado")
      print("Tente novamente")
    elif valor != valor_QR:
      print("Valor informado diferente do QR Code")
      print("Tente novamente")
    else:
      posicao_recebedor = nomes.index(recebedor) 
          
      if (saldo[ID] - valor) >= 0:
        saldo[ID] -= valor
        saldo[posicao_recebedor] += valor
        print("\nTransação efetuada")
        print("Seu saldo atual é: R$", saldo[ID])
        print("Saldo de todos os clientes", saldo, "\n") #NÃO MOSTRAR PARA O USUÁRIO, SOMENTE PARA TESTE
        repete_pagar = False
      else:
        print("Saldo insuficiente")
        print("Seu saldo é de: ", "R$ ",saldo[ID])
        saldo_zero = True
        while saldo_zero:
          print("Tentar novamente ou sair?")
          print("Para Tentar Novamente - Digite 'T'")
          print("Para sair - Digite 'SAIR'")
          decisao = 0
          decisao = input("Opção: ").upper()
          if decisao == "T":
            saldo_zero = False
            repete_pagar = True
          elif decisao == "SAIR":
            saldo_zero = False
            repete_pagar = False
          else:
            print("Escolha Inválida")
            print("Tente Novamente\n")




#------------------------------------------- CASO 2 -------------------------------------------
#----------------------------- AQUI É PARA RECEBER (GERAR QR CODE) ----------------------------

def receber():
  
  valor = float(input("Gerar QR Code de qual valor? ")) #CORRIGIR, se apertar só "enter" ou tiver letras da crash
  import random
  n_aleatorio = (random.randrange(1000, 9999))

  print("Seu QR Code é:", ID,";", primeiro_nome[0].upper(),";", valor,";", n_aleatorio, "\n")





#------------------------------------------ INICIO --------------------------------------------

nomes = ["Julia Camargo", "Davi Montanha", "Diego Jota Ribas"]
e_mails = ["ju_lima@gmail", "davi&montanha@gmail", "ego&jota@gmail"]
senhas = ["1234", "2345", "3456"]
saldo = [1000.0, 250.0, 3000.0]

#------------------------------------------ ACESSO --------------------------------------------
while (1): #Looping infinito
  repetir = True
  while repetir:
    print("Login")
    nome_completo = input("Coloque seu nome completo: ").title()
    senha = input("Coloque sua senha: ")

    if nome_completo in nomes:
      ID = nomes.index(nome_completo) # MOSTRA A POSIÇÃO DA PALAVRA DENTRO DA LISTA
      if senha in senhas[ID]: #CORRIGIR, se eu aperto "enter" na senha, ele aparece "Acesso autorizado"
        print("Acesso autorizado")
        primeiro_nome = nome_completo.split()
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
    print("Para voltar - Digite 'VOLTAR'")
    escolha = 0
    escolha = input("Opção: ").upper()

    if escolha == "P":
      print("Você escolheu a opção Pagamento") #(CASO 1)
      pagar()
      PR = False
    elif escolha == "R":
      print("Você escolheu a opção Receber") #(CASO 2)
      receber()
      PR = False
    elif escolha == "VOLTAR":
      print("Você escolheu a opção voltar") 
      print("Até breve")
      PR = False
    else:
      print("Opção inválida")
      print("Tente Novamente")


