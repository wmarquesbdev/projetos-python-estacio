def calcular_custo_viagem(distancia, consumo_medio, preco_combustivel):
  if consumo_medio <= 0:
    return None
  
  litros_necessarios = distancia / consumo_medio
  custo_total = litros_necessarios * preco_combustivel
  
  return custo_total

try:
  distancia_viagem = float(input('Digite a distância total da viagem (em km): '))
  consumo_veiculo = float(input('Digite o consumo médio do carro (km por litro): '))
  preco_litro = float(input('Digite o preço do litro do combustível (R$): '))
  
  custo_final = calcular_custo_viagem(distancia_viagem, consumo_veiculo, preco_litro)
  
  if custo_final is not None:
    print(f'Para uma viagem de {distancia_viagem} km: ')
    print(f'O custo estimado apenas com combustível será de: R$ {custo_final:.2f}')
  else:
    print('Erro: O consumo do veículo deve ser maior que zero.')

except ValueError:
  print('Erro: Número digitado inválido.')