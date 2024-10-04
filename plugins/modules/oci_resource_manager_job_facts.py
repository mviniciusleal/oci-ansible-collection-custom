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
module: oci_resource_manager_job_facts
short_description: Fetches details about one or multiple Job resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Job resources in Oracle Cloud Infrastructure
    - Lists jobs according to the specified filter. By default, the list is ordered by time created.
    - "- To list all jobs in a stack, provide the stack L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
      - To list all jobs in a compartment, provide the compartment L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
      - To return a specific job, provide the job L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm). (Equivalent to
        L(GetStack,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/resourcemanager/latest/Stack/GetStack).)"
    - If I(job_id) is specified, the details of a single Job will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    job_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the job.
            - Required to get a specific job.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - A filter to return only resources that exist in the compartment, identified by
              L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        type: str
    stack_id:
        description:
            - The stack L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) on which to filter.
        type: str
    lifecycle_state:
        description:
            - A filter that returns all resources that match the specified lifecycle state.
              The state value is case-insensitive.
            - "Allowable values:
              - ACCEPTED
              - IN_PROGRESS
              - FAILED
              - SUCCEEDED
              - CANCELING
              - CANCELED"
        type: str
        choices:
            - "ACCEPTED"
            - "IN_PROGRESS"
            - "FAILED"
            - "SUCCEEDED"
            - "CANCELING"
            - "CANCELED"
    display_name:
        description:
            - A filter to return only resources that match the given display name exactly.
              Use this filter to list a resource by name.
              Requires `sortBy` set to `DISPLAYNAME`.
              Alternatively, when you know the resource OCID, use the related Get operation.
        type: str
        aliases: ["name"]
    sort_by:
        description:
            - The field to use when sorting returned resources.
              By default, `TIMECREATED` is ordered descending.
              By default, `DISPLAYNAME` is ordered ascending. Note that you can sort only on one field.
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
    sort_order:
        description:
            - The sort order to use when sorting returned resources. Ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific job
  oci_resource_manager_job_facts:
    # required
    job_id: "ocid1.job.oc1..xxxxxxEXAMPLExxxxxx"

- name: List jobs
  oci_resource_manager_job_facts:

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    stack_id: "ocid1.stack.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_state: ACCEPTED
    display_name: display_name_example
    sort_by: TIMECREATED
    sort_order: ASC

