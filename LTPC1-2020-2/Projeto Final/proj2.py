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

print("Para realizar pagamento - Digite 'P'")
print("Para receber - Digite 'R'")

escolha = 0
escolha = input("Opção: ").upper()
if escolha == "P":
  print("Vc escolheu P")#(CASO 1)
else:
  print("Vc escolheu R")#(CASO 2)





#------------------------AQUI É PARA PAGAR (CASO 1)---------------------------------------------
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


#----------------------------AQUI É PARA RECEBER (GERAR QR CODE) (CASO 2)--------------------
#CORRIGIR POSSIVEIS DEFEITOS
#TENTAR FAZER ISSO UMA FUNÇÃO (def) PARA QUE SEJA DECIDIDO QUAL DELAS IR ATRAVÉS DE UM "if"
#GERAR AQUI A CHAVE, O QR CODE "5;PERIGO;1;1234"

ID = nomes.index(um_nome)
um_nome.upper()
valor = int(input("Gerar Qr Code de qual valor? "))
import random
n_aleatorio = (random.randrange(1000, 9999))

print("Seu QR Code é:", ID,";", um_nome.upper(),";", valor,";", n_aleatorio)

