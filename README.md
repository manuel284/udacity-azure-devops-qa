# Udacity-Ensuring-Quality-Releases

## Instructions
1. Configure the storage account and state backend<br/>
https://docs.microsoft.com/en-us/azure/developer/terraform/store-state-in-azure-storage<br/>
[create_terraform_storageaccount.sh](create_terraform_storageaccount.sh)<br/>
Sample output:<br/>
```
$ . create_terraform_storageaccount.sh
{
  "id": "/subscriptions/****/resourceGroups/tstate",
  "location": "eastus",
  "managedBy": null,
  "name": "tstate",
  "properties": {
    "provisioningState": "Succeeded"
  },
  "tags": null,
  "type": "Microsoft.Resources/resourceGroups"
}
{
  "accessTier": "Hot",
  "allowBlobPublicAccess": null,
  "allowSharedKeyAccess": null,
  "azureFilesIdentityBasedAuthentication": null,
  "blobRestoreStatus": null,
  "creationTime": "2021-05-08T07:43:36.898469+00:00",
  "customDomain": null,
  "enableHttpsTrafficOnly": true,
  "enableNfsV3": null,
  "encryption": {
    "encryptionIdentity": null,
    "keySource": "Microsoft.Storage",
    "keyVaultProperties": null,
    "requireInfrastructureEncryption": null,
    "services": {
      "blob": {
        "enabled": true,
        "keyType": "Account",
        "lastEnabledTime": "2021-05-08T07:43:37.007862+00:00"
      },
      "file": {
        "enabled": true,
        "keyType": "Account",
        "lastEnabledTime": "2021-05-08T07:43:37.007862+00:00"
      },
      "queue": null,
      "table": null
    }
  },
  "extendedLocation": null,
  "failoverInProgress": null,
  "geoReplicationStats": null,
  "id": "/subscriptions/****/resourceGroups/tstate/providers/Microsoft.Storage/storageAccounts/****",
  "identity": null,
  "isHnsEnabled": null,
  "kind": "StorageV2",
  "largeFileSharesState": null,
  "lastGeoFailoverTime": null,
  "location": "eastus",
  "minimumTlsVersion": null,
  "name": "****",
  "networkRuleSet": {
    "bypass": "AzureServices",
    "defaultAction": "Allow",
    "ipRules": [],
    "resourceAccessRules": null,
    "virtualNetworkRules": []
  },
  "primaryEndpoints": {
    "blob": "https://****.blob.core.windows.net/",
    "dfs": "https://****.dfs.core.windows.net/",
    "file": "https://****.file.core.windows.net/",
    "internetEndpoints": null,
    "microsoftEndpoints": null,
    "queue": "https://****.queue.core.windows.net/",
    "table": "https://****.table.core.windows.net/",
    "web": "https://****.z13.web.core.windows.net/"
  },
  "primaryLocation": "eastus",
  "privateEndpointConnections": [],
  "provisioningState": "Succeeded",
  "resourceGroup": "tstate",
  "routingPreference": null,
  "secondaryEndpoints": null,
  "secondaryLocation": null,
  "sku": {
    "name": "Standard_LRS",
    "tier": "Standard"
  },
  "statusOfPrimary": "available",
  "statusOfSecondary": null,
  "tags": {},
  "type": "Microsoft.Storage/storageAccounts"
}
{
  "created": true
}
storage_account_name: ****
container_name: tstate
access_key: ****
subscription_id: ****
```

2. Create a Service Principal for Terraform<br/>
https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/service_principal_client_secret<br/>
[create_terraform_serviceprincipal.sh](create_terraform_serviceprincipal.sh)<br/>
Sample output:<br/>
```
$ . create_terraform_serviceprincipal.sh 
Changing "terraform" to a valid URI of "http://terraform", which is the required format used for service principal names
Creating 'Contributor' role assignment under scope '/subscriptions/****'
  Retrying role assignment creation: 1/36
  Retrying role assignment creation: 2/36
The output includes credentials that you must protect. Be sure that you do not include these credentials in your code or check the credentials into your source control. For more information, see https://aka.ms/azadsp-cli
{
  "appId": "****",
  "displayName": "terraform",
  "name": "http://terraform",
  "password": "****",
  "tenant": "****"
}
```
