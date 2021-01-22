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


class RestoreParameters(Model):
    """Parameters to indicate the information about the restore.

    :param restore_mode: Describes the mode of the restore. Possible values
     include: 'PointInTime'
    :type restore_mode: str or ~azure.mgmt.cosmosdb.models.RestoreMode
    :param restore_source: The id of the restorable database account from
     which the restore has to be initiated. For example:
     /subscriptions/{subscriptionId}/providers/Microsoft.DocumentDB/locations/{location}/restorableDatabaseAccounts/{restorableDatabaseAccountName}
    :type restore_source: str
    :param restore_timestamp_in_utc: Time to which the account has to be
     restored (ISO-8601 format).
    :type restore_timestamp_in_utc: datetime
    :param databases_to_restore: List of specific databases available for
     restore.
    :type databases_to_restore:
     list[~azure.mgmt.cosmosdb.models.DatabaseRestoreResource]
    """

    _attribute_map = {
        'restore_mode': {'key': 'restoreMode', 'type': 'str'},
        'restore_source': {'key': 'restoreSource', 'type': 'str'},
        'restore_timestamp_in_utc': {'key': 'restoreTimestampInUtc', 'type': 'iso-8601'},
        'databases_to_restore': {'key': 'databasesToRestore', 'type': '[DatabaseRestoreResource]'},
    }

    def __init__(self, **kwargs):
        super(RestoreParameters, self).__init__(**kwargs)
        self.restore_mode = kwargs.get('restore_mode', None)
        self.restore_source = kwargs.get('restore_source', None)
        self.restore_timestamp_in_utc = kwargs.get('restore_timestamp_in_utc', None)
        self.databases_to_restore = kwargs.get('databases_to_restore', None)
