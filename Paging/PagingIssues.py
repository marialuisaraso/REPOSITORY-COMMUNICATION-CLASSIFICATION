import requests

url = 'https://api.github.com/graphql'
headers = {'Authorization': 'Bearer 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'}

def get_issues(cursor=None):
    query = """
    query {
      repository(owner: "kamranahmedse", name: "developer-roadmap") {
        issues(first: 10, after: %s) {
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

# Inicialmente, obtemos as primeiras 10 issues sem cursor
result = get_issues()

with open('Paging/outputs/issuesOutput.txt', 'w') as file:
    # Escrevemos os resultados no arquivo
    file.write(str(result))

# Iteramos para obter as próximas páginas usando os cursores
while result['data']['repository']['issues']['pageInfo']['hasNextPage']:
    cursor = result['data']['repository']['issues']['pageInfo']['endCursor']
    result = get_issues(cursor)

    with open('Paging/outputs/issuesOutput.txt', 'a') as file:
        file.write(str(result))
