def Testepar(Num):
    if Num % 2 == 0:
        return True
    else:
        return False

Num = 0

Num = int(input("Digite um número: "))

modulo = Testepar(Num)

if modulo == False:
    print("O número digitado é ímpar.")
else:
    print("O número digitado é par.")