# 5 - Escreva em Python um algoritmo que solicite para o usuário inserir notas de alunos entre 0 e 10 em um loop infinito com condição de
#parada uma nota igual a -999. A cada iteração valide que a nota seja entre 0 e 10 e solicite uma nota correta em caso de erro.
#Após obter todas as notas, o programa deve mostrar:

#notasteste = [1, 3, 9, 4, 1, 2, 5, 9, 9]

notas = []

# Função Média Aritmética Simples
def calculoMediaSimples(notas):
  qtdElementos = len(notas)
  soma = 0
  for x in notas:
    soma = soma + float(x)
    media = soma/qtdElementos
  return media 
#print("média s:", round(mediasimples(notas), 2))

# Função Média Harmônica
def calculoMediaHarmonica(notas):
  qtdeElementos = len(notas)
  somaI = 0
  for x in notas:
    somaI = somaI + 1/float(x)
    media =  qtdeElementos/somaI
  return media
#print("media h:", round(mediaharmonica(notas), 2))

# Função Média Geométrica
def calculoMediaGeometrica(notas):
  qtdElementos = len(notas)
  elemento = 1
  for x in notas:
    elemento = elemento * float(x)
    media = pow(elemento, 1/qtdElementos)
  return media
#print("media g:", round(mediageometrica(notas), 2))

# Função da Moda
def calculoModa(notas):
  elemento = list()
  for x in notas:
    elemento.append(notas.count(float(x)))
    indice = elemento.index(max(elemento))
    moda = notas[indice]
  return moda
#print("moda", moda(notas))

# Função para Variância
def calculoVariancia(notas):
  qtdElementos = len(notas)
  elemento = 0
  for x in notas:
    elemento = elemento + pow(float(x) - calculoMediaSimples(notas), 2)
    variancia = elemento/qtdElementos
  return variancia
#print("variancia", round(variancia(notas), 2))

# Função de Desvio Padrão
def calculoDesvioPadrao(notas):
  return pow(calculoVariancia(notas), 1/2)
#print("desvio padrao", round(desviopadrao(notas), 2))

# Função de Coeficiente da Variância
def calculoCoeficienteDeVariancia(notas):
  return (calculoDesvioPadrao(notas)/calculoMediaSimples(notas)) * 100
#print("coeficiente de variancia", round(coeficientedevariancia(notas), 2))


while (True):
  entrada = input('DIGITE UMA NOTA VÁLIDA:')
  
  if (entrada == "-999"):
    break

  if (float(entrada) >= 0 and float(entrada) <= 10):
    notas.append(entrada)
  else:
    print("NOTA INVÁLIDA")

print("Notas Válidas:", notas)


print("MEDIA SIMPLES:", (round(calculoMediaSimples(notas), 2)))
print("MÉDIA HARMÔNICA:", (round(calculoMediaHarmonica(notas), 2)))
print("MÉDIA GEOMÉTRICA:", (round(calculoMediaGeometrica(notas), 2)))
print("MODA:", (calculoModa(notas)))
print("VARIÂNCIA:", (round(calculoVariancia(notas), 2)))
print("DESVIO PADRÃO:", (round(calculoDesvioPadrao(notas), 2)))
print("COEFICIENTE DE VARIÂNCIA:", (round(calculoCoeficienteDeVariancia(notas), 2)))
