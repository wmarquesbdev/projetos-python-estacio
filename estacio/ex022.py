percentual_desconto = 0.10

preco_original = float(input('Digite o preço do produto: R$ '))

valor_desconto = preco_original * percentual_desconto
novo_preco = preco_original - valor_desconto

print(f'Preço original: R$ {preco_original:.2f}')
print(f'Valor do desconto: R$ {valor_desconto:.2f}')
print(f'Novo preço com desconto: R$ {novo_preco:.2f}')