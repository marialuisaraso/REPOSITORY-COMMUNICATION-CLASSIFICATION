# import requests
# import os

# def main():
#     tokens = ['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', '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', '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', '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']  # Adicione quantos tokens desejar    
#     url = 'https://api.github.com/graphql'

#     def get_repos(cursor=None, token=None):
#         query = """
#     {
#       search(query: "stars:>0", type: REPOSITORY, first: 1000, after: %s) {
#         edges {
#           node {
#             ... on Repository {
#               name
#               owner {
#                 login
#               }
#               stargazers {
#                 totalCount
#               }
#               forks {
#                 totalCount
#               }
#               url
#               description
#             }
#           }
#         }
#         pageInfo {
#           endCursor
#           hasNextPage
#         }
#       }
#     }
#         """ % (f'"{cursor}"' if cursor else "null")

#         headers = {'Authorization': f'Bearer {token}'}
#         response = requests.post(url, json={'query': query}, headers=headers)
#         if response.status_code == 200:
#             return response.json()
#         return None

#     result = get_repos(None, tokens[0])

#     if result is not None:
#         tmp_json = []
#         with open('Tools/Paging/outputs/reposOutput.txt', 'w') as file:
#             file.write(str(result))

#         max_iter = 3000
#         iter = 0
#         while result['data']['search']['edges']['pageInfo']['hasNextPage'] and iter < max_iter:
#             print("pagingRepos [{}/{}]".format(iter, max_iter))
#             iter += 1
#             cursor = result['data']['search']['edges']['pageInfo']['endCursor']
            
#             random_token = tokens[iter % len(tokens)]

#             result = get_repos(cursor, random_token)
#             if result is not None:
#                 nodes = result['data']['search']['edges']['node']['name']['owner']['stargazers']['forks']['url']['description']
#                 for node in nodes:
#                     tmp_json.append(node)
#             else:
#                 break

#         with open('Tools/Paging/outputs/reposOutput.txt', 'w') as file:
#             file.write(str(tmp_json))

#         with open('Tools/Paging/output_final/reposOutput.txt', 'w') as file:
#             pass

#         for tmp in tmp_json:
#             with open('Tools/Paging/output_final/reposOutput.txt', 'a') as file:
#                 tmp_text = str(tmp['message'])
#                 tmp_text = tmp_text.replace('\n', '')
#                 tmp_text = os.linesep.join([s for s in tmp_text.splitlines() if s])
#                 tmp_text = tmp_text.replace('\n', '')
#                 file.write(str(tmp_text) + '\n')
#     else:
#         print("AUTHENTICATION ERROR.")


# if __name__ == "__main__":
#     main()
# import requests
# import os

# def main():
#     tokens = [
#         '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',
#         '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',
#         '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',
#         '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'
#     ]  # Adicione quantos tokens desejar
#     url = 'https://api.github.com/graphql'

#     def get_repos(cursor=None, token=None):
#         query = """
#         {
#           search(query: "stars:>0", type: REPOSITORY, first: 100, after: %s) {
#             edges {
#               node {
#                 ... on Repository {
#                   name
#                   owner {
#                     login
#                   }
#                   stargazers {
#                     totalCount
#                   }
#                   forks {
#                     totalCount
#                   }
#                   url
#                   description
#                 }
#               }
#             }
#             pageInfo {
#               endCursor
#               hasNextPage
#             }
#           }
#         }
#         """ % (f'"{cursor}"' if cursor else "null")

#         headers = {'Authorization': f'Bearer {token}'}
#         response = requests.post(url, json={'query': query}, headers=headers)
#         if response.status_code == 200:
#             response_json = response.json()
#             if 'errors' in response_json:
#                 print(f"Query failed with errors: {response_json['errors']}")
#                 return None
#             if 'data' not in response_json:
#                 print(f"Query response is missing 'data': {response_json}")
#                 return None
#             return response_json
#         else:
#             print(f"Query failed with status code {response.status_code}: {response.text}")
#             return None

#     result = get_repos(None, tokens[0])

#     if result is not None:
#         tmp_json = []
#         with open('Tools/Paging/outputs/reposOutput.txt', 'w') as file:
#             file.write(str(result))

#         max_iter = 3000
#         iter = 0
#         page_info = result['data']['search']['pageInfo']
#         while page_info['hasNextPage'] and iter < max_iter:
#             print("pagingRepos [{}/{}]".format(iter, max_iter))
#             iter += 1
#             cursor = page_info['endCursor']
            
#             random_token = tokens[iter % len(tokens)]

#             result = get_repos(cursor, random_token)
#             if result is not None:
#                 for edge in result['data']['search']['edges']:
#                     node = edge['node']
#                     tmp_json.append(node)
#                 page_info = result['data']['search']['pageInfo']
#             else:
#                 break

#         with open('Tools/Paging/outputs/reposOutput.txt', 'w') as file:
#             file.write(str(tmp_json))

#         with open('Tools/Paging/output_final/reposOutput.txt', 'w') as file:
#             pass

#         for tmp in tmp_json:
#             with open('Tools/Paging/output_final/reposOutput.txt', 'a') as file:
#                 tmp_text = f"{tmp['name']} by {tmp['owner']['login']}\nStars: {tmp['stargazers']['totalCount']}\nForks: {tmp['forks']['totalCount']}\nURL: {tmp['url']}\nDescription: {tmp['description']}\n"
#                 tmp_text = tmp_text.replace('\n', '')
#                 tmp_text = os.linesep.join([s for s in tmp_text.splitlines() if s])
#                 tmp_text = tmp_text.replace('\n', '')
#                 file.write(str(tmp_text) + '\n')
#     else:
#         print("AUTHENTICATION ERROR.")


# if __name__ == "__main__":
#     main()

import requests

def get_top_repositories(num_repos, github_token):
    url = 'https://api.github.com/graphql'
    headers = {
        'Authorization': f'Bearer {github_token}',
        'Content-Type': 'application/json'
    }
    
    query = """
    query ($cursor: String) {
      search(query: "stars:>1", type: REPOSITORY, first: 100, after: $cursor) {
        repositoryCount
        edges {
          cursor
          node {
            ... on Repository {
              nameWithOwner
              stargazers {
                totalCount
              }
            }
          }
        }
      }
    }
    """
    
    repositories = []
    cursor = None
    
    while len(repositories) < num_repos:
        variables = {'cursor': cursor}
        response = requests.post(url, headers=headers, json={'query': query, 'variables': variables})
        
        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            break
        
        data = response.json()
        search_data = data['data']['search']
        
        repositories.extend([
            {
                'nameWithOwner': edge['node']['nameWithOwner'],
                'stargazers': edge['node']['stargazers']['totalCount']
            }
            for edge in search_data['edges']
        ])
        
        if len(search_data['edges']) < 100:
            # Se receber menos que o número de itens por página, acabou os resultados
            break
        
        cursor = search_data['edges'][-1]['cursor']
    
    return repositories[:num_repos]

# Substitua 'your_github_token' pelo seu token de autenticação do GitHub
tokens = ['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', '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', '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', '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']  # Adicione quantos tokens desejar    
top_1000_repositories = get_top_repositories(1000, tokens[0])

for repo in top_1000_repositories:
    print(f"{repo['nameWithOwner']} - Stars: {repo['stargazers']}")

