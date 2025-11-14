#Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:
#O produto do dobro do primeiro com metade do segundo.
#A soma do triplo do primeiro com o terceiro.
#O terceiro elevado ao cubo.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

produto = num1 * 2 * (num2/ 2)
print(f"O dobro do primeiro com a metade do segundo é {produto}")

triplo = num1 * 3 + (num3/ 3)
print(f"O triplo o primeiro com o terceiro é {triplo}")

terceiro = num3 ** 3  #** potencição
print(f"O terceiro elevado ao cubo é {terceiro}")




