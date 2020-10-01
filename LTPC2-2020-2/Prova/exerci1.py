dados = []

n = 5

while len(dados) < n:
  if len(dados) != 0:
    dados.append(len(dados)+2)
  else:
    dados.append(3)
  print(dados)
  
