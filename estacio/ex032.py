
print("=" * 30)
print("     CAIXA ELETRÔNICO     ")
print("=" * 30)
print("Notas disponíveis: R$ 1, 5, 10, 50, 100")
print("Limite de saque: Mínimo R$ 10 e Máximo R$ 600\n")

valor_saque = int(input("Digite o valor que deseja sacar: R$ "))

if 10 <= valor_saque <= 600:
  print(f"\nCalculando a distribuição de notas para R$ {valor_saque}...\n")

  valor_restante = valor_saque
  
  notas_100 = valor_restante // 100
  valor_restante %= 100

  notas_50 = valor_restante // 50
  valor_restante %= 50

  notas_10 = valor_restante // 10
  valor_restante %= 10

  notas_5 = valor_restante // 5
  valor_restante %= 5

  notas_1 = valor_restante

  print("Você receberá:")
  
  if notas_100 > 0:
    print(f"-> {notas_100} nota(s) de R$ 100")
  if notas_50 > 0:
    print(f"-> {notas_50} nota(s) de R$ 50")
  if notas_10 > 0:
    print(f"-> {notas_10} nota(s) de R$ 10")
  if notas_5 > 0:
    print(f"-> {notas_5} nota(s) de R$ 5")
  if notas_1 > 0:
    print(f"-> {notas_1} nota(s) de R$ 1")

else:
  print("\nValor inválido! O saque deve ser entre R$ 10,00 e R$ 600,00.")