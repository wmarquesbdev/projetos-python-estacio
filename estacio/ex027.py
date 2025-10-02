import random

total_alunos = 50

alunas_altas = 0

total_alunos_masculinos = 0
alunos_masculinos_status_bom = 0

for i in range(total_alunos):
  matricula = i + 1
  sexo = random.choice(['M', 'F'])
  altura = random.randint(150, 195)
  status_fisico = random.randint(1, 3)
  
  if sexo == 'F' and altura > 170:
    alunas_altas += 1
    
  if sexo == 'M':
    total_alunos_masculinos += 1
    if status_fisico == 1:
      alunos_masculinos_status_bom += 1

if total_alunos_masculinos > 0:
  percentual_masc_bom = (alunos_masculinos_status_bom / total_alunos_masculinos) * 100
else:
  percentual_masc_bom = 0

print(f'a) Quantidade de alunas do sexo feminino com altura superior a 170 cm: {alunas_altas}')

print(f'- Total de alunos do sexo masculino: {total_alunos_masculinos}')
print(f'- Alunos masculino com status "bom": {alunos_masculinos_status_bom}')
print(f'b) Percentual de alunos do sexo masculino com status "bom": {percentual_masc_bom:.2f}%')