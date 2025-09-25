def calcular_area_retangulo(base, altura):
  return base * altura

try:
  base_retangulo = float(input('Digite a base do retângulo: '))
  altura_retangulo = float(input('Digite a altura do retângulo: '))
  
  area_retangulo = calcular_area_retangulo(base_retangulo, altura_retangulo)
  
  resultado = (f'''
Base: {base_retangulo}
Altura: {altura_retangulo}
Área: {area_retangulo}
''')
  
  print(resultado)

except ValueError:
  print('Erro: Número digitado inválido.')