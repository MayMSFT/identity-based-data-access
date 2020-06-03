# identity-based-data-access

This private preview feature is to address the security concern for [AzureML datastore](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-access-data) storing secrets, which is then accessible to everyone with datastore reader role.

Now users can can create datastore without providing credentials. We will instead use users' identity for data access in notebook and compute identity for data access in remote trianing. 

**Known Issue**
- [Compute](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.compute.amlcompute.amlcompute?view=azure-ml-py#add-identity-identity-type--identity-id-none-) user assigned identity (UAI) is not supported at the moment.
- [DataReference](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.data.data_reference.datareference?view=azure-ml-py) and [PipelineData](https://docs.microsoft.com/en-us/python/api/azureml-pipeline-core/azureml.pipeline.core.pipelinedata?view=azure-ml-py) are not supported at the moment.
