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
module: oci_dts_transfer_appliance_encryption_passphrase_facts
short_description: Fetches details about a TransferApplianceEncryptionPassphrase resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a TransferApplianceEncryptionPassphrase resource in Oracle Cloud Infrastructure
    - Describes a transfer appliance encryptionPassphrase in detail
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    id:
        description:
            - ID of the Transfer Job
        type: str
        required: true
    transfer_appliance_label:
        description:
            - Label of the Transfer Appliance
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific transfer_appliance_encryption_passphrase
  oci_dts_transfer_appliance_encryption_passphrase_facts:
    # required
    id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    transfer_appliance_label: transfer_appliance_label_example

"""

RETURN = """
transfer_appliance_encryption_passphrase:
    description:
        - TransferApplianceEncryptionPassphrase resource
    returned: on success
    type: complex
    contains:
        encryption_passphrase:
            description:
                - ""
            returned: on success
            type: str
            sample: encryption_passphrase_example
    sample: {
        "encryption_passphrase": "encryption_passphrase_example"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.dts import TransferApplianceClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TransferApplianceEncryptionPassphraseFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "id",
            "transfer_appliance_label",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_transfer_appliance_encryption_passphrase,
            id=self.module.params.get("id"),
            transfer_appliance_label=self.module.params.get("transfer_appliance_label"),
        )


TransferApplianceEncryptionPassphraseFactsHelperCustom = get_custom_class(
    "TransferApplianceEncryptionPassphraseFactsHelperCustom"
)


class ResourceFactsHelper(
    TransferApplianceEncryptionPassphraseFactsHelperCustom,
    TransferApplianceEncryptionPassphraseFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            id=dict(type="str", required=True),
            transfer_appliance_label=dict(type="str", required=True),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="transfer_appliance_encryption_passphrase",
        service_client_class=TransferApplianceClient,
        namespace="dts",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(transfer_appliance_encryption_passphrase=result)


if __name__ == "__main__":
    main()
