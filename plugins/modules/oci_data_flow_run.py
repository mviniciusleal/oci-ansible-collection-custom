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
module: oci_data_flow_run
short_description: Manage a Run resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create and update a Run resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a run for an application.
    - "This resource has the following action operations in the M(oracle.oci.oci_data_flow_run_actions) module: change_compartment, cancel."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    application_log_config:
        description:
            - ""
        type: dict
        suboptions:
            log_group_id:
                description:
                    - The log group id for where log objects will be for Data Flow Runs.
                type: str
                required: true
            log_id:
                description:
                    - The log id of the log object the Application Logs of Data Flow Run will be shipped to.
                type: str
                required: true
    application_id:
        description:
            - The OCID of the associated application. If this value is set, then no value for the execute parameter is required. If this value is not set, then
              a value for the execute parameter is required, and a new application is created and associated with the new run.
        type: str
    archive_uri:
        description:
            - A comma separated list of one or more archive files as Oracle Cloud Infrastructure URIs. For example, ``oci://path/to/a.zip,oci://path/to/b.zip``.
              An Oracle Cloud Infrastructure URI of an archive.zip file containing custom dependencies that may be used to support the execution of a Python,
              Java, or Scala application.
              See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.
        type: str
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
        type: list
        elements: str
    compartment_id:
        description:
            - The OCID of a compartment.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    configuration:
        description:
            - "The Spark configuration passed to the running process.
              See https://spark.apache.org/docs/latest/configuration.html#available-properties.
              Example: { \\"spark.app.name\\" : \\"My App Name\\", \\"spark.shuffle.io.maxRetries\\" : \\"4\\" }
              Note: Not all Spark properties are permitted to be set.  Attempting to set a property that is
              not allowed to be overwritten will cause a 400 status to be returned."
        type: dict
    display_name:
        description:
            - A user-friendly name that does not have to be unique. Avoid entering confidential information. If this value is not specified, it will be derived
              from the associated application's displayName or set by API using fileUri's application file name.
            - Required for create, update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
        aliases: ["name"]
    driver_shape:
        description:
            - The VM shape for the driver. Sets the driver cores and memory.
        type: str
    driver_shape_config:
        description:
            - ""
        type: dict
        suboptions:
            ocpus:
                description:
                    - The total number of OCPUs used for the driver or executors.
                      See L(here,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/Shape/) for details.
                type: float
            memory_in_gbs:
                description:
                    - The amount of memory used for the driver or executors.
                type: float
    execute:
        description:
            - "The input used for spark-submit command. For more details see https://spark.apache.org/docs/latest/submitting-applications.html#launching-
              applications-with-spark-submit.
              Supported options include ``--class``, ``--file``, ``--jars``, ``--conf``, ``--py-files``, and main application file with arguments.
              Example: ``--jars oci://path/to/a.jar,oci://path/to/b.jar --files oci://path/to/a.json,oci://path/to/b.csv --py-files
              oci://path/to/a.py,oci://path/to/b.py --conf spark.sql.crossJoin.enabled=true --class org.apache.spark.examples.SparkPi oci://path/to/main.jar
              10``
              Note: If execute is specified together with applicationId, className, configuration, fileUri, language, arguments, parameters during application
              create/update, or run create/submit,
              Data Flow service will use derived information from execute input only."
        type: str
    executor_shape:
        description:
            - The VM shape for the executors. Sets the executor cores and memory.
        type: str
    executor_shape_config:
        description:
            - ""
        type: dict
        suboptions:
            ocpus:
                description:
                    - The total number of OCPUs used for the driver or executors.
                      See L(here,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/Shape/) for details.
                type: float
            memory_in_gbs:
                description:
                    - The amount of memory used for the driver or executors.
                type: float
    logs_bucket_uri:
        description:
            - An Oracle Cloud Infrastructure URI of the bucket where the Spark job logs are to be uploaded.
              See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.
        type: str
    metastore_id:
        description:
            - The OCID of OCI Hive Metastore.
        type: str
    num_executors:
        description:
            - The number of executor VMs requested.
        type: int
    parameters:
        description:
            - "An array of name/value pairs used to fill placeholders found in properties like
              `Application.arguments`.  The name must be a string of one or more word characters
              (a-z, A-Z, 0-9, _).  The value can be a string of 0 or more characters of any kind.
              Example:  [ { name: \\"iterations\\", value: \\"10\\"}, { name: \\"input_file\\", value: \\"mydata.xml\\" }, { name: \\"variable_x\\", value:
              \\"${x}\\"} ]"
        type: list
        elements: dict
        suboptions:
            name:
                description:
                    - "The name of the parameter.  It must be a string of one or more word characters
                      (a-z, A-Z, 0-9, _).
                      Examples: \\"iterations\\", \\"input_file\\""
                type: str
                required: true
            value:
                description:
                    - "The value of the parameter. It must be a string of 0 or more characters of any kind.
                      Examples: \\"\\" (empty string), \\"10\\", \\"mydata.xml\\", \\"${x}\\""
                type: str
                required: true
    pool_id:
        description:
            - The OCID of a pool. Unique Id to indentify a dataflow pool resource.
        type: str
    spark_version:
        description:
            - The Spark version utilized to run the application. This value may be set if applicationId is not since the Spark version will be taken from the
              associated application.
        type: str
    type:
        description:
            - The Spark application processing type.
        type: str
        choices:
            - "BATCH"
            - "STREAMING"
            - "SESSION"
    warehouse_bucket_uri:
        description:
            - An Oracle Cloud Infrastructure URI of the bucket to be used as default warehouse directory
              for BATCH SQL runs.
              See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.
        type: str
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    freeform_tags:
        description:
            - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    max_duration_in_minutes:
        description:
            - The maximum duration in minutes for which an Application should run. Data Flow Run would be terminated
              once it reaches this duration from the time it transitions to `IN_PROGRESS` state.
            - This parameter is updatable.
        type: int
    idle_timeout_in_minutes:
        description:
            - "The timeout value in minutes used to manage Runs. A Run would be stopped after inactivity for this amount of time period.
              Note: This parameter is currently only applicable for Runs of type `SESSION`. Default value is 2880 minutes (2 days)"
            - This parameter is updatable.
        type: int
    run_id:
        description:
            - The unique ID for the run
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Run.
            - Use I(state=present) to create or update a Run.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create run
  oci_data_flow_run:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    application_log_config:
      # required
      log_group_id: "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx"
      log_id: "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"
    application_id: "ocid1.application.oc1..xxxxxxEXAMPLExxxxxx"
    archive_uri: archive_uri_example
    arguments: [ "arguments_example" ]
    configuration: null
    display_name: display_name_example
    driver_shape: driver_shape_example
    driver_shape_config:
      # optional
      ocpus: 3.4
      memory_in_gbs: 3.4
    execute: execute_example
    executor_shape: executor_shape_example
    executor_shape_config:
      # optional
      ocpus: 3.4
      memory_in_gbs: 3.4
    logs_bucket_uri: logs_bucket_uri_example
    metastore_id: "ocid1.metastore.oc1..xxxxxxEXAMPLExxxxxx"
    num_executors: 56
    parameters:
    - # required
      name: name_example
      value: value_example
    pool_id: "ocid1.pool.oc1..xxxxxxEXAMPLExxxxxx"
    spark_version: spark_version_example
    type: BATCH
    warehouse_bucket_uri: warehouse_bucket_uri_example
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}
    max_duration_in_minutes: 56
    idle_timeout_in_minutes: 56

