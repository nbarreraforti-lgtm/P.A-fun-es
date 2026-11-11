def Cnadador(Idade):
    if Idade < 5:
        Categoria = "Não permitido"
    if Idade >= 5 and Idade <= 7:
        Categoria = "Infantil A"
    elif Idade >= 8 and Idade <= 10:
        Categoria = "Infantil B"
    elif Idade >= 11 and Idade <= 13:
        Categoria = "Juvenil A"
    elif Idade >= 14 and Idade <= 17:
        Categoria = "Juvenil B"
    elif Idade >= 18:
        Categoria = "Adulto"
    return Idade, Categoria

Idade = 0
Categoria = ""

Idade = int(input("Digite a idade do nadador: "))

Idade, Categoria = Cnadador(Idade)
if Categoria == "Não permitido":
    print("O nadador não é permitido na competição.")
    
if Categoria != "Não permitido":
    print(f"O nadador tem {Idade} anos e pertence a categoria {Categoria}.")