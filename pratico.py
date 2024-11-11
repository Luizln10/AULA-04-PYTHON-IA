listaValores = []

def soma(valor):
  total1 = 0
  for valores in valor:
    total1 += valores
  print(f"A soma é {total1}")
def sub(valor):
  total2 = 0
  for valores in valor:
    total2 += valores
    print(f"A subtração é {total2}")
def mult(valor):
  total3 = 0
  for valores in valor:
    total3 += valores
    print(f"A multiplicação é {total3}")
def div(valor):
  total4 = 0
  for valores in valor:
    total4 += valores
    print(f"A divisão é {total4}")
numeros = input("Digite um número:")
for num in numeros.split():
  try:
    listaValores.append(float(num))
  except:
    print("ERRO")
soma(listaValores)