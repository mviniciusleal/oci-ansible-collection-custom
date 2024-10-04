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
module: oci_tenant_manager_control_plane_link_facts
short_description: Fetches details about one or multiple Link resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Link resources in Oracle Cloud Infrastructure
    - Return a (paginated) list of links.
    - If I(link_id) is specified, the details of a single Link will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    link_id:
        description:
            - OCID of the link to retrieve.
            - Required to get a specific link.
        type: str
        aliases: ["id"]
    parent_tenancy_id:
        description:
            - The ID of the parent tenancy this link is associated with.
        type: str
    child_tenancy_id:
        description:
            - The ID of the child tenancy this link is associated with.
        type: str
    lifecycle_state:
        description:
            - The lifecycle state of the resource.
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "INACTIVE"
            - "UPDATING"
            - "FAILED"
            - "TERMINATED"
    sort_order:
        description:
            - The sort order to use, whether 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific link
  oci_tenant_manager_control_plane_link_facts:
    # required
    link_id: "ocid1.link.oc1..xxxxxxEXAMPLExxxxxx"

- name: List links
  oci_tenant_manager_control_plane_link_facts:

    # optional
    parent_tenancy_id: "ocid1.parenttenancy.oc1..xxxxxxEXAMPLExxxxxx"
    child_tenancy_id: "ocid1.childtenancy.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_state: CREATING
    sort_order: ASC

"""

RETURN = """
links:
    description:
        - List of Link resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - OCID of the link.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        parent_tenancy_id:
            description:
                - OCID of the parent tenancy.
            returned: on success
            type: str
            sample: "ocid1.parenttenancy.oc1..xxxxxxEXAMPLExxxxxx"
        child_tenancy_id:
            description:
                - OCID of the child tenancy.
            returned: on success
            type: str
            sample: "ocid1.childtenancy.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - Lifecycle state of the link.
            returned: on success
            type: str
            sample: CREATING
        time_created:
            description:
                - Date-time when this link was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - Date-time when this link was last updated.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_terminated:
            description:
                - Date-time when this link was terminated.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "parent_tenancy_id": "ocid1.parenttenancy.oc1..xxxxxxEXAMPLExxxxxx",
        "child_tenancy_id": "ocid1.childtenancy.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "time_terminated": "2013-10-20T19:20:30+01:00"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.tenant_manager_control_plane import LinkClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class LinkFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "link_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_link, link_id=self.module.params.get("link_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "parent_tenancy_id",
            "child_tenancy_id",
            "lifecycle_state",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_links, **optional_kwargs
        )


LinkFactsHelperCustom = get_custom_class("LinkFactsHelperCustom")


class ResourceFactsHelper(LinkFactsHelperCustom, LinkFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            link_id=dict(aliases=["id"], type="str"),
            parent_tenancy_id=dict(type="str"),
            child_tenancy_id=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "ACTIVE",
                    "INACTIVE",
                    "UPDATING",
                    "FAILED",
                    "TERMINATED",
                ],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="link",
        service_client_class=LinkClient,
        namespace="tenant_manager_control_plane",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(links=result)


if __name__ == "__main__":
    main()
