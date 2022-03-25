# Jira extractor

This project is for extracting Jira project data. Might be useful if you need to report on a project board full of tickets.

# Setup
You will need to perform the following steps to install python libraries


## For Linux & OSX
```
python3 -m venv venv
source venv/bin/activate
python venv/bin/pip install atlassian-python-api python-dateutil
```

## For Windows  (using Powershell)
```
python -m venv venv
.\venv\Scripts\activate.ps1
python .\venv\Scripts\pip.exe install atlassian-python-api python-dateutil

```

## Required environment variables for Linux & OSX
```
export JIRA_URL=<jira url>
export JIRA_USER=<account>
export JIRA_PASSWORD=<pw>
export JIRA_PROJECT=<project key>
```

## Required environment variables for Windows (using Powershell)
```
$Env:JIRA_URL=<jira url>
$Env:JIRA_USER=<account>
$Env:JIRA_PASSWORD=<pw>
$Env:JIRA_PROJECT=<project key>
```

## Disabling Windows Execution-Policy
```
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope CurrentUser
```

# atlassian-python-api

[docs here](https://github.com/atlassian-api/atlassian-python-api)
