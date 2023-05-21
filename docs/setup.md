# Setup

1. Generate a pulumi access token using the boxcutter@jpfm.dev account:
   ```
   op item create \
     --category='API Credential' \
     --title='boxcutter pulumi access token' \
     --vault='Boxcutter' \
     username='boxcutter@jpfm.dev' \
     credential='<token>'
   ```

1. Set `PULUMI_ACCESS_TOKEN` as an environment variable:
   ```
   # op item get 'boxcutter pulumi access token' --vault Boxcutter
   # op item get xr2kqh5pcnr6xqavmnoziboema --format json
   export PULUMI_ACCESS_TOKEN=$(op read 'op://Boxcutter/boxcutter pulumi access token/credential')
   ```

1. Create a new python project:
   ```
   docker container run -it --rm \
     --env PULUMI_ACCESS_TOKEN \
     --workdir /app \
     --mount type=bind,source="$(pwd)",target=/app \
     --entrypoint bash \
     docker.io/boxcutter/pulumi-python \
       -c "pulumi new python \
            --stack org \
            --name pulumi-boxcutter-actions-github-repository \
            --description 'Manage GitHub repositories in the boxcutter-actions org with pulumi'"
   ```

1. Generate the CI/CD secret used to manage all the other repositories in the
   GitHub organization. Generate a GitHub personal access token under the
   `amazing-flowers` account with the `repo` and `read:org` permissions.
   ```
   op item create \
     --category='API Credential' \
     --title='boxcutter pulumi-github-repository GitHub personal access token' \
     --vault='Boxcutter' \
     username='amazing-flowers' \
     credential='ghp_<token>' \
     validFrom='2023-05-20' \
     expires='2023-08-18'
   ```

1. Add the GitHub personal access token to the Pulumi stack:
   ```
   pulumi stack select org
   pulumi config set github:owner boxcutter
   op read 'op://Boxcutter/boxcutter pulumi-github-repository GitHub personal access token/credential' \
     | pulumi config set github:token --secret
   ```

1. Provision the project:
   ```
   $ docker container run -it --rm \
       --env PULUMI_ACCESS_TOKEN \
       --workdir /app \
       --mount type=bind,source="$(pwd)",target=/app \
       --entrypoint bash \
       docker.io/boxcutter/pulumi-python
   % pulumi stack select org
   % pulumi preview
   % pulumi up
   ```