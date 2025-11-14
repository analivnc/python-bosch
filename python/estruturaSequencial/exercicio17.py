#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
#  Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
#  que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor.
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
import math
area = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))

#latas
litroLata = 18
valorLata = 80
pinturaTotalLata = 108

#galoes

livroGalao = 3.6
pinturadosGaloes = 21.6
valorGalao = 25

areaFolga = area + (area * (10/100))

#calculo lata
calculoLata = areaFolga / pinturaTotalLata
quantidadeLatas = math.ceil(calculoLata)
valorFinal = valorLata * quantidadeLatas
print(f"Você precisa de {quantidadeLatas} latas e o preço é de {valorFinal} reais")

#calculo galões
calculoGalao = areaFolga / pinturadosGaloes
quantidadeGaloes = math.ceil(calculoGalao)
valorFinalGalao = valorGalao * quantidadeGaloes
print(f"Você precisa de {quantidadeGaloes} latas e o preço é de {valorFinalGalao} reais")

#Calculo Latas e Galoes
lataInteira = areaFolga // pinturaTotalLata
resto = areaFolga % pinturaTotalLata
galoesCobrir = math.ceil(resto/ pinturadosGaloes)

precoFinal = (lataInteira * 80) + (galoesCobrir * valorGalao)
print(f"Você precisa de {lataInteira} latas, {galoesCobrir} galões para o resto e o preço total será: {precoFinal}")

































