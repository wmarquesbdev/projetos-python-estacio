nomeUsuario = input('Qual é o nome de usuário? ')
idadeUsuario = int(input('Qual é a idade? '))

if idadeUsuario <= 2:
  tipo = 'Bebê'
elif idadeUsuario <= 11:
  tipo = 'Criança'
elif idadeUsuario <= 21:
  tipo = 'Jovem'
elif idadeUsuario <= 64:
  tipo = 'Adulto'
elif idadeUsuario <= 100:
  tipo = 'Idoso'
else:
  tipo = 'Mumia'
  
print(f'{nomeUsuario} está com {idadeUsuario} e pela tabela é considerado um {tipo}')