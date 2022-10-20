# Disciplina: Probabilidade e Estatística
# Aluno: Cristina Andrade de Faria - MAT: 2224290068
# Lista 3


# 1 - Uma amostra de gaúchos foi investigada em relação ao consumo de sal diário.Escreva em python uma lista com os valores mostrados acima e calcule:

amostra = [10, 13, 17, 9, 8, 11, 13, 7]

# a) Média aritmética simples;

def mediaSimples(amostra):                    
  qtdElementos = len(amostra)
  soma = 0
  for e in amostra:
    soma = soma + e
  mediaS = soma / qtdElementos
  return(mediaS)

print("a)", round(mediaSimples(amostra), 2))

# b) Média harmônica;

def mediaHarmonica(amostra):
  qtdElementos = len(amostra)
  soma = 0
  for e in amostra:
    soma = soma + 1 / e
  mediaH = qtdElementos / soma
  return(mediaH)

print("b)", round(mediaHarmonica(amostra), 2))

# c) Média geométrica;

def mediaGeometrica(amostra):
  qtdElementos = len(amostra)
  mult = 1
  for e in amostra:
    mult = mult * e
    media = pow(mult, 1 / qtdElementos)
  return(media)

print("c)", round(mediaGeometrica(amostra), 2))

# d) Moda;

def moda(amostra):
  a = list()
  for e in amostra:
    a.append(amostra.count(e))
    indice = a.index(max(a))
    mod = amostra[indice]
  return(mod)

print("d)", moda(amostra))

# e) Variância;

def variancia(amostra):
  qtdElementos = len(amostra)
  soma = 0
  for e in amostra:
   soma = soma + pow(e - mediaSimples(amostra), 2)
   var = soma / qtdElementos   
  return (var)

print("e)", variancia(amostra))

# f) Desvio padrão;

def desvioPadrao(amostra):
  return pow(variancia(amostra), 1 / 2)

print("f)", round(desvioPadrao(amostra), 2))
