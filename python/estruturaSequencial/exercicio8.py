#Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês.

hora = float(input("Quanto você ganha por hora? "))
horasTrabalhadas = float(input("Quantas horas você trabalha por mês? "))

resultado = hora * horasTrabalhadas

print(f"O total do seu salário é de {resultado}")