# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import unittest

from azure_devtools.scenario_tests import AllowLargeResponse
from azure.cli.testsdk import (ScenarioTest, ResourceGroupPreparer)

from .utils import is_private_preview_subscription, TEST_WORKSPACE, TEST_RG, TEST_SUBS, TEST_WORKSPACE_CREATE_DELETE, TEST_WORKSPACE_LOCATION, TEST_WORKSPACE_SA

TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


class QuantumWorkspacesScenarioTest(ScenarioTest):

    @AllowLargeResponse()
    def test_workspace(self):
        # Since azure quantum is still in private preview, we require
        # these tests to run in a specific subscription (AzureQuantum-test)
        # if running somewhere else, just skip
        if not is_private_preview_subscription(self):
            self.skipTest(f"Need to run azure quantum tests in subscription {TEST_SUBS}")

        # Because we are in private preview, we need to set the subscription again so it gets
        # reflected in the recordings. Once this is not dependent on a particular subscription
        # this can be removed.
        self.cmd(f"az account set -s {TEST_SUBS}")

        # clear
        self.cmd(f'az quantum workspace clear')

        # list
        workspaces = self.cmd(f'az quantum workspace list -l {TEST_WORKSPACE_LOCATION} -o json').get_output_in_json()
        assert len(workspaces) > 0
        self.cmd('az quantum workspace list -o json', checks=[
            self.check(f"[?name=='{TEST_WORKSPACE}'].resourceGroup | [0]", TEST_RG)
        ])

        # set
        self.cmd(f'az quantum workspace set -g {TEST_RG} -w {TEST_WORKSPACE} -l {TEST_WORKSPACE_LOCATION} -o json', checks=[
            self.check("name", TEST_WORKSPACE)
        ])

        # show
        self.cmd(f'az quantum workspace show -o json', checks=[
            self.check("name", TEST_WORKSPACE)
        ])

        # clear
        self.cmd(f'az quantum workspace clear')

        # create
        self.cmd(f'az quantum workspace create -g {TEST_RG} -w {TEST_WORKSPACE_CREATE_DELETE} -l {TEST_WORKSPACE_LOCATION} -a {TEST_WORKSPACE_SA} -o json --skip-role-assignment', checks=[
            self.check("name", TEST_WORKSPACE_CREATE_DELETE),
            self.check("provisioningState", "Accepted")  # Status is accepted since we're not linking the storage account.
        ])

        # delete
        self.cmd(f'az quantum workspace delete -g {TEST_RG} -w {TEST_WORKSPACE_CREATE_DELETE} -o json', checks=[
            self.check("name", TEST_WORKSPACE_CREATE_DELETE),
            self.check("provisioningState", "Deleting")
        ])
