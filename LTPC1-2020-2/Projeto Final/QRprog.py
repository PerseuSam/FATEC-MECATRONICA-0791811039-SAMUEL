##Aqui é para inserir o QR code (e eu vou ter que dar um jeito do programa entender)**********


##Maneira que deve ser colocado o QR code corretamente: "1 ; DAVI ; 325 ; 5155"
##Por exemplo, a conta de ID 5, do usuário Samuel, vai gerar um QRCode para receber o valor de 13 reias, mais um número aleatório, String gerada:
## "5 ; SAMUEL ; 13 ; 5155"

QR_code = input("Insira o QR Code: ")
print(QR_code) 
#posicao = QR_code[4]
marcar = 0
posicao = 0
primeira_posicao = 0
segunda_posicao = 0
terceira_posicao = 0
nominho = 0
valorzinho = 0

posicao_do_pontoEvirgula = 0
while posicao < len(QR_code):
  if QR_code[posicao] == ";":
    marcar += 1
    posicao_do_pontoEvirgula = posicao
    if marcar == 1:
      primeira_posicao = posicao_do_pontoEvirgula
    if  marcar == 2:
      segunda_posicao = posicao_do_pontoEvirgula
      nominho = QR_code[(primeira_posicao + 2) : (segunda_posicao - 1)]
      print(nominho)

    if marcar == 3:
      terceira_posicao = posicao_do_pontoEvirgula
      valorzinho = int(QR_code[(segunda_posicao + 2) : (terceira_posicao - 1)])
      print(valorzinho)
  posicao = posicao + 1

um_nome = input("Insira um nome(DAVI): ").upper()
valor = int(input("Insira um valor(325): "))

if nominho == um_nome:
  print("nome correto")
  if valor == valorzinho:
    print("valor correto")
  else:
    print("arrume o valor")
else:
  print("Dados diferentes")
  
#1 ; DAVI ; 325 ; 5155

##********************************************************************************************
