preco_por_quilo = 59.00

peso_do_prato_kg = float(input("Digite o peso do prato em quilos (ex: 0.550): "))

if peso_do_prato_kg >= 0:
  valor_a_pagar = peso_do_prato_kg * preco_por_quilo

  print(f"Peso do prato: {peso_do_prato_kg:.3f} kg")
  print(f"Valor a pagar: R$ {valor_a_pagar:.2f}")
else:
  print("\nErro: O peso do prato não pode ser um número negativo.")
