FMULT = 2.0

salarioBase = float(input("Digite seu salário-base mensal [R$]: "))
vendas = float(input("Digite o total bruto de suas vendas no mês [R$]: "))
comiss = float(input("Digite o percentual de comissão sobre as vendas: "))
hrExtras = float(input("Digite o total de horas extras no mês: "))
diasEfetivos = float(input("Digite o número de dias efetivamente trabalhados no mês: "))
hrNominais = float(input("Digite o número de horas nominais de trabalho por dia: "))
imposto = float(input("Digite a alíquota de imposto retido na fonte (sobre o salário-base): "))

# 1. Calcular a parcela de horas extras
# 1.1 Valor da hora extra
valHrExtra = (salarioBase / (hrNominais * diasEfetivos)) * FMULT

# 1.2 Total devido pelas horas extras
totalHrExtra = valHrExtra * hrExtras

# 2. Calcular a parcela de comissão
valComiss = (comiss / 100) * vendas

# 3. Calcular o salário bruto
salarioBruto = salarioBase + totalHrExtra + valComiss
print("-" * 30)
print(f"Comissão: R$ {valComiss:.2f}")
print(f"Horas extras: R$ {totalHrExtra:.2f}")
print(f"Salário bruto: R$ {salarioBruto:.2f}")

# 4. Calcular o imposto retido na fonte
impostoRetido = (imposto / 100) * salarioBase

# 5. Calcular o salári líquido
salarioLiq = salarioBruto - impostoRetido

print(f"Imposto retido na fonte: R$ {impostoRetido:.2f}")
print(f"Salário líquido: R$ {salarioLiq:.2f}")