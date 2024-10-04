#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.
# GENERATED FILE - DO NOT EDIT - MANUAL CHANGES WILL BE OVERWRITTEN


from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_data_flow_run_facts
short_description: Fetches details about one or multiple Run resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Run resources in Oracle Cloud Infrastructure
    - Lists all runs of an application in the specified compartment.  Only one parameter other than compartmentId may also be included in a query. The query
      must include compartmentId. If the query does not include compartmentId, or includes compartmentId but two or more other parameters an error is returned.
    - If I(run_id) is specified, the details of a single Run will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    run_id:
        description:
            - The unique ID for the run
            - Required to get a specific run.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The OCID of the compartment.
            - Required to list multiple runs.
        type: str
    application_id:
        description:
            - The ID of the application.
        type: str
    pool_id:
        description:
            - The ID of the pool.
        type: str
    owner_principal_id:
        description:
            - The OCID of the user who created the resource.
        type: str
    display_name_starts_with:
        description:
            - The displayName prefix.
        type: str
    lifecycle_state:
        description:
            - The LifecycleState of the run.
        type: str
        choices:
            - "ACCEPTED"
            - "IN_PROGRESS"
            - "CANCELING"
            - "CANCELED"
            - "FAILED"
            - "SUCCEEDED"
            - "STOPPING"
            - "STOPPED"
    time_created_greater_than:
        description:
            - The epoch time that the resource was created.
        type: str
    sort_by:
        description:
            - The field used to sort the results. Multiple fields are not supported.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
            - "language"
            - "runDurationInMilliseconds"
            - "lifecycleState"
            - "totalOCpu"
            - "dataReadInBytes"
            - "dataWrittenInBytes"
    sort_order:
        description:
            - The ordering of results in ascending or descending order.
        type: str
        choices:
            - "ASC"
            - "DESC"
    display_name:
        description:
            - The query parameter for the Spark application name.
        type: str
        aliases: ["name"]
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific run
  oci_data_flow_run_facts:
    # required
    run_id: "ocid1.run.oc1..xxxxxxEXAMPLExxxxxx"

- name: List runs
  oci_data_flow_run_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    application_id: "ocid1.application.oc1..xxxxxxEXAMPLExxxxxx"
    pool_id: "ocid1.pool.oc1..xxxxxxEXAMPLExxxxxx"
    owner_principal_id: "ocid1.ownerprincipal.oc1..xxxxxxEXAMPLExxxxxx"
    display_name_starts_with: display_name_starts_with_example
    lifecycle_state: ACCEPTED
    time_created_greater_than: 2013-10-20T19:20:30+01:00
    sort_by: timeCreated
    sort_order: ASC
    display_name: display_name_example

