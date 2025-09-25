def calcular_custo_viagem(distancia, consumo_medio, preco_combustivel):
  litros_necessarios = distancia / consumo_medio
  custo_total = litros_necessarios * preco_combustivel
  
  return custo_total

try:
  distancia_viagem = float(input('Digite a distância total da viagem (em km): '))
  consumo_veiculo = float(input('Digite o consumo médio do carro (km por litro): '))
  preco_litro = float(input('Digite o preço do litro do combustível (R$): '))
  
  custo_final = calcular_custo_viagem(distancia_viagem, consumo_veiculo, preco_litro)
  
  resultado = (f'''
Distância: {distancia_viagem}km
Custo estimado do combustível: {custo_final:.2f}
''')
  
  print(resultado)

except ValueError:
  print('Erro: Número digitado inválido.')