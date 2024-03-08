from math import *

print("Escolha uma opção de entrada: ")

print("[1] - Amplitude de Campo Eletrico\n[2] - Amplitude do Campo Magnetico\n[3] - Intensidade da Onda Magnetica\n")
print("[4] - Frequencia\n[5] - Comprimento da onda\n[6] - Numero de onda\n[7] - Frequencia Angular\n")
opcao = int(input("Digite a opção desejada: "))
if opcao < 1 or opcao > 7:
  print("Opção invalida")

if opcao == 6: 
  numero_onda = float(input("Digite o numero de onda [rad/m]: "))
  comprimento_onda = (2 * pi)/numero_onda
  print("Comprimento de onda: %.2f m\n", comprimento_onda)


