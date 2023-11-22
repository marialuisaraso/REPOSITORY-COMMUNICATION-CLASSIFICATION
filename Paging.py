import requests
from json import dump
from json import loads

token = "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"

def run_query(json, headers) -> object:  # A simple function to use requests.post to make the API call.

    request = requests.post('https://api.github.com/graphql', json=json, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}. {}"
                        .format(request.status_code, json['query'],
                                json['variables']))


query = """
query github {

  repository(owner: "microsoft", name: "vscode") {
            pullRequests(first: 100{AFTER}) {
                pageInfo {
                    hasNextPage
                    endCursor
                }
                edges {
                    node {
                        title
                        url
                        createdAt
                        commits(last: 10) {
                            edges {
                                node {
                                    commit {
                                        message
                                        author {
                                            name
                                            email
                                            date
                                        }
                                    }
                                }
                            }
                        }
                        comments(last: 10) {
                            nodes {
                                body
                                author {
                                    login
                                }
                                createdAt
                            }
                        }
                    }
                }
            }
            issues(last: 10) {
                edges {
                    node {
                        title
                        url
                        body
                        createdAt
                        comments(last: 10) {
                            nodes {
                                body
                                author {
                                    login
                                }
                                createdAt
                            }
                        }
                    }
                }
            }
        }
}
"""

finalQuery = query.replace("{AFTER}", "")

json = {
    "query": finalQuery, "variables": {}
}

headers = {"Authorization": "Bearer " + token}

total_pages = 1

result = run_query(json, headers)

print(result['data']['repository']['pullRequests']['edges'])

edges = result['data']['repository']['pullRequests']['edges']
next_page = result["data"]["repository"]['pullRequests']["pageInfo"]["hasNextPage"]

# paginating
while (next_page and total_pages < 3):
    total_pages += 1
    cursor = result["data"]["repository"]['pullRequests']["pageInfo"]["endCursor"]
    next_query = query.replace("{AFTER}", ", after: \"%s\"" % cursor)
    json["query"] = next_query
    # salvar
    result = run_query(json, headers)
    edges += result['data']['repository']['pullRequests']['edges']
    next_page = result["data"]["repository"]['pullRequests']["pageInfo"]["hasNextPage"]