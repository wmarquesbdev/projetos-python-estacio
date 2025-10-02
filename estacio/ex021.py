percentual_comissao = 0.04

salario_fixo = float(input('Digite o valor do salário fixo: R$ '))
valor_vendas = float(input('Digite o valor total de vendas: R$ '))

valor_comissao = valor_vendas * percentual_comissao

salario_final = salario_fixo + valor_comissao

print(f'Valor da comissão: R$ {valor_comissao:.2f}')
print(f'Salário final: R$ {salario_final:.2f}')