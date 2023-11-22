import requests

url = 'https://api.github.com/graphql'
headers = {'Authorization': 'Bearer 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'}

def get_pull_requests(cursor=None):
    query = """
    query {
      repository(owner: "microsoft", name: "vscode") {
        pullRequests(first: 10, after: %s) {
          nodes {
            title
            body
          }
          pageInfo {
            endCursor
            hasNextPage
          }
        }
      }
    }
    """ % (f'"{cursor}"' if cursor else "null")

    response = requests.post(url, json={'query': query}, headers=headers)
    return response.json()

# Inicialmente, obtemos as primeiras 10 pull requests sem cursor
result = get_pull_requests()

with open('Paging/outputs/prsOutput.txt', 'w') as file:
    # Escrevemos os resultados no arquivo
    file.write(str(result))

# Iteramos para obter as próximas páginas usando os cursores
while result['data']['repository']['pullRequests']['pageInfo']['hasNextPage']:
    cursor = result['data']['repository']['pullRequests']['pageInfo']['endCursor']
    result = get_pull_requests(cursor)

    with open('Paging/outputs/prsOutput.txt', 'a') as file:
        file.write(str(result))