- name: Update run
  oci_data_flow_run:
    # required
    run_id: "ocid1.run.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}
    max_duration_in_minutes: 56
    idle_timeout_in_minutes: 56

- name: Update run using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_data_flow_run:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}
    max_duration_in_minutes: 56
    idle_timeout_in_minutes: 56

"""

RETURN = """
run:
    description:
        - Details of the Run resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        archive_uri:
            description:
                - A comma separated list of one or more archive files as Oracle Cloud Infrastructure URIs. For example,
                  ``oci://path/to/a.zip,oci://path/to/b.zip``. An Oracle Cloud Infrastructure URI of an archive.zip file containing custom dependencies that may
                  be used to support the execution of a Python, Java, or Scala application.
                  See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.
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
            returned: on success
            type: list
            sample: []
        application_id:
            description:
                - The application ID.
            returned: on success
            type: str
            sample: "ocid1.application.oc1..xxxxxxEXAMPLExxxxxx"
        application_log_config:
            description:
                - ""
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
            returned: on success
            type: str
            sample: class_name_example
        compartment_id:
            description:
                - The OCID of a compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        configuration:
            description:
                - "The Spark configuration passed to the running process.
                  See https://spark.apache.org/docs/latest/configuration.html#available-properties.
                  Example: { \\"spark.app.name\\" : \\"My App Name\\", \\"spark.shuffle.io.maxRetries\\" : \\"4\\" }
                  Note: Not all Spark properties are permitted to be set.  Attempting to set a property that is
                  not allowed to be overwritten will cause a 400 status to be returned."
            returned: on success
            type: dict
            sample: {}
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
        driver_shape:
            description:
                - The VM shape for the driver. Sets the driver cores and memory.
            returned: on success
            type: str
            sample: driver_shape_example
        driver_shape_config:
            description:
                - ""
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
            returned: on success
            type: str
            sample: execute_example
        executor_shape:
            description:
                - The VM shape for the executors. Sets the executor cores and memory.
            returned: on success
            type: str
            sample: executor_shape_example
        executor_shape_config:
            description:
                - ""
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
            returned: on success
            type: str
            sample: file_uri_example
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
        logs_bucket_uri:
            description:
                - An Oracle Cloud Infrastructure URI of the bucket where the Spark job logs are to be uploaded.
                  See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.
            returned: on success
            type: str
            sample: logs_bucket_uri_example
        metastore_id:
            description:
                - The OCID of OCI Hive Metastore.
            returned: on success
            type: str
            sample: "ocid1.metastore.oc1..xxxxxxEXAMPLExxxxxx"
        num_executors:
            description:
                - The number of executor VMs requested.
            returned: on success
            type: int
            sample: 56
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
        parameters:
            description:
                - "An array of name/value pairs used to fill placeholders found in properties like
                  `Application.arguments`.  The name must be a string of one or more word characters
                  (a-z, A-Z, 0-9, _).  The value can be a string of 0 or more characters of any kind.
                  Example:  [ { name: \\"iterations\\", value: \\"10\\"}, { name: \\"input_file\\", value: \\"mydata.xml\\" }, { name: \\"variable_x\\", value:
                  \\"${x}\\"} ]"
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
        pool_id:
            description:
                - The OCID of a pool. Unique Id to indentify a dataflow pool resource.
            returned: on success
            type: str
            sample: "ocid1.pool.oc1..xxxxxxEXAMPLExxxxxx"
        private_endpoint_dns_zones:
            description:
                - "An array of DNS zone names.
                  Example: `[ \\"app.examplecorp.com\\", \\"app.examplecorp2.com\\" ]`"
            returned: on success
            type: list
            sample: []
        private_endpoint_max_host_count:
            description:
                - The maximum number of hosts to be accessed through the private endpoint. This value is used
                  to calculate the relevant CIDR block and should be a multiple of 256.  If the value is not a
                  multiple of 256, it is rounded up to the next multiple of 256. For example, 300 is rounded up
                  to 512.
            returned: on success
            type: int
            sample: 56
        private_endpoint_nsg_ids:
            description:
                - An array of network security group OCIDs.
            returned: on success
            type: list
            sample: []
        private_endpoint_id:
            description:
                - The OCID of a private endpoint.
            returned: on success
            type: str
            sample: "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
        private_endpoint_subnet_id:
            description:
                - The OCID of a subnet.
            returned: on success
            type: str
            sample: "ocid1.privateendpointsubnet.oc1..xxxxxxEXAMPLExxxxxx"
        run_duration_in_milliseconds:
            description:
                - The duration of the run in milliseconds.
            returned: on success
            type: int
            sample: 56
        spark_version:
            description:
                - The Spark version utilized to run the application.
            returned: on success
            type: str
            sample: spark_version_example
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
        total_o_cpu:
            description:
                - The total number of oCPU requested by the run.
            returned: on success
            type: int
            sample: 56
        type:
            description:
                - The Spark application processing type.
            returned: on success
            type: str
            sample: BATCH
        warehouse_bucket_uri:
            description:
                - An Oracle Cloud Infrastructure URI of the bucket to be used as default warehouse directory
                  for BATCH SQL runs.
                  See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.
            returned: on success
            type: str
            sample: warehouse_bucket_uri_example
        max_duration_in_minutes:
            description:
                - The maximum duration in minutes for which an Application should run. Data Flow Run would be terminated
                  once it reaches this duration from the time it transitions to `IN_PROGRESS` state.
            returned: on success
            type: int
            sample: 56
        idle_timeout_in_minutes:
            description:
                - "The timeout value in minutes used to manage Runs. A Run would be stopped after inactivity for this amount of time period.
                  Note: This parameter is currently only applicable for Runs of type `SESSION`. Default value is 2880 minutes (2 days)"
            returned: on success
            type: int
            sample: 56
    sample: {
        "archive_uri": "archive_uri_example",
        "arguments": [],
        "application_id": "ocid1.application.oc1..xxxxxxEXAMPLExxxxxx",
        "application_log_config": {
            "log_group_id": "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx",
            "log_id": "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "class_name": "class_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "configuration": {},
        "data_read_in_bytes": 56,
        "data_written_in_bytes": 56,
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
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
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "language": "SCALA",
        "lifecycle_details": "lifecycle_details_example",
        "lifecycle_state": "ACCEPTED",
        "logs_bucket_uri": "logs_bucket_uri_example",
        "metastore_id": "ocid1.metastore.oc1..xxxxxxEXAMPLExxxxxx",
        "num_executors": 56,
        "opc_request_id": "ocid1.opcrequest.oc1..xxxxxxEXAMPLExxxxxx",
        "owner_principal_id": "ocid1.ownerprincipal.oc1..xxxxxxEXAMPLExxxxxx",
        "owner_user_name": "owner_user_name_example",
        "parameters": [{
            "name": "name_example",
            "value": "value_example"
        }],
        "pool_id": "ocid1.pool.oc1..xxxxxxEXAMPLExxxxxx",
        "private_endpoint_dns_zones": [],
        "private_endpoint_max_host_count": 56,
        "private_endpoint_nsg_ids": [],
        "private_endpoint_id": "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx",
        "private_endpoint_subnet_id": "ocid1.privateendpointsubnet.oc1..xxxxxxEXAMPLExxxxxx",
        "run_duration_in_milliseconds": 56,
        "spark_version": "spark_version_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "total_o_cpu": 56,
        "type": "BATCH",
        "warehouse_bucket_uri": "warehouse_bucket_uri_example",
        "max_duration_in_minutes": 56,
        "idle_timeout_in_minutes": 56
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.data_flow import DataFlowClient
    from oci.data_flow.models import CreateRunDetails
    from oci.data_flow.models import UpdateRunDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataFlowRunHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get and list"""

    def get_possible_entity_types(self):
        return super(DataFlowRunHelperGen, self).get_possible_entity_types() + [
            "dataflowrun",
            "dataflowruns",
            "dataFlowdataflowrun",
            "dataFlowdataflowruns",
            "dataflowrunresource",
            "dataflowrunsresource",
            "run",
            "runs",
            "dataFlowrun",
            "dataFlowruns",
            "runresource",
            "runsresource",
            "dataflow",
        ]

    def get_module_resource_id_param(self):
        return "run_id"

    def get_module_resource_id(self):
        return self.module.params.get("run_id")

    def get_get_fn(self):
        return self.client.get_run

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_run, run_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_run, run_id=self.module.params.get("run_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["application_id", "pool_id", "display_name"]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(self.client.list_runs, **kwargs)

    def get_create_model_class(self):
        return CreateRunDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_run,
            call_fn_args=(),
            call_fn_kwargs=dict(create_run_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateRunDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_run,
            call_fn_args=(),
            call_fn_kwargs=dict(
                update_run_details=update_details,
                run_id=self.module.params.get("run_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )


DataFlowRunHelperCustom = get_custom_class("DataFlowRunHelperCustom")


class ResourceHelper(DataFlowRunHelperCustom, DataFlowRunHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            application_log_config=dict(
                type="dict",
                options=dict(
                    log_group_id=dict(type="str", required=True),
                    log_id=dict(type="str", required=True),
                ),
            ),
            application_id=dict(type="str"),
            archive_uri=dict(type="str"),
            arguments=dict(type="list", elements="str"),
            compartment_id=dict(type="str"),
            configuration=dict(type="dict"),
            display_name=dict(aliases=["name"], type="str"),
            driver_shape=dict(type="str"),
            driver_shape_config=dict(
                type="dict",
                options=dict(
                    ocpus=dict(type="float"), memory_in_gbs=dict(type="float")
                ),
            ),
            execute=dict(type="str"),
            executor_shape=dict(type="str"),
            executor_shape_config=dict(
                type="dict",
                options=dict(
                    ocpus=dict(type="float"), memory_in_gbs=dict(type="float")
                ),
            ),
            logs_bucket_uri=dict(type="str"),
            metastore_id=dict(type="str"),
            num_executors=dict(type="int"),
            parameters=dict(
                type="list",
                elements="dict",
                options=dict(
                    name=dict(type="str", required=True),
                    value=dict(type="str", required=True),
                ),
            ),
            pool_id=dict(type="str"),
            spark_version=dict(type="str"),
            type=dict(type="str", choices=["BATCH", "STREAMING", "SESSION"]),
            warehouse_bucket_uri=dict(type="str"),
            defined_tags=dict(type="dict"),
            freeform_tags=dict(type="dict"),
            max_duration_in_minutes=dict(type="int"),
            idle_timeout_in_minutes=dict(type="int"),
            run_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="run",
        service_client_class=DataFlowClient,
        namespace="data_flow",
    )

    result = dict(changed=False)

    if resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
