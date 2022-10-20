# 3 - Os dados em rol relacionados a seguir referm-se a produção diária de leite de vacas da raça holandesa obtidas em duas ordenhas, em kg:
# Calcule o coeficiênte de variação dos dados:

rol = [4.0, 4.5, 5.0, 5.0, 5.0, 5.5, 6.0, 6.0, 6.5, 6.5, 6.5, 6.5, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.5, 8.5, 9.0, 9.0, 9.0, 9.5, 10.0, 10.0, 10.5, 10.5, 11.0, 12.0, 12.5, 13.0, 13.0]

def mediaSimples(rol):
  qtdElementos = len(rol)
  soma = 0
  for e in rol:
    soma = soma + e
    mediaS = soma / qtdElementos
  return mediaS
#print("MS =", mediaSimples(rol))
def desvioPadrao(rol):
  qtdElementos = len(rol)
  soma = 0
  for e in rol:
    soma = soma + pow(e - mediaSimples(rol), 2)
    desvio = soma / qtdElementos
  return pow(desvio, 1/2)
#print("DP =", desvioPadrao(rol))
def coeficienteDeVariacao(rol):
  return(desvioPadrao(rol)/mediaSimples(rol)) * 100
        
print("CV =", round(coeficienteDeVariacao(rol), 2),"%")
