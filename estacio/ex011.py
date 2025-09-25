nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

if idade <= 2:
  tipo = 'Bebê'
elif idade <= 11:
  tipo = 'Criança'
elif idade <= 21:
  tipo = 'Jovem'
elif idade <= 64:
  tipo = 'Adulto'
elif idade <= 100:
  tipo = 'Idoso'
else:
  tipo = 'Mumia'
  
resultado = (f'''
Nome: {nome}
Idade: {idade} anos
Tipo: {tipo}
''')

print(resultado)