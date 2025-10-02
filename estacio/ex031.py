turno = input("Em que turno você estuda? Digite M-matutino, V-vespertino ou N-noturno: ")

turno_formatado = turno.upper()

if turno_formatado == 'M':
    print("Bom Dia!")
elif turno_formatado == 'V':
    print("Boa Tarde!")
elif turno_formatado == 'N':
    print("Boa Noite!")
else:
    print("Valor Inválido!")