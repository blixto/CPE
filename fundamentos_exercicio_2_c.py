print("Digite os tamanhos dos lados do triângulo...")
a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))
if a + b > c and a + c > b and b + c > a:
  s = (a+b+c)/2
  A = (s*(s-a)*(s-b)*(s-c))**0.5
  print(f"Os lados informados formam um triângulo de área {A}.")
else:
  print("É impossível formar um triângulo com os lados informados.")