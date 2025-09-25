numeroConta = float(input('Digite o número da conta do cliente: '))
saldoCliente = float(input('Qual é o saldo? '))
debitoCliente = float(input('Qual é o valor de deposito? '))
creditoCliente = float(input('Qual é o valor de saque? '))

saldoAtual = saldoCliente + debitoCliente - creditoCliente

if saldoAtual >= 0:
  print(f'Seu saldo: R${saldoAtual} é negativo.')
else:
  print(f'Seu saldo: R${saldoAtual} é positivo.')