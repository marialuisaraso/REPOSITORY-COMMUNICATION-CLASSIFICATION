import math

def calcular_desvio_padrao(numeros):
    # Calcula a média
    media = sum(numeros) / len(numeros)
    
    # Calcula a soma dos quadrados das diferenças em relação à média
    soma_quadrados_diff = sum((x - media) ** 2 for x in numeros)
    
    # Calcula a variância
    variancia = soma_quadrados_diff / len(numeros)
    
    # Calcula o desvio padrão
    desvio_padrao = math.sqrt(variancia)
    
    return desvio_padrao

def main():
    nome_arquivo = ("Tools/Index/VIMcommits.txt")

    try:
        with open(nome_arquivo, 'r') as arquivo:
            numeros = [float(linha.strip()) for linha in arquivo]
            
            if len(numeros) < 2:
                print("Pelo menos dois números são necessários para calcular o desvio padrão.")
            else:
                desvio = calcular_desvio_padrao(numeros)
                print("Desvio padrão:", desvio)
    except FileNotFoundError:
        print("O arquivo especificado não foi encontrado.")
    except ValueError:
        print("O arquivo contém valores inválidos.")

if __name__ == "__main__":
    main()
