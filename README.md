# digitraffic-actions

Project contains custom Github actions for use in Digitraffic projects.

Actions are stored in their own branches - the main branch doesn't contain any action code.

## Usage

Refer to this project in your workflow file, pinned to the full commit SHA of the action branch, with the branch name as a comment:

```yaml
jobs:
  Run-action:
    runs-on: ubuntu-latest
    steps:
      - name: run action
        uses: tmfg/digitraffic-actions@<commit-sha> # <action-branch>
```

Do not refer to the branch name directly (`@<action-branch>`): branches are mutable, so a SHA is the only way to guarantee that the workflow runs the reviewed version. The SHA of a branch can be found with `git ls-remote https://github.com/tmfg/digitraffic-actions <action-branch>`.

## Available actions

[Run task in ECS](https://github.com/tmfg/digitraffic-actions/tree/ecs-run-task/v1)

[Update ECS task definition](https://github.com/tmfg/digitraffic-actions/tree/update-task-def/v1)

[Update ECS service](https://github.com/tmfg/digitraffic-actions/tree/ecs-service-update/v1)

[Mirror repository](https://github.com/tmfg/digitraffic-actions/tree/mirror/v1)

[Publish workflow artifacts on GitHub Pages](https://github.com/tmfg/digitraffic-actions/tree/gh-pages-publish/v1)

[Build and publish a Hugo generated site on GitHub Pages](https://github.com/tmfg/digitraffic-actions/tree/publish-hugo-site/v1)

[Send Slack notifications of Dependabot alerts](https://github.com/tmfg/digitraffic-actions/tree/dependabot-slack/v1)

[Send Slack notifications](https://github.com/tmfg/digitraffic-actions/tree/slack-notify/v1)

[Log workflow inputs](https://github.com/tmfg/digitraffic-actions/tree/log-workflow-inputs/v1)



