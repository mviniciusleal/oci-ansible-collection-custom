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
module: oci_dashboard_service_dashboard
short_description: Manage a Dashboard resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Dashboard resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new dashboard in the dashboard group's compartment using the details provided in request body.
    - "**Caution:** Resources for the Dashboard service are created in the tenacy's home region.
      Although it is possible to create dashboard resource in regions other than the home region,
      you won't be able to view those resources in the Console.
      Therefore, creating resources outside of the home region is not recommended."
    - "This resource has the following action operations in the M(oracle.oci.oci_dashboard_service_dashboard_actions) module: change_dashboard_group."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    dashboard_group_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the dashboard group that the dashbaord is associated
              with.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    display_name:
        description:
            - "A user-friendly name for the dashboard. Does not have to be unique, and it can be changed. Avoid entering confidential information.
              Leading and trailing spaces and the following special characters are not allowed: <>()=/'\\"&\\\\"
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    description:
        description:
            - "A short description of the dashboard. It can be changed. Avoid entering confidential information.
              The following special characters are not allowed: <>()=/'\\"&\\\\"
            - This parameter is updatable.
        type: str
    schema_version:
        description:
            - The schema describing how to interpret the dashboard configuration and widgets.
            - Required for create using I(state=present), update using I(state=present) with dashboard_id present.
        type: str
        choices:
            - "V1"
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
    config:
        description:
            - The layout and widget placement for the dashboard.
            - This parameter is updatable.
        type: dict
    widgets:
        description:
            - The basic visualization building blocks of a dashboard.
            - Required for create using I(state=present).
            - This parameter is updatable.
            - Applicable when schema_version is 'V1'
        type: list
        elements: dict
    dashboard_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the dashboard.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    opc_cross_region:
        description:
            - "To identify if the call is cross-regional. In CRUD calls for a resource, to
              identify that the call originates from different region, set the
              `CrossRegionIdentifierHeader` parameter to a region name (ex - `US-ASHBURN-1`)
              The call will be served from a Replicated bucket.
              For same-region calls, the value is unassigned."
            - This parameter is updatable.
        type: str
    state:
        description:
            - The state of the Dashboard.
            - Use I(state=present) to create or update a Dashboard.
            - Use I(state=absent) to delete a Dashboard.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create dashboard with schema_version = V1
  oci_dashboard_service_dashboard:
    # required
    dashboard_group_id: "ocid1.dashboardgroup.oc1..xxxxxxEXAMPLExxxxxx"
    schema_version: V1

    # optional
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    config: null
    widgets: [ "widgets_example" ]

- name: Update dashboard with schema_version = V1
  oci_dashboard_service_dashboard:
    # required
    schema_version: V1

    # optional
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    config: null
    widgets: [ "widgets_example" ]

- name: Update dashboard using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with schema_version = V1
  oci_dashboard_service_dashboard:
    # required
    dashboard_group_id: "ocid1.dashboardgroup.oc1..xxxxxxEXAMPLExxxxxx"
    schema_version: V1

    # optional
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    config: null
    widgets: [ "widgets_example" ]

- name: Delete dashboard
  oci_dashboard_service_dashboard:
    # required
    dashboard_id: "ocid1.dashboard.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

    # optional
    opc_cross_region: us-phoenix-1

- name: Delete dashboard using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_dashboard_service_dashboard:
    # required
    dashboard_group_id: "ocid1.dashboardgroup.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
dashboard:
    description:
        - Details of the Dashboard resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the dashboard resource.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        dashboard_group_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the dashboard group that the dashboard belongs to.
            returned: on success
            type: str
            sample: "ocid1.dashboardgroup.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - "A user-friendly name for the dashboard. Does not have to be unique, and it can be changed. Avoid entering confidential information.
                  Leading and trailing spaces and the following special characters are not allowed: <>()=/'\\"&\\\\"
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - "A short description of the dashboard. It can be changed. Avoid entering confidential information.
                  The following special characters are not allowed: <>()=/'\\"&\\\\"
            returned: on success
            type: str
            sample: description_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the dashboard. A
                  dashboard is always in the same compartment as its dashboard group.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        schema_version:
            description:
                - The schema describing how to interpret the dashboard configuration and widgets.
            returned: on success
            type: str
            sample: V1
        time_created:
            description:
                - The date and time the dashboard was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the dashboard was updated, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the dashboard.
            returned: on success
            type: str
            sample: CREATING
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
        config:
            description:
                - The dashboard configuration. For example, the layout and widget placement.
            returned: on success
            type: dict
            sample: {}
        widgets:
            description:
                - The visualization building blocks of the dashboard.
            returned: on success
            type: list
            sample: []
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "dashboard_group_id": "ocid1.dashboardgroup.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "schema_version": "V1",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "config": {},
        "widgets": []
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
    from oci.dashboard_service import DashboardClient
    from oci.dashboard_service.models import CreateDashboardDetails
    from oci.dashboard_service.models import UpdateDashboardDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DashboardHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(DashboardHelperGen, self).get_possible_entity_types() + [
            "consoledashboard",
            "consoledashboards",
            "dashboardServiceconsoledashboard",
            "dashboardServiceconsoledashboards",
            "consoledashboardresource",
            "consoledashboardsresource",
            "dashboard",
            "dashboards",
            "dashboardServicedashboard",
            "dashboardServicedashboards",
            "dashboardresource",
            "dashboardsresource",
            "dashboardservice",
        ]

    def get_module_resource_id_param(self):
        return "dashboard_id"

    def get_module_resource_id(self):
        return self.module.params.get("dashboard_id")

    def get_get_fn(self):
        return self.client.get_dashboard

    def get_resource(self):
        optional_params = [
            "opc_cross_region",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_dashboard,
            dashboard_id=self.module.params.get("dashboard_id"),
            **optional_kwargs
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "dashboard_group_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["display_name", "opc_cross_region"]

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
            self.client.list_dashboards, **kwargs
        )

    def get_create_model_class(self):
        return CreateDashboardDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_dashboard,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_dashboard_details=create_details,
                opc_cross_region=self.module.params.get("opc_cross_region"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateDashboardDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_dashboard,
            call_fn_args=(),
            call_fn_kwargs=dict(
                dashboard_id=self.module.params.get("dashboard_id"),
                update_dashboard_details=update_details,
                opc_cross_region=self.module.params.get("opc_cross_region"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_dashboard,
            call_fn_args=(),
            call_fn_kwargs=dict(
                dashboard_id=self.module.params.get("dashboard_id"),
                opc_cross_region=self.module.params.get("opc_cross_region"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


DashboardHelperCustom = get_custom_class("DashboardHelperCustom")


class ResourceHelper(DashboardHelperCustom, DashboardHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            dashboard_group_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            schema_version=dict(type="str", choices=["V1"]),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            config=dict(type="dict"),
            widgets=dict(type="list", elements="dict"),
            dashboard_id=dict(aliases=["id"], type="str"),
            opc_cross_region=dict(type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="dashboard",
        service_client_class=DashboardClient,
        namespace="dashboard_service",
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
