import requests, os

def main():
  url = 'https://api.github.com/graphql'
  headers = {'Authorization': 'Bearer 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'}

  def get_commits(cursor=None):
      query = """
      query {
        repository(owner: "kamranahmedse", name: "developer-roadmap") {
          ref(qualifiedName: "master") {
            target {
              ... on Commit {
                history(first: 100, after: %s) {
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

  with open('Tools/Paging/outputs/commitsOutput.txt', 'w') as file:
      # Escrevemos os resultados no arquivo
      file.write(str(result))

  # Iteramos para obter as próximas páginas usando os cursores
  # Iteramos para obter as próximas páginas usando os cursores
  max_iter = 50
  iter = 0
  tmp_json = []
  while result['data']['repository']['ref']['target']['history']['pageInfo']['hasNextPage'] and iter < max_iter:
      print("pagingCommits [{}/{}]".format(iter, max_iter))
      iter += 1
      cursor = result['data']['repository']['ref']['target']['history']['pageInfo']['endCursor']
      result = get_commits(cursor)
      nodes = result['data']['repository']['ref']['target']['history']['nodes']
      for node in nodes:
        tmp_json.append(node)
  print("end of while")
  with open('Tools/Paging/outputs/commitsOutput.txt', 'w') as file:
      file.write(str(tmp_json))


  with open('Tools/Paging/output_final/commitsOutput.txt', 'w') as file:
    pass


  for tmp in tmp_json:
    with open('Tools/Paging/output_final/commitsOutput.txt', 'a') as file:
      tmp_text = str(tmp['message'])
      tmp_text = tmp_text.replace('\n', '')
      tmp_text = os.linesep.join([s for s in tmp_text.splitlines() if s])
      tmp_text = tmp_text.replace('\n', '')

      file.write(str(tmp_text) + '\n')
  

# main()