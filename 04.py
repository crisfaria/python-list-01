# 4 - A tabela apresenta a produção de café, em milhões de toneladas, na região DELTA:

cafe = [12, 15, 18, 22, 17, 14, 18, 23, 29, 12]

# a) Valor da produção média;

def mediaProd(cafe):
  qtdElementos = len(cafe)
  soma = 0
  for c in cafe:
    soma = soma + c
    mediaP = soma / qtdElementos
  return mediaP
print("a) A produção média foi de:", mediaProd(cafe))

# b) Valor da mediana da produção;

def medianaProd(cafe):
  qtdElementos = len(cafe)
  cafe.sort()
  if qtdElementos % 2 == 0:
    pos1 = (qtdElementos / 2) - 1
    pos2 = qtdElementos / 2
    med = (cafe[int(pos1)] + cafe[int(pos2)]/2)
  else:
    pos = (qtdElementos - 1)/2
    med = cafe[int(pos)]
  return med

print("b) A mediana da produção foi de:", medianaProd(cafe))
# c) Valor do desvio padrão da produção;

def desvioPadrao(cafe):
  qtdElementos = len(cafe)
  soma = 0
  for x in cafe:
    soma = soma + pow(x - mediaProd(cafe), 2)
    soma = soma / qtdElementos
  return pow(soma, 1/2)

print("c) O desvio padrão da produção foi de:", round(desvioPadrao(cafe), 2))
