#Faça um programa que verifique se uma letra digitada é vogal ou consoante.
letra = (input("Digite uma letra para saber se é vogal ou consoante: "))

if letra in 'aeiou': #Se a letra estiver dentro da sequência ‘aeiou’, então é uma vogal.
    print('É uma vogal')
else:
    print('É uma consoante')
