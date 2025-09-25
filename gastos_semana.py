gastos_da_semana = [25.50, 40.00, 15.75, 80.00, 35.20, 110.00, 5.00]

total_gasto = sum(gastos_da_semana) # Soma todos os valores da lista (gastos_da_semana)

numero_de_dias = len(gastos_da_semana) # Conta quantos itens existem na lista (gastos_da_semana)

media_de_gastos_diarios = total_gasto / numero_de_dias # Divide o total pela quantidade de itens

resultados = (f'''
Lista de gastos da semana: {gastos_da_semana}
Total de gastos: R${total_gasto}
Número de dias: {numero_de_dias}
Gastos por dia: R${media_de_gastos_diarios:.2f}
''')

print(resultados)