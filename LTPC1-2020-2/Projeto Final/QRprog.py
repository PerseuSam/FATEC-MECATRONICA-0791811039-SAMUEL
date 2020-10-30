QR_code = input("Insira o QR Code: ")
print(QR_code) 
#posicao = QR_code[4]
marcar = 0
posicao = 0
primeira_posicao = 0
segunda_posicao = 0
terceira_posicao = 0
nominho = 0
senhazinha = 0

posicao_do_pontoEvirgula = 0
while posicao < len(QR_code):
  if QR_code[posicao] == ";":
    marcar += 1
    posicao_do_pontoEvirgula = posicao
    if marcar == 1:
      primeira_posicao = posicao_do_pontoEvirgula
      print("passou aqui")
    if  marcar == 2:
      print("passou aqui")
      segunda_posicao = posicao_do_pontoEvirgula
      nominho = QR_code[(primeira_posicao + 2) : (segunda_posicao - 1)]
      print(nominho)

    if marcar == 3:
      print("passou aqui")
      terceira_posicao = posicao_do_pontoEvirgula
      senhazinha = QR_code[(segunda_posicao + 2) : (terceira_posicao - 1)]
      print(senhazinha)
  print(marcar)
  posicao = posicao + 1

#1 ; DAVI ; 325 ; 5155
