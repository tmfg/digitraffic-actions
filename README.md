# Digitraffic custom github actions

Project contains custom github actions for use with Digitraffic project.

Actions are stored in their own branches and thus the main branch doesn't contain any action code.

# Mirror action

Action for mirroring a single branch with tags to another repository.

## Changes in v2
Upgrade from node from 12 to 16.

## Usage

Required parameters:
* `mirror-repo` defines to which repo to mirror content.
* `ssh-private-key` private key is used to authenticate to the mirror repository.
* `refspec` optionally you can define another branch/refspec. Default: master

Remember to add the public keypair as a deploy key to the mirror repository.

**NB:** It is recommended to disable Github Actions in the destination repository.

Refer to this project and appropriate branch in your workflow file:

```yaml
name: 'Mirror repo to public'
on:
  push:
    branches:
      - master
jobs:
  Mirror-action:
    runs-on: ubuntu-latest
    steps:
      - name: Mirror
        uses: tmfg/digitraffic-actions@mirror/v2
        with:
          mirror-repo: <git+ssh-url>
          ssh-private-key: ${{ secrets.SSH_MIRROR_KEY }}
```

## Generating ssh deploy keys

```bash
ssh-keygen -t ed25519 -a 100 -C "mirror key for <repository-name>" -f <repository-name>
```

## Technical stuff

Mirroring action uses `git push` with `--follow-tags` instead of `--mirror`.

It appears the `--mirror` is possibly destructive action. Firstly mirror will push all refs and then runs `--prune` which will remove refs which are
not locally available. Prune may in some circumstances try to delete branches which are not allowed to be deleted such as `master` and thus fails the
whole operation.

Push with `--follow-tags` pushes only the given ref–mirror action uses `master` as a default–and updates only the tags that are referencing to the
pushed commits. Mirror action only mirrors a portion of the source repository.
