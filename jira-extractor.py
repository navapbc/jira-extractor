#!/usr/bin/env python3
"""
A script for exporting reportable data into csv format. Fit for excelification.
"""
import sys
from atlassian import Jira
from dateutil import parser
import os
import json
import csv
import argparse
import itertools

jiraUrl = os.environ["JIRA_URL"]
jiraUser = os.environ["JIRA_USER"]
jiraPassword = os.environ["JIRA_PASSWORD"]
jiraProject = os.environ["JIRA_PROJECT"]

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
def parse_args():
    parser = argparse.ArgumentParser(
        description="Extract common Jira project fields to CSV for excelification"
    )
    parser.add_argument(
        "--load_issues", help="Get the permission access block for all buckets in the account", action='store_true'
    )
    parser.set_defaults(
        load_issues=True, 
    )

    known_args, unknown_args = parser.parse_known_args()
    return known_args    

def get_issues():
    jira = Jira(
        url=jiraUrl,
        username=jiraUser,
        password=jiraPassword)
    JQL = f'project = {jiraProject} ORDER BY issuekey'

    lastFound = 0
    total = 1
    issues = []
    data = {}
    while (lastFound < total):
        try:
            data = jira.jql(JQL,start=lastFound)
            lastFound = data["maxResults"]+data["startAt"]
            total = data["total"]
        except:
            sys.exit("failed to paginate using jira api.")   

        issues = list(itertools.chain(issues,data["issues"]))

    return issues

def load_issues():
    with open('jira_query_result.json') as json_file:
        data = json.load(json_file)
        return data

def save_issues(data):
    with open('jira_query_result.json', 'w') as json_file:
        json.dump(data, json_file)

def write_csv(data):
    csvfile = open('issues.csv', 'w', newline='')
    headers = [
        'Key',
        'Type', 
        'Priority', 
        'Components', 
        'Labels', 
        'Status', 
        'Resolution', 
        'Reporter',
        'Assignee',
        'Date Due',
        'Date Created',
        'Date Updated',
        'Summary'
    ]
    csvWriter = csv.writer(csvfile, delimiter=',', quotechar='"')
    csvWriter.writerow(headers)
    for i in data:
        ii = i["fields"]
        csvWriter.writerow([
            i["key"],
            ii["issuetype"]["name"],
            ii["priority"]["name"],
            '-'.join(sorted([j["name"] for j in ii["components"]])) if ii["components"] else None,
            '-'.join(sorted([j for j in ii["labels"]])) if ii["labels"] else None,
            ii["status"]["name"],
            ii["resolution"]["name"] if ii["resolution"] else None,
            ii["reporter"]["displayName"],
            ii["assignee"]["displayName"] if ii["assignee"] else None,
            parser.parse(ii["duedate"]).strftime('%m/%d/%Y') if ii["duedate"] else None,
            parser.parse(ii["created"]).strftime('%m/%d/%Y') if ii["created"] else None,
            parser.parse(ii["updated"]).strftime('%m/%d/%Y') if ii["updated"] else None,
            ii["summary"]
        ])
    csvfile.close() 

def main():    
    data = {}

    data = get_issues()
    write_csv(data)
#    save_issues(data)

if __name__ == "__main__":
    main()