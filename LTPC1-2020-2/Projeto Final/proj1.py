usuarios = [["Carlos Augusto", "augusto.carlos@gmail.com", "2358"], ["Ana Carolina", "ana.carlo@gmail.com", "6752"], ["Igor Moraes", "imoraes.raes@gmail.com", "1374"]]


contas = [[1000], [250], [3000]]





#Para receber  #“5;PERIGO;1;1234”
print("Olá")
codigo = input("Para gerar o código - Digite QR: ").upper()

if codigo == "QR":
  nome = input("Insira seu nome: ")
  valor = ("Insira o valor: ")
  

  print("5;PERIGO;1;1234")


#Para pagar

print("Olá")
usuario = input("informe o usuário: ").title()
valor = float(input("Informe o valor: "))
QR_code = input("informe o QR Code: ")

print(usuario)
print(valor)
print(QR_code)
