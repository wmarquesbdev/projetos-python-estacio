n1 = float(input('Digite o número 1: '))
n2 = float(input('Digite o número 2: '))
n3 = float(input('Digite o número 3: '))

n = [n1, n2, n3]

maior = max(n)
menor = min(n)

resultado = (f'''
Números: {n}
Maior: {maior}
Menor: {menor}
''')

print(resultado)