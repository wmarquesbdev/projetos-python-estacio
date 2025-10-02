cardapio = {
    100: {"nome": "Cachorro Quente", "preco": 11.20},
    101: {"nome": "Ovo Simples",     "preco": 8.30},
    102: {"nome": "Bauru com Ovo",   "preco": 11.50},
    103: {"nome": "Hambúrguer",      "preco": 16.20},
    201: {"nome": "Refrigerante",    "preco": 6.00},
    202: {"nome": "Suco",            "preco": 7.50},
    203: {"nome": "Água Mineral",    "preco": 4.70}
}

print("="*45)
print("         CARDÁPIO LANCHONETE BURGÃO")
print("="*45)

for codigo, info in cardapio.items():
  print(f"{info['nome']:<18} | Código: {codigo} | Preço: R$ {info['preco']:.2f}")
print("="*45)

codigo_sanduiche = int(input("Digite o código do sanduíche: "))
codigo_bebida = int(input("Digite o código da bebida: "))

item_sanduiche = cardapio[codigo_sanduiche]
item_bebida = cardapio[codigo_bebida]

valor_total = item_sanduiche['preco'] + item_bebida['preco']

print("\n--- Resumo do Pedido ---")
print(f"Sanduíche: {item_sanduiche['nome']} - R$ {item_sanduiche['preco']:.2f}")
print(f"Bebida:    {item_bebida['nome']} - R$ {item_bebida['preco']:.2f}")
print("--------------------------")
print(f"TOTAL A PAGAR: R$ {valor_total:.2f}")