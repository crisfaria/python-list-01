# 6 - Escreva em Python um algoritmo que solicite para o usuário inserir 3 notas de um aluno (entre 0 e 10)
#O programa deve calcular a média ponderada com os pesos 3, 4 e 3 para as 3 notas recebidas.

notas = []
pesos = []

qtdNotas = int(input("DIGITE A QUANTIDADE DE NOTAS: "))

for i in range(qtdNotas):
  nota = float(input("Digite a nota #" + str(i + 1) + ": "))
  peso = float(input("Digite o peso #" + str(i + 1) + ": "))

  notas.append(nota)
  pesos.append(peso)

somatorioPesos = 0

for p in (pesos):
  somatorioPesos += p

somatorioNotas = 0

for index, n in enumerate(notas):
  somatorioNotas += n * pesos[index]
  mediaPonderada = somatorioNotas / somatorioPesos

print("A Média Ponderada:", round(mediaPonderada, 2))
