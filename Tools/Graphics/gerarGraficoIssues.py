#QUANTIDADE DE COMENTARIOS POR ISSUE
import pandas as pd
from ggplot import *

# Ler o arquivo texto e carregar os dados em um DataFrame do pandas
def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
    valores = [float(linha.strip()) for linha in linhas]
    return pd.DataFrame({'Valores': valores})

# Função para gerar o gráfico boxplot
def gerar_boxplot(dados):
    return ggplot(aes(x='1'), data=dados) + geom_boxplot()

# Nome do arquivo de entrada
nome_arquivo = 'dados.txt'

# Ler os dados do arquivo
dados = ler_arquivo(nome_arquivo)

# Gerar o gráfico boxplot
grafico = gerar_boxplot(dados)

# Exibir o gráfico
print(grafico)
