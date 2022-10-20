# 2 - Os resultados baseados em uma escala de ansiedade para uma amostra de nove sujeitos são:

amostra = [67, 75, 63, 72, 77, 78, 81, 77, 80]

# a) Média aritmética simples, harmônica e geométrica;

def mediaSimples(amostra):
  qtdElementos = len(amostra)
  soma = 0
  for e in amostra:
    soma = soma + e
    mediaS = soma / qtdElementos
  return(mediaS)
print("a) media aritmética simples:", round(mediaSimples(amostra), 2))

def mediaHarmonica(amostra):
    qtdElementos = len(amostra)
    soma = 0
    for e in amostra:
      soma = soma + 1 / e
      mediaH = qtdElementos / soma
    return(mediaH)
print(  "media aritmética harmônica:", round(mediaHarmonica(amostra), 2))

def mediaGeometrica(amostra):
  qtdElementos = len(amostra)
  mult = 1
  for e in amostra:
    mult = mult * e
    mediaG = pow(mult, 1 / qtdElementos)
  return(mediaG)
print(  "media aritmética geométrica:", round(mediaGeometrica(amostra), 2))

# b) Moda;

def moda(amostra):
  a = list()
  for e in amostra:
    a.append(amostra.count(e))
    indice = a.index(max(a))
    mod = amostra[indice]
  return(mod)

print("b) moda:", moda(amostra))

# c) Mediana;

def mediana(amostra):
  qtdElementos = len(amostra)
  amostra.sort()
  if qtdElementos % 2 == 0:
    pos1 = (qtdElementos / 2) - 1
    pos2 = qtdElementos / 2
    med = (amostra[int(pos1)] + amostra[int(pos2)]) / 2
  else:
    pos = (qtdElementos - 1) / 2
    med = amostra[int(pos)]
  return(med)

print("c) mediana:", mediana(amostra))

# d) Variância;

def variancia(amostra):
  qtdElementos = len(amostra)
  soma = 0
  for e in amostra:
    soma = soma + pow(e - mediaSimples(amostra), 2)
    var = soma / qtdElementos
  return (var) 

print("d) variância:", round(variancia(amostra), 2))

# e) Desvio padrão;

def desvioPadrao(amostra):
  return pow(variancia(amostra), 1/2)

print("e) desvio padrão:", round(desvioPadrao(amostra), 2))
