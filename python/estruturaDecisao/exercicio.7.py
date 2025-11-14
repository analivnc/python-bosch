#Faça um programa que leia três números e mostre o maior e o menor deles:
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o primeiro número: '))
num3 = int(input('Digite o primeiro número: '))

maior = num1
menor = num1

if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3

if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

print(f'O número maior é: {maior}')
print(f'O número menor é: {menor}')
