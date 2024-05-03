import os
import requests
import uuid
import sys

GITHUB_TOKEN = os.getenv("TOKEN")
GITHUB_REPO_OWNER = os.getenv("GITHUB_REPO_OWNER")
GITHUB_REPO = os.getenv("GITHUB_REPO")
CRITICAL_ONLY = os.getenv("CRITICAL_ONLY")
OUTPUT_KEY = os.getenv("OUTPUT_KEY")


def set_multiline_output(name, value):
    with open(os.environ["GITHUB_OUTPUT"], "a") as fh:
        delimiter = uuid.uuid1()
        print(f"{name}<<{delimiter}", file=fh)
        print(value, file=fh)
        print(delimiter, file=fh)


headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json",
}

response = requests.get(
    f"https://api.github.com/repos/{GITHUB_REPO_OWNER}/{GITHUB_REPO}/dependabot/alerts",
    headers=headers,
)

if response.status_code == 200:
    alerts = (
        [
            {
                "summary": alert["security_advisory"]["summary"],
                "url": alert["url"],
                "severity": alert["security_advisory"]["severity"],
            }
            for alert in response.json()
            if alert["state"] == "open"
        ]
        if not CRITICAL_ONLY == "true"
        else [
            {
                "summary": alert["security_advisory"]["summary"],
                "url": alert["url"],
                "severity": alert["security_advisory"]["severity"],
            }
            for alert in response.json()
            if alert["state"] == "open"
            and alert["security_advisory"]["severity"] == "critical"
        ]
    )

    if len(alerts) > 0:
        output_string = "\n".join(
            [
                f'{alert["severity"]}: {alert["summary"]} {(alert["url"])}'
                for alert in alerts
            ]
        )
        set_multiline_output(OUTPUT_KEY, output_string)
        sys.exit(1)

else:
    print(f"Getting Dependabot alerts failed with status code {response.status_code}")