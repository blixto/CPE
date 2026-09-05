numero = int(input("Informe um número inteiro: "))
print(f"{numero} é ", end="")
if numero != 0:
  if numero > 0:
    print("positivo e ", end="")
  else:
    print("negativo e ", end="")
  if abs(numero) % 2 == 0:
    print("par")
  else:
    print("ímpar")
else:
  print("zero")