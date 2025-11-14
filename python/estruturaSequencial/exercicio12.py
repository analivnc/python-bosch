#Tendo como dados de entrada um arquivo em Gigabytes, 
# construa um algoritmo que faça a conversão para Megabytes, usando a seguinte fórmula: Gigabytes * 1024

gb = float(input("Digite o tamanho do arquivo: "))
mb = gb * 1024

print(f"A conversão é de gigabytes para megabytes é de {mb}")
