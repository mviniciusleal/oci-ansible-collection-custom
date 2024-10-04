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
module: oci_devops_trigger_facts
short_description: Fetches details about one or multiple Trigger resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Trigger resources in Oracle Cloud Infrastructure
    - Returns a list of triggers.
    - If I(trigger_id) is specified, the details of a single Trigger will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    trigger_id:
        description:
            - Unique trigger identifier.
            - Required to get a specific trigger.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The OCID of the compartment in which to list resources.
        type: str
    project_id:
        description:
            - unique project identifier
        type: str
    lifecycle_state:
        description:
            - A filter to return only triggers that matches the given lifecycle state.
        type: str
        choices:
            - "ACTIVE"
            - "DELETING"
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
        aliases: ["name"]
    sort_order:
        description:
            - The sort order to use. Use either ascending or descending.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for time created is descending. Default order for display name is
              ascending. If no value is specified, then the default time created value is considered.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific trigger
  oci_devops_trigger_facts:
    # required
    trigger_id: "ocid1.trigger.oc1..xxxxxxEXAMPLExxxxxx"

- name: List triggers
  oci_devops_trigger_facts:

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    project_id: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_state: ACTIVE
    display_name: display_name_example
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
triggers:
    description:
        - List of Trigger resources
    returned: on success
    type: complex
    contains:
        repository_id:
            description:
                - The OCID of the DevOps code repository.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx"
        actions:
            description:
                - The list of actions that are to be performed for this trigger.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                type:
                    description:
                        - The type of action that will be taken. Allowed value is TRIGGER_BUILD_PIPELINE.
                    returned: on success
                    type: str
                    sample: TRIGGER_BUILD_PIPELINE
                filter:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        trigger_source:
                            description:
                                - Source of the trigger. Allowed values are, GITHUB and GITLAB.
                            returned: on success
                            type: str
                            sample: BITBUCKET_CLOUD
                        events:
                            description:
                                - The events, for example, PUSH, PULL_REQUEST_MERGE.
                            returned: on success
                            type: list
                            sample: []
                        include:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                head_ref:
                                    description:
                                        - Branch for push event; source branch for pull requests.
                                    returned: on success
                                    type: str
                                    sample: head_ref_example
                                base_ref:
                                    description:
                                        - The target branch for pull requests; not applicable for push requests.
                                    returned: on success
                                    type: str
                                    sample: base_ref_example
                                file_filter:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        file_paths:
                                            description:
                                                - The file paths/glob pattern for files.
                                            returned: on success
                                            type: list
                                            sample: []
                                repository_name:
                                    description:
                                        - The repository name for trigger events.
                                    returned: on success
                                    type: str
                                    sample: repository_name_example
                        exclude:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                file_filter:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        file_paths:
                                            description:
                                                - The file paths/glob pattern for files.
                                            returned: on success
                                            type: list
                                            sample: []
                build_pipeline_id:
                    description:
                        - The OCID of the build pipeline to be triggered.
                    returned: on success
                    type: str
                    sample: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"
        trigger_url:
            description:
                - The endpoint that listens to trigger events.
                - Returned for get operation
            returned: on success
            type: str
            sample: trigger_url_example
        connection_id:
            description:
                - The OCID of the connection resource used to get details for triggered events.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx"
        id:
            description:
                - Unique identifier that is immutable on creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Trigger display name. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - Description about the trigger.
            returned: on success
            type: str
            sample: description_example
        project_id:
            description:
                - The OCID of the DevOps project to which the trigger belongs to.
            returned: on success
            type: str
            sample: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the compartment that contains the trigger.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        trigger_source:
            description:
                - Source of the trigger.
            returned: on success
            type: str
            sample: GITHUB
        time_created:
            description:
                - The time the trigger was created. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the trigger was updated. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the trigger.
            returned: on success
            type: str
            sample: ACTIVE
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: lifecycle_details_example
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
    sample: [{
        "repository_id": "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx",
        "actions": [{
            "type": "TRIGGER_BUILD_PIPELINE",
            "filter": {
                "trigger_source": "BITBUCKET_CLOUD",
                "events": [],
                "include": {
                    "head_ref": "head_ref_example",
                    "base_ref": "base_ref_example",
                    "file_filter": {
                        "file_paths": []
                    },
                    "repository_name": "repository_name_example"
                },
                "exclude": {
                    "file_filter": {
                        "file_paths": []
                    }
                }
            },
            "build_pipeline_id": "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"
        }],
        "trigger_url": "trigger_url_example",
        "connection_id": "ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "project_id": "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "trigger_source": "GITHUB",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACTIVE",
        "lifecycle_details": "lifecycle_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.devops import DevopsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DevopsTriggerFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "trigger_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_trigger, trigger_id=self.module.params.get("trigger_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "project_id",
            "lifecycle_state",
            "display_name",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_triggers, **optional_kwargs
        )


DevopsTriggerFactsHelperCustom = get_custom_class("DevopsTriggerFactsHelperCustom")


class ResourceFactsHelper(DevopsTriggerFactsHelperCustom, DevopsTriggerFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            trigger_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            project_id=dict(type="str"),
            lifecycle_state=dict(type="str", choices=["ACTIVE", "DELETING"]),
            display_name=dict(aliases=["name"], type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="trigger",
        service_client_class=DevopsClient,
        namespace="devops",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(triggers=result)


if __name__ == "__main__":
    main()
