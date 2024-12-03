
@description('The name of the resource group to create')
param resourceGroupName string = 'AZ-Bicep'

@description('The location of the resource group')
param location string = 'uksouth'

resource resourceGroup 'Microsoft.Resources/resourceGroups@2021-04-01' = {
  name: resourceGroupName
  location: location
}
