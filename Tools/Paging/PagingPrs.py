import requests, os

def main():
  url = 'https://api.github.com/graphql'
  headers = {'Authorization': 'Bearer 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'}

  def get_pull_requests(cursor=None):
      query = """
      query {
        repository(owner: "kamranahmedse", name: "developer-roadmap") {
          pullRequests(first: 100, after: %s) {
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

  with open('Tools/Paging/outputs/prsOutput.txt', 'w') as file:
      # Escrevemos os resultados no arquivo
      file.write(str(result))

  # Iteramos para obter as próximas páginas usando os cursores
  max_iter = 50
  iter = 0
  tmp_json = []
  while result['data']['repository']['pullRequests']['pageInfo']['hasNextPage'] and iter < max_iter:
      print("pagingPrs [{}/{}]".format(iter, max_iter))

      iter += 1
      cursor = result['data']['repository']['pullRequests']['pageInfo']['endCursor']
      result = get_pull_requests(cursor)
      nodes = result['data']['repository']['pullRequests']['nodes']
      for node in nodes:
        tmp_json.append(node)
  print("end of while")
  with open('Tools/Paging/outputs/prsOutput.txt', 'w') as file:
      file.write(str(tmp_json))

  with open('Tools/Paging/output_final/prsOutput.txt', 'w') as file:
     pass

  for tmp in tmp_json:
    with open('Tools/Paging/output_final/prsOutput.txt', 'a') as file:
      tmp_text = str(tmp['body'])
      tmp_text = tmp_text.replace('\n', '')
      tmp_text = os.linesep.join([s for s in tmp_text.splitlines() if s])
      tmp_text = tmp_text.replace('\n', '')
      file.write(str(tmp_text) + '\n')


# main()