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

import uuid
from msrest.pipeline import ClientRawResponse

from .. import models


class RestorableSqlContainersOperations(object):
    """RestorableSqlContainersOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: The API version to use for this operation. Constant value: "2020-06-01-preview".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2020-06-01-preview"

        self.config = config

    def list(
            self, location, instance_id, restorable_sql_database_rid=None, custom_headers=None, raw=False, **operation_config):
        """Lists all the restorable Azure Cosmos DB SQL containers available for a
        specific database.

        :param location: Cosmos DB region, with spaces between words and each
         word capitalized.
        :type location: str
        :param instance_id: The instanceId GUID of a restorable database
         account.
        :type instance_id: str
        :param restorable_sql_database_rid: The resource id of the restorable
         SQL database.
        :type restorable_sql_database_rid: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of RestorableSqlContainerGetResult
        :rtype:
         ~azure.mgmt.cosmosdb.models.RestorableSqlContainerGetResultPaged[~azure.mgmt.cosmosdb.models.RestorableSqlContainerGetResult]
        :raises:
         :class:`DefaultErrorResponseException<azure.mgmt.cosmosdb.models.DefaultErrorResponseException>`
        """
        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str', min_length=1),
                    'location': self._serialize.url("location", location, 'str'),
                    'instanceId': self._serialize.url("instance_id", instance_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str', min_length=1)
                if restorable_sql_database_rid is not None:
                    query_parameters['restorableSqlDatabaseRid'] = self._serialize.query("restorable_sql_database_rid", restorable_sql_database_rid, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def internal_paging(next_link=None):
            request = prepare_request(next_link)

            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                raise models.DefaultErrorResponseException(self._deserialize, response)

            return response

        # Deserialize response
        header_dict = None
        if raw:
            header_dict = {}
        deserialized = models.RestorableSqlContainerGetResultPaged(internal_paging, self._deserialize.dependencies, header_dict)

        return deserialized
    list.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.DocumentDB/locations/{location}/restorableDatabaseAccounts/{instanceId}/restorableSqlContainers'}

    def get(
            self, location, instance_id, restorable_sql_container_id, custom_headers=None, raw=False, **operation_config):
        """Get the properties of a restorable SQL container.

        :param location: Cosmos DB region, with spaces between words and each
         word capitalized.
        :type location: str
        :param instance_id: The instanceId GUID of a restorable database
         account.
        :type instance_id: str
        :param restorable_sql_container_id: The GUID of the restorable SQL
         container.
        :type restorable_sql_container_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of None
        :rtype:
         ~azure.mgmt.cosmosdb.models.RestorableSqlContainerGetResult[None]
        :raises:
         :class:`DefaultErrorResponseException<azure.mgmt.cosmosdb.models.DefaultErrorResponseException>`
        """
        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.get.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str', min_length=1),
                    'location': self._serialize.url("location", location, 'str'),
                    'instanceId': self._serialize.url("instance_id", instance_id, 'str'),
                    'restorableSqlContainerId': self._serialize.url("restorable_sql_container_id", restorable_sql_container_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str', min_length=1)

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def internal_paging(next_link=None):
            request = prepare_request(next_link)

            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                raise models.DefaultErrorResponseException(self._deserialize, response)

            return response

        # Deserialize response
        header_dict = None
        if raw:
            header_dict = {}
        deserialized = models.RestorableSqlContainerGetResult(internal_paging, self._deserialize.dependencies, header_dict)

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.DocumentDB/locations/{location}/restorableDatabaseAccounts/{instanceId}/restorableSqlContainers/{restorableSqlContainerId}'}
