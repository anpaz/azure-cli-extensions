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

from .arm_resource_properties_py3 import ARMResourceProperties


class SqlStoredProcedureCreateUpdateParameters(ARMResourceProperties):
    """Parameters to create and update Cosmos DB storedProcedure.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: The unique resource identifier of the ARM resource.
    :vartype id: str
    :ivar name: The name of the ARM resource.
    :vartype name: str
    :ivar type: The type of Azure resource.
    :vartype type: str
    :param location: The location of the resource group to which the resource
     belongs.
    :type location: str
    :param tags:
    :type tags: dict[str, str]
    :param identity:
    :type identity: ~azure.mgmt.cosmosdb.models.ManagedServiceIdentity
    :param resource: Required. The standard JSON format of a storedProcedure
    :type resource: ~azure.mgmt.cosmosdb.models.SqlStoredProcedureResource
    :param options: Required. A key-value pair of options to be applied for
     the request. This corresponds to the headers sent with the request.
    :type options: ~azure.mgmt.cosmosdb.models.CreateUpdateOptions
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'resource': {'required': True},
        'options': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'identity': {'key': 'identity', 'type': 'ManagedServiceIdentity'},
        'resource': {'key': 'properties.resource', 'type': 'SqlStoredProcedureResource'},
        'options': {'key': 'properties.options', 'type': 'CreateUpdateOptions'},
    }

    def __init__(self, *, resource, options, location: str=None, tags=None, identity=None, **kwargs) -> None:
        super(SqlStoredProcedureCreateUpdateParameters, self).__init__(location=location, tags=tags, identity=identity, **kwargs)
        self.resource = resource
        self.options = options
