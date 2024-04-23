
import requests
import os

def main():
    tokens = ['', '', '', '']  # ADD YOUR TOKENS
    url = 'https://api.github.com/graphql'

    def get_issues(cursor=None, token=None):
        query = """
        query {
          repository(owner: "codemirror", name: "codemirror5") {
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

        headers = {'Authorization': f'Bearer {token}'}
        response = requests.post(url, json={'query': query}, headers=headers)
        if response.status_code == 200:
            return response.json()
        return None

    result = get_issues(None, tokens[0])

    if result is not None:
        tmp_json = []
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

        for tmp in tmp_json:
            with open('Tools/Graphics/issuesComments.txt', 'a') as file2:
                file2.write(str(tmp['comments']['totalCount']) + "\n")  # Adiciona a contagem de comentários
    else:
        print("AUTHENTICATION ERROR.")

if __name__ == "__main__":
    main()
