
Nota, Nota1, Nota2 = 0.0, 0.0, 0.0

def mediaf(Nota, Nota1, Nota2, Criterio):
    if Criterio == "A":
        media = (Nota + Nota1 + Nota2) / 3
    elif Criterio == "B":
        media = (Nota*2 + Nota1*3 + Nota2*5) / 10
    return media

Nota = int(input("Digite a primeira nota: "))
Nota1 = int(input("Digite a segunda nota: "))
Nota2 = int(input("Digite a terceira nota: "))

Criterio = str(input("Digite A ou B para o cálculo da média: "))

media = mediaf(Nota, Nota1, Nota2, Criterio)
print("A média é: ", media)