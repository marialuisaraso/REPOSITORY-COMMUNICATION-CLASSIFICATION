import requests
import os

def main():
    tokens = ['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', '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', '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', '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']  # Adicione quantos tokens desejar    
    url = 'https://api.github.com/graphql'
    def get_commits(cursor=None, token=None):
        query = """
        query {
          repository(owner: "codemirror", name: "codemirror5") {
            ref(qualifiedName: "master") {
              target {
                ... on Commit {
                  history(first: 100, after: %s) {
                    nodes {
                      oid
                      message
                      comments(first: 100) {
                        nodes {
                          author {
                            login
                          }
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
            }
          }
        }
        """ % (f'"{cursor}"' if cursor else "null")

        headers = {'Authorization': f'Bearer {token}'}
        response = requests.post(url, json={'query': query}, headers=headers)
        if response.status_code == 200:
            return response.json()
        return None

    result = get_commits(None, tokens[0])

    if result is not None:
        tmp_json = []
        with open('Tools/Paging/outputs/commitsOutput.txt', 'w') as file:
            file.write(str(result))

        max_iter = 3000
        iter = 0
        while result['data']['repository']['ref']['target']['history']['pageInfo']['hasNextPage'] and iter < max_iter:
            print("pagingCommits [{}/{}]".format(iter, max_iter))
            iter += 1
            cursor = result['data']['repository']['ref']['target']['history']['pageInfo']['endCursor']
            
            random_token = tokens[iter % len(tokens)]

            result = get_commits(cursor, random_token)
            if result is not None:
                nodes = result['data']['repository']['ref']['target']['history']['nodes']
                for node in nodes:
                    tmp_json.append(node)
            else:
                break

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
    else:
        print("AUTHENTICATION ERROR.")


if __name__ == "__main__":
    main()
