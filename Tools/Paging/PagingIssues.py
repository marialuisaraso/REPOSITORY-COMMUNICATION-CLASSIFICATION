import requests, os

def main():
  url = 'https://api.github.com/graphql'
  headers = {'Authorization': 'Bearer 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'}

  def get_issues(cursor=None):
      query = """
      query {
        repository(owner: "kamranahmedse", name: "developer-roadmap") {
          issues(first: 100, after: %s) {
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

  with open('Tools/Paging/outputs/issuesOutput.txt', 'w') as file:
      # Escrevemos os resultados no arquivo
      file.write(str(result))

  # Iteramos para obter as próximas páginas usando os cursores
  max_iter = 100
  iter = 0
  tmp_json = []
  while result['data']['repository']['issues']['pageInfo']['hasNextPage'] and iter < max_iter:
      print("pagingIssues [{}/{}]".format(iter, max_iter))

      iter += 1
      cursor = result['data']['repository']['issues']['pageInfo']['endCursor']
      result = get_issues(cursor)
      nodes = result['data']['repository']['issues']['nodes']
      for node in nodes:
        tmp_json.append(node)
  print("end of while")
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
