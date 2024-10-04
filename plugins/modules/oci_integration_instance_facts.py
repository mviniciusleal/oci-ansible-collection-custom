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
module: oci_integration_instance_facts
short_description: Fetches details about one or multiple IntegrationInstance resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple IntegrationInstance resources in Oracle Cloud Infrastructure
    - Returns a list of Integration Instances.
    - If I(integration_instance_id) is specified, the details of a single IntegrationInstance will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    integration_instance_id:
        description:
            - Unique Integration Instance identifier.
            - Required to get a specific integration_instance.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required to list multiple integration_instances.
        type: str
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable.
            - "Example: `My new resource`"
        type: str
        aliases: ["name"]
    lifecycle_state:
        description:
            - Life cycle state to query on.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "INACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order
              for TIMECREATED is descending. Default order for DISPLAYNAME is
              ascending. If no value is specified TIMECREATED is default.
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific integration_instance
  oci_integration_instance_facts:
    # required
    integration_instance_id: "ocid1.integrationinstance.oc1..xxxxxxEXAMPLExxxxxx"

- name: List integration_instances
  oci_integration_instance_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    lifecycle_state: CREATING
    sort_order: ASC
    sort_by: TIMECREATED

"""

RETURN = """
integration_instances:
    description:
        - List of IntegrationInstance resources
    returned: on success
    type: complex
    contains:
        idcs_info:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                idcs_app_location_url:
                    description:
                        - URL for the location of the IDCS Application (used by IDCS APIs)
                    returned: on success
                    type: str
                    sample: idcs_app_location_url_example
                idcs_app_display_name:
                    description:
                        - The IDCS application display name associated with the instance
                    returned: on success
                    type: str
                    sample: idcs_app_display_name_example
                idcs_app_id:
                    description:
                        - The IDCS application ID associated with the instance
                    returned: on success
                    type: str
                    sample: "ocid1.idcsapp.oc1..xxxxxxEXAMPLExxxxxx"
                idcs_app_name:
                    description:
                        - The IDCS application name associated with the instance
                    returned: on success
                    type: str
                    sample: idcs_app_name_example
                instance_primary_audience_url:
                    description:
                        - "The URL used as the primary audience for integration flows in this instance
                          type: string"
                    returned: on success
                    type: str
                    sample: instance_primary_audience_url_example
        attachments:
            description:
                - A list of associated attachments to other services
                - Returned for get operation
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
        id:
            description:
                - Unique identifier that is immutable on creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Integration Instance Identifier, can be renamed.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - Compartment Identifier.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        integration_instance_type:
            description:
                - Standard or Enterprise type,
                  Oracle Integration Generation 2 uses ENTERPRISE and STANDARD,
                  Oracle Integration 3 uses ENTERPRISEX and STANDARDX
            returned: on success
            type: str
            sample: STANDARD
        time_created:
            description:
                - The time the the IntegrationInstance was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the IntegrationInstance was updated. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the integration instance.
            returned: on success
            type: str
            sample: CREATING
        state_message:
            description:
                - An message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: state_message_example
        is_byol:
            description:
                - Bring your own license.
            returned: on success
            type: bool
            sample: true
        instance_url:
            description:
                - The Integration Instance URL.
            returned: on success
            type: str
            sample: instance_url_example
        message_packs:
            description:
                - The number of configured message packs (if any)
            returned: on success
            type: int
            sample: 56
        is_file_server_enabled:
            description:
                - The file server is enabled or not.
            returned: on success
            type: bool
            sample: true
        is_visual_builder_enabled:
            description:
                - VisualBuilder is enabled or not.
            returned: on success
            type: bool
            sample: true
        custom_endpoint:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                hostname:
                    description:
                        - A custom hostname to be used for the integration instance URL, in FQDN format.
                    returned: on success
                    type: str
                    sample: hostname_example
                certificate_secret_id:
                    description:
                        - Optional OCID of a vault/secret containing a private SSL certificate bundle to be used for the custom hostname.
                    returned: on success
                    type: str
                    sample: "ocid1.certificatesecret.oc1..xxxxxxEXAMPLExxxxxx"
                certificate_secret_version:
                    description:
                        - The secret version used for the certificate-secret-id (if certificate-secret-id is specified).
                    returned: on success
                    type: int
                    sample: 56
                alias:
                    description:
                        - When creating the DNS CNAME record for the custom hostname, this value must be specified in the rdata.
                    returned: on success
                    type: str
                    sample: alias_example
        alternate_custom_endpoints:
            description:
                - A list of alternate custom endpoints used for the integration instance URL.
            returned: on success
            type: complex
            contains:
                hostname:
                    description:
                        - A custom hostname to be used for the integration instance URL, in FQDN format.
                    returned: on success
                    type: str
                    sample: hostname_example
                certificate_secret_id:
                    description:
                        - Optional OCID of a vault/secret containing a private SSL certificate bundle to be used for the custom hostname.
                    returned: on success
                    type: str
                    sample: "ocid1.certificatesecret.oc1..xxxxxxEXAMPLExxxxxx"
                certificate_secret_version:
                    description:
                        - The secret version used for the certificate-secret-id (if certificate-secret-id is specified).
                    returned: on success
                    type: int
                    sample: 56
                alias:
                    description:
                        - When creating the DNS CNAME record for the custom hostname, this value must be specified in the rdata.
                    returned: on success
                    type: str
                    sample: alias_example
        consumption_model:
            description:
                - The entitlement used for billing purposes.
            returned: on success
            type: str
            sample: UCM
        network_endpoint_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                network_endpoint_type:
                    description:
                        - The type of network endpoint.
                    returned: on success
                    type: str
                    sample: PUBLIC
                allowlisted_http_ips:
                    description:
                        - "Source IP addresses or IP address ranges ingress rules. (ex: \\"168.122.59.5\\", \\"10.20.30.0/26\\")
                          An invalid IP or CIDR block will result in a 400 response."
                    returned: on success
                    type: list
                    sample: []
                allowlisted_http_vcns:
                    description:
                        - Virtual Cloud Networks allowed to access this network endpoint.
                    returned: on success
                    type: complex
                    contains:
                        id:
                            description:
                                - The Virtual Cloud Network OCID.
                            returned: on success
                            type: str
                            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                        allowlisted_ips:
                            description:
                                - "Source IP addresses or IP address ranges ingress rules. (ex: \\"168.122.59.5\\", \\"10.20.30.0/26\\")
                                  An invalid IP or CIDR block will result in a 400 response."
                            returned: on success
                            type: list
                            sample: []
                is_integration_vcn_allowlisted:
                    description:
                        - The Integration service's VCN is allow-listed to allow integrations to call back into other integrations
                    returned: on success
                    type: bool
                    sample: true
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name,
                  type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Usage of predefined tag keys. These predefined keys are scoped to
                  namespaces.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        shape:
            description:
                - Shape
            returned: on success
            type: str
            sample: DEVELOPMENT
        private_endpoint_outbound_connection:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                outbound_connection_type:
                    description:
                        - The type of Outbound Connection.
                    returned: on success
                    type: str
                    sample: PRIVATE_ENDPOINT
                subnet_id:
                    description:
                        - Customer Private Network VCN Subnet OCID. This is a required argument.
                    returned: on success
                    type: str
                    sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
                nsg_ids:
                    description:
                        - One or more Network security group Ids. This is an optional argument.
                    returned: on success
                    type: list
                    sample: []
    sample: [{
        "idcs_info": {
            "idcs_app_location_url": "idcs_app_location_url_example",
            "idcs_app_display_name": "idcs_app_display_name_example",
            "idcs_app_id": "ocid1.idcsapp.oc1..xxxxxxEXAMPLExxxxxx",
            "idcs_app_name": "idcs_app_name_example",
            "instance_primary_audience_url": "instance_primary_audience_url_example"
        },
        "attachments": [{
            "target_role": "PARENT",
            "is_implicit": true,
            "target_id": "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx",
            "target_instance_url": "target_instance_url_example",
            "target_service_type": "target_service_type_example"
        }],
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "integration_instance_type": "STANDARD",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "state_message": "state_message_example",
        "is_byol": true,
        "instance_url": "instance_url_example",
        "message_packs": 56,
        "is_file_server_enabled": true,
        "is_visual_builder_enabled": true,
        "custom_endpoint": {
            "hostname": "hostname_example",
            "certificate_secret_id": "ocid1.certificatesecret.oc1..xxxxxxEXAMPLExxxxxx",
            "certificate_secret_version": 56,
            "alias": "alias_example"
        },
        "alternate_custom_endpoints": [{
            "hostname": "hostname_example",
            "certificate_secret_id": "ocid1.certificatesecret.oc1..xxxxxxEXAMPLExxxxxx",
            "certificate_secret_version": 56,
            "alias": "alias_example"
        }],
        "consumption_model": "UCM",
        "network_endpoint_details": {
            "network_endpoint_type": "PUBLIC",
            "allowlisted_http_ips": [],
            "allowlisted_http_vcns": [{
                "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
                "allowlisted_ips": []
            }],
            "is_integration_vcn_allowlisted": true
        },
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "shape": "DEVELOPMENT",
        "private_endpoint_outbound_connection": {
            "outbound_connection_type": "PRIVATE_ENDPOINT",
            "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
            "nsg_ids": []
        }
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.integration import IntegrationInstanceClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class IntegrationInstanceFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "integration_instance_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_integration_instance,
            integration_instance_id=self.module.params.get("integration_instance_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "lifecycle_state",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_integration_instances,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


IntegrationInstanceFactsHelperCustom = get_custom_class(
    "IntegrationInstanceFactsHelperCustom"
)


class ResourceFactsHelper(
    IntegrationInstanceFactsHelperCustom, IntegrationInstanceFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            integration_instance_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "INACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="integration_instance",
        service_client_class=IntegrationInstanceClient,
        namespace="integration",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(integration_instances=result)


if __name__ == "__main__":
    main()
