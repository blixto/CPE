VOGAIS = "aeiou"
palavra = input("Digite uma palavra de até 5 letras: ")
palavra = palavra[0:5].lower()
contagem = 0
if len(palavra) > 0 and palavra[0] in VOGAIS:
  contagem += 1
if len(palavra) > 1 and palavra[1] in VOGAIS:
  contagem += 1
if len(palavra) > 2 and palavra[2] in VOGAIS:
  contagem += 1
if len(palavra) > 3 and palavra[3] in VOGAIS:
  contagem += 1
if len(palavra) > 4 and palavra[4] in VOGAIS:
  contagem += 1
print(f"Existem {contagem} vogais na palavra '{palavra}'.")