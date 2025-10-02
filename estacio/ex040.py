salario_joao = 1200.00
conta_1 = 200.00
conta_2 = 120.00
percentual_multa = 0.02

multa_c1 = conta_1 * percentual_multa
total_conta_1 = conta_1 + multa_c1

multa_c2 = conta_2 * percentual_multa
total_conta_2 = conta_2 + multa_c2

total_a_pagar = total_conta_1 + total_conta_2

salario_restante = salario_joao - total_a_pagar

print("--- Extrato Financeiro de João ---")
print(f"Salário Bruto: R$ {salario_joao:.2f}")
print("-" * 35)
print("Despesas com multa (2%):")
print(f"  - Conta 1: R$ {conta_1:.2f} + R$ {multa_c1:.2f} (multa) = R$ {total_conta_1:.2f}")
print(f"  - Conta 2: R$ {conta_2:.2f} + R$ {multa_c2:.2f} (multa) = R$ {total_conta_2:.2f}")
print("-" * 35)
print(f"Total a Pagar: R$ {total_a_pagar:.2f}")
print("=" * 35)
print(f"SALÁRIO RESTANTE: R$ {salario_restante:.2f}")
print("=" * 35)