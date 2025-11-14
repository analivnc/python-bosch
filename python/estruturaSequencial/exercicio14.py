#João, um pescador, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
#Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento 
#de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
#João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
#Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
#Imprima os dados do programa com as mensagens adequadas.

peso = float(input("Digite o peso: "))

limite = 50

if peso > limite:
    excesso = peso - limite
    multa = excesso * 4
    print("Você excedeu o limite de pesca.")
    print("Excesso:", excesso, "kg")
    print("Multa a pagar: R$", multa)
else:
    excesso = 0
    multa = 0
    print("Dentro do limite, sem multa.")



    







