def calcular_media(*notas):
  return sum(notas) / len(notas) # Soma das notas dividido pela quantidade de itens

try:
  nome_aluno = input('Digite seu nome: ')
  nome_disciplina = input('Digite a disciplina: ')
  
  notas_aluno = []
  for i in range(4):
    nota = float(input(f'Digite a nota {i+1}: '))
    notas_aluno.append(nota)
    
  media_final = calcular_media(*notas_aluno)
  
  resultado = (f'''
Nome: {nome_aluno}
Disciplina: {nome_disciplina}
Notas: {notas_aluno}
Média: {media_final}
''')
  
  print(resultado)
  
except ValueError:
  print('Erro: Número digitado inválido.')