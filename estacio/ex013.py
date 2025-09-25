numero = float(input('Digite um número: '))

if numero%2==0:
  situacao = 'Par'
else:
  situacao = 'Ímpar'

resultado = (f'''
O número {numero} é: {situacao}
''')
  
print(resultado)