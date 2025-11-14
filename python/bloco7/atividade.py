#Substitui uma parte do texto por outra.
frase = "Eu gosto de Java"
print(frase.replace("Java", "Python"))  # Resultado: "Eu gosto de Python"


#Retorna o tamanho (número de caracteres ou itens).
palavra = "computador"
print(len(palavra))   #retorna 10

#Remove espaços em branco do início e do fim da string.
nome = "  AnaLi  "
print(nome.strip())  #retorna "AnaLi"

# divide uma string em uma lista de substrings, com base em um delimitador especificado (que é um espaço por padrão). 
data = "2025-11-06"
partes_data = data.split('-')
print(partes_data) #retorna ['2025', '11', '06']


# Retorna o número de vezes que o valor aparece na lista
minha_lista = ['a', 'b', 'a', 'c']
contagem_a = minha_lista.count('a') #retorna 2








