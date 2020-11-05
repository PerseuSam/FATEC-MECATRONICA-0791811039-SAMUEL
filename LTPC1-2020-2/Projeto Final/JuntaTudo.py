#print(" ".join(nome_completo)) #QUANDO PRECISAR MOSTAR O NOME INTEIRO SEM SEPARAÇÃO

#---------------------------------- 1) CRIAR CONTA -------------------------------------

def cria_conta():

  continuar_2 = True
  while continuar_2:
    nome_completo = (input("\nVamos começar pelo seu nome, qual seu nome completo? ").title()).split()
    print("Olá", nome_completo[0].title())
    e_mail = input("Agora digite seu e-mail: ") #CORRIGIR  
    print("Estamos quase lá")
    senha = input("Digite uma senha: ") #CORRIGIR  

    usuarios.append(" ".join(nome_completo))
    e_mails.append(e_mail)
    senhas.append(senha)
    valor = int(input("Insira um valor inicial: "))
    saldo.append(valor)

    print("\nUsuários") #NÃO MOSTRAR PARA O USUÁRIO, SOMENTE PARA TESTE
    print(usuarios) #NÃO MOSTRAR PARA O USUÁRIO, SOMENTE PARA TESTE

    print("\nE-mails") #NÃO MOSTRAR PARA O USUÁRIO, SOMENTE PARA TESTE
    print(e_mails) #NÃO MOSTRAR PARA O USUÁRIO, SOMENTE PARA TESTE

    print("\nSenhas") #NÃO MOSTRAR PARA O USUÁRIO, SOMENTE PARA TESTE
    print(senhas) #NÃO MOSTRAR PARA O USUÁRIO, SOMENTE PARA TESTE

    print("\nSaldos") #NÃO MOSTRAR PARA O USUÁRIO, SOMENTE PARA TESTE
    print(saldo) #NÃO MOSTRAR PARA O USUÁRIO, SOMENTE PARA TESTE

    continuar_2 = input("\nAdicionar mais algúem? (S/N)").upper() == "S"




#---------------------------------- 2) TRANSAÇÕES --------------------------------------
def transacao():

  repetir = True
  while repetir:
    print(usuarios) #NÃO MOSTRAR PARA O USUÁRIO, SOMENTE PARA TESTE
    print(senhas) #NÃO MOSTRAR PARA O USUÁRIO, SOMENTE PARA TESTE
    print("\nLogin")
    nome_completo = input("Coloque seu nome completo: ").title()
    senha = input("Coloque sua senha: ")

    if nome_completo in usuarios:
      ID = usuarios.index(nome_completo) # MOSTRA A POSIÇÃO DA PALAVRA DENTRO DA LISTA
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

  #------------------------ ESCOLHA ENTRE PAGAR OU RECEBER(GERAR QR CODE) ----------------------

  PR = True
  while PR:
    print("\nPara realizar pagamento - Digite 'P'")
    print("Para receber - Digite 'R'")
    print("Para voltar - Digite 'VOLTAR'")
    escolha = 0
    escolha = input("Opção: ").upper()

    if escolha == "P":
      print("Você escolheu a opção Pagamento") #(CASO 1: PAGAMENTO)
      repete_pagar = True
      while repete_pagar:
        verificaNome = True
        while verificaNome:
          recebedor = input("\nPara quem você deseja pagar?(Nome completo) ").title()
          if recebedor in usuarios:
            verificaNome = False
          else:
            print("Algo errado")
            print("Tente novamente")

        verificaValor = True
        while verificaValor:
          valor = input("Insira o valor: ")
          if valor.isdigit():
            valor = int(valor)
            verificaValor = False
          else:
            print("Algo errado")
            print("Tente novamente")

        QR_code = input("Insira o QR Code: ") #CORRIGIR?, se digita algo dierente do QR Code, da crash

        ID_recebedor = usuarios.index(recebedor)
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
              ID_QR = int(QR_code[:primeira_posicao])
            if  marcar == 2:
              segunda_posicao = posicao_do_pontoEvirgula
              recebedor_QR = (QR_code[(primeira_posicao+1) : segunda_posicao]).title()
            if marcar == 3:
              terceira_posicao = posicao_do_pontoEvirgula
              valor_QR = int(QR_code[(segunda_posicao+1) : terceira_posicao])
          posicao = posicao + 1


        if recebedor == nome_completo or primeiro_nome[0].upper() != recebedor_QR.upper() or ID_recebedor != ID_QR:
          print("Algo deu errado")
          print("Tente novamente")
        elif valor != valor_QR:
          print("Valor informado diferente do QR Code")
          print("Tente novamente")
        else:
          posicao_recebedor = usuarios.index(recebedor) 
          
        if (saldo[ID] - valor) >= 0:
          saldo[ID] -= valor
          saldo[posicao_recebedor] += valor
          print("\nTransação efetuada")
          print("Seu saldo atual é: R$", saldo[ID])
          print("Saldo de todos os clientes:", saldo, "\n") #NÃO MOSTRAR PARA O USUÁRIO, SOMENTE PARA TESTE
          repete_pagar = False
        else:
          print("Saldo insuficiente")
          print("Seu saldo é de: R$ ",saldo[ID])
          saldo_zero = True
          while saldo_zero:
            print("Tentar novamente ou sair?")
            print("Para Tentar Novamente - Digite 'T'")
            print("Para voltar - Digite 'VOLTAR'")
            decisao = 0
            decisao = input("Opção: ").upper()
            if decisao == "T":
              saldo_zero = False
              repete_pagar = True
            elif decisao == "VOLTAR":
              saldo_zero = False
              repete_pagar = False
            else:
              print("Escolha Inválida")
              print("Tente Novamente\n")
      PR = False

    elif escolha == "R":
      print("Você escolheu a opção Receber") #(CASO 2: RECEBIMENTO)
      verificaNumero = True
      while verificaNumero:
        valor = input("\nGerar QR Code de qual valor? ")
        if valor.isdigit():
          valor = int(valor)
          verificaNumero = False
        else:
          print("Algo errado")
          print("Tente novamente")

        import random
        n_aleatorio = (random.randrange(1000, 9999))
        print("Seu QR Code é: {};{};{};{}".format(ID, primeiro_nome[0].upper(), valor, n_aleatorio), "\n")
        PR = False

    elif escolha == "VOLTAR":
      print("Você escolheu a opção voltar\n") 
      PR = False

    else:
      print("Opção inválida")
      print("Tente Novamente")



#--------------------------------------- INICIO ----------------------------------------

usuarios = ["Ana Lima", "Davi Reis", "Diego Jota"]
e_mails = ["a_lima@gmail", "davi&rei@gmail", "ego&jota@gmail"]
senhas = ["1234", "2345", "3456"]
saldo = [1000, 250, 3000]



#-------------------------------------- ABERTURA ---------------------------------------

programa_completo = True
while programa_completo:

  print("Olá!")
  print("Em que posso ajudá-lo hoje?\n")
  continuar_1 = True
  while continuar_1:
    print("Para adicionar usuário - Digite 1")
    print("Para realizar transações - Digite 2")
    print("Para sair - Digite sair")
    opcao = 0
    opcao = input("Opção: ") #CORRIGIR   
    if opcao == "1": #CADASTRO DE PESSOAS NOVAS
      cria_conta()
      continuar_1 = False

    elif opcao == "2": #ENTRA EM TRANSAÇÕES
      transacao()
      continuar_1 = False

    elif opcao == "sair":
      print("Até breve") #SAI DO PROGRAMA TODO
      continuar_1 = False
      programa_completo = False

    else:
      print("Opção inválida")
      print("Tente novamente\n")
