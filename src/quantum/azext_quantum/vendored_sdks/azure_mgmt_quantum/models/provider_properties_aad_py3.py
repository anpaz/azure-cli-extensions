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


class ProviderPropertiesAad(Model):
    """Azure Active Directory info.

    :param application_id: Provider's application id.
    :type application_id: str
    :param tenant_id: Provider's tenant id.
    :type tenant_id: str
    """

    _attribute_map = {
        'application_id': {'key': 'applicationId', 'type': 'str'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
    }

    def __init__(self, *, application_id: str=None, tenant_id: str=None, **kwargs) -> None:
        super(ProviderPropertiesAad, self).__init__(**kwargs)
        self.application_id = application_id
        self.tenant_id = tenant_id