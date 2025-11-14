import random

print("Jogo de Adivinhação da Ana Li!")
print("Tente adivinhar o jogo")

repetir = True
continuar = "s"
numTentativas = 0
numero_secreto = random.randint(1, 50)


while(repetir):

    palpite = int(input("Seu palpite: "))


    if palpite > numero_secreto:
        numTentativas += 1
        print("Muito alto! Tente um numero menor")
    elif palpite < numero_secreto:
        print("Muito baixo! Tente um numero maior")
        numTentativas += 1
    else:
        numTentativas += 1
        print("Você acertou<3! Em", numTentativas, "tentativas")
        continuar = input("Quer jogar novamente? s/n ")
        if (continuar == "s"): 
            numTentativas = 0
            numero_secreto = random.randint(1, 50)
            continue
        elif (continuar != "s"):
            print("Obrigada por jogar")
            break



