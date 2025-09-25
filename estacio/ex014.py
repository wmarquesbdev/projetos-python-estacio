def calculo_saldo_atual(saldo, debito, credito):
  return saldo - debito + credito

try:
  numero_conta = input('Digite o número da conta: ')
  saldo_usuario = float(input('Digite o saldo: '))
  debito_usuario = float(input('Digite o valor de saque: '))
  credito_usuario = float(input('Digite o valor de depósito: '))
  
  saldo_atual = calculo_saldo_atual(saldo_usuario, debito_usuario, credito_usuario) 
  
  situacao_saldo = 'Positivo' if saldo_atual >= 0 else 'Negativo'
  
  resultado = (f'''
Conta: {numero_conta}
Saldo anterior: {saldo_usuario}
Valor de saque: {debito_usuario}
Valor de depósito: {credito_usuario}
Saldo atual: {saldo_atual}
Situação: Saldo {situacao_saldo}            
''')
  
  print(resultado)
  
except ValueError:
  print('Erro: Número digitado inválido.')