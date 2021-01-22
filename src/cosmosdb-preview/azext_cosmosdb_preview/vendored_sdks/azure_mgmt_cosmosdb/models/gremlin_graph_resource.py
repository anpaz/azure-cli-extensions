# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class GremlinGraphResource(Model):
    """Cosmos DB Gremlin graph resource object.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. Name of the Cosmos DB Gremlin graph
    :type id: str
    :param indexing_policy: The configuration of the indexing policy. By
     default, the indexing is automatic for all document paths within the graph
    :type indexing_policy: ~azure.mgmt.cosmosdb.models.IndexingPolicy
    :param partition_key: The configuration of the partition key to be used
     for partitioning data into multiple partitions
    :type partition_key: ~azure.mgmt.cosmosdb.models.ContainerPartitionKey
    :param default_ttl: Default time to live
    :type default_ttl: int
    :param unique_key_policy: The unique key policy configuration for
     specifying uniqueness constraints on documents in the collection in the
     Azure Cosmos DB service.
    :type unique_key_policy: ~azure.mgmt.cosmosdb.models.UniqueKeyPolicy
    :param conflict_resolution_policy: The conflict resolution policy for the
     graph.
    :type conflict_resolution_policy:
     ~azure.mgmt.cosmosdb.models.ConflictResolutionPolicy
    """

    _validation = {
        'id': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'indexing_policy': {'key': 'indexingPolicy', 'type': 'IndexingPolicy'},
        'partition_key': {'key': 'partitionKey', 'type': 'ContainerPartitionKey'},
        'default_ttl': {'key': 'defaultTtl', 'type': 'int'},
        'unique_key_policy': {'key': 'uniqueKeyPolicy', 'type': 'UniqueKeyPolicy'},
        'conflict_resolution_policy': {'key': 'conflictResolutionPolicy', 'type': 'ConflictResolutionPolicy'},
    }

    def __init__(self, **kwargs):
        super(GremlinGraphResource, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.indexing_policy = kwargs.get('indexing_policy', None)
        self.partition_key = kwargs.get('partition_key', None)
        self.default_ttl = kwargs.get('default_ttl', None)
        self.unique_key_policy = kwargs.get('unique_key_policy', None)
        self.conflict_resolution_policy = kwargs.get('conflict_resolution_policy', None)
