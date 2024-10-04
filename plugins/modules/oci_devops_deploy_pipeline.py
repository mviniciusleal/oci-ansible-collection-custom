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
module: oci_devops_deploy_pipeline
short_description: Manage a DeployPipeline resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a DeployPipeline resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new deployment pipeline.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    project_id:
        description:
            - The OCID of a project.
            - Required for create using I(state=present).
        type: str
    description:
        description:
            - Optional description about the deployment pipeline.
            - This parameter is updatable.
        type: str
    display_name:
        description:
            - Deployment pipeline display name. Avoid entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    deploy_pipeline_parameters:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            items:
                description:
                    - List of parameters defined for a deployment pipeline.
                type: list
                elements: dict
                required: true
                suboptions:
                    name:
                        description:
                            - "Name of the parameter (case-sensitive). Parameter name must be ^[a-zA-Z][a-zA-Z_0-9]*$."
                        type: str
                        required: true
                    default_value:
                        description:
                            - Default value of the parameter.
                        type: str
                    description:
                        description:
                            - Description of the parameter.
                        type: str
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace. See L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    deploy_pipeline_id:
        description:
            - Unique pipeline identifier.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the DeployPipeline.
            - Use I(state=present) to create or update a DeployPipeline.
            - Use I(state=absent) to delete a DeployPipeline.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create deploy_pipeline
  oci_devops_deploy_pipeline:
    # required
    project_id: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    display_name: display_name_example
    deploy_pipeline_parameters:
      # required
      items:
      - # required
        name: name_example

        # optional
        default_value: default_value_example
        description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update deploy_pipeline
  oci_devops_deploy_pipeline:
    # required
    deploy_pipeline_id: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    display_name: display_name_example
    deploy_pipeline_parameters:
      # required
      items:
      - # required
        name: name_example

        # optional
        default_value: default_value_example
        description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update deploy_pipeline using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_devops_deploy_pipeline:
    # required
    display_name: display_name_example

    # optional
    description: description_example
    deploy_pipeline_parameters:
      # required
      items:
      - # required
        name: name_example

        # optional
        default_value: default_value_example
        description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete deploy_pipeline
  oci_devops_deploy_pipeline:
    # required
    deploy_pipeline_id: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete deploy_pipeline using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_devops_deploy_pipeline:
    # required
    display_name: display_name_example
    state: absent

