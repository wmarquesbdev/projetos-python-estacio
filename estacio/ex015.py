sexo_usuario = input('Digite seu sexo: ').upper()
  
feminino = ['F', 'FEMININO', 'MULHER', 'FEMEA']
masculino = ['M', 'MASCULINO', 'HOMEM', 'MACHO']
  
if sexo_usuario in feminino:
  situacao = 'Feminino'
elif sexo_usuario in masculino:
  situacao = 'Masculino'
else:
  situacao = 'Sexo inválido'
    
resultado = (f'''
Você é do sexo: {situacao}
''')
  
print(resultado)