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
3. Create a Service Connection<br/>
In the Project settings of your DevOps project, add a new service connection (Azure Resource Manager) called `udacity-qa`.
4. Create environment with terraform<br/>
Run the pipeline to create the resources.
5. Add the VM to your environment<br/>
Under Environments/TEST, add a new resource (VM-Linux).<br/>
Copy the registration script, ssh into your vm and run the script.
4. Create a log analytics workspace<br/>
https://docs.microsoft.com/en-us/cli/azure/monitor/log-analytics/workspace?view=azure-cli-latest#az_monitor_log_analytics_workspace_create<br/>
[create_log_analytics_workspace.sh](create_log_analytics_workspace.sh)<br/>
    Sample output:<br/>
    ```
    $ . create_log_analytics_workspace.sh 
    {
      "id": "/subscriptions/****/resourceGroups/rg-log-analytics",
      "location": "eastus",
      "managedBy": null,
      "name": "rg-log-analytics",
      "properties": {
        "provisioningState": "Succeeded"
      },
      "tags": null,
      "type": "Microsoft.Resources/resourceGroups"
    }
    {
      "customerId": "****",
      "eTag": null,
      "id": "/subscriptions/****/resourcegroups/rg-log-analytics/providers/microsoft.operationalinsights/workspaces/toast-log",
      "location": "eastus",
      "name": "toast-log",
      "privateLinkScopedResources": null,
      "provisioningState": "Succeeded",
      "publicNetworkAccessForIngestion": "Enabled",
      "publicNetworkAccessForQuery": "Enabled",
      "resourceGroup": "rg-log-analytics",
      "retentionInDays": 30,
      "sku": {
        "capacityReservationLevel": null,
        "lastSkuUpdate": "Sun, 09 May 2021 08:13:06 GMT",
        "maxCapacityReservationLevel": 3000,
        "name": "pergb2018"
      },
      "tags": null,
      "type": "Microsoft.OperationalInsights/workspaces",
      "workspaceCapping": {
        "dailyQuotaGb": -1.0,
        "dataIngestionStatus": "RespectQuota",
        "quotaNextResetTime": "Sun, 09 May 2021 21:00:00 GMT"
      }
    }

    {
      "primarySharedKey": "****",
      "secondarySharedKey": "****"
    }
    ```
    Get the customerId and primarySharedKey from the output.
4. Install the log analytics agent on our vm<br/>
https://docs.microsoft.com/en-us/azure/azure-monitor/agents/agent-linux#install-the-agent-using-wrapper-script<br/>
Run below commands on your VM.<br/>
Ensure that GDB is installed:
```
sudo apt-get update
$ sudo apt-get install gdb
```
`wget https://raw.githubusercontent.com/Microsoft/OMS-Agent-for-Linux/master/installer/scripts/onboard_agent.sh && sh onboard_agent.sh -w <YOUR WORKSPACE ID> -s <YOUR WORKSPACE PRIMARY KEY> -d opinsights.azure.com`<br/>
Replace `<YOUR WORKSPACE ID>` with the customerId and `<YOUR WORKSPACE PRIMARY KEY>` with the primarySharedKey from the previous step.