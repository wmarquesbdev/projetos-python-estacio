def calcular_nota():
  nota = int(input('Digite sua nota (0 a 100): '))
  
  if nota >= 90:
    nota_aluno = 'A'
  elif nota >= 80:
    nota_aluno = 'B'
  elif nota >= 70:
    nota_aluno = 'C'
  elif nota >= 60:
    nota_aluno = 'D'
  else:
    nota_aluno = 'F'
  
  print(f'Sua nota é: {nota_aluno}')

calcular_nota()