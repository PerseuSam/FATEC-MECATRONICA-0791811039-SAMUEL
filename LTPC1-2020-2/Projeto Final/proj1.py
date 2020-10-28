usuarios = {"1":["Carlos Augusto", "augusto.carlos@gmail.com", "2358"], "2":["Ana Carolina", "ana.carlo@gmail.com", "6752"], "3":["Igor Moraes", "imoraes.raes@gmail.com", "1374"]}

contas = {"1":[1000], "2":[250], "3":[3000]}

import random



#Para receber  #“5;PERIGO;1;1234”
print("Olá")
codigo = input("Para gerar o código - Digite QR: ").upper()

if codigo == "QR":
  nome = input("Insira seu nome: ").title()
  valor = int(input("Insira o valor: "))
  ID = int(input("Seu ID: "))
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


#Para pagar

print("Olá")
usuario = input("informe o usuário: ").title()
valor = float(input("Informe o valor: "))
QR_code = input("informe o QR Code: ")

print(usuario)
print(valor)
print(QR_code)
