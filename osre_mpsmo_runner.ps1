$Env:JIRA_URL = 'https://jiraent.cms.gov'
$Env:JIRA_USER = '<account>'
$Env:JIRA_PASSWORD = '<pw>'
$Env:JIRA_PROJECT = 'MPSMO'
python -m venv venv
.\venv\Scripts\activate.ps1
python .\venv\Scripts\pip.exe install atlassian-python-api python-dateutil
python .\jira-extractor.py