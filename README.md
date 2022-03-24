# Jira extractor

This project is for extracting Jira project data. Might be useful if you need to report on a project board full of tickets.

# Setup

```
python3 -m venv venv
source venv/bin/activate
python venv/bin/pip install atlassian-python-api python-dateutil
```

## Required environment variables
```
export JIRA_URL=<jira url>
export JIRA_USER=<account>
export JIRA_PASSWORD=<pw>
export JIRA_PROJECT=<project key>
```

# atlassian-python-api

[docs here](https://github.com/atlassian-api/atlassian-python-api)
