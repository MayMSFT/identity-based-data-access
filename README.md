# identity-based-data-access

This private preview feature aims to:
1. Address the security concern for [AzureML datastore](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-access-data) storing secrets. Today, users have to register datastore with credentials, which is then accessible to anyone with datastore reader role in the workspace.
2. Enable eyes-off training. For companies with sensitive data, we make it possible for data scientists to do training without access to the actual data content. You can grant data access to compute only. So that data scientists won't be able to access or read the data using their own identity but they can still submit experiments to train with the data using compute identity. 

Now users can can create datastore without providing credentials. We will instead use users' identity for data access in notebook and compute identity for data access in remote trianing. <br><br>
[Sample notebook using estimator](./train-with-estimator/)<br>
[Sample notebook using pipeline](./multi-step-pipelines/)
