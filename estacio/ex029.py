altura = float(input("Digite sua altura em metros (ex: 1.75): "))
sexo = input("Digite seu sexo ('M' para Homem ou 'F' para Mulher): ")

if sexo.upper().startswith('M'):
  peso_ideal = (72.7 * altura) - 58
  print(f"\nPara um homem com {altura:.2f}m de altura, o peso ideal é: {peso_ideal:.2f} kg.")
elif sexo.upper().startswith('F'):
  peso_ideal = (62.1 * altura) - 44.7
  print(f"\nPara uma mulher com {altura:.2f}m de altura, o peso ideal é: {peso_ideal:.2f} kg.")
else:
  print("\nErro: Opção de sexo inválida. Por favor, digite 'M' ou 'F'.")