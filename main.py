from math import *
import numpy as np

v = 3 * 10**8

print("Escolha uma opção de entrada: ")

print("[1] - Amplitude de Campo Eletrico\n[2] - Amplitude do Campo Magnetico\n[3] - Intensidade da Onda Magnetica\n")
print("[4] - Frequencia\n[5] - Comprimento da onda\n[6] - Numero de onda\n[7] - Frequencia Angular\n")
opcao = int(input("Digite a opção desejada: "))
if opcao < 1 or opcao > 7:
  print("Opção invalida")

if opcao == 1:
  amplitude_eletrico = float(input("Digite a amplitude do campo eletrico[V/m]: "))
  amplitude_magnetico = amplitude_eletrico/v
  print(f"A amplitude do campo magnetico é {np.format_float_scientific(np.float32(amplitude_magnetico), precision=3)}T")
  intensidade_onda_magnetica = (amplitude_eletrico * amplitude_eletrico)/(2 * (0.0000004 * pi))
  print(f"A intensidade da onda magnetica é {np.format_float_scientific(np.float32(intensidade_onda_magnetica), precision=3)} W/mˆ2")

if opcao == 2:
  amplitude_magnetico = float(input("Digite a amplitude do campo magnetico[T]: "))
  amplitude_eletrico = amplitude_magnetico * v
  print(f"A amplitude do campo eletrico é {np.format_float_scientific(np.float32(amplitude_eletrico), precision=3)}V/m")
  intensidade_onda_magnetica = (amplitude_eletrico * amplitude_eletrico)/(2 * (0.0000004 * pi))
  print(f"A intensidade da onda magnetica é {np.format_float_scientific(np.float32(intensidade_onda_magnetica), precision=3)} W/mˆ2")

if opcao == 3:
  intensidade_onda_magnetica = float(input("Digite a intensidade da onda magnetica[W/mˆ2]: "))
  amplitude_eletrico = sqrt(2 * (intensidade_onda_magnetica * (0.0000004 * pi)))
  print(f"A amplitude do campo eletrico é {np.format_float_scientific(np.float32(amplitude_eletrico), precision=3)}V/m")
  amplitude_magnetico = amplitude_eletrico/v
  print(f"A amplitude do campo magnetico é {np.format_float_scientific(np.float32(amplitude_magnetico), precision=3)}T")

if opcao == 4:
  frequencia = float(input("Digite a frequencia [Hz]: "))
  frequencia_angular = frequencia * (2 * pi)
  print(f"A frequencia angular é: {np.format_float_scientific(np.float32(frequencia_angular), precision=3)} rad/s")
  comprimento_onda = v / frequencia
  print(f"O comprimento de onda é: {np.format_float_scientific(np.float32(comprimento_onda), precision=3)} m")
  numero_onda = (2 * pi) / comprimento_onda
  print(f"O numero de onda é: {np.format_float_scientific(np.float32(numero_onda), precision=3)} rad/m")

if opcao == 5:
  comprimento_onda = float(input("Digite o comprimento de onda [m]: "))
  numero_onda = (2 * pi) / comprimento_onda
  print(f"O numero de onda é: {np.format_float_scientific(np.float32(numero_onda), precision=3)} rad/m")
  frequencia = v / comprimento_onda
  print(f"A frequencia é: {np.format_float_scientific(np.float32(frequencia), precision=3)} Hz")
  frequencia_angular = frequencia * (2 * pi)
  print(f"A frequencia angular é: {np.format_float_scientific(np.float32(frequencia_angular), precision=3)} rad/s")

if opcao == 6:
  numero_onda = float(input("Digite o numero de onda [rad/m]: "))
  comprimento_onda = (2 * pi)/numero_onda
  print("Comprimento de onda: %.4f m\n", np.format_float_scientific(np.float32(comprimento_onda), precision=3))
  frequencia = v / comprimento_onda
  print("Frequencia: %.4f Hz\n", np.format_float_scientific(np.float32(frequencia), precision=3))
  frequencia_angular = frequencia * (2 * pi)
  print("Frequencia angular: %.4f rad/s\n", np.format_float_scientific(np.float32(frequencia_angular), precision=3))

if opcao == 7:
  frequencia_angular = float(input("Digite a frequencia angular [rad/s]: "))
  frequencia = frequencia_angular / (2 * pi)
  print("Frequencia: %.4f Hz\n", np.format_float_scientific(np.float32(frenquecia), precision=3))
  comprimento_onda = v / frequencia
  print("Comprimento de onda: %.4f m\n", np.format_float_scientific(np.float32(comprimento_onda), precision=3))
  numero_onda = (2 * pi) / comprimento_onda
  print("Numero de onda: %.4f rad/m\n", np.format_float_scientific(np.float32(numero_onda), precision=3))
