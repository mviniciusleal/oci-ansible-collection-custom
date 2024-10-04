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
module: oci_announcements_service_announcements_preferences
short_description: Manage an AnnouncementsPreferences resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create and update an AnnouncementsPreferences resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a request that specifies preferences for the tenancy regarding receiving announcements by email.
    - This call is subject to an Announcements limit that applies to the total number of requests across all read or write operations. Announcements might
      throttle this call to reject an otherwise valid request when the total rate of operations exceeds 20 requests per second for a given user. The service
      might also throttle this call to reject an otherwise valid request when the total rate of operations exceeds 100 requests per second for a given tenancy.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    preference_id:
        description:
            - The ID of the preference.
            - Required for update using I(state=present).
        type: str
        aliases: ["id"]
    type:
        description:
            - The entity type, which specifies a model that either creates new announcement email preferences or updates existing preferences.
        type: str
        required: true
    is_unsubscribed:
        description:
            - A Boolean value to indicate whether the specified compartment chooses to not to receive informational announcements by email.
              (Manage preferences for receiving announcements by email by specifying the `preferenceType` attribute instead.)
            - This parameter is updatable.
        type: bool
    compartment_id:
        description:
            - The OCID of the compartment for which you want to manage announcement email preferences. (Specify the tenancy by providing the
              root compartment OCID.)
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    preference_type:
        description:
            - The string representing the user's preference, whether to opt in to only required announcements, to opt in to all announcements, including
              informational announcements, or to opt out of all announcements.
        type: str
        choices:
            - "OPT_IN_TENANT_ANNOUNCEMENTS"
            - "OPT_IN_TENANT_AND_INFORMATIONAL_ANNOUNCEMENTS"
            - "OPT_OUT_ALL_ANNOUNCEMENTS"
        required: true
    preferred_time_zone:
        description:
            - "The time zone in which the user prefers to receive announcements. Specify the preference with a value that uses the IANA Time Zone Database
              format (x-obmcs-time-zone). For example - America/Los_Angeles"
            - This parameter is updatable.
        type: str
    state:
        description:
            - The state of the AnnouncementsPreferences.
            - Use I(state=present) to create or update an AnnouncementsPreferences.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource ]
"""

EXAMPLES = """
- name: Create announcements_preferences
  oci_announcements_service_announcements_preferences:
    # required
    type: type_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    preference_type: OPT_IN_TENANT_ANNOUNCEMENTS

    # optional
    is_unsubscribed: true
    preferred_time_zone: preferred_time_zone_example

- name: Update announcements_preferences
  oci_announcements_service_announcements_preferences:
    # required
    preference_id: "ocid1.preference.oc1..xxxxxxEXAMPLExxxxxx"
    type: type_example
    preference_type: OPT_IN_TENANT_ANNOUNCEMENTS

    # optional
    is_unsubscribed: true
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    preferred_time_zone: preferred_time_zone_example

"""

RETURN = """
announcements_preferences:
    description:
        - Details of the AnnouncementsPreferences resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        type:
            description:
                - The entity type, which specifies either an object or a summary object for announcement email preferences.
            returned: on success
            type: str
            sample: type_example
        compartment_id:
            description:
                - The OCID of the compartment for which the email preferences apply. Because announcements are
                  specific to a tenancy, specify the tenancy by providing the root compartment OCID.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        id:
            description:
                - The ID of the preferences.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        is_unsubscribed:
            description:
                - A Boolean value to indicate whether the specified compartment chooses to not to receive informational announcements by email.
                  (Manage preferences for receiving announcements by email by specifying the `preferenceType` attribute instead.)
            returned: on success
            type: bool
            sample: true
        time_created:
            description:
                - When the preferences were set initially.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - When the preferences were last updated.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        preference_type:
            description:
                - The string representing the user's preference regarding receiving announcements by email.
            returned: on success
            type: str
            sample: preference_type_example
        preferred_time_zone:
            description:
                - "The time zone in which the user prefers to receive announcements. Specify the preference with a value that uses the IANA Time Zone Database
                  format (x-obmcs-time-zone). For example - America/Los_Angeles"
            returned: on success
            type: str
            sample: preferred_time_zone_example
    sample: {
        "type": "type_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "is_unsubscribed": true,
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "preference_type": "preference_type_example",
        "preferred_time_zone": "preferred_time_zone_example"
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
    from oci.announcements_service import AnnouncementsPreferencesClient
    from oci.announcements_service.models import CreateAnnouncementsPreferencesDetails
    from oci.announcements_service.models import UpdateAnnouncementsPreferencesDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AnnouncementsPreferencesHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get and list"""

    def get_possible_entity_types(self):
        return super(
            AnnouncementsPreferencesHelperGen, self
        ).get_possible_entity_types() + [
            "announcementspreferences",
            "announcementspreference",
            "announcementsServiceannouncementspreferences",
            "announcementsServiceannouncementspreference",
            "announcementspreferencesresource",
            "announcementspreferenceresource",
            "announcementsservice",
        ]

    def get_module_resource_id_param(self):
        return "preference_id"

    def get_module_resource_id(self):
        return self.module.params.get("preference_id")

    def get_get_fn(self):
        return self.client.get_announcements_preference

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_announcements_preference, preference_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_announcements_preference,
            preference_id=self.module.params.get("preference_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_announcements_preferences, **kwargs
        )

    def get_create_model_class(self):
        return CreateAnnouncementsPreferencesDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_announcements_preference,
            call_fn_args=(),
            call_fn_kwargs=dict(announcements_preference_details=create_details,),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateAnnouncementsPreferencesDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_announcements_preference,
            call_fn_args=(),
            call_fn_kwargs=dict(
                preference_id=self.module.params.get("preference_id"),
                announcements_preference_details=update_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )


AnnouncementsPreferencesHelperCustom = get_custom_class(
    "AnnouncementsPreferencesHelperCustom"
)


class ResourceHelper(
    AnnouncementsPreferencesHelperCustom, AnnouncementsPreferencesHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            preference_id=dict(aliases=["id"], type="str"),
            type=dict(type="str", required=True),
            is_unsubscribed=dict(type="bool"),
            compartment_id=dict(type="str"),
            preference_type=dict(
                type="str",
                required=True,
                choices=[
                    "OPT_IN_TENANT_ANNOUNCEMENTS",
                    "OPT_IN_TENANT_AND_INFORMATIONAL_ANNOUNCEMENTS",
                    "OPT_OUT_ALL_ANNOUNCEMENTS",
                ],
            ),
            preferred_time_zone=dict(type="str"),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="announcements_preferences",
        service_client_class=AnnouncementsPreferencesClient,
        namespace="announcements_service",
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
