# Notify Slack

Send a colour-coded Slack notification via [Incoming Webhook](https://api.slack.com/messaging/webhooks).

Drop-in replacement for the deprecated [`8398a7/action-slack`](https://github.com/8398a7/action-slack) action, covering the subset of features used in Digitraffic workflows. Zero external dependencies — uses only `curl` and `jq` (both pre-installed on GitHub-hosted runners).

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
| `status` | **yes** | | Job status: `success`, `failure`, or `cancelled`. Determines the attachment colour (green / red / grey). |
| `text` | **yes** | | Main message text (supports Slack mrkdwn). |
| `fields` | no | `''` | Comma-separated metadata fields to show below the text. Supported: `repo`, `job`, `took`, `workflowRun`. |
| `job_name` | no | `github.job` | Override the job name shown in the `job` field. |
| `webhook-url` | **yes** | | Slack Incoming Webhook URL. |

## Migration from `8398a7/action-slack`

Replace:

```yaml
- uses: 8398a7/action-slack@v3
  with:
    status: failure
    text: FAILED My Workflow
    fields: repo, job, took
  env:
    SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK_URL }}
```

With:

```yaml
- uses: tmfg/digitraffic-actions@slack-notify/v1
  with:
    status: failure
    text: FAILED My Workflow
    fields: repo, job, took
    webhook-url: ${{ secrets.SLACK_WEBHOOK_URL }}
```

Key differences:
- The webhook URL is now an **input** (`webhook-url`) instead of an environment variable (`SLACK_WEBHOOK_URL`).
- The `job_name` input works the same way.
- The `took` field uses runner uptime as an approximation (the runner VM is created fresh per job, so uptime ≈ job duration).
