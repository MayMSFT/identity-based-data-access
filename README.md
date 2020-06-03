# identity-based-data-access

This private preview feature is to address the security concern for [AzureML datastore](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-access-data) storing secrets, which is then accessible to everyone with datastore reader role.

Now users can can create datastore without providing credentials. We will instead use users' identity for data access in notebook and compute identity for data access in remote trianing. 

**Known Issue**
- Compute user assigned identity (UAI) is not supported at the moment.
- DataReference/PipelineData is not supported at the moment.
