inicio = int(input('Digite um número inteiro: '))
fim = int(input('Digite outro número inteiro: '))

numeros = []

for contador in range(min(inicio, fim) + 1, max(inicio, fim)):
	numeros.append(contador)
 
print(numeros)