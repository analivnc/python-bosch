#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

import math
tamanhoMetros = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))

coberturaLitro = 3
capacidadeLata = 18
precoLata = 80

litrosNec = tamanhoMetros / coberturaLitro

latasnec = math.ceil(litrosNec / capacidadeLata) #arredonda pra cima

precoTotal = latasnec * precoLata

print(f"A area a ser pintada é: {tamanhoMetros}")
print(f"Quantidade de tinta: : {litrosNec:.2f}")
print(f"A quantidade de latas: {latasnec}")
print(f"O preço total é: {precoTotal}")





