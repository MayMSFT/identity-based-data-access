# [Private Preview] identity-based-data-access

This private preview feature aims to:
1. Address the security concern for [AzureML datastore](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-access-data) storing secrets. Today, users have to register datastore with credentials, which is then accessible to anyone with datastore reader role in the workspace.
2. Enable eyes-off training. For companies with sensitive data, we make it possible for data scientists to do training without access to the actual data content. You can grant data access to compute only. So that data scientists won't be able to access or read the data using their own identity but they can still submit experiments to train with the data using compute identity. 

Now users can can create datastore without providing credentials. We will instead use users' identity for data access in notebook and compute identity for data access in remote trianing. <br><br>
[Sample notebook using estimator](./train-with-estimator/)<br>
[Sample notebook using pipeline](./multi-step-pipelines/)

## Terms of Use
This is a private preview feature of Azure Machine Learning and is subject to the [Azure Legal Terms](https://azure.microsoft.com/en-us/support/legal/?ranMID=24542&ranEAID=msYS1Nvjv4c&ranSiteID=msYS1Nvjv4c-pQVqGgzMLX3ysSdCWd8org&epi=msYS1Nvjv4c-pQVqGgzMLX3ysSdCWd8org&irgwc=1&OCID=AID2000142_aff_7593_1243925&tduid=%28ir__6kriqwk10wkftwnk0higqpq2m22xi0gd9xxevzpz00%29%287593%29%281243925%29%28msYS1Nvjv4c-pQVqGgzMLX3ysSdCWd8org%29%28%29&irclickid=_6kriqwk10wkftwnk0higqpq2m22xi0gd9xxevzpz00) and the [Supplemental Terms for Azure Previews](https://azure.microsoft.com/en-us/support/legal/preview-supplemental-terms/)<br>
