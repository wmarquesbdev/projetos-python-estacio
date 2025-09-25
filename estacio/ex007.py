def calcular_area_triangulo(base, altura):
  return base * altura
  
try:
  base_usuario = float(input('Digite a base do triângulo: '))
  altura_usuario = float(input('Digite a altura do triângulo: '))
  
  area = calcular_area_triangulo(base_usuario, altura_usuario)

  print(f'Área do triângulo: {area}')

except ValueError:
  print('Erro: Número digitado inválido.')