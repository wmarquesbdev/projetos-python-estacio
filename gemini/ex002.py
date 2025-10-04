numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros_pares = []
numeros_impares = []

for numero_par in numeros:
  if numero_par % 2 == 0:
    numeros_pares.append(numero_par)

for numero_impar in numeros:
  if numero_impar % 2 != 0:
    numeros_impares.append(numero_impar)

texto_dos_numeros_pares = ', '.join(str(n) for n in numeros_pares)
texto_dos_numeros_impares = ', '.join(str(n) for n in numeros_impares)

print(f'Lista: {numeros}')
print(f'Númros pares: {texto_dos_numeros_pares}')
print(f'Númros pares: {texto_dos_numeros_impares}')