#Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$

hora = float(input("Quanto você ganha por hora? "))

horasTrabalhadas = float(input("Quantas horas você trabalha por mês? "))
salarioBruto = hora * horasTrabalhadas
descontoIr = salarioBruto * 0.11
descontoInss = salarioBruto * 0.08
descontoSindicato = salarioBruto * 00.5
desconto = descontoInss + descontoSindicato + descontoIr

salarioLiquido = salarioBruto - desconto

print(f"Seu salário bruto é: {salarioBruto}")
print(f"O desconto do inss é: {descontoInss}")
print(f"O desconto do sindicato é: {descontoSindicato}")
print(f"O desconto do IR é: {descontoIr}")
print(f"O salario líquido é de {salarioLiquido}")


