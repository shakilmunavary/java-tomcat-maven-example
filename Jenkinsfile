```yaml
name: Terraform CI/CD

on:
  push:
    branches: [ main ]
  pull_request:
  workflow_dispatch:

concurrency:
  group: terraform-${{ github.ref }}
  cancel-in-progress: false

env:
  TF_IN_AUTOMATION: "true"
  TF_INPUT: "false"
  TF_CLI_ARGS_init: "-input=false"
  TF_CLI_ARGS_apply: "-input=false -auto-approve"
  TF_CLI_ARGS_plan: "-input=false"
  TF_WORKSPACE: "default"

jobs:
  terraform-plan:
    name: Terraform Plan
    runs-on: ubuntu-latest
    defaults:
      run:
        working-directory: .
    env:
      ARM_SUBSCRIPTION_ID: ${{ secrets.ARM_SUBSCRIPTION_ID }}
      ARM_TENANT_ID: ${{ secrets.ARM_TENANT_ID }}
      ARM_CLIENT_ID: ${{ secrets.ARM_CLIENT_ID }}
      ARM_CLIENT_SECRET: ${{ secrets.ARM_CLIENT_SECRET }}

    steps:
      - name: Checkout Terraform repo
        uses: actions/checkout@v4
        with:
          repository: shakilmunavary/java-tomcat-maven-example
          ref: master

      - name: Setup Terraform
        uses: hashicorp/setup-terraform@v3
        with:
          terraform_version: 1.5.0

      - name: Cache .terraform
        uses: actions/cache@v3
        with:
          path: .terraform
          key: terraform-${{ runner.os }}-${{ hashFiles('**/.terraform.lock.hcl') }}
          restore-keys: |
            terraform-${{ runner.os }}-

      - name: Terraform Init (AzureRM backend)
        run: |
          terraform init \
            -backend-config="subscription_id=${ARM_SUBSCRIPTION_ID}" \
            -backend-config="tenant_id=${ARM_TENANT_ID}" \
            -backend-config="client_id=${ARM_CLIENT_ID}" \
            -backend-config="client_secret=${ARM_CLIENT_SECRET}"
        # Assumes backend "azurerm" is configured in backend.tf with storage_account_name, container_name, key, etc.

      - name: Terraform Validate
        run: terraform validate

      - name: Terraform Plan
        run: terraform plan -out=tfplan.binary

      - name: Convert Plan to JSON (optional)
        run: terraform show -json tfplan.binary > tfplan.json

      - name: Upload Plan Artifact
        uses: actions/upload-artifact@v3
        with:
          name: tfplan
          path: |
            tfplan.binary
            tfplan.json

  terraform-apply:
    name: Terraform Apply (manual approval)
    needs: terraform-plan
    runs-on: ubuntu-latest
    environment:
      name: production
      # Configure protection rules for this environment in GitHub (required reviewers) to enforce manual approval
    defaults:
      run:
        working-directory: .
    env:
      ARM_SUBSCRIPTION_ID: ${{ secrets.ARM_SUBSCRIPTION_ID }}
      ARM_TENANT_ID: ${{ secrets.ARM_TENANT_ID }}
      ARM_CLIENT_ID: ${{ secrets.ARM_CLIENT_ID }}
      ARM_CLIENT_SECRET: ${{ secrets.ARM_CLIENT_SECRET }}

    if: github.event_name == 'workflow_dispatch' || github.ref == 'refs/heads/main'

    steps:
      - name: Checkout Terraform repo
        uses: actions/checkout@v4
        with:
          repository: shakilmunavary/java-tomcat-maven-example
          ref: master

      - name: Setup Terraform
        uses: hashicorp/setup-terraform@v3
        with:
          terraform_version: 1.5.0

      - name: Cache .terraform
        uses: actions/cache@v3
        with:
          path: .terraform
          key: terraform-${{ runner.os }}-${{ hashFiles('**/.terraform.lock.hcl') }}
          restore-keys: |
            terraform-${{ runner.os }}-

      - name: Download Plan Artifact
        uses: actions/download-artifact@v3
        with:
          name: tfplan
          path: .

      - name: Terraform Init (AzureRM backend)
        run: |
          terraform init \
            -backend-config="subscription_id=${ARM_SUBSCRIPTION_ID}" \
            -backend-config="tenant_id=${ARM_TENANT_ID}" \
            -backend-config="client_id=${ARM_CLIENT_ID}" \
            -backend-config="client_secret=${ARM_CLIENT_SECRET}"

      - name: Terraform Apply
        run: terraform apply tfplan.binary
**[INFRA_CICD_CODE_GENERATION_COMPLETE]**