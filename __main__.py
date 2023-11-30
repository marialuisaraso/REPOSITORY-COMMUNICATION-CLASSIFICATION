import json
from json import dumps
import os
from Paging import PagingCommits
from Paging import PagingIssues
from Paging import PagingPullRequests
from dotenv import load_dotenv, find_dotenv
from Vader.Vader.vaderSentiment import Vader
import json

# load_dotenv(find_dotenv())

# mining = PagingIssues(os.getenv("TOKEN"))
# with open('MiningResults.json', 'w') as arquivo:
#     arquivo.write(json.dumps(mining.get_issues(), sort_keys=True, indent=4))
#     arquivo.close()

def extract_fields(data):
    items = []
    # Extrai os campos "title" e "message"
    for issue in data["data"]["repository"]["issues"]["nodes"]["title"]["body"]:
        title = issue["title"]
        message = issue["body"]  
        items.append((title, message))
    return items

# Nome do arquivo JSON
file_name = "'Paging/outputs/issuesOutput.txt'"

# Tente abrir o arquivo e ler os dados
try:
    with open(file_name, "r") as json_file:
        data = json.load(json_file)
        print("Dados da mineração, em JSON, lidos com sucesso.\n")
        print("MENU DE FERRAMENTAS ANÁLISE DE SENTIMENTOS PARA OS DADOS EXTRAÍDOS:")
        print("1- VADER")
        print("2- SENTISTRENGTH")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            Vader()
        if escolha == "2":
            print("Opção 2")

except FileNotFoundError:
    print(f"O arquivo '{file_name}' não foi encontrado.")
except json.JSONDecodeError:
    print(f"O arquivo '{file_name}' não é um JSON válido.")

# Extrai os campos e escreve em um arquivo de texto
items = extract_fields(data)
with open("output.txt", "w") as file:
    for title, message in items:
        file.write(f"{title}\n")
        file.write(f"{message}\n\n")

