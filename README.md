# Notify Slack

Send a colour-coded Slack notification via [Incoming Webhook](https://api.slack.com/messaging/webhooks).

Drop-in replacement for the deprecated [`8398a7/action-slack`](https://github.com/8398a7/action-slack) action, covering the subset of features used in Digitraffic workflows. Zero external dependencies — uses only Node.js (pre-installed on GitHub-hosted runners).

## Usage

```yaml
- name: Notify Slack
  if: failure()
  uses: tmfg/digitraffic-actions@slack-notify/v1
  with:
    status: failure
    text: FAILED My Workflow
    fields: repo, job, took
    webhook-url: ${{ secrets.SLACK_WEBHOOK_URL }}
```

## Inputs

| Input | Required | Default | Description |
|---|---|---|---|
| `status` | **yes** | | Job status: `success` or `failure`. Determines the attachment colour (green / red). |
| `text` | **yes** | | Main message text (supports Slack mrkdwn). |
| `fields` | no | `''` | Comma-separated metadata fields to show below the text. Supported: `repo`, `job`, `took`, `workflowRun`. |
| `job_name` | no | `github.job` | Override the job name shown in the `job` field. |
| `webhook-url` | **yes** | | Slack Incoming Webhook URL. |

