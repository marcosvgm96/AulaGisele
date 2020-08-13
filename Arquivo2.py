numerointeiro = int(input("Digite um numero entre 1 e 5: "))
if numerointeiro < 1:
    print("Numero invalido!")
elif numerointeiro > 5:
    print("Numero invalido!")
else:
    if numerointeiro == 1:
        print("UM")
    elif numerointeiro == 2:
        print("DOIS")
    elif numerointeiro == 3:
        print("TRES")
    elif numerointeiro == 4:
        print("QUATRO")
    else:
        print("CINCO")