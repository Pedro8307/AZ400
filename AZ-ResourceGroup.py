import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

# Acquire a credential object using DefaultAzureCredential
credential = DefaultAzureCredential()

# Use your Azure subscription ID
subscription_id = "a2370bc5-c828-41f1-8c20-0d4f829f108d"

# Initialize the Resource Management Client
resource_client = ResourceManagementClient(credential, subscription_id)

# Define the resource group parameters
resource_group_name = "Az400"  # Resource group name
location = "uksouth"           # Azure region

# Create or update the resource group
print(f"Creating resource group '{resource_group_name}' in location '{location}'...")
rg_result = resource_client.resource_groups.create_or_update(
    resource_group_name,
    {"location": location}
)

# Output the result
print(f"Provisioned resource group '{rg_result.name}' in the '{rg_result.location}' region")
