print("CALCULADORA FINANCEIRA")

salario = float(input("Digite seu salário: "))
aluguel = float(input("Digite valor do aluguel: "))
internet = float(input("Digite valor da internet: "))
mercado = float(input("Digite valor do mercado: "))
agua = float(input("Digite valor do água: "))
luz = float(input("Digite valor da luz: "))

total_despesas = aluguel + internet + mercado + agua + luz

saldo = salario - total_despesas

print("\nRESULTADO")
print("----------------")

print(f"Salário: R$ {salario}")
print(f"Despesas: R$ {total_despesas}")
print(f"Saldo final: R$ {saldo}")


if saldo > 1000:
    print("Excelente")
elif saldo >= 500:
    print("Bom")
else:
    print("Precisa melhorar")

percentual = (saldo / salario) * 100
print(f"Percentual do saldo em relação ao salário: {percentual:.2f}%")
