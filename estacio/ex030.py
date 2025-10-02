limite_peso_kg = 50.0
valor_multa_por_kg = 4.00

peso = float(input("Digite o peso total de peixes (em kg): "))

if peso < 0:
  print("\nErro: O peso não pode ser um número negativo.")
else:
  excesso = 0.0
  multa = 0.0
  
  if peso > limite_peso_kg:
    excesso = peso - limite_peso_kg
    multa = excesso * valor_multa_por_kg

  print(f"Peso total informado: {peso:.2f} kg")
  print(f"Limite de peso regulamentado: {limite_peso_kg:.2f} kg")
  print(f"Peso excedente: {excesso:.2f} kg")
  print(f"Valor da multa a ser paga: R$ {multa:.2f}")