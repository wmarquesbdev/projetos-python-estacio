preco_litro_alcool = 1.90
preco_litro_gasolina = 2.50

litros_vendidos = float(input("Digite a quantidade de litros vendidos: "))
tipo_combustivel = input("Digite o tipo de combustível (A para Álcool, G para Gasolina): ")

valor_a_pagar = 0
dados_validos = True

if litros_vendidos <= 0:
  print("\nErro: A quantidade de litros deve ser maior que zero.")
  dados_validos = False
  
tipo_formatado = tipo_combustivel.strip().upper()

if tipo_formatado == 'A':
  preco_bruto = litros_vendidos * preco_litro_alcool
  if litros_vendidos <= 20:
    desconto = 0.03
  else:
    desconto = 0.05
    valor_a_pagar = preco_bruto * (1 - desconto)
elif tipo_formatado == 'G':
    preco_bruto = litros_vendidos * preco_litro_gasolina
    if litros_vendidos <= 20:
      desconto = 0.04
    else:
      desconto = 0.06
      valor_a_pagar = preco_bruto * (1 - desconto)
else:
    print("\nErro: Tipo de combustível inválido. Por favor, use 'A' ou 'G'.")
    dados_validos = False

if dados_validos:
    print(f"\nO valor total a ser pago pelo cliente é: R$ {valor_a_pagar:.2f}")