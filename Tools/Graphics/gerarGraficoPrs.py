import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Ler o arquivo texto e carregar os dados em um DataFrame do pandas
def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
    valores = [float(linha.strip()) for linha in linhas]
    return pd.DataFrame({'Valores': valores})

# Nome do arquivo de entrada
nome_arquivo = 'Tools/Graphics/prsComments.txt'

# Ler os dados do arquivo
dados = ler_arquivo(nome_arquivo)

# Aplicar logaritmo aos valores
dados['Valores'] = np.log10(dados['Valores'])

# Gerar o gráfico boxplot usando Seaborn
sns.boxplot(data=dados)
plt.title('COMENTÁRIOS POR PR (EM LOG)')
plt.show()
