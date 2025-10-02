preco_pao = 1.00
preco_broa = 3.50
percentual_poupanca = 0.10

qtd_paes = int(input("Digite a quantidade de pães franceses vendidos: "))
qtd_broas = int(input("Digite a quantidade de broas vendidas: "))

if qtd_paes < 0 or qtd_broas < 0:
  print("\nErro: As quantidades não podem ser números negativos.")
else:
  total_arrecadado_paes = qtd_paes * preco_pao
  total_arrecadado_broas = qtd_broas * preco_broa
  total_geral = total_arrecadado_paes + total_arrecadado_broas

  valor_poupanca = total_geral * percentual_poupanca

  print(f"Total arrecadado com a venda de pães: R$ {total_arrecadado_paes:.2f}")
  print(f"Total arrecadado com a venda de broas: R$ {total_arrecadado_broas:.2f}")
  print(f"TOTAL ARRECADADO (PÃES + BROAS): R$ {total_geral:.2f}")
  print(f"VALOR A GUARDAR NA POUPANÇA (10%): R$ {valor_poupanca:.2f}")