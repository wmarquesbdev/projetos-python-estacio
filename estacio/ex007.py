def calcular_area_triangulo(base, altura):
  return base * altura

try:
  base_triangulo = float(input('Digite a base do triângulo: '))
  altura_triangulo = float(input('Digite a altura do triângulo: '))
  
  area_triangulo = calcular_area_triangulo(base_triangulo, altura_triangulo)
  
  resultado = (f'''
Base: {base_triangulo}
Altura: {altura_triangulo}
Área: {area_triangulo}
''')
  
  print(resultado)
  
except ValueError:
  print('Erro: Número digitado inválido.')