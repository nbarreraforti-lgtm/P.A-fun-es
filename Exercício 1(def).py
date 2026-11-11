def Rsalario(salario,porcentagem):
    reajuste = (((salario*porcentagem)/100)+salario)
    if reajuste < 1400:
        indice = 1
    elif reajuste >= 1400 and reajuste <= 1800:
        indice = 2
    elif reajuste > 1800:
        indice = 3
    return(reajuste, indice)

salario,porcentagem,indice,reajuste = 0.0,0.0,0.0,0.0
while True:
    salario = float(input("Digite o salário, ou para sair, tecle 1: "))
    if salario == 1:
        break
    porcentagem = float(input("Digite a porcentagem para o cálculo do reajuste: "))
    reajuste, indice = Rsalario(salario, porcentagem)

    if indice == 1:
            print(f"R${reajuste} está abaixo da média, dentro da faixa {indice}.")
    elif indice == 2:
            print(f"R${reajuste} está na média, dentro da faixa {indice}.")
    elif indice == 3:
            print(f"R${reajuste} está acima da média, dentro da faixa {indice}.")
    