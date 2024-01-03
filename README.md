# publish-hugo-site/v1

Generates and deploys a Hugo site to Github Pages with given configuration file.

## Usage

### Prerequisites

1. Deployment to GitHub Pages via GitHub Actions must be enabled in your repo
2. The branch you are deploying from must be allowed to deploy to environment `github-pages` (see https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site#creating-a-custom-github-actions-workflow-to-publish-your-site)

### Example

```yml
# Deployment to GitHub Pages requires these GITHUB_TOKEN permissions
permissions:
  contents: read
  pages: write
  id-token: write

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - name: Deploy to Pages
        id: deployment
        uses: tmfg/digitraffic-actions@publish-hugo-site/v1
        with:
          HUGO_VERSION: 0.120.4
          CONFIG_FILE_PATH: config/my_config.yml
```
