import os
from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient

credential = AzureCliCredential()
subscription_id = os.environ["a2370bc5-c828-41f1-8c20-0d4f829f108d"]

resource_client = ResourceManagementClient(credential, subscription_id)

rg_list = resource_client.resource_groups.list()

for rg in rg_list:
    print(rg.name)