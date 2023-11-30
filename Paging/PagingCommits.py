import requests

url = 'https://api.github.com/graphql'
headers = {'Authorization': 'Bearer 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'}

def get_commits(cursor=None):
    query = """
    query {
      repository(owner: "kamranahmedse", name: "developer-roadmap") {
        ref(qualifiedName: "master") {
          target {
            ... on Commit {
              history(first: 10, after: %s) {
                nodes {
                  oid
                  message
                }
                pageInfo {
                  endCursor
                  hasNextPage
                }
              }
            }
          }
        }
      }
    }
    """ % (f'"{cursor}"' if cursor else "null")

    response = requests.post(url, json={'query': query}, headers=headers)
    return response.json()

# Inicialmente, obtemos os primeiros 10 commits sem cursor
result = get_commits()

with open('Paging/outputs/commitsOutput.txt', 'w') as file:
    # Escrevemos os resultados no arquivo
    file.write(str(result))

# Iteramos para obter as próximas páginas usando os cursores
while result['data']['repository']['ref']['target']['history']['pageInfo']['hasNextPage']:
    cursor = result['data']['repository']['ref']['target']['history']['pageInfo']['endCursor']
    result = get_commits(cursor)

    with open('Paging/outputs/commitsOutput.txt', 'a') as file:
        file.write(str(result))
