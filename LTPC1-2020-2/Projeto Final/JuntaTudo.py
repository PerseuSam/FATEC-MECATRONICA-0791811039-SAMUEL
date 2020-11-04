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
      pagar()
      PR = False
    elif escolha == "R":
      print("Você escolheu a opção Receber") #(CASO 2: RECEBIMENTO)
      receber()
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

    elif opcao == "2": #ENTRA EM TRANSAÇÕES (ETAPA FEITA EM "aPrincipal.py")
      transacao()
      continuar_1 = False

    elif opcao == "sair":
      print("Até breve") #SAI DO PROGRAMA TODO
      continuar_1 = False
      programa_completo = False

    else:
      print("Opção inválida")
      print("Tente novamente\n")
                  
