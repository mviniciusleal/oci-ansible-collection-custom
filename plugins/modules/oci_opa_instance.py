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
module: oci_opa_instance
short_description: Manage an OpaInstance resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an OpaInstance resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new OpaInstance.
    - "This resource has the following action operations in the M(oracle.oci.oci_opa_instance_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - Compartment Identifier
            - Required for create using I(state=present).
        type: str
    consumption_model:
        description:
            - Parameter specifying which entitlement to use for billing purposes
        type: str
    shape_name:
        description:
            - Shape of the instance.
            - Required for create using I(state=present).
        type: str
    metering_type:
        description:
            - MeteringType Identifier
        type: str
    idcs_at:
        description:
            - IDCS Authentication token. This is required for all realms with IDCS. This property is optional, as it is not required for non-IDCS realms.
        type: str
    is_breakglass_enabled:
        description:
            - indicates if breakGlass is enabled for the opa instance.
        type: bool
    display_name:
        description:
            - OpaInstance Identifier. User-friendly name for the instance. Avoid entering confidential information. You can change this value anytime.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    description:
        description:
            - Description of the Oracle Process Automation instance.
            - This parameter is updatable.
        type: str
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    opa_instance_id:
        description:
            - unique OpaInstance identifier
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the OpaInstance.
            - Use I(state=present) to create or update an OpaInstance.
            - Use I(state=absent) to delete an OpaInstance.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create opa_instance
  oci_opa_instance:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    shape_name: shape_name_example
    display_name: display_name_example

    # optional
    consumption_model: consumption_model_example
    metering_type: metering_type_example
    idcs_at: idcs_at_example
    is_breakglass_enabled: true
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update opa_instance
  oci_opa_instance:
    # required
    opa_instance_id: "ocid1.opainstance.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update opa_instance using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_opa_instance:
    # required
    display_name: display_name_example

    # optional
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete opa_instance
  oci_opa_instance:
    # required
    opa_instance_id: "ocid1.opainstance.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete opa_instance using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_opa_instance:
    # required
    display_name: display_name_example
    state: absent

