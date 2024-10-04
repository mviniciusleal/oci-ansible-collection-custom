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
module: oci_opsi_importable_compute_entity_facts
short_description: Fetches details about one or multiple ImportableComputeEntity resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ImportableComputeEntity resources in Oracle Cloud Infrastructure
    - "Gets a list of available compute intances running cloud agent to add a new hostInsight.  An Compute entity is \\"available\\"
      and will be shown if all the following conditions are true:
         1. Compute is running OCA
         2. OCI Management Agent is not enabled or If OCI Management Agent is enabled
            2.1 The agent OCID is not already being used for an existing hostInsight.
            2.2 The agent availabilityStatus = 'ACTIVE'
            2.3 The agent lifecycleState = 'ACTIVE'"
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        type: str
        required: true
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - Compute entity list sort options.
        type: str
        choices:
            - "computeId"
            - "computeDisplayName"
            - "platformType"
            - "hostName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List importable_compute_entities
  oci_opsi_importable_compute_entity_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    sort_order: ASC
    sort_by: computeId

"""

RETURN = """
importable_compute_entities:
    description:
        - List of ImportableComputeEntity resources
    returned: on success
    type: complex
    contains:
        entity_source:
            description:
                - Source of the importable agent entity.
            returned: on success
            type: str
            sample: MACS_MANAGED_EXTERNAL_HOST
        compute_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Compute Instance
            returned: on success
            type: str
            sample: "ocid1.compute.oc1..xxxxxxEXAMPLExxxxxx"
        compute_display_name:
            description:
                - The L(Display Name,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm#Display) of the Compute Instance
            returned: on success
            type: str
            sample: compute_display_name_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    sample: [{
        "entity_source": "MACS_MANAGED_EXTERNAL_HOST",
        "compute_id": "ocid1.compute.oc1..xxxxxxEXAMPLExxxxxx",
        "compute_display_name": "compute_display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.opsi import OperationsInsightsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ImportableComputeEntityFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_importable_compute_entities,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ImportableComputeEntityFactsHelperCustom = get_custom_class(
    "ImportableComputeEntityFactsHelperCustom"
)


class ResourceFactsHelper(
    ImportableComputeEntityFactsHelperCustom, ImportableComputeEntityFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(
                type="str",
                choices=["computeId", "computeDisplayName", "platformType", "hostName"],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="importable_compute_entity",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(importable_compute_entities=result)


if __name__ == "__main__":
    main()
