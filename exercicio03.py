#Exercício
mes = { 
    1:"Mês de Janeiro",
    2:"Mês de Fevereiro",
    3:"Mês de Março",
    4:"Mês de Abril",
    5:"Mês de Maio",
    6:"Mês de Junho",
    7:"Mês de Julho",
    8:"Mês de Agosto",
    9:"Mês de Setembro",
    10:"Mês de Outubro",
    11:"Mês de Novembro",
    12:"Mês de Dezembro",
}
while(True):
    numeroMes = (int(input("Digite o número do mês: ")))
    if numeroMes in mes:
        print(mes[numeroMes])
        break
    else:
        print("Número digitado inexistente")