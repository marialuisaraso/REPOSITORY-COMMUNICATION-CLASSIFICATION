import requests
import os

def main():
    tokens = ['', '', '', '']  # ADD YOUR TOKENS
    url = 'https://api.github.com/graphql'

    def get_pull_requests(cursor=None, token=None):
      query = """
      query {
        repository(owner: "codemirror", name: "codemirror5") {
          pullRequests(first: 100, after: %s) {
            nodes {
              title
              body
              comments(first: 100) {
                nodes {
                  body
                }
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

      headers = {'Authorization': f'Bearer {token}'}
      response = requests.post(url, json={'query': query}, headers=headers)
      if response.status_code == 200:
          return response.json()
      return None

    result = get_pull_requests(None, tokens[0])

    if result is not None:
        tmp_json = []
        with open('Tools/Paging/outputs/prsOutput.txt', 'w') as file:
            file.write(str(result))

        max_iter = 3000
        iter = 0
        while result['data']['repository']['pullRequests']['pageInfo']['hasNextPage'] and iter < max_iter:
            print("pagingPrs [{}/{}]".format(iter, max_iter))
            iter += 1
            cursor = result['data']['repository']['pullRequests']['pageInfo']['endCursor']
            
            random_token = tokens[iter % len(tokens)]

            result = get_pull_requests(cursor, random_token)
            if result is not None:
                nodes = result['data']['repository']['pullRequests']['nodes']
                for node in nodes:
                    tmp_json.append(node)
            else:
                break

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
    else:
        print("AUTHENTICATION ERROR.")


if __name__ == "__main__":
    main()
