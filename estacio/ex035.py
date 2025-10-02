def gerar_cupom(tipo_carne, qtd_kg, preco_total, tipo_pagamento, valor_desconto, valor_a_pagar):
    print("\n" + "="*40)
    print("      HIPERMERCADO TABAJARA - CUPOM FISCAL      ")
    print("="*40)
    print(f"Tipo da Carne:         {tipo_carne}")
    print(f"Quantidade:            {qtd_kg:.3f} Kg")
    print(f"Preço Total Bruto:     R$ {preco_total:.2f}")
    print("-" * 40)
    print(f"Tipo de Pagamento:     {tipo_pagamento}")
    print(f"Valor do Desconto:     R$ {valor_desconto:.2f}")
    print("-" * 40)
    print(f"VALOR A PAGAR:         R$ {valor_a_pagar:.2f}")
    print("="*40)
    print("           Volte Sempre!            ")
    print("="*40)


print("--- PROMOÇÃO DE CARNES TABAJARA ---")
print("1 - Filé Duplo")
print("2 - Alcatra")
print("3 - Picanha")

escolha_carne = input("Digite o número correspondente ao tipo de carne: ")
quantidade_kg = float(input("Digite a quantidade em Kg que deseja comprar: "))
usa_cartao_tabajara = input("A compra será feita com o Cartão Tabajara? (S/N): ")

nome_carne = ""
preco_por_kg = 0
dados_validos = True

if escolha_carne == '1':
  nome_carne = "Filé Duplo"
  if quantidade_kg <= 5:
    preco_por_kg = 34.90
  else:
    preco_por_kg = 35.80
elif escolha_carne == '2':
  nome_carne = "Alcatra"
  if quantidade_kg <= 5:
    preco_por_kg = 44.90
  else:
    preco_por_kg = 46.80
elif escolha_carne == '3':
  nome_carne = "Picanha"
  if quantidade_kg <= 5:
    preco_por_kg = 66.90
  else:
    preco_por_kg = 67.80
else:
  print("\nErro: Opção de carne inválida.")
  dados_validos = False

if quantidade_kg <= 0:
  print("\nErro: A quantidade de carne deve ser maior que zero.")
  dados_validos = False

if dados_validos:
  preco_total_bruto = quantidade_kg * preco_por_kg
  valor_desconto_final = 0.0
  tipo_pagamento_texto = "Outro"

  if usa_cartao_tabajara.strip().upper().startswith('S'):
    tipo_pagamento_texto = "Cartão Tabajara"
    valor_desconto_final = preco_total_bruto * 0.05
    
  valor_final_a_pagar = preco_total_bruto - valor_desconto_final
  gerar_cupom(nome_carne, quantidade_kg, preco_total_bruto, tipo_pagamento_texto, valor_desconto_final, valor_final_a_pagar)