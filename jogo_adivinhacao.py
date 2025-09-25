import random

numero_secreto = random.randint(1, 100)
palpite = None

while palpite != numero_secreto:
  palpite = int(input('tente adivinhar o número secreto: '))
  if palpite < numero_secreto:
    print('O número secreto é MAIOR.')
  elif palpite > numero_secreto:
    print('O número secreto é MENOR.')

print(f'Você acertou, o número secreto é {numero_secreto}')