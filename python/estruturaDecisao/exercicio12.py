#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
#  que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
#  mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR: - Salário Bruto até 900 (inclusive) - isento - Salário Bruto até 1500 (inclusive)
#  - desconto de 5% - Salário Bruto até 2500 (inclusive) - desconto de 10% - Salário Bruto acima de 2500 - desconto de 20%
#Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#Salário Bruto: (5 * 220)        : R$ 1100,00
#(-) IR (5%)                     : R$   55,00
#(-) INSS ( 10%)                 : R$  110,00
#FGTS (11%)                      : R$  121,00
#Total de descontos              : R$  165,00
#Salário Liquido                 : R$  935,00

valorHora = int(input('Qual é o valor da sua hora?  '))
quantidadeHoraTrabalhadaMes = int(input('Qual a quantidade de horas que você trabalha no mês? '))
 
salarioBruto = valorHora * quantidadeHoraTrabalhadaMes
sindicato = salarioBruto * 0.03
ir = 0
inss = salarioBruto * 0.10
fgts = salarioBruto * 0.11



if salarioBruto <= 900:
    ir = 0
elif salarioBruto <= 1500:
    ir = salarioBruto * 0.05
elif salarioBruto <= 2500:
    ir = salarioBruto * 0.10
else: ir = salarioBruto * 0.20

totalDesconto = inss + sindicato + ir
salarioLiquido = salarioBruto - totalDesconto



print(f"O salário bruto é de: {salarioBruto}")
print(f"Ir: {ir}")
print(f'inss: {inss}')
print(f'fgts: {fgts}')
print(f'O total de desconto é: {totalDesconto}')
print(f'O salário liquido é de {salarioLiquido}')

