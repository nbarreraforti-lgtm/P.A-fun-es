def Fatorial(Num):
    if Num == 0:
        return 1
    else:
        return Num * Fatorial(Num - 1)

Num = 0

Num = int(input("Digite um número: "))

print(f"O fatorial de {Num} é {Fatorial(Num)}")