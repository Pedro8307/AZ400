// =========== main.bicep ===========

// Setting target scope
targetScope = 'subscription'

// Creating resource group
resource rg 'Microsoft.Resources/resourceGroups@2021-01-01' = {
  name: 'VALUE'
  location: 'VALUE'
}
