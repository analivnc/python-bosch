#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanhoArquivo = int(input("Digite o tamanho do arquivo para download em mb: "))
velocidadeLink = int(input("Digite a velocidade de um link de internet em mbps: "))

#converte megabytes para megabits (tamanhoArquivo * 8)
tempoDownload = (tamanhoArquivo * 8) / (velocidadeLink * 60) #transforma a taxa de megabits por segundo em minutos

print(f"O tempo aproximado de download é de {tempoDownload:.2f}")







