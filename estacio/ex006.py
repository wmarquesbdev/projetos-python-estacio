def calcular_area_retangulo(base, altura):
  return base * altura

try:
  base_usuario = float(input('Digite a base do retângulo: '))
  altura_usuario = float(input('Digite a altura do retângulo: '))

  area = calcular_area_retangulo(base_usuario, altura_usuario)

  print(f'Área do retângulo: {area}')

except ValueError:
  print('Erro: Número digitado inválido.')