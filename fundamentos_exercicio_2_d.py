km = float(input("Distância (km): "))
TX_MIN = 30
DESC = 5/100
if km <= 0:
  print("Distância inválida")
elif km <= 50:
  total = TX_MIN+km*1.75
elif km <= 150:
  total = TX_MIN+50*1.75+(km-50)*1.65
else:
  total = TX_MIN+50*1.75+100*1.65+(km-150)*1.50
if km > 0:
  if km > 300:
    total -= total*DESC
  medio = total/km
  print(f"Total: R$ {total:.2f}")
  print(f"Médio: R$ {medio:.2f}/km")