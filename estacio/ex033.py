def analisar_numero(numero):
  if numero > 0:
    prop_pos_neg = "Positivo"
  elif numero < 0:
    prop_pos_neg = "Negativo"
  else:
    prop_pos_neg = "Neutro (Zero)"

  if numero % 1 == 0:
    prop_int_dec = "Inteiro"

    if numero % 2 == 0:
      prop_par_impar = "Par"
    else:
      prop_par_impar = "Ímpar"
  else:
    prop_int_dec = "Decimal"
    prop_par_impar = "Não se aplica (é decimal)"
     
  return prop_par_impar, prop_pos_neg, prop_int_dec

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("\nEscolha a operação que deseja realizar:")
print("  +  para Adição")
print("  -  para Subtração")
print("  * para Multiplicação")
print("  /  para Divisão")
operacao = input("Digite o símbolo da operação: ")

resultado = 0
calculo_valido = True

if operacao == '+':
  resultado = num1 + num2
elif operacao == '-':
  resultado = num1 - num2
elif operacao == '*':
  resultado = num1 * num2
elif operacao == '/':
  if num2 != 0:
    resultado = num1 / num2
  else:
    print("\nErro: Não é possível dividir por zero.")
    calculo_valido = False
else:
  print("\nErro: Operação inválida. Escolha um dos símbolos: +, -, *, /")
  calculo_valido = False

if calculo_valido:
  propriedades = analisar_numero(resultado)

  print(f"O resultado da operação é: {resultado}")
  print(f" -> O número é: {propriedades[0]} (Par ou Ímpar)")
  print(f" -> O número é: {propriedades[1]} (Positivo ou Negativo)")
  print(f" -> O número é: {propriedades[2]} (Inteiro ou Decimal)")
