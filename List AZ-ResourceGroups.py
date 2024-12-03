from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient

# Authenticate using AzureCliCredential
credential = AzureCliCredential()

# Your Azure subscription ID
subscription_id = "a2370bc5-c828-41f1-8c20-0d4f829f108d"

# Initialize Resource Management Client
resource_client = ResourceManagementClient(credential, subscription_id)

# List resource groups
print("Listing resource groups in subscription:")
rg_list = resource_client.resource_groups.list()

for rg in rg_list:
    print(f"- {rg.name}")
