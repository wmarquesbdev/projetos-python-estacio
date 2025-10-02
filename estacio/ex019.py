lado1 = float(input('Digite o 1° lado do Triângulo: '))
lado2 = float(input('Digite o 2° lado do Triângulo: '))
lado3 = float(input('Digite o 3° lado do Triângulo: '))

if lado1 == lado2 and lado2 == lado3:
  print('O triângulo é equilátero.')
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
  print('O triângulo é isóceles.')
else:
  print('O triângulo é escaleno.')