"""

RETURN = """
runs:
    description:
        - List of Run resources
    returned: on success
    type: complex
    contains:
        archive_uri:
            description:
                - A comma separated list of one or more archive files as Oracle Cloud Infrastructure URIs. For example,
                  ``oci://path/to/a.zip,oci://path/to/b.zip``. An Oracle Cloud Infrastructure URI of an archive.zip file containing custom dependencies that may
                  be used to support the execution of a Python, Java, or Scala application.
                  See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.
                - Returned for get operation
            returned: on success
            type: str
            sample: archive_uri_example
        arguments:
            description:
                - "The arguments passed to the running application as command line arguments.  An argument is
                  either a plain text or a placeholder. Placeholders are replaced using values from the parameters
                  map.  Each placeholder specified must be represented in the parameters map else the request
                  (POST or PUT) will fail with a HTTP 400 status code.  Placeholders are specified as
                  `Service Api Spec`, where `name` is the name of the parameter.
                  Example:  `[ \\"--input\\", \\"${input_file}\\", \\"--name\\", \\"John Doe\\" ]`
                  If \\"input_file\\" has a value of \\"mydata.xml\\", then the value above will be translated to
                  `--input mydata.xml --name \\"John Doe\\"`"
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        application_log_config:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                log_group_id:
                    description:
                        - The log group id for where log objects will be for Data Flow Runs.
                    returned: on success
                    type: str
                    sample: "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx"
                log_id:
                    description:
                        - The log id of the log object the Application Logs of Data Flow Run will be shipped to.
                    returned: on success
                    type: str
                    sample: "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"
        class_name:
            description:
                - The class for the application.
                - Returned for get operation
            returned: on success
            type: str
            sample: class_name_example
        configuration:
            description:
                - "The Spark configuration passed to the running process.
                  See https://spark.apache.org/docs/latest/configuration.html#available-properties.
                  Example: { \\"spark.app.name\\" : \\"My App Name\\", \\"spark.shuffle.io.maxRetries\\" : \\"4\\" }
                  Note: Not all Spark properties are permitted to be set.  Attempting to set a property that is
                  not allowed to be overwritten will cause a 400 status to be returned."
                - Returned for get operation
            returned: on success
            type: dict
            sample: {}
        driver_shape:
            description:
                - The VM shape for the driver. Sets the driver cores and memory.
                - Returned for get operation
            returned: on success
            type: str
            sample: driver_shape_example
        driver_shape_config:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                ocpus:
                    description:
                        - The total number of OCPUs used for the driver or executors.
                          See L(here,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/Shape/) for details.
                    returned: on success
                    type: float
                    sample: 10
                memory_in_gbs:
                    description:
                        - The amount of memory used for the driver or executors.
                    returned: on success
                    type: float
                    sample: 10
        execute:
            description:
                - "The input used for spark-submit command. For more details see https://spark.apache.org/docs/latest/submitting-applications.html#launching-
                  applications-with-spark-submit.
                  Supported options include ``--class``, ``--file``, ``--jars``, ``--conf``, ``--py-files``, and main application file with arguments.
                  Example: ``--jars oci://path/to/a.jar,oci://path/to/b.jar --files oci://path/to/a.json,oci://path/to/b.csv --py-files
                  oci://path/to/a.py,oci://path/to/b.py --conf spark.sql.crossJoin.enabled=true --class org.apache.spark.examples.SparkPi oci://path/to/main.jar
                  10``
                  Note: If execute is specified together with applicationId, className, configuration, fileUri, language, arguments, parameters during
                  application create/update, or run create/submit,
                  Data Flow service will use derived information from execute input only."
                - Returned for get operation
            returned: on success
            type: str
            sample: execute_example
        executor_shape:
            description:
                - The VM shape for the executors. Sets the executor cores and memory.
                - Returned for get operation
            returned: on success
            type: str
            sample: executor_shape_example
        executor_shape_config:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                ocpus:
                    description:
                        - The total number of OCPUs used for the driver or executors.
                          See L(here,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/Shape/) for details.
                    returned: on success
                    type: float
                    sample: 10
                memory_in_gbs:
                    description:
                        - The amount of memory used for the driver or executors.
                    returned: on success
                    type: float
                    sample: 10
        file_uri:
            description:
                - An Oracle Cloud Infrastructure URI of the file containing the application to execute.
                  See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.
                - Returned for get operation
            returned: on success
            type: str
            sample: file_uri_example
        logs_bucket_uri:
            description:
                - An Oracle Cloud Infrastructure URI of the bucket where the Spark job logs are to be uploaded.
                  See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.
                - Returned for get operation
            returned: on success
            type: str
            sample: logs_bucket_uri_example
        metastore_id:
            description:
                - The OCID of OCI Hive Metastore.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.metastore.oc1..xxxxxxEXAMPLExxxxxx"
        num_executors:
            description:
                - The number of executor VMs requested.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        parameters:
            description:
                - "An array of name/value pairs used to fill placeholders found in properties like
                  `Application.arguments`.  The name must be a string of one or more word characters
                  (a-z, A-Z, 0-9, _).  The value can be a string of 0 or more characters of any kind.
                  Example:  [ { name: \\"iterations\\", value: \\"10\\"}, { name: \\"input_file\\", value: \\"mydata.xml\\" }, { name: \\"variable_x\\", value:
                  \\"${x}\\"} ]"
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - "The name of the parameter.  It must be a string of one or more word characters
                          (a-z, A-Z, 0-9, _).
                          Examples: \\"iterations\\", \\"input_file\\""
                    returned: on success
                    type: str
                    sample: name_example
                value:
                    description:
                        - "The value of the parameter. It must be a string of 0 or more characters of any kind.
                          Examples: \\"\\" (empty string), \\"10\\", \\"mydata.xml\\", \\"${x}\\""
                    returned: on success
                    type: str
                    sample: value_example
        private_endpoint_dns_zones:
            description:
                - "An array of DNS zone names.
                  Example: `[ \\"app.examplecorp.com\\", \\"app.examplecorp2.com\\" ]`"
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        private_endpoint_max_host_count:
            description:
                - The maximum number of hosts to be accessed through the private endpoint. This value is used
                  to calculate the relevant CIDR block and should be a multiple of 256.  If the value is not a
                  multiple of 256, it is rounded up to the next multiple of 256. For example, 300 is rounded up
                  to 512.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        private_endpoint_nsg_ids:
            description:
                - An array of network security group OCIDs.
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        private_endpoint_id:
            description:
                - The OCID of a private endpoint.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
        private_endpoint_subnet_id:
            description:
                - The OCID of a subnet.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.privateendpointsubnet.oc1..xxxxxxEXAMPLExxxxxx"
        spark_version:
            description:
                - The Spark version utilized to run the application.
                - Returned for get operation
            returned: on success
            type: str
            sample: spark_version_example
        warehouse_bucket_uri:
            description:
                - An Oracle Cloud Infrastructure URI of the bucket to be used as default warehouse directory
                  for BATCH SQL runs.
                  See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.
                - Returned for get operation
            returned: on success
            type: str
            sample: warehouse_bucket_uri_example
        max_duration_in_minutes:
            description:
                - The maximum duration in minutes for which an Application should run. Data Flow Run would be terminated
                  once it reaches this duration from the time it transitions to `IN_PROGRESS` state.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        idle_timeout_in_minutes:
            description:
                - "The timeout value in minutes used to manage Runs. A Run would be stopped after inactivity for this amount of time period.
                  Note: This parameter is currently only applicable for Runs of type `SESSION`. Default value is 2880 minutes (2 days)"
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        application_id:
            description:
                - The application ID.
            returned: on success
            type: str
            sample: "ocid1.application.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of a compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        data_read_in_bytes:
            description:
                - The data read by the run in bytes.
            returned: on success
            type: int
            sample: 56
        data_written_in_bytes:
            description:
                - The data written by the run in bytes.
            returned: on success
            type: int
            sample: 56
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        display_name:
            description:
                - A user-friendly name. This name is not necessarily unique.
            returned: on success
            type: str
            sample: display_name_example
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        id:
            description:
                - The ID of a run.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        language:
            description:
                - The Spark language.
            returned: on success
            type: str
            sample: SCALA
        lifecycle_details:
            description:
                - The detailed messages about the lifecycle state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        lifecycle_state:
            description:
                - The current state of this run.
            returned: on success
            type: str
            sample: ACCEPTED
        opc_request_id:
            description:
                - Unique Oracle assigned identifier for the request.
                  If you need to contact Oracle about a particular request, please provide the request ID.
            returned: on success
            type: str
            sample: "ocid1.opcrequest.oc1..xxxxxxEXAMPLExxxxxx"
        owner_principal_id:
            description:
                - The OCID of the user who created the resource.
            returned: on success
            type: str
            sample: "ocid1.ownerprincipal.oc1..xxxxxxEXAMPLExxxxxx"
        owner_user_name:
            description:
                - The username of the user who created the resource.  If the username of the owner does not exist,
                  `null` will be returned and the caller should refer to the ownerPrincipalId value instead.
            returned: on success
            type: str
            sample: owner_user_name_example
        pool_id:
            description:
                - The OCID of a pool. Unique Id to indentify a dataflow pool resource.
            returned: on success
            type: str
            sample: "ocid1.pool.oc1..xxxxxxEXAMPLExxxxxx"
        run_duration_in_milliseconds:
            description:
                - The duration of the run in milliseconds.
            returned: on success
            type: int
            sample: 56
        total_o_cpu:
            description:
                - The total number of oCPU requested by the run.
            returned: on success
            type: int
            sample: 56
        time_created:
            description:
                - "The date and time the resource was created, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
                  Example: `2018-04-03T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - "The date and time the resource was updated, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
                  Example: `2018-04-03T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        type:
            description:
                - The Spark application processing type.
            returned: on success
            type: str
            sample: BATCH
    sample: [{
        "archive_uri": "archive_uri_example",
        "arguments": [],
        "application_log_config": {
            "log_group_id": "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx",
            "log_id": "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "class_name": "class_name_example",
        "configuration": {},
        "driver_shape": "driver_shape_example",
        "driver_shape_config": {
            "ocpus": 10,
            "memory_in_gbs": 10
        },
        "execute": "execute_example",
        "executor_shape": "executor_shape_example",
        "executor_shape_config": {
            "ocpus": 10,
            "memory_in_gbs": 10
        },
        "file_uri": "file_uri_example",
        "logs_bucket_uri": "logs_bucket_uri_example",
        "metastore_id": "ocid1.metastore.oc1..xxxxxxEXAMPLExxxxxx",
        "num_executors": 56,
        "parameters": [{
            "name": "name_example",
            "value": "value_example"
        }],
        "private_endpoint_dns_zones": [],
        "private_endpoint_max_host_count": 56,
        "private_endpoint_nsg_ids": [],
        "private_endpoint_id": "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx",
        "private_endpoint_subnet_id": "ocid1.privateendpointsubnet.oc1..xxxxxxEXAMPLExxxxxx",
        "spark_version": "spark_version_example",
        "warehouse_bucket_uri": "warehouse_bucket_uri_example",
        "max_duration_in_minutes": 56,
        "idle_timeout_in_minutes": 56,
        "application_id": "ocid1.application.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "data_read_in_bytes": 56,
        "data_written_in_bytes": 56,
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "language": "SCALA",
        "lifecycle_details": "lifecycle_details_example",
        "lifecycle_state": "ACCEPTED",
        "opc_request_id": "ocid1.opcrequest.oc1..xxxxxxEXAMPLExxxxxx",
        "owner_principal_id": "ocid1.ownerprincipal.oc1..xxxxxxEXAMPLExxxxxx",
        "owner_user_name": "owner_user_name_example",
        "pool_id": "ocid1.pool.oc1..xxxxxxEXAMPLExxxxxx",
        "run_duration_in_milliseconds": 56,
        "total_o_cpu": 56,
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "type": "BATCH"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.data_flow import DataFlowClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataFlowRunFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "run_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_run, run_id=self.module.params.get("run_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "application_id",
            "pool_id",
            "owner_principal_id",
            "display_name_starts_with",
            "lifecycle_state",
            "time_created_greater_than",
            "sort_by",
            "sort_order",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_runs,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


DataFlowRunFactsHelperCustom = get_custom_class("DataFlowRunFactsHelperCustom")


class ResourceFactsHelper(DataFlowRunFactsHelperCustom, DataFlowRunFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            run_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            application_id=dict(type="str"),
            pool_id=dict(type="str"),
            owner_principal_id=dict(type="str"),
            display_name_starts_with=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "ACCEPTED",
                    "IN_PROGRESS",
                    "CANCELING",
                    "CANCELED",
                    "FAILED",
                    "SUCCEEDED",
                    "STOPPING",
                    "STOPPED",
                ],
            ),
            time_created_greater_than=dict(type="str"),
            sort_by=dict(
                type="str",
                choices=[
                    "timeCreated",
                    "displayName",
                    "language",
                    "runDurationInMilliseconds",
                    "lifecycleState",
                    "totalOCpu",
                    "dataReadInBytes",
                    "dataWrittenInBytes",
                ],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            display_name=dict(aliases=["name"], type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="run",
        service_client_class=DataFlowClient,
        namespace="data_flow",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(runs=result)


if __name__ == "__main__":
    main()
