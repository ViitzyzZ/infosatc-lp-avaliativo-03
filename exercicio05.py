#Exercício 5.
idadeMediaH = 0 #nao funcionol sem declarar 
idadeMediaM = 0
mediaGrupo = 0
H = 0
F = 0

for x in range(10):
    while(True):
        sexo    = (str(input("Digite o sexo da pessoa (masculino ou feminino):")))
        idade   = (int(input("Digite a idade da pessoa:")))
        if sexo.lower() == ("masculino"):
            idadeMediaH += idade
            mediaGrupo  += idade
            H += 1
            break
        elif sexo.lower() == ("feminino"):
            idadeMediaM += idade
            mediaGrupo  += idade
            F += 1
            break

if idadeMediaH > 0: print("A idade média dos homens foi:",idadeMediaH / H)
if idadeMediaM > 0: print("A idade média das mulheres foi:",idadeMediaM / F)
if mediaGrupo > 0:  print("A idade média do grupo foi:",mediaGrupo / (H + F))