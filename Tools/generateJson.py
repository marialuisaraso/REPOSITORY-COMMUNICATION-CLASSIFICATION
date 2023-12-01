from Paging import PagingCommits
from Paging import PagingIssues
from Paging import PagingPrs
import json
from json import dumps



PagingIssues.main()
PagingCommits.main()
PagingPrs.main()


# with open('Tools/Paging/output_final/prsOutput.txt', 'a') as file:
#     with open('Tools/Paging/output_final/issuesOutput.txt', 'a') as file:
#     with open('Tools/Paging/output_final/commitsOutput.txt', 'a') as file:
# agroup all in finalOutput.txt
with open('Tools/Paging/output_final/commitsOutput.txt', 'r') as file:
    commits_data = file.read()
with open('Tools/Paging/output_final/issuesOutput.txt', 'r') as file:
    issues_data = file.read()
with open('Tools/Paging/output_final/prsOutput.txt', 'r') as file:
    prs_data = file.read()

with open('Tools/Paging/output_final/finalOutput.txt', 'w') as file:
    file.write(commits_data)
    file.write(issues_data)
    file.write(prs_data)