#Faça um programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

ano = int(input("Informe um número correspondente a um ano: "))

if (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)): #% → pega o resto da divisão
    print("É um ano bissexto")
else:
    print("Não é bissexto") 