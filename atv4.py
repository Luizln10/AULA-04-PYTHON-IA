n1 = float(input("Digite o primeiro número:"))
n2 = float(input("Digite o segundo número:"))

def subtração(n1, n2):
  sub = n1 - n2
  print(f"A subtração será {sub}")
  return subtração
subtração(n1, n2)