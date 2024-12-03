import os
from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient

# Explicitly set the path to Azure CLI for Linux (Codespaces environment)
os.environ["AZURE_CLI_PATH"] = "/usr/bin/az"  # Adjust if your 'which az' command returns a different path

# Authenticate using AzureCliCredential
credential = AzureCliCredential()

# Use your Azure subscription ID
subscription_id = "a2370bc5-c828-41f1-8c20-0d4f829f108d"

# Initialize Resource Management Client
resource_client = ResourceManagementClient(credential, subscription_id)

# Define the resource group parameters
resource_group_name = "Az-400"  # Resource group name
location = "uksouth"           # Azure region

# Create or update the resource group
print(f"Creating resource group '{resource_group_name}' in location '{location}'...")
rg_result = resource_client.resource_groups.create_or_update(
    resource_group_name,
    {"location": location}
)

# Output the result
print(f"Provisioned resource group '{rg_result.name}' in the '{rg_result.location}' region")
