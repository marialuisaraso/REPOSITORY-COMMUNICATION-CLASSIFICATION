import json

commits_file = "Tools/commitsResults.json"
prs_file = "Tools/prsResults.json"
issues_file = "Tools/issuesResults.json"

def main():
    def extract_commit_fields(data):
        items = []
        # Extrai os campos "title" e "message"
        for issue in data["data"]["repository"]["issues"]["nodes"]["title"]["body"]:
            title = issue["title"]
            message = issue["body"]  
            items.append((title, message))
        return items

    def extract_issues_fields(data):
        items = []
        # Extrai os campos "title" e "message"
        for issue in data["data"]["repository"]["issues"]["nodes"]["title"]["body"]:
            title = issue["title"]
            message = issue["body"]  
            items.append((title, message))
        return items

    def extract_prs_fields(data):
        items = []
        # Extrai os campos "title" e "message"
        for issue in data["data"]["repository"]["issues"]["nodes"]["title"]["body"]:
            title = issue["title"]
            message = issue["body"]  
            items.append((title, message))
        return items

    def commits():
        with open(commits_file, "r") as file1:
            commits_data = json.load(file1)
        
        commits_items = extract_commit_fields(commits_data)
        with open("commitsInput.txt", "w") as file:
            for title, message in commits_items:
                file.write(f"{title}\n")
                file.write(f"{message}\n\n")

    def issues():
        with open(issues_file, "r") as file2:
            issues_data = json.load(file2)
        
        issues_items = extract_issues_fields(issues_data)
        with open("issuesInput.txt", "w") as file:
            for title, message in issues_items:
                file.write(f"{title}\n")
                file.write(f"{message}\n\n")

    def prs():
        with open(prs_file, "r") as file3:
            prs_data = json.load(file3)
        
        prs_items = extract_prs_fields(prs_data)
        with open("prsInput.txt", "w") as file:
            for title, message in prs_items:
                file.write(f"{title}\n")
                file.write(f"{message}\n\n")
    
    commits()
    issues()
    prs()

main()