"""

RETURN = """
opa_instance:
    description:
        - Details of the OpaInstance resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Unique identifier that is immutable on creation
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - OpaInstance Identifier, can be renamed
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - Description of the Process Automation instance.
            returned: on success
            type: str
            sample: description_example
        compartment_id:
            description:
                - Compartment Identifier
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        instance_url:
            description:
                - OPA Instance URL
            returned: on success
            type: str
            sample: instance_url_example
        consumption_model:
            description:
                - The entitlement used for billing purposes
            returned: on success
            type: str
            sample: UCM
        shape_name:
            description:
                - Shape of the instance.
            returned: on success
            type: str
            sample: DEVELOPMENT
        metering_type:
            description:
                - MeteringType Identifier
            returned: on success
            type: str
            sample: EXECUTION_PACK
        time_created:
            description:
                - The time when OpaInstance was created. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the OpaInstance was updated. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the OpaInstance.
            returned: on success
            type: str
            sample: CREATING
        identity_app_guid:
            description:
                - This property specifies the GUID of the Identity Application instance OPA has created inside the user-specified identity domain. This identity
                  application instance may be used to host user role mappings to grant access to this OPA instance for users within the identity domain.
            returned: on success
            type: str
            sample: identity_app_guid_example
        identity_app_display_name:
            description:
                - This property specifies the name of the Identity Application instance OPA has created inside the user-specified identity domain. This identity
                  application instance may be used to host user roll mappings to grant access to this OPA instance for users within the identity domain.
            returned: on success
            type: str
            sample: identity_app_display_name_example
        identity_domain_url:
            description:
                - This property specifies the domain url of the Identity Application instance OPA has created inside the user-specified identity domain. This
                  identity application instance may be used to host user roll mappings to grant access to this OPA instance for users within the identity
                  domain.
            returned: on success
            type: str
            sample: identity_domain_url_example
        identity_app_opc_service_instance_guid:
            description:
                - This property specifies the OPC Service Instance GUID of the Identity Application instance OPA has created inside the user-specified identity
                  domain. This identity application instance may be used to host user roll mappings to grant access to this OPA instance for users within the
                  identity domain.
            returned: on success
            type: str
            sample: identity_app_opc_service_instance_guid_example
        is_breakglass_enabled:
            description:
                - indicates if breakGlass is enabled for the opa instance.
            returned: on success
            type: bool
            sample: true
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
        attachments:
            description:
                - A list of associated attachments to other services
            returned: on success
            type: complex
            contains:
                target_role:
                    description:
                        - "The role of the target attachment.
                             * `PARENT` - The target instance is the parent of this attachment.
                             * `CHILD` - The target instance is the child of this attachment."
                    returned: on success
                    type: str
                    sample: PARENT
                is_implicit:
                    description:
                        - "* If role == `PARENT`, the attached instance was created by this service instance
                          * If role == `CHILD`, this instance was created from attached instance on behalf of a user"
                    returned: on success
                    type: bool
                    sample: true
                target_id:
                    description:
                        - The OCID of the target instance (which could be any other OCI PaaS/SaaS resource), to which this instance is attached.
                    returned: on success
                    type: str
                    sample: "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx"
                target_instance_url:
                    description:
                        - The dataplane instance URL of the attached instance
                    returned: on success
                    type: str
                    sample: target_instance_url_example
                target_service_type:
                    description:
                        - "The type of the target instance, such as \\"FUSION\\"."
                    returned: on success
                    type: str
                    sample: target_service_type_example
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "instance_url": "instance_url_example",
        "consumption_model": "UCM",
        "shape_name": "DEVELOPMENT",
        "metering_type": "EXECUTION_PACK",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "identity_app_guid": "identity_app_guid_example",
        "identity_app_display_name": "identity_app_display_name_example",
        "identity_domain_url": "identity_domain_url_example",
        "identity_app_opc_service_instance_guid": "identity_app_opc_service_instance_guid_example",
        "is_breakglass_enabled": true,
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "attachments": [{
            "target_role": "PARENT",
            "is_implicit": true,
            "target_id": "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx",
            "target_instance_url": "target_instance_url_example",
            "target_service_type": "target_service_type_example"
        }]
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
    from oci.opa import OpaInstanceClient
    from oci.opa.models import CreateOpaInstanceDetails
    from oci.opa.models import UpdateOpaInstanceDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OpaInstanceHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(OpaInstanceHelperGen, self).get_possible_entity_types() + [
            "processautomationinstance",
            "processautomationinstances",
            "opaprocessautomationinstance",
            "opaprocessautomationinstances",
            "processautomationinstanceresource",
            "processautomationinstancesresource",
            "opainstance",
            "opainstances",
            "opaopainstance",
            "opaopainstances",
            "opainstanceresource",
            "opainstancesresource",
            "opa",
        ]

    def get_module_resource_id_param(self):
        return "opa_instance_id"

    def get_module_resource_id(self):
        return self.module.params.get("opa_instance_id")

    def get_get_fn(self):
        return self.client.get_opa_instance

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_opa_instance, opa_instance_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_opa_instance,
            opa_instance_id=self.module.params.get("opa_instance_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["compartment_id", "display_name"]

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
            self.client.list_opa_instances, **kwargs
        )

    def get_create_model_class(self):
        return CreateOpaInstanceDetails

    def get_exclude_attributes(self):
        return ["idcs_at"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_opa_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(create_opa_instance_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateOpaInstanceDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_opa_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                opa_instance_id=self.module.params.get("opa_instance_id"),
                update_opa_instance_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_opa_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                opa_instance_id=self.module.params.get("opa_instance_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


OpaInstanceHelperCustom = get_custom_class("OpaInstanceHelperCustom")


class ResourceHelper(OpaInstanceHelperCustom, OpaInstanceHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            consumption_model=dict(type="str"),
            shape_name=dict(type="str"),
            metering_type=dict(type="str"),
            idcs_at=dict(type="str"),
            is_breakglass_enabled=dict(type="bool"),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            opa_instance_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="opa_instance",
        service_client_class=OpaInstanceClient,
        namespace="opa",
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