"""

RETURN = """
jobs:
    description:
        - List of Job resources
    returned: on success
    type: complex
    contains:
        is_third_party_provider_experience_enabled:
            description:
                - When `true`, the stack sources third-party Terraform providers from
                  L(Terraform Registry,https://registry.terraform.io/browse/providers) and allows
                  L(custom providers,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/resourcemanager/latest/datatypes/CustomTerraformProvider).
                  For more information about stack sourcing of third-party Terraform providers, see
                  L(Third-party Provider
                  Configuration,https://docs.cloud.oracle.com/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm#third-party-providers).
                - Returned for get operation
            returned: on success
            type: bool
            sample: true
        is_provider_upgrade_required:
            description:
                - Specifies whether or not to upgrade provider versions.
                  Within the version constraints of your Terraform configuration, use the latest versions available from the source of Terraform providers.
                  For more information about this option, see L(Dependency Lock File (terraform.io),https://www.terraform.io/language/files/dependency-lock).
                - Returned for get operation
            returned: on success
            type: bool
            sample: true
        failure_details:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                code:
                    description:
                        - Job failure reason.
                    returned: on success
                    type: str
                    sample: INTERNAL_SERVICE_ERROR
                message:
                    description:
                        - A human-readable error string.
                    returned: on success
                    type: str
                    sample: message_example
        cancellation_details:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                is_forced:
                    description:
                        - Indicates whether a forced cancellation was requested for the job while it was running.
                          A forced cancellation can result in an incorrect state file.
                          For example, the state file might not reflect the exact state of the provisioned resources.
                    returned: on success
                    type: bool
                    sample: true
        working_directory:
            description:
                - File path to the directory to use for running Terraform.
                  If not specified, the root directory is used.
                  Required when using a zip Terraform configuration (`configSourceType` value of `ZIP_UPLOAD`) that contains folders.
                  Ignored for the `configSourceType` value of `COMPARTMENT_CONFIG_SOURCE`.
                  For more information about required and recommended file structure, see
                  L(File Structure (Terraform Configurations for Resource
                  Manager),https://docs.cloud.oracle.com/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm#filestructure).
                - Returned for get operation
            returned: on success
            type: str
            sample: working_directory_example
        variables:
            description:
                - "Terraform variables associated with this resource.
                  Maximum number of variables supported is 250.
                  The maximum size of each variable, including both name and value, is 8192 bytes.
                  Example: `{\\"CompartmentId\\": \\"compartment-id-value\\"}`"
                - Returned for get operation
            returned: on success
            type: dict
            sample: {}
        config_source:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                workspace_id:
                    description:
                        - The id of the workspace in Bitbucket Cloud for the configuration source.
                    returned: on success
                    type: str
                    sample: "ocid1.workspace.oc1..xxxxxxEXAMPLExxxxxx"
                project_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the L(DevOps
                          project,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/devops/latest/Project/).
                    returned: on success
                    type: str
                    sample: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
                repository_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the L(DevOps
                          repository,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/devops/latest/Repository/).
                    returned: on success
                    type: str
                    sample: "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx"
                configuration_source_provider_id:
                    description:
                        - Unique identifier (L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm))
                          for the Bitbucket Cloud configuration source.
                    returned: on success
                    type: str
                    sample: "ocid1.configurationsourceprovider.oc1..xxxxxxEXAMPLExxxxxx"
                repository_url:
                    description:
                        - The URL of the Bitbucket Cloud repository.
                    returned: on success
                    type: str
                    sample: repository_url_example
                branch_name:
                    description:
                        - The name of the branch within the Bitbucket Cloud repository.
                    returned: on success
                    type: str
                    sample: branch_name_example
                commit_id:
                    description:
                        - The unique identifier (SHA-1 hash) of the individual change to the Bitbucket Cloud repository.
                    returned: on success
                    type: str
                    sample: "ocid1.commit.oc1..xxxxxxEXAMPLExxxxxx"
                region:
                    description:
                        - "The name of the bucket's region.
                          Example: `us-phoenix-1`"
                    returned: on success
                    type: str
                    sample: us-phoenix-1
                namespace:
                    description:
                        - The Object Storage namespace that contains the bucket.
                    returned: on success
                    type: str
                    sample: namespace_example
                bucket_name:
                    description:
                        - The name of the bucket that contains the Terraform configuration files.
                    returned: on success
                    type: str
                    sample: bucket_name_example
                config_source_record_type:
                    description:
                        - The type of configuration source to use for the Terraform configuration.
                    returned: on success
                    type: str
                    sample: BITBUCKET_CLOUD_CONFIG_SOURCE
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the job.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        stack_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the stack that is associated with the job.
            returned: on success
            type: str
            sample: "ocid1.stack.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment in which the job's associated stack
                  resides.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The job's display name.
            returned: on success
            type: str
            sample: display_name_example
        operation:
            description:
                - The type of job executing.
            returned: on success
            type: str
            sample: PLAN
        job_operation_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                execution_plan_job_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the plan job that contains the execution
                          plan used for this job,
                          or `null` if no execution plan was used.
                    returned: on success
                    type: str
                    sample: "ocid1.executionplanjob.oc1..xxxxxxEXAMPLExxxxxx"
                execution_plan_rollback_strategy:
                    description:
                        - Specifies the source of the execution plan for rollback to apply.
                          Use `AUTO_APPROVED` to run the job without an execution plan for rollback.
                    returned: on success
                    type: str
                    sample: FROM_PLAN_ROLLBACK_JOB_ID
                execution_plan_rollback_job_id:
                    description:
                        - "The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of a plan rollback job, for use when
                          specifying `\\"FROM_PLAN_ROLLBACK_JOB_ID\\"` as the `executionPlanRollbackStrategy`."
                    returned: on success
                    type: str
                    sample: "ocid1.executionplanrollbackjob.oc1..xxxxxxEXAMPLExxxxxx"
                execution_plan_strategy:
                    description:
                        - Specifies the source of the execution plan to apply.
                          Use `AUTO_APPROVED` to run the job without an execution plan.
                    returned: on success
                    type: str
                    sample: FROM_PLAN_JOB_ID
                operation:
                    description:
                        - Terraform-specific operation to execute.
                    returned: on success
                    type: str
                    sample: APPLY
                terraform_advanced_options:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        is_refresh_required:
                            description:
                                - "Specifies whether to refresh the state for each resource before running the job (operation).
                                  Refreshing the state can affect performance. Consider setting to `false` if the configuration includes several resources.
                                  Used with the following operations: `PLAN`, `APPLY`, `DESTROY`."
                            returned: on success
                            type: bool
                            sample: true
                        parallelism:
                            description:
                                - "Limits the number of concurrent Terraform operations when L(walking the
                                  graph,https://www.terraform.io/docs/internals/graph.html#walking-the-graph).
                                  Use this parameter to help debug Terraform issues or to accomplish certain special use cases.
                                  A higher value might cause resources to be throttled.
                                  Used with the following operations: `PLAN`, `APPLY`, `DESTROY`."
                            returned: on success
                            type: int
                            sample: 56
                        detailed_log_level:
                            description:
                                - Enables detailed logs at the specified verbosity for running the job (operation).
                            returned: on success
                            type: str
                            sample: ERROR
                target_rollback_job_id:
                    description:
                        - "The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of a successful apply job, for use when
                          specifying `\\"AUTO_APPROVED\\"` as the `executionPlanRollbackStrategy`."
                    returned: on success
                    type: str
                    sample: "ocid1.targetrollbackjob.oc1..xxxxxxEXAMPLExxxxxx"
        apply_job_plan_resolution:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                plan_job_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) that specifies the most recently executed plan
                          job.
                    returned: on success
                    type: str
                    sample: "ocid1.planjob.oc1..xxxxxxEXAMPLExxxxxx"
                is_use_latest_job_id:
                    description:
                        - Specifies whether to use the L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the most recently
                          run plan job.
                          `True` if using the latest job L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm). Must be a plan job
                          that completed successfully.
                    returned: on success
                    type: bool
                    sample: true
                is_auto_approved:
                    description:
                        - Specifies whether to use the configuration directly, without reference to a Plan job.
                          `True` if using the configuration directly. Note that it is not necessary
                          for a Plan job to have run successfully.
                    returned: on success
                    type: bool
                    sample: true
        resolved_plan_job_id:
            description:
                - Deprecated. Use the property `executionPlanJobId` in `jobOperationDetails` instead.
                  The plan job L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) that was used (if this was an apply job and
                  was not auto-approved).
            returned: on success
            type: str
            sample: "ocid1.resolvedplanjob.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - "The date and time when the job was created.
                  Format is defined by RFC3339.
                  Example: `2020-01-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_finished:
            description:
                - "The date and time when the job stopped running, irrespective of whether the job ran successfully.
                  Format is defined by RFC3339.
                  Example: `2020-01-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - Current state of the specified job.
                  For more information about job lifecycle states in Resource Manager, see
                  L(Key Concepts,https://docs.cloud.oracle.com/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#concepts__JobStates).
            returned: on success
            type: str
            sample: ACCEPTED
        freeform_tags:
            description:
                - "Free-form tags associated with this resource. Each tag is a key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: [{
        "is_third_party_provider_experience_enabled": true,
        "is_provider_upgrade_required": true,
        "failure_details": {
            "code": "INTERNAL_SERVICE_ERROR",
            "message": "message_example"
        },
        "cancellation_details": {
            "is_forced": true
        },
        "working_directory": "working_directory_example",
        "variables": {},
        "config_source": {
            "workspace_id": "ocid1.workspace.oc1..xxxxxxEXAMPLExxxxxx",
            "project_id": "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx",
            "repository_id": "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx",
            "configuration_source_provider_id": "ocid1.configurationsourceprovider.oc1..xxxxxxEXAMPLExxxxxx",
            "repository_url": "repository_url_example",
            "branch_name": "branch_name_example",
            "commit_id": "ocid1.commit.oc1..xxxxxxEXAMPLExxxxxx",
            "region": "us-phoenix-1",
            "namespace": "namespace_example",
            "bucket_name": "bucket_name_example",
            "config_source_record_type": "BITBUCKET_CLOUD_CONFIG_SOURCE"
        },
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "stack_id": "ocid1.stack.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "operation": "PLAN",
        "job_operation_details": {
            "execution_plan_job_id": "ocid1.executionplanjob.oc1..xxxxxxEXAMPLExxxxxx",
            "execution_plan_rollback_strategy": "FROM_PLAN_ROLLBACK_JOB_ID",
            "execution_plan_rollback_job_id": "ocid1.executionplanrollbackjob.oc1..xxxxxxEXAMPLExxxxxx",
            "execution_plan_strategy": "FROM_PLAN_JOB_ID",
            "operation": "APPLY",
            "terraform_advanced_options": {
                "is_refresh_required": true,
                "parallelism": 56,
                "detailed_log_level": "ERROR"
            },
            "target_rollback_job_id": "ocid1.targetrollbackjob.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "apply_job_plan_resolution": {
            "plan_job_id": "ocid1.planjob.oc1..xxxxxxEXAMPLExxxxxx",
            "is_use_latest_job_id": true,
            "is_auto_approved": true
        },
        "resolved_plan_job_id": "ocid1.resolvedplanjob.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_finished": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACCEPTED",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.resource_manager import ResourceManagerClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class JobFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "job_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_job, job_id=self.module.params.get("job_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "stack_id",
            "lifecycle_state",
            "display_name",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_jobs, **optional_kwargs
        )


JobFactsHelperCustom = get_custom_class("JobFactsHelperCustom")


class ResourceFactsHelper(JobFactsHelperCustom, JobFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            job_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            stack_id=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "ACCEPTED",
                    "IN_PROGRESS",
                    "FAILED",
                    "SUCCEEDED",
                    "CANCELING",
                    "CANCELED",
                ],
            ),
            display_name=dict(aliases=["name"], type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="job",
        service_client_class=ResourceManagerClient,
        namespace="resource_manager",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(jobs=result)


if __name__ == "__main__":
    main()
