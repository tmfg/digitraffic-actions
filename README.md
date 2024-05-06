# dependabot-slack/v1

Sends a Slack notification containing a listing of currently open Dependabot alerts of given severity level(s) in the repository where the action is run.

Uses https://github.com/marketplace/actions/action-slack

## Usage

### Prerequisites

1. A GitHub Personal Access Token with permissions to access the Dependabot alerts for the target repository via the GitHub API.

2. A Slack webhook for posting the notification.

### Example

Run on a schedule and send a Slack notification if alerts of `critical` or `high` severity are found:

```yml
name: Check Dependabot alerts and notify Slack

on:
  schedule:
    - cron: "0 6,9,12 * * *"

jobs:
  check_alerts_and_notify_slack:
    runs-on: ubuntu-latest
    steps:
      - name: Check Dependabot alerts
        uses: tmfg/digitraffic-actions@dependabot-slack/v1
        with:
          TOKEN: ${{ secrets.DEPENDABOT_TOKEN }}
          SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK_URL }}
          CRITICAL: "true"
          HIGH: "true"
          MEDIUM: "false"
          LOW: "false"
```
