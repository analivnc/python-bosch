#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
# sabendo que a decisão é sempre pelo mais barato:

produto1 = float(input('Qual é o preço do produto 1? '))
produto2 = float(input('Qual é o preço do produto 2? '))
produto3 = float(input('Qual é o preço do produto 3? '))

produtoBarato = produto1 

if produto2 < produtoBarato:
    produtoBarato = produto2
if produto3 < produtoBarato:
    produtoBarato = produto3

print(f"O produto que você deve comprar é: {produtoBarato}")





