#print(" ".join(nome_completo)) #QUANDO PRECISAR MOSTAR O NOME INTEIRO SEM SEPARAÇÃO
#--------------------------------------- INICIO ----------------------------------------

usuarios = ["Ana Lima", "Davi Reis", "Diego Jota"]
e_mails = ["a_lima@gmail", "davi&rei@gmail", "ego&jota@gmail"]
senhas = ["1234", "2345", "3456"]
saldo = [1000, 250, 3000]
#-------------------------------------- ABERTURA ---------------------------------------

print("Olá!")
print("Em que posso ajudá-lo hoje?\n")

programa = True
while programa:
  
  continuar_1 = True
  while continuar_1:
    print("Para adicionar usuário - Digite 1")
    print("Para realizar transações - Digite 2")
    print("Para sair - Digite sair")
    opcao = 0
    opcao = input("Opção: ") #CORRIGIR   
    if opcao == "1": #CADASTRO DE PESSOAS NOVAS
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
      continuar_1 = False

    elif opcao == "2": #ENTRA EM TRANSAÇÕES (ETAPA FEITA EM "aPrincipal.py")
      print("entrando")
      continuar_1 = False

    elif opcao == "sair":
      print("Até breve") #SAI DO PROGRAMA TODO
      continuar_1 = False
      programa = False

    else:
      print("Opção inválida")
      print("Tente novamente\n")

            
