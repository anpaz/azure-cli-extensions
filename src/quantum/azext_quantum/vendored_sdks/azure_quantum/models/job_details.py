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


class JobDetails(Model):
    """Job details.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param id: The job id.
    :type id: str
    :param name: The job name. Is not required for the name to be unique and
     it's only used for display purposes.
    :type name: str
    :param container_uri: Required. The blob container SAS uri, the container
     is used to host job data.
    :type container_uri: str
    :param input_data_uri: The input blob SAS uri, if specified, it will
     override the default input blob in the container.
    :type input_data_uri: str
    :param input_data_format: Required. The format of the input data.
    :type input_data_format: str
    :param input_params: The input parameters for the job. JSON object used by
     the target solver. It is expected that the size of this object is small
     and only used to specify parameters for the execution target, not the
     input data.
    :type input_params: object
    :param provider_id: Required. The unique identifier for the provider.
    :type provider_id: str
    :param target: Required. The target identifier to run the job.
    :type target: str
    :param metadata: The job metadata. Metadata provides client the ability to
     store client-specific information
    :type metadata: dict[str, str]
    :param output_data_uri: The output blob SAS uri. When a job finishes
     successfully, results will be uploaded to this blob.
    :type output_data_uri: str
    :param output_data_format: The format of the output data.
    :type output_data_format: str
    :ivar status: The job status. Possible values include: 'Waiting',
     'Executing', 'Succeeded', 'Failed', 'Cancelled'
    :vartype status: str or ~quantum.models.JobStatus
    :ivar creation_time: The creation time of the job.
    :vartype creation_time: str
    :ivar begin_execution_time: The time when the job began execution.
    :vartype begin_execution_time: str
    :ivar end_execution_time: The time when the job finished execution.
    :vartype end_execution_time: str
    :ivar cancellation_time: The time when a job was successfully cancelled.
    :vartype cancellation_time: str
    :ivar error_data: The error data for the job. This is expected only when
     Status 'Failed'.
    :vartype error_data: ~quantum.models.RestError
    """

    _validation = {
        'container_uri': {'required': True},
        'input_data_format': {'required': True},
        'provider_id': {'required': True},
        'target': {'required': True},
        'status': {'readonly': True},
        'creation_time': {'readonly': True},
        'begin_execution_time': {'readonly': True},
        'end_execution_time': {'readonly': True},
        'cancellation_time': {'readonly': True},
        'error_data': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'container_uri': {'key': 'containerUri', 'type': 'str'},
        'input_data_uri': {'key': 'inputDataUri', 'type': 'str'},
        'input_data_format': {'key': 'inputDataFormat', 'type': 'str'},
        'input_params': {'key': 'inputParams', 'type': 'object'},
        'provider_id': {'key': 'providerId', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'metadata': {'key': 'metadata', 'type': '{str}'},
        'output_data_uri': {'key': 'outputDataUri', 'type': 'str'},
        'output_data_format': {'key': 'outputDataFormat', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'creation_time': {'key': 'creationTime', 'type': 'str'},
        'begin_execution_time': {'key': 'beginExecutionTime', 'type': 'str'},
        'end_execution_time': {'key': 'endExecutionTime', 'type': 'str'},
        'cancellation_time': {'key': 'cancellationTime', 'type': 'str'},
        'error_data': {'key': 'errorData', 'type': 'RestError'},
    }

    def __init__(self, **kwargs):
        super(JobDetails, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
        self.container_uri = kwargs.get('container_uri', None)
        self.input_data_uri = kwargs.get('input_data_uri', None)
        self.input_data_format = kwargs.get('input_data_format', None)
        self.input_params = kwargs.get('input_params', None)
        self.provider_id = kwargs.get('provider_id', None)
        self.target = kwargs.get('target', None)
        self.metadata = kwargs.get('metadata', None)
        self.output_data_uri = kwargs.get('output_data_uri', None)
        self.output_data_format = kwargs.get('output_data_format', None)
        self.status = None
        self.creation_time = None
        self.begin_execution_time = None
        self.end_execution_time = None
        self.cancellation_time = None
        self.error_data = None
