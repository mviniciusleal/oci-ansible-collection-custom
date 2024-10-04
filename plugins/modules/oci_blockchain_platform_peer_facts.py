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
module: oci_blockchain_platform_peer_facts
short_description: Fetches details about one or multiple BlockchainPlatformPeer resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple BlockchainPlatformPeer resources in Oracle Cloud Infrastructure
    - List Blockchain Platform Peers
    - If I(peer_id) is specified, the details of a single BlockchainPlatformPeer will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    peer_id:
        description:
            - Peer identifier.
            - Required to get a specific blockchain_platform_peer.
        type: str
        aliases: ["id"]
    blockchain_platform_id:
        description:
            - Unique service identifier.
        type: str
        required: true
    display_name:
        description:
            - "A user-friendly name. Does not have to be unique, and it's changeable.
              Example: `My new resource`"
        type: str
        aliases: ["name"]
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is
              ascending. If no value is specified TIMECREATED is default.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific blockchain_platform_peer
  oci_blockchain_platform_peer_facts:
    # required
    peer_id: "ocid1.peer.oc1..xxxxxxEXAMPLExxxxxx"
    blockchain_platform_id: "ocid1.blockchainplatform.oc1..xxxxxxEXAMPLExxxxxx"

- name: List blockchain_platform_peers
  oci_blockchain_platform_peer_facts:
    # required
    blockchain_platform_id: "ocid1.blockchainplatform.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
blockchain_platform_peers:
    description:
        - List of BlockchainPlatformPeer resources
    returned: on success
    type: complex
    contains:
        role:
            description:
                - Peer role
                - Returned for get operation
            returned: on success
            type: str
            sample: role_example
        alias:
            description:
                - peer alias
                - Returned for get operation
            returned: on success
            type: str
            sample: alias_example
        ocpu_allocation_param:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                ocpu_allocation_number:
                    description:
                        - Number of OCPU allocation
                    returned: on success
                    type: float
                    sample: 3.4
        host:
            description:
                - Host on which the Peer exists
                - Returned for get operation
            returned: on success
            type: str
            sample: host_example
        ad:
            description:
                - Availability Domain of peer
                - Returned for get operation
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
        peer_key:
            description:
                - peer identifier
            returned: on success
            type: str
            sample: peer_key_example
        lifecycle_state:
            description:
                - The current state of the peer.
            returned: on success
            type: str
            sample: ACTIVE
    sample: [{
        "role": "role_example",
        "alias": "alias_example",
        "ocpu_allocation_param": {
            "ocpu_allocation_number": 3.4
        },
        "host": "host_example",
        "ad": "Uocm:PHX-AD-1",
        "peer_key": "peer_key_example",
        "lifecycle_state": "ACTIVE"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.blockchain import BlockchainPlatformClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BlockchainPlatformPeerFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "blockchain_platform_id",
            "peer_id",
        ]

    def get_required_params_for_list(self):
        return [
            "blockchain_platform_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_peer,
            blockchain_platform_id=self.module.params.get("blockchain_platform_id"),
            peer_id=self.module.params.get("peer_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
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
            self.client.list_peers,
            blockchain_platform_id=self.module.params.get("blockchain_platform_id"),
            **optional_kwargs
        )


BlockchainPlatformPeerFactsHelperCustom = get_custom_class(
    "BlockchainPlatformPeerFactsHelperCustom"
)


class ResourceFactsHelper(
    BlockchainPlatformPeerFactsHelperCustom, BlockchainPlatformPeerFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            peer_id=dict(aliases=["id"], type="str"),
            blockchain_platform_id=dict(type="str", required=True),
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
        resource_type="blockchain_platform_peer",
        service_client_class=BlockchainPlatformClient,
        namespace="blockchain",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(blockchain_platform_peers=result)


if __name__ == "__main__":
    main()
