num, num1, num2 = 0,0,0

def Nmaior(num, num1, num2):
    if num > num1 and num > num2:
        indice =1
    elif num1 > num and num1 > num2:
        indice = 2
    elif num2 > num and num2 > num1:
        indice = 3
    return indice

num = int(input("Digite o primeiro número: "))
num1 = int(input("Digite o segundo número: "))
num2 = int(input("Digite o terceiro número: "))

num_maior = Nmaior(num, num1, num2)

if num_maior == 1:
    print(f"O maior número é: {num}")
elif num_maior == 2:
    print(f"O maior número é: {num1}")  
elif num_maior == 3:
    print(f"O maior número é: {num2}")
