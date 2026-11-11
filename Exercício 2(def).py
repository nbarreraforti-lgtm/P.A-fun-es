
N1, N2, N3, indice = 0.0,0.0,0.0,0.0

def Fmedia(N1,N2,N3):
    media = (N1+N2*2+N3*3)/6
    if media >= 9:
        indice = 1
    elif media >= 7.5 and media < 9:
        indice = 2
    elif media >= 6 and media < 7.5:
        indice = 3
    elif media >= 4 and media < 6:
        indice = 4
    elif media < 4:
        indice = 5
    return(media,indice)
    

N1 = float(input("Digite a primeira nota: "))
N2 = float(input("Digite a segunda nota: "))
N3 = float(input("Digite a terceira nota: "))

media, indice = Fmedia(N1,N2,N3)

if indice == 1:
    print(f"O aluno apresentou a média {media} e está no conceito A")

elif indice == 2:
    print(f"O aluno apresentou a média {media} e está no conceito B")

elif indice == 3:
    print(f"O aluno apresentou a média {media} e está no conceito C")

elif indice == 4:
    print(f"O aluno apresentou a média {media} e está no conceito D")

elif indice == 5:
    print(f"O aluno apresentou a média {media} e está no conceito E")
