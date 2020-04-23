# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.profiles import CustomResourceType


QUANTUM_DATA = CustomResourceType('azext_quantum.vendored_sdks.azure_quantum', 'QuantumClient')
QUANTUM_MGMT = CustomResourceType('azext_quantum.vendored_sdks.azure_mgmt_quantum', 'QuantumManagementClient')
