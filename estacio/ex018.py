def calcular_folha_pagamento():
  valor_hora = float(input('Digite o valor que ganha por hora de trabalho: R$'))
  horas_trabalhadas = float(input('Digite a quantidade de horas trabalhadas no mês: '))

  salario_bruto = valor_hora * horas_trabalhadas
  
  if salario_bruto <= 900:
    percentual_ir = 0
  elif salario_bruto <= 1500:
    percentual_ir = 5
  elif salario_bruto <= 2500:
    percentual_ir = 10
  else:
    percentual_ir = 20
  
  valor_ir = salario_bruto * (percentual_ir / 100)
  valor_sindicato = salario_bruto * 0.03
  valor_fgts = salario_bruto * 0.11
  total_descontos = valor_ir + valor_sindicato
  salario_liquido = salario_bruto - total_descontos
  
  print(f'Salário Bruto: {salario_bruto:.2f}')
  print(f'(-) IR ({percentual_ir}%): R${valor_ir:.2f}')
  print(f'(-) Sindicato (3%): R${valor_sindicato:.2F}')
  print(f'FGTS (11%): R${valor_fgts:.2f}')
  print(f'Total de descontos: R${total_descontos:.2f}')
  print(f'Salário Líquido: R$:{salario_liquido:.2f}')

calcular_folha_pagamento()