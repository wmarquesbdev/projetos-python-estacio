peso_fatia_queijo = 50
peso_fatia_presunto = 50
peso_hamburguer = 100

qtd_fatias_queijo = 2
qtd_fatias_presunto = 1
qtd_hamburguer = 1

gramas_por_quilo = 1000

qtd_sanduiches = int(input('Digite a quantidade de sanduíches a fazer: '))

if qtd_sanduiches < 0:
  print('Erro: A quantidade de sanduíches não pode ser menor que zero.')
else:
  total_gramas_queijo = (qtd_fatias_queijo * peso_fatia_queijo) * qtd_sanduiches
  total_gramas_presunto = (qtd_fatias_presunto * peso_fatia_presunto) * qtd_sanduiches
  total_gramas_carne = (qtd_hamburguer * peso_hamburguer) * qtd_sanduiches
  
  total_kg_queijo = total_gramas_queijo / gramas_por_quilo
  total_kg_presunto = total_gramas_presunto / gramas_por_quilo
  total_kg_carne = total_gramas_carne / gramas_por_quilo
  
  print(f'Para fazer {qtd_sanduiches} sanduíche(s), você precisará de:')
  print(f'Queijo: {total_kg_queijo:.3f} kg')
  print(f'Presunto: {total_kg_presunto:.3f} kg')
  print(f'Carne (Hambúrguer): {total_kg_carne:.3f} kg')