def calcular_media(*notas):
  return sum(notas) / len(notas)

try:
  nome_aluno = input('Digite seu nome: ')
  nome_disciplina = input('Digite a disciplina: ')
  
  notas_aluno = [float(input(f'Digite a nota {i+1}: ')) for i in range(3)]
  
  media_final = calcular_media(*notas_aluno)
  
  situacao_aluno = 'Aprovado' if media_final >= 6.0 else 'Reprovado'
  
  resultado = (f'''
Nome: {nome_aluno}
Notas: {notas_aluno}
Média: {media_final}
Situação: {situacao_aluno}
''')
  
  print(resultado)
  
except ValueError:
  print('Erro: Número digitado inválido.')