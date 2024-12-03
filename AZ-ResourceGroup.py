
import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

# Authenticate with Azure using DefaultAzureCredential
credential = DefaultAzureCredential()

# Retrieve subscription ID (set it as an environment variable or hardcode it here)
subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID", "YOUR_SUBSCRIPTION_ID")

# Initialize Resource Management Client
resource_client = ResourceManagementClient(credential, subscription_id)

# Define the resource group parameters
resource_group_name = "MyResourceGroup"  # Replace with your desired resource group name
location = "eastus"                      # Replace with your desired Azure region

# Create or update the resource group
print(f"Creating resource group '{resource_group_name}' in location '{location}'...")
rg_result = resource_client.resource_groups.create_or_update(
    resource_group_name,
    {"location": location}
)

# Output the result
print(f"Provisioned resource group '{rg_result.name}' in the '{rg_result.location}' region")
