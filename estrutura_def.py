# A função def é como uma "receita" ou "ferramenta" que você cria para usar depois.
# Ela fica guardada esperando para ser chamada.

def verificar_maioridade(idade):
  if idade >= 18:
    return True
  else:
    return False

try:
  idade_usuario = int(input('Digite sua idade:'))
  
  maior = verificar_maioridade(idade_usuario)
  
  if maior == True:
    print('Você é de maior.')
  else:
    print('Você é de menor.')

except ValueError:
  print('Erro: Número digitado inválido.')