def vparcela(valor, parcela):

    Vparcela = valor / parcela
   
    if parcela == 1:
        Vvalor = valor - (valor * 0.05)
    elif parcela == 2:
        Vvalor = valor + (valor * 0.01)
    elif parcela == 3:
        Vvalor = valor + (valor * 0.045)
    elif parcela == 4:
        Vvalor = valor + (valor * 0.075)
    elif parcela == 5:
        Vvalor = valor + (valor * 0.10)

    Valor_final = Vvalor / parcela

    return Valor_final
valor, parcela = 0.0,0.0

valor = float(input("Digite o valor do produto: "))
parcela = float(input("Digite o valor da parcela: "))

Valor_final = vparcela(valor, parcela)

print(f"O valor da parcela é: {Valor_final}")