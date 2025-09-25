numero = float(input('Digite um número: '))

if numero > 10:
  situacao_numero = 'Maior que 10'
elif numero < 10:
  situacao_numero = 'Menor que 10'
else:
  situacao_numero = 'Igual a 10'
  
resultado = (f'''
O número {numero} é: {situacao_numero}
''')

print(resultado)