"""

RETURN = """
deploy_pipeline:
    description:
        - Details of the DeployPipeline resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Unique identifier that is immutable on creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        description:
            description:
                - Optional description about the deployment pipeline.
            returned: on success
            type: str
            sample: description_example
        display_name:
            description:
                - Deployment pipeline display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        project_id:
            description:
                - The OCID of a project.
            returned: on success
            type: str
            sample: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the compartment where the pipeline is created.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_pipeline_artifacts:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                items:
                    description:
                        - List of all artifacts used in the pipeline.
                    returned: on success
                    type: complex
                    contains:
                        deploy_artifact_id:
                            description:
                                - The OCID of an artifact
                            returned: on success
                            type: str
                            sample: "ocid1.deployartifact.oc1..xxxxxxEXAMPLExxxxxx"
                        display_name:
                            description:
                                - Display name of the artifact. Avoid entering confidential information.
                            returned: on success
                            type: str
                            sample: display_name_example
                        deploy_pipeline_stages:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                items:
                                    description:
                                        - List of stages.
                                    returned: on success
                                    type: complex
                                    contains:
                                        deploy_stage_id:
                                            description:
                                                - The OCID of a stage
                                            returned: on success
                                            type: str
                                            sample: "ocid1.deploystage.oc1..xxxxxxEXAMPLExxxxxx"
                                        display_name:
                                            description:
                                                - Display name of the stage. Avoid entering confidential information.
                                            returned: on success
                                            type: str
                                            sample: display_name_example
        deploy_pipeline_environments:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                items:
                    description:
                        - List of all environments used in the pipeline.
                    returned: on success
                    type: complex
                    contains:
                        deploy_environment_id:
                            description:
                                - The OCID of an Environment
                            returned: on success
                            type: str
                            sample: "ocid1.deployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
                        display_name:
                            description:
                                - Display name of the environment. Avoid entering confidential information.
                            returned: on success
                            type: str
                            sample: display_name_example
                        deploy_pipeline_stages:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                items:
                                    description:
                                        - List of stages.
                                    returned: on success
                                    type: complex
                                    contains:
                                        deploy_stage_id:
                                            description:
                                                - The OCID of a stage
                                            returned: on success
                                            type: str
                                            sample: "ocid1.deploystage.oc1..xxxxxxEXAMPLExxxxxx"
                                        display_name:
                                            description:
                                                - Display name of the stage. Avoid entering confidential information.
                                            returned: on success
                                            type: str
                                            sample: display_name_example
        time_created:
            description:
                - Time the deployment pipeline was created. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - Time the deployment pipeline was updated. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the deployment pipeline.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        deploy_pipeline_parameters:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                items:
                    description:
                        - List of parameters defined for a deployment pipeline.
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - "Name of the parameter (case-sensitive). Parameter name must be ^[a-zA-Z][a-zA-Z_0-9]*$."
                            returned: on success
                            type: str
                            sample: name_example
                        default_value:
                            description:
                                - Default value of the parameter.
                            returned: on success
                            type: str
                            sample: default_value_example
                        description:
                            description:
                                - Description of the parameter.
                            returned: on success
                            type: str
                            sample: description_example
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace. See L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces. See L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\":
                  \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "description": "description_example",
        "display_name": "display_name_example",
        "project_id": "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "deploy_pipeline_artifacts": {
            "items": [{
                "deploy_artifact_id": "ocid1.deployartifact.oc1..xxxxxxEXAMPLExxxxxx",
                "display_name": "display_name_example",
                "deploy_pipeline_stages": {
                    "items": [{
                        "deploy_stage_id": "ocid1.deploystage.oc1..xxxxxxEXAMPLExxxxxx",
                        "display_name": "display_name_example"
                    }]
                }
            }]
        },
        "deploy_pipeline_environments": {
            "items": [{
                "deploy_environment_id": "ocid1.deployenvironment.oc1..xxxxxxEXAMPLExxxxxx",
                "display_name": "display_name_example",
                "deploy_pipeline_stages": {
                    "items": [{
                        "deploy_stage_id": "ocid1.deploystage.oc1..xxxxxxEXAMPLExxxxxx",
                        "display_name": "display_name_example"
                    }]
                }
            }]
        },
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "deploy_pipeline_parameters": {
            "items": [{
                "name": "name_example",
                "default_value": "default_value_example",
                "description": "description_example"
            }]
        },
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
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
    from oci.devops import DevopsClient
    from oci.devops.models import CreateDeployPipelineDetails
    from oci.devops.models import UpdateDeployPipelineDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DevopsDeployPipelineHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(
            DevopsDeployPipelineHelperGen, self
        ).get_possible_entity_types() + [
            "devopsdeploypipeline",
            "devopsdeploypipelines",
            "devopsdevopsdeploypipeline",
            "devopsdevopsdeploypipelines",
            "devopsdeploypipelineresource",
            "devopsdeploypipelinesresource",
            "deploypipeline",
            "deploypipelines",
            "deploypipelineresource",
            "deploypipelinesresource",
            "devops",
        ]

    def get_module_resource_id_param(self):
        return "deploy_pipeline_id"

    def get_module_resource_id(self):
        return self.module.params.get("deploy_pipeline_id")

    def get_get_fn(self):
        return self.client.get_deploy_pipeline

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_deploy_pipeline, deploy_pipeline_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_deploy_pipeline,
            deploy_pipeline_id=self.module.params.get("deploy_pipeline_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["project_id", "display_name"]

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
        return oci_common_utils.list_all_resources(
            self.client.list_deploy_pipelines, **kwargs
        )

    def get_create_model_class(self):
        return CreateDeployPipelineDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_deploy_pipeline,
            call_fn_args=(),
            call_fn_kwargs=dict(create_deploy_pipeline_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateDeployPipelineDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_deploy_pipeline,
            call_fn_args=(),
            call_fn_kwargs=dict(
                deploy_pipeline_id=self.module.params.get("deploy_pipeline_id"),
                update_deploy_pipeline_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_deploy_pipeline,
            call_fn_args=(),
            call_fn_kwargs=dict(
                deploy_pipeline_id=self.module.params.get("deploy_pipeline_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DevopsDeployPipelineHelperCustom = get_custom_class("DevopsDeployPipelineHelperCustom")


class ResourceHelper(DevopsDeployPipelineHelperCustom, DevopsDeployPipelineHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            project_id=dict(type="str"),
            description=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            deploy_pipeline_parameters=dict(
                type="dict",
                options=dict(
                    items=dict(
                        type="list",
                        elements="dict",
                        required=True,
                        options=dict(
                            name=dict(type="str", required=True),
                            default_value=dict(type="str"),
                            description=dict(type="str"),
                        ),
                    )
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            deploy_pipeline_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="deploy_pipeline",
        service_client_class=DevopsClient,
        namespace="devops",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
