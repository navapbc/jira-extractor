#!/usr/bin/env python3
from atlassian import Jira
from pprint import pprint
import os
import json

jiraUrl = os.environ["JIRA_URL"]
jiraUser = os.environ["JIRA_USER"]
jiraPassword = os.environ["JIRA_PASSWORD"]
jiraProject = os.environ["JIRA_PROJECT"]


jira = Jira(
    url=jiraUrl,
    username=jiraUser,
    password=jiraPassword)
JQL = f'project = {jiraProject} ORDER BY issuekey'
#  AND status IN ("To Do", "In Progress") 
data = jira.jql(JQL)
with open('jira_query_result.json') as json_file:
    data = json.dump(data, json_file)

#pprint(data["issues"][0])
# new_issue = {
#     'project': {'key': 'MPSMO'},
#     'summary': "One small step for tickets, one giant leap for automation!",
#     'description': "All your base are belong to us",
#     'issuetype': {'name': 'Task'}
# }
# jira.create_issue(new_issue)

# fields to produce
# Type, Priority, Components, Labels, Status, Resolution, Reporter, Assignee, Date Due, Date Created, Date Updated


def main():
    print("foo")

if __name__ == "__name__":
    main()