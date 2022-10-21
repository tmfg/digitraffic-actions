# gh-pages-publish/v1

This action publishes workflow artifacts on GitHub Pages and generates links to the files in the workflow summary. 

## Usage

### Prerequisites

As a prerequisite for publishing material on Pages, your repo needs to have a branch configured for Pages content. By default, GitHub Pages will publish content from a branch called `gh-pages`. 

Running the following commands will create an [orphan branch](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt---orphanltnew-branchgt) named `gh-pages` in your repository:

```shell
git checkout --orphan gh-pages
git rm -rf .
git commit --allow-empty -m "root commit"
git push origin gh-pages
```

### Running the action

You may publish a single file or the contents of a directory and its subdirectories by providing either a file and its full path or a directory as the value of the input variable `FILE_PATH`.

The following example publishes a file from the location `reports/report.html` on GitHub Pages. This file will be pushed to branch `gh-pages` with the  commit message given in `COMMIT_MESSAGE`, which in the example also prints out the name of the branch from which the workflow was run. `LINK_TEXT` is printed out on the link to the published file at the bottom of your workflow summary page.

```yaml
- name: Publish report on GitHub Pages
  uses: tmfg/digitraffic-actions@gh-pages-publish/v1
  with:
    FILE_PATH: reports/report.html
    COMMIT_MESSAGE: Upload ESLint report for branch ${GITHUB_REF##*/}
    LINK_TEXT: ESLint report
```

If you do not want to generate links to the file/files, add `SKIP_LINK: true`. 

Below is an example of a workflow summary page with a link to the published file:

<img width="600" alt="image" src="https://user-images.githubusercontent.com/92532596/191916445-19427ee5-329d-4966-ae96-13f80ec75f4c.png">
