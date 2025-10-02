custo_anel_chip = 4.00
custo_anel_alimento = 3.50
qtd_aneis_alimento = 2

quantidade_frangos = int(input('Digite a quantidade total de frangos na granja: '))

if quantidade_frangos < 0:
  print('A quantidade de frangos não pode ser menos que zero.')
else:
  custo_por_frango = custo_anel_chip + (qtd_aneis_alimento * custo_anel_alimento)
  gasto_total = custo_por_frango * quantidade_frangos
  
  print(f'Quantidade de frangos: {quantidade_frangos}')
  print(f'Custo para marcar um frango: R$ {custo_por_frango:.2f}')
  print(f'Gato total da granja: R$ {gasto_total:.2f}')