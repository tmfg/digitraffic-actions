# Digitraffic custom github actions

Project contains custom github actions for use with Digitraffic project.

Actions are stored in their own branches and thus the main branch doesn't contain any action code.

# Mirror action

## Usage

Required parameters:
* `mirror-repo` defines to which repo to mirror content.
* `ssh-private-key` private key is used to authenticate to the mirror repository.
* `refspec` optionally you can define another branch/refspec. Default: master

Remember to add the public keypair as a deploy key to the mirror repository

Refer to this project and appropriate branch in your workflow file:

```yaml
jobs:
  Mirror-action:
    runs-on: ubuntu-latest
    steps:
      - name: Mirror
        uses: tmfg/digitraffic-actions@mirror/v1
        with:
          mirror-repo: <git+ssh-url>
          ssh-private-key: ${{ secrets.SSH_PRIVATE_KEY }}
```
