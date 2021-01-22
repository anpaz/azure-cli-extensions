# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines


def monitor_data_collection_rule_association_list(client,
                                                  resource_group_name=None,
                                                  data_collection_rule_name=None,
                                                  resource_uri=None):
    if resource_group_name and data_collection_rule_name is not None:
        return client.list_by_rule(resource_group_name=resource_group_name,
                                   data_collection_rule_name=data_collection_rule_name)
    return client.list_by_resource(resource_uri=resource_uri)


def monitor_data_collection_rule_association_show(client,
                                                  resource_uri,
                                                  association_name):
    return client.get(resource_uri=resource_uri,
                      association_name=association_name)


def monitor_data_collection_rule_association_delete(client,
                                                    resource_uri,
                                                    association_name):
    return client.delete(resource_uri=resource_uri,
                         association_name=association_name)


def monitor_data_collection_rule_list(client,
                                      resource_group_name=None):
    if resource_group_name:
        return client.list_by_resource_group(resource_group_name=resource_group_name)
    return client.list_by_subscription()


def monitor_data_collection_rule_show(client,
                                      resource_group_name,
                                      data_collection_rule_name):
    return client.get(resource_group_name=resource_group_name,
                      data_collection_rule_name=data_collection_rule_name)


def monitor_data_collection_rule_delete(client,
                                        resource_group_name,
                                        data_collection_rule_name):
    return client.delete(resource_group_name=resource_group_name,
                         data_collection_rule_name=data_collection_rule_name)
