#Faça um programa que leia um número e exiba o dia correspondente da semana.
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido

diaDaSemana = int(input("Digite um número para cada dia da semana: 1-Domingo 2-Segunda 3-Terça 4-Quarta 5-Quinta 6- Sábado: "))

if diaDaSemana == 1:
    print("Domingo")
elif diaDaSemana == 2:
    print("Segunda")
elif diaDaSemana == 3:
    print("Terça")
elif diaDaSemana == 4:
    print("Quarta")
elif diaDaSemana == 5:
    print("Quinta")
elif diaDaSemana == 6:
    print("Sexta")
elif diaDaSemana == 7:
    print("Sábado")
