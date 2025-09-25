numero = float(input('Digite um número: '))

if numero >= 0:
  situacao = 'Positivo'
else:
  situacao = 'Negativo'

resultado = (f'''
O número {numero} é: {situacao}
''')

print(resultado)