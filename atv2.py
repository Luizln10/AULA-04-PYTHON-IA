horario = int(input("Digite as horas:"))

def saudacao(horario):
  if horario >= 6 and horario <= 12:
    print("Bom dia!")
  elif horario > 12 and horario <= 18:
    print("Boa tarde!")
  elif horario > 18 and horario <= 5:
    print("Boa noite!")
  else:
    print("ERRO")
  return saudacao
saudacao(horario)