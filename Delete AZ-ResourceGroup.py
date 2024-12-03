from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient

# Authenticate using AzureCliCredential
credential = AzureCliCredential()

# Your Azure subscription ID
subscription_id = "VALUE"

# Initialize Resource Management Client
resource_client = ResourceManagementClient(credential, subscription_id)

# Define the resource group to delete
resource_group_name = "VALUE"  # Replace with your resource group name

# Delete the resource group
print(f"Deleting resource group '{resource_group_name}'...")
delete_operation = resource_client.resource_groups.begin_delete(resource_group_name)
delete_operation.wait()  # Wait for the deletion to complete
print(f"Resource group '{resource_group_name}' deleted successfully.")
