# Digitraffic custom github actions

Project contains custom github actions for use with Digitraffic project.

Actions are stored in their own branches and thus the main branch doesn't contain any action code.

## Usage

Refer to this project and appropriate branch in your workflow file:

```yaml
jobs:
  Run-action:
    runs-on: ubuntu-latest
    steps:
      - name: run action
        uses: tmfg/digitraffic-actions@<action-branch>
```
