def calcular_nota(nota1, nota2, nota3, nota4, media):
  if media >= 6.0:
    return 'Aprovado'
  elif media >= 5.0:
    return 'de Recuperação'
  else:
    return 'Reprovado'
  
  return (nota1 + nota2 + nota3 + nota4) / 4

try:
  nome_aluno = input('Digite o nome do aluno: ')
  n1 = float(input('Digite a nota 1: '))
  n2 = float(input('Digite a nota 2: '))
  n3 = float(input('Digite a nota 3: '))
  n4 = float(input('Digite a nota 4: '))

  media = calcular_nota(n1, n2, n3, n4)
  
  print(f'{nome_aluno}, sua média foi de {media} e você está {situacao}.')
  
except ValueError:
  print('Erro: Número digitado inválido.')