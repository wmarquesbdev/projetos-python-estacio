preco_pequena = 10.00
preco_media = 12.00
preco_grande = 15.00

qtd_pequenas = int(input('Digite a quantidade de camisetas PEQUENAS: '))
qtd_medias = int(input('Digite a quantidade de camisetas MÉDIAS: '))
qtd_grandes = int(input('Digite a quantidade de camisetas GRANDES: '))

if qtd_pequenas < 0 or qtd_pequenas < 0 or qtd_grandes < 0:
  print('Erro: A quantidade de camisetas não pode ser menor que zero.')
else:
  total_pequenas = qtd_pequenas * preco_pequena
  total_medias = qtd_medias * preco_media
  total_grandes = qtd_grandes * preco_grande
  
  valor_total_compra = total_pequenas + total_medias + total_grandes
  
  print(f'Camisetas pequenas: {qtd_pequenas} x R$ {preco_pequena:.2f} = R$ {total_pequenas:.2f}')
  print(f'Camisetas médias: {qtd_medias} x R$ {preco_media:.2f} = R$ {total_medias:.2f}')
  print(f'Camisetas grandes: {qtd_grandes} x R$ {preco_grande:.2f} = R$ {total_grandes:.2f}')
  print(f'Valor total da compra: {valor_total_compra:.2f}')