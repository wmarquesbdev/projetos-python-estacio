def contar_vogais(frase): 
  contador = 0
  
  vogais = 'aeiou'
  
  for letra in frase.lower():
    if letra in vogais:
      contador += 1
  
  return contador
  
frase_usuario = input('Digite uma frase: ')
total_vogais = contar_vogais(frase_usuario)

print(f'A frase {frase_usuario} tem {total_vogais} vogais.')