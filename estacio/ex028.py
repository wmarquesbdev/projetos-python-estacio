num_int1 = int(input("Digite o 1º número inteiro: "))
num_int2 = int(input("Digite o 2º número inteiro: "))
num_real = float(input("Digite o 3º número (real): "))

calculo_a = (2 * num_int1) * (num_int2 / 2)
calculo_b = (3 * num_int1) + num_real
calculo_c = num_real ** 3

print(f"a) O produto do dobro do primeiro com metade do segundo é: {calculo_a}")
print(f"b) A soma do triplo do primeiro com o terceiro é: {calculo_b}")
print(f"c) O terceiro número elevado ao cubo é: {calculo_c:.2f}")