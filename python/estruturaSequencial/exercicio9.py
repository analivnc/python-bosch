# Faça um programa que peça a temperatura em graus Fahrenheit,
#  transforme e mostre a temperatura em graus Celsius. Fórmula: C = 5 * ((F-32) / 9)

fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
celcius = 5 * fahrenheit - 32 / 9

print(f"A conversão é {celcius}")
