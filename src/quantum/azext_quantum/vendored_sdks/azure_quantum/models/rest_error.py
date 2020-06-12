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
from msrest.exceptions import HttpOperationError


class RestError(Model):
    """An Error response.

    :param code: An identifier for the error. Codes are invariant and are
     intended to be consumed programmatically.
    :type code: str
    :param message: A message describing the error, intended to be suitable
     for displaying in a user interface.
    :type message: str
    """

    _attribute_map = {
        'code': {'key': 'error.code', 'type': 'str'},
        'message': {'key': 'error.message', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(RestError, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.message = kwargs.get('message', None)


class RestErrorException(HttpOperationError):
    """Server responsed with exception of type: 'RestError'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(RestErrorException, self).__init__(deserialize, response, 'RestError', *args)
