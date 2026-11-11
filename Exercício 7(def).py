def Testenum(Num):
    if Num < 0:
        return False
    else:
        return True

Num = 0

Num = int(input("Digite um número: "))

modulo = Testenum(Num)

if modulo == False:
    print("O número digitado é negativo.")
else:
    print("O número digitado é positivo.")