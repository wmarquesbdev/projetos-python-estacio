dias_por_mes = 30

dia = int(input("Digite o dia (1 a 30): "))
mes = int(input("Digite o mês (1 a 12): "))

if not (1 <= dia <= 30):
  print("\nErro: O dia informado é inválido. Por favor, digite um número entre 1 e 30.")
elif not (1 <= mes <= 12):
  print("\nErro: O mês informado é inválido. Por favor, digite um número entre 1 e 12.")
else:
  dias_passados = (mes - 1) * dias_por_mes + dia

  print(f"Considerando meses de 30 dias e ignorando anos bissextos:")
  print(f"Desde o início do ano até a data {dia:02d}/{mes:02d}, se passaram {dias_passados} dias.")