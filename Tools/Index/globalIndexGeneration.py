import re

def extrair_e_somar_ultimo_numero1(linha):
    # Expressão regular para encontrar os números
    padrao1 = r"[-+]?\d*\.\d+|\d+"
    numeros1 = re.findall(padrao1, linha)
    
    # Verificar se há números na linha
    if numeros1:
        ultimo_numero1 = 0
        # Pegar somente o último número
        ultimo_numero1 = float(numeros1[-1])
        return ultimo_numero1
    else:
        return 0.0  # Retorna 0 se nenhum número for encontrado na linha
    
def extrair_e_somar_ultimo_numero2(linha):
    # Expressão regular para encontrar os números
    padrao2 = r"[-+]?\d*\.\d+|\d+"
    numeros2 = re.findall(padrao2, linha)
    
    # Verificar se há números na linha
    if numeros2:
        ultimo_numero2 = 0
        # Pegar somente o último número
        ultimo_numero2 = float(numeros2[-1])
        return ultimo_numero2
    else:
        return 0.0  # Retorna 0 se nenhum número for encontrado na linha
    
def extrair_e_somar_ultimo_numero3(linha):
    # Expressão regular para encontrar os números
    padrao3 = r"[-+]?\d*\.\d+|\d+"
    numeros3 = re.findall(padrao3, linha)
    
    # Verificar se há números na linha
    if numeros3:
        ultimo_numero3 = 0
        # Pegar somente o último número
        ultimo_numero3 = float(numeros3[-1])
        return ultimo_numero3
    else:
        return 0.0  # Retorna 0 se nenhum número for encontrado na linha

# Função para processar o arquivo de entrada
def processar_arquivo_entrada1(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        index_score1 = 0
        for linha in arquivo:
            ultimo_numero1 = extrair_e_somar_ultimo_numero1(linha)
            index_score1 += ultimo_numero1
        return index_score1
    
# Função para processar o arquivo de entrada
def processar_arquivo_entrada2(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        index_score2 = 0
        for linha in arquivo:
            ultimo_numero2 = extrair_e_somar_ultimo_numero2(linha)
            index_score2 += ultimo_numero2
        return index_score2
    
# Função para processar o arquivo de entrada
def processar_arquivo_entrada3(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        index_score3 = 0
        for linha in arquivo:
            ultimo_numero3 = extrair_e_somar_ultimo_numero3(linha)
            index_score3 += ultimo_numero3
        return index_score3

# Nome do arquivo de entrada
nome_arquivo_entrada1 = "issuesVaderOutput.txt"
nome_arquivo_entrada2 = "commitsVaderOutput.txt"
nome_arquivo_entrada3 = "prsVaderOutput.txt"



# Processar o arquivo de entrada
final_index_score1 = processar_arquivo_entrada1(nome_arquivo_entrada1)
final_index_score1 = final_index_score1 / 708887
print("\n ISSUES INDEX:", final_index_score1, "\n")
final_index_score2 = processar_arquivo_entrada2(nome_arquivo_entrada2)
final_index_score2 = final_index_score2 / 126168
print("COMMITS INDEX:", final_index_score2, "\n")
final_index_score3 = processar_arquivo_entrada3(nome_arquivo_entrada3)
final_index_score3 = final_index_score3 / 47774
print("PRS INDEX:", final_index_score3, "\n")

final_index_score_general = final_index_score3 + final_index_score2 + final_index_score1
print("GLOBAL INDEX:", final_index_score_general, "\n")

def classificar_valor(x):
    if x >= -3 and x < -2:
        return "SUPER NEGATIVE"
    elif x >= -2 and x < -1:
        return "NEGATIVE"
    elif x >= -1 and x < -0.5:
        return "NEUTRAL-NEGATIVE"
    elif x >= -0.5 and x <= 0.5:
        return "NEUTRAL"
    elif x > 0.5 and x <= 1:
        return "NEUTRAL-POSITIVE"
    elif x > 1 and x <= 2:
        return "POSITIVE"
    elif x > 2 and x <= 3:
        return "SUPER POSITIVE"
    else:
        return "OUT OF INTERVAL"

# Exemplo de uso
classificacao = classificar_valor(final_index_score_general)
print(f"GLOBAL INDEX {final_index_score_general} IS INSIDE {classificacao} INTERVAL. \n")
