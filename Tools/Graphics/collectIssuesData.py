
import requests
import os

def main():
    # Lista de tokens de autenticação
    tokens = ['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', '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', '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', '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']  # Adicione quantos tokens desejar
    url = 'https://api.github.com/graphql'

    def get_issues(cursor=None, token=None):
        query = """
        query {
          repository(owner: "microsoft", name: "vscode") {
            issues(first: 100, after: %s) {
              nodes {
                title
                body
                comments {
                  totalCount
                }
              }
              pageInfo {
                endCursor
                hasNextPage
              }
            }
          }
        }
        """ % (f'"{cursor}"' if cursor else "null")

        # Alternar entre os tokens de autenticação
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.post(url, json={'query': query}, headers=headers)
        if response.status_code == 200:
            return response.json()
        # Se nenhum token funcionar, retornar None
        return None

    # Inicialmente, obtemos os primeiros 10 commits sem cursor
    result = get_issues(None, tokens[0])

    if result is not None:
        tmp_json = []
        with open('Tools/Paging/outputs/issuesOutput.txt', 'w') as file:
            # Escrevemos os resultados no arquivo
            file.write(str(result))

        # Iteramos para obter as próximas páginas usando os cursores
        max_iter = 3000
        iter = 0
        while result['data']['repository']['issues']['pageInfo']['hasNextPage'] and iter < max_iter:
            print("pagingIssues [{}/{}]".format(iter, max_iter))
            iter += 1
            cursor = result['data']['repository']['issues']['pageInfo']['endCursor']
            
            random_token = tokens[iter % len(tokens)]

            result = get_issues(cursor, random_token)
            if result is not None:
                nodes = result['data']['repository']['issues']['nodes']
                for node in nodes:
                    tmp_json.append(node)
            else:
                break

        with open('Tools/Paging/outputs/issuesOutput.txt', 'w') as file:
            file.write(str(tmp_json))

        with open('Tools/Paging/output_final/issuesOutput.txt', 'w') as file:
            pass

        for tmp in tmp_json:
            with open('Tools/Paging/output_final/issuesOutput.txt', 'a') as file:
                tmp_text = str(tmp['body'])
                tmp_text = tmp_text.replace('\n', '')
                tmp_text = os.linesep.join([s for s in tmp_text.splitlines() if s])
                tmp_text = tmp_text.replace('\n', '')
                file.write(str(tmp_text) + '\n')
            with open('Tools/Graphics/issuesComments.txt', 'a') as file2:
                file2.write("Total de Comentários: " + str(tmp['comments']['totalCount']) + '\n')  # Adiciona a contagem de comentários
    else:
        print("Erro de autenticação.")

if __name__ == "__main__":
    main()
