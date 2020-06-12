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


class ProviderPropertiesManagedApplication(Model):
    """Provider's Managed-Application info.

    :param publisher_id: Provider's publisher id
    :type publisher_id: str
    :param offer_id: Provider's offer id
    :type offer_id: str
    """

    _attribute_map = {
        'publisher_id': {'key': 'publisherId', 'type': 'str'},
        'offer_id': {'key': 'offerId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ProviderPropertiesManagedApplication, self).__init__(**kwargs)
        self.publisher_id = kwargs.get('publisher_id', None)
        self.offer_id = kwargs.get('offer_id', None)
