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

from .provider_properties import ProviderProperties


class ProviderDescriptionProperties(ProviderProperties):
    """A list of Provider-specific properties.

    :param description: Description about this Provider.
    :type description: str
    :param default_endpoint: Provider's default endpoint.
    :type default_endpoint: str
    :param aad: Azure Acitve Directory info.
    :type aad: ~quantum.models.ProviderPropertiesAad
    :param managed_application: Provider's Managed-Application info
    :type managed_application:
     ~quantum.models.ProviderPropertiesManagedApplication
    :param targets: The list of targets available from this provider
    :type targets: list[~quantum.models.TargetDescription]
    :param skus: The list of skus selected for this provider
    :type skus: list[~quantum.models.SkuDescription]
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'default_endpoint': {'key': 'defaultEndpoint', 'type': 'str'},
        'aad': {'key': 'aad', 'type': 'ProviderPropertiesAad'},
        'managed_application': {'key': 'managedApplication', 'type': 'ProviderPropertiesManagedApplication'},
        'targets': {'key': 'targets', 'type': '[TargetDescription]'},
        'skus': {'key': 'skus', 'type': '[SkuDescription]'},
    }

    def __init__(self, **kwargs):
        super(ProviderDescriptionProperties, self).__init__(**kwargs)
