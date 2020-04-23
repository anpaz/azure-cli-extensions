# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

def cf_quantum_mgmt(cli_ctx, *_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from .vendored_sdks.azure_mgmt_quantum import QuantumManagementClient
    return get_mgmt_service_client(cli_ctx, QuantumManagementClient)


def cf_workspaces(cli_ctx, *_):
    return cf_quantum_mgmt(cli_ctx).workspaces