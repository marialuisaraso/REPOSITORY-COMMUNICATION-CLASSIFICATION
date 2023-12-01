from Paging import PagingCommits
from Paging import PagingIssues
from Paging import PagingPrs
import json
from json import dumps

def issuesJson():
    with open('issuesResults.json', 'w') as arquivo1:
        arquivo1.write(json.dumps(PagingIssues.main(), sort_keys=True, indent=4))
        arquivo1.close()

def commitsJson():
    with open('commitsResults.json', 'w') as arquivo2:
        arquivo2.write(json.dumps(PagingCommits.main(), sort_keys=True, indent=4))
        arquivo2.close()

def prsJson():
    with open('prsResults.json', 'w') as arquivo3:
        arquivo3.write(json.dumps(PagingPrs.main(), sort_keys=True, indent=4))
        arquivo3.close()

issuesJson()
commitsJson()
prsJson()