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


class RestorableDatabaseAccountGetResult(ARMResourceProperties):
    """A Azure Cosmos DB restorable database account.

    Variables are only populated by the server, and will be ignored when
    sending a request.

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
    :param account_name: The name of the global database account
    :type account_name: str
    :param creation_time: The creation time of the restorable database account
     (ISO-8601 format).
    :type creation_time: datetime
    :param deletion_time: The time at which the restorable database account
     has been deleted (ISO-8601 format).
    :type deletion_time: datetime
    :ivar api_type: The API type of the restorable database account. Possible
     values include: 'MongoDB', 'Gremlin', 'Cassandra', 'Table', 'Sql',
     'GremlinV2'
    :vartype api_type: str or ~azure.mgmt.cosmosdb.models.ApiType
    :ivar restorable_locations: List of regions where the of the database
     account can be restored from.
    :vartype restorable_locations:
     list[~azure.mgmt.cosmosdb.models.RestorableLocationResource]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'api_type': {'readonly': True},
        'restorable_locations': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'identity': {'key': 'identity', 'type': 'ManagedServiceIdentity'},
        'account_name': {'key': 'properties.accountName', 'type': 'str'},
        'creation_time': {'key': 'properties.creationTime', 'type': 'iso-8601'},
        'deletion_time': {'key': 'properties.deletionTime', 'type': 'iso-8601'},
        'api_type': {'key': 'properties.apiType', 'type': 'str'},
        'restorable_locations': {'key': 'properties.restorableLocations', 'type': '[RestorableLocationResource]'},
    }

    def __init__(self, *, location: str=None, tags=None, identity=None, account_name: str=None, creation_time=None, deletion_time=None, **kwargs) -> None:
        super(RestorableDatabaseAccountGetResult, self).__init__(location=location, tags=tags, identity=identity, **kwargs)
        self.account_name = account_name
        self.creation_time = creation_time
        self.deletion_time = deletion_time
        self.api_type = None
        self.restorable_locations = None
