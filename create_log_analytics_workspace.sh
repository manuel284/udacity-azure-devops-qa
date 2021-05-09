LOCATION="eastus"
RG_NAME="rg-log-analytics"
LOG_NAME="toast-log"
SKU="PerGB2018"

az group create \
  -n $RG_NAME \
  -l $LOCATION

az monitor log-analytics workspace create \
  -g $RG_NAME \
  -n $LOG_NAME \
  -l $LOCATION \
  --sku $SKU


az monitor log-analytics workspace get-shared-keys \
  --resource-group $RG_NAME \
  --workspace-name $LOG_NAME
