# Earthquake Data Pipeline
> Pipeline that processes data about earthquakes

## Create Azure resources using Azure CLI in PowerShell

Login to Azure Portal using `az login`.

### Create a resource group

```powershell
$resourceGroupName ="earthquake-data-rg"
az group create `
    --name $resourceGroupName ` 
    --location norwayeast
```

### Create a storage account

```powershell
$storageAccountName="earthquakedatasa"
az storage account create `
    --name $storageAccountName `
    --location norwayeast `
    --resource-group $resourceGroupName `
    --sku Standard_LRS
```
