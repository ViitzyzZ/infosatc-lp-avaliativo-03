idadeDoador = 0
pesoDoador = 0
horasDormidas =0

idade = (int(input("Digite a sua idade: ")))
peso = (float(input("Digite o seu peso: ")))
hora = (int(input("Informe quantas horas dormiu na noite passada: ")))

if idade >= 16 and idade <= 69:
    idadeDoador += 1
else:
    print("Idade fora dos requisitos!")

if peso > 50:
    pesoDoador += 1
else:
    print("Peso fora dos requisitos!")

if hora >= 6:
    horasDormidas += 1
else:
    print("Horas de sono fora dos requisitos!")

if idadeDoador == 1 and pesoDoador == 1 and horasDormidas == 1:
    print("Você atende os requisitos para ser um doador!")
else:
    print("Você não atende os requisitos para ser um doador.")