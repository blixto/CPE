p = input("Digite um texto: ")
q = input("Digite um texto: ")
if p.lower() in q.lower():
  print(f"'{p}' está contido em '{q}'")
else:
  print(f"'{p}' não está contido em '{q}'")