#Faça um programa que leia três números e mostre-os em ordem decrescente:
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o primeiro número: '))
num3 = int(input('Digite o primeiro número: '))

numerosOrdemDecrescente = [num1, num2, num3]

numerosOrdemDecrescente.sort(reverse=True) #função que imprime números em ordem decrescente

print(f"Números em ordem de decrescente{numerosOrdemDecrescente}")