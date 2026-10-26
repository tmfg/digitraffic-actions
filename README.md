# Log workflow inputs

Logs the caller workflow's inputs and the triggering actor to the job log and to the job summary as a markdown table.

## Usage

```yaml
jobs:
  log_parameters:
    runs-on: ubuntu-latest
    steps:
      - name: Log workflow inputs
        uses: tmfg/digitraffic-actions@log-workflow-inputs/v1
        with:
          inputs: ${{ toJSON(inputs) }}
```

A composite action cannot see the caller's `inputs` context, so they must be passed explicitly as JSON.

> [!WARNING]
> The values are written to the job log and summary. Do not pass secrets.

## Inputs

| Input | Required | Default | Description |
|---|---|---|---|
| `inputs` | no | `{}` | Workflow inputs as JSON, i.e. `${{ toJSON(inputs) }}`. |

Requires `jq`, which is pre-installed on GitHub-hosted runners.
