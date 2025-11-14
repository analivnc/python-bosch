#int - números inteiros Ex: 7, -4, 0, 9827

#float - números reais. Ex: 4.5, 0.76, -15.2

#bool - booleano. valores lógicos. ex: True ou False

#str - conjunto de caracteres. ex 'Olá mundo'

n1 = int(input('Digite um numero: '))
n2  = int(input('Digite um numero: '))
soma = n1 + n2
print(f'A soma {n1} e {n2} vale {soma}' ) 


n1 = input('Digite um numero: ')
print(n1.isnumeric())

n1 = input('Digite algo: ')
print(n1.isalpha())


n1 = input('Digite algo: ')
print(n1.isalnum())

n1 = input('Digite algo: ')
print(n1.isspace())
#espaços

n1 = ' '.isspace()
print(n1)

n1 = input('Digite algo: ')
print(n1.isupper())


n1 = input('Digite algo: ')
print(n1.islower())

n1 = input('Digite algo: ')
print(n1.istitle())

n1 = input('Digite algo: ')
print(n1.startswith('o'))