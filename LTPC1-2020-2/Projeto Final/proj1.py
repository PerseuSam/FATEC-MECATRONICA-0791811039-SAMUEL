#usuario (RELACIONAR O ID COM O USUARIO)
#valor "OK"
#string do qr code

usuarios = {1:["Carlos Augusto", "augusto.carlos@gmail.com", "2358"], 2:["Ana Carolina", "ana.carlo@gmail.com", "6752"], 3:["Igor Moraes", "imoraes.raes@gmail.com", "1374"]}

nome_completo = input("Insira seu nome: ").title()

for nome_completo in usuarios.keys():
  if nome_completo in []:
    print([])
  else:
    print("vc é incrivel, mas ainda está errado :( ")





print("------------------------------------------")


##BOM, NÃO MEXER

contas = {1:1000, 2:250, 3:3000}

dinheiro = int(input("coloca dinheiro: "))
ID = int(input("Informe o ID:"))
  #Verifica se a categoria já existe no dicionario
if ID in contas.keys():
  #Categoria já existe
  contas[ID] += dinheiro
  print(contas)
else:
  #Categoria não existe
  print("essa conta não existe")





##BOM, NÃO MEXER

#Para receber  #“5;PERIGO;1;1234”
print("Olá")
codigo = input("Para gerar o código - Digite QR: ").upper()

if codigo == "QR":
  nome = input("Insira seu nome: ").title()
  valor = int(input("Insira o valor: "))
  ID = int(input("Seu ID: "))
  import random
  aleatorio = (random.randrange(1000, 9999))
  
  memoria = []
  memoria.append(nome)
  memoria.append(valor)
  memoria.append(ID)
  memoria.append(aleatorio)
  print("QR Code: ", ID, ";", nome, ";", valor, ";", aleatorio)
  print(memoria)
else:
  print("deu ruim")
