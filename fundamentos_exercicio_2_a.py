'''
v1>v2>v3
v1>v3>v2
v2>v1>v3
v2>v3>v1
v3>v1>v2
v3>v2>v1
'''

v1 = int(input("Digite um valor: "))
v2 = int(input("Digite um valor: "))
v3 = int(input("Digite um valor: "))
if v1 > v2 and v2 > v3:
  print(f"Maior: {v1}\nMeio: {v2}")
elif v1 > v3 and v3 > v2:
  print(f"Maior: {v1}\nMeio: {v3}")
elif v2 > v1 and v1 > v3:
  print(f"Maior: {v2}\nMeio: {v1}")
elif v2 > v3 and v3 > v1:
  print(f"Maior: {v2}\nMeio: {v3}")
elif v3 > v1 and v1 > v2:
  print(f"Maior: {v3}\nMeio: {v1}")
elif v3 > v2 and v2 > v1:
  print(f"Maior: {v3}\nMeio: {v2}")
else:
  pass
