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

## Available actions

[Run task in ECS](https://github.com/tmfg/digitraffic-actions/tree/ecs-run-task/v1)

[Update ECS task definition](https://github.com/tmfg/digitraffic-actions/tree/update-task-def/v1)

[Update ECS service](https://github.com/tmfg/digitraffic-actions/tree/ecs-service-update/v1)

[Mirror repository](https://github.com/tmfg/digitraffic-actions/tree/mirror/v1)

[Publish workflow artifacts on GitHub Pages](https://github.com/tmfg/digitraffic-actions/tree/gh-pages-publish/v1)

[Build and publish a Hugo generated site on GitHub Pages](https://github.com/tmfg/digitraffic-actions/tree/publish-hugo-site/v1)



