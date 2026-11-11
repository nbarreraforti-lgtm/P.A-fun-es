def Rsalario(salario,filhos):
    if salario < 1000:
        salario = salario + (salario * 0.09)
    elif salario >= 1000 and salario <= 3000:
        salario = salario + (salario*0.07)
    elif salario > 3000:
        salario = salario + (salario*0.05)

    if filhos < 3:
        salario = salario + (salario*0.01)
    elif filhos > 3:
        salario = salario + (salario*0.02)

    return salario

salario, filhos = 0.0,0

salario = float(input("Digite o salário do funcionário: "))
filhos = int(input("Digite o número de filhos do funcionário: "))

Fsalario = Rsalario(salario,filhos)

print("O salário do funcionário após o reajuste é: R$",Fsalario)