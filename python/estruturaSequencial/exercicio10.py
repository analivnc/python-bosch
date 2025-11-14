#Faça um programa que peça a temperatura em graus Celsius,
#transforme e mostre em graus Fahrenheit. Fórmula: F = (C * 9/5) + 32

celcius = float(input("Digite a temperatura: "))
fahrenheit =  celcius * 9/5 + 32

print(f"A conversão é de: {fahrenheit}")