def calculo_aumento_salario(salario_atual, percentual_aumento):
  valor_do_aumento = salario_atual * (percentual_aumento / 100)
  novo_salario = salario_atual + valor_do_aumento
  return novo_salario, valor_do_aumento

try:
  salario_usuario = float(input('Digite o salário atual: R$ '))

  if salario_usuario <= 280:
    percentual_usuario = 20
  elif salario_usuario <= 700:
    percentual_usuario = 15
  elif salario_usuario <= 1500:
    percentual_usuario = 10
  else:
    percentual_usuario = 5

  salario_final, valor_aumento_calculado = calculo_aumento_salario(salario_usuario, percentual_usuario)

  resultado = (f'''
  Salário antes do reajuste: R${salario_usuario:.2f}
  Percentual de aumento: {percentual_usuario}%
  Valor do aumento: {valor_aumento_calculado:.2f}
  Novo salário: {salario_final}
  ''')

  print(resultado)
  
except ValueError:
  print('Erro: Número digitado inválido.')