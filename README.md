# Openshift Origin on GCP

Provision and bootstrapping of your Openshift Origin Cluster on Google Cloud Platform


Create a composite type:
```sh

$ gcloud beta deployment-manager types create openshift-origin --template=jinja/openshift-origin.jinja

```
