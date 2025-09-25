letraDigitada = input('Qual é seu sexo? ').upper()

if letraDigitada == 'M':
  sexo = 'Masculino'
elif letraDigitada == 'F':
  sexo = 'Feminino'
else:
  print('Sexo inválido.')
  
print(f'Seu sexo é {sexo}')