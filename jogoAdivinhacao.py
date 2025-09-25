import random

numeroSecreto = random.randint(1, 100)
palpite = None

while palpite != numeroSecreto:
  palpite = int(input('tente adivinhar o número secreto: '))
  if palpite < numeroSecreto:
    print('O número secreto é MAIOR.')
  elif palpite > numeroSecreto:
    print('O número secreto é MENOR.')

print(f'Você acertou, o número secreto é {numeroSecreto}')