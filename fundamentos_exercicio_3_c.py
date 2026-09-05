# Caso de teste:
# SOCORRAM ME SUBI NO ON IBUS EM MARROCOS
frase = input("Digite uma frase: ")
frase.lower()
inverso = frase[::-1]
if frase == inverso:
  print("A frase inserida é palíndroma.")
else:
  print("A frase inserida não é palíndroma.")