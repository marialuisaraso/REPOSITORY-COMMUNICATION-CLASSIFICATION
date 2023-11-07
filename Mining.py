import requests

def get_query(owner, repo_name):
    query = """
    query github {
        repository(owner: "%s", name: "%s") {
            pullRequests(last: 10) {
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
    """ % (owner, repo_name)
    return query

class Mining:
    def __init__(self, token):
        self.token = token
    
    def run_github_query(self):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'bearer {self.token}'
        }
        url = 'https://api.github.com/graphql'
        owner = "microsoft"
        repo_name = "vscode"
        query = get_query(owner, repo_name)
        request = requests.post(f'{url}', json={'query': query}, headers=headers)
        if request.status_code == 200: # return valid json request
            return request.json()
        elif request.status_code == 502: # reprocessing bad request
            return self.run_github_query()
        else:
            raise Exception(f'The query failed: {request.status_code}. {query}')

