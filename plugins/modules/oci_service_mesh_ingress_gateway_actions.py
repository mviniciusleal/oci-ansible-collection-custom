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
module: oci_service_mesh_ingress_gateway_actions
short_description: Perform actions on an IngressGateway resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an IngressGateway resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a IngressGateway resource from one compartment identifier to another. When provided, If-Match is checked against
      ETag values of the resource.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    ingress_gateway_id:
        description:
            - Unique IngressGateway identifier.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
        type: str
        required: true
    action:
        description:
            - The action to perform on the IngressGateway.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on ingress_gateway
  oci_service_mesh_ingress_gateway_actions:
    # required
    ingress_gateway_id: "ocid1.ingressgateway.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
ingress_gateway:
    description:
        - Details of the IngressGateway resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Unique identifier that is immutable on creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - A user-friendly name. The name has to be unique within the same service mesh and cannot be changed after creation.
                  Avoid entering confidential information.
                - "Example: `My unique resource name`"
            returned: on success
            type: str
            sample: name_example
        description:
            description:
                - Description of the resource. It can be changed after creation.
                  Avoid entering confidential information.
                - "Example: `This is my new resource`"
            returned: on success
            type: str
            sample: description_example
        mesh_id:
            description:
                - The OCID of the service mesh in which this ingress gateway is created.
            returned: on success
            type: str
            sample: "ocid1.mesh.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The time when this resource was created in an RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time when this resource was updated in an RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        hosts:
            description:
                - Array of hostnames and their listener configuration that this gateway will bind to.
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - A user-friendly name for the host. The name must be unique within the same ingress gateway.
                          This name can be used in the ingress gateway route table resource to attach a route to this host.
                        - "Example: `MyExampleHost`"
                    returned: on success
                    type: str
                    sample: name_example
                hostnames:
                    description:
                        - "Hostnames of the host. Applicable only for HTTP and TLS_PASSTHROUGH listeners.
                          Wildcard hostnames are supported in the prefix form.
                          Examples of valid hostnames are \\"www.example.com\\", \\"*.example.com\\", \\"*.com\\"."
                    returned: on success
                    type: list
                    sample: []
                listeners:
                    description:
                        - The listeners for the ingress gateway.
                    returned: on success
                    type: complex
                    contains:
                        protocol:
                            description:
                                - Type of protocol used.
                            returned: on success
                            type: str
                            sample: HTTP
                        port:
                            description:
                                - Port on which ingress gateway is listening.
                            returned: on success
                            type: int
                            sample: 56
                        tls:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                mode:
                                    description:
                                        - "DISABLED: Connection can only be plaintext.
                                          PERMISSIVE: Connection can be either plaintext or TLS/mTLS. If the clientValidation.trustedCaBundle property is
                                          configured for the listener, mTLS is performed and the client's certificates are validated by the gateway.
                                          TLS: Connection can only be TLS.
                                          MUTUAL_TLS: Connection can only be MTLS."
                                    returned: on success
                                    type: str
                                    sample: DISABLED
                                server_certificate:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        secret_name:
                                            description:
                                                - "Name of the secret.
                                                  For Kubernetes this is the name of the Kubernetes secret of type tls.
                                                  For other platforms the secrets must be mounted at: /etc/oci/secrets/${secretName}/tls.{key,crt}"
                                            returned: on success
                                            type: str
                                            sample: secret_name_example
                                        type:
                                            description:
                                                - Type of certificate.
                                            returned: on success
                                            type: str
                                            sample: OCI_CERTIFICATES
                                        certificate_id:
                                            description:
                                                - The OCID of the leaf certificate resource.
                                            returned: on success
                                            type: str
                                            sample: "ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx"
                                client_validation:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        trusted_ca_bundle:
                                            description:
                                                - ""
                                            returned: on success
                                            type: complex
                                            contains:
                                                secret_name:
                                                    description:
                                                        - "Name of the secret.
                                                          For Kubernetes this will be the name of an opaque Kubernetes secret with key ca.crt.
                                                          For other platforms the secret must be mounted at: /etc/oci/secrets/${secretName}/ca.crt"
                                                    returned: on success
                                                    type: str
                                                    sample: secret_name_example
                                                type:
                                                    description:
                                                        - Type of certificate.
                                                    returned: on success
                                                    type: str
                                                    sample: OCI_CERTIFICATES
                                                ca_bundle_id:
                                                    description:
                                                        - The OCID of the CA Bundle resource.
                                                    returned: on success
                                                    type: str
                                                    sample: "ocid1.cabundle.oc1..xxxxxxEXAMPLExxxxxx"
                                        subject_alternate_names:
                                            description:
                                                - A list of alternate names to verify the subject identity in the certificate presented by the client.
                                            returned: on success
                                            type: list
                                            sample: []
        mtls:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                certificate_id:
                    description:
                        - The OCID of the certificate resource that will be used for mTLS authentication with other virtual services in the mesh.
                    returned: on success
                    type: str
                    sample: "ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx"
                maximum_validity:
                    description:
                        - The number of days the mTLS certificate is valid.  This value should be less than the Maximum Validity Duration
                          for Certificates (Days) setting on the Certificate Authority associated with this Mesh.  The certificate will
                          be automatically renewed after 2/3 of the validity period, so a certificate with a maximum validity of 45 days
                          will be renewed every 30 days.
                    returned: on success
                    type: int
                    sample: 56
        access_logging:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                is_enabled:
                    description:
                        - Determines if the logging configuration is enabled.
                    returned: on success
                    type: bool
                    sample: true
        lifecycle_state:
            description:
                - The current state of the Resource.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in a Failed
                  state.
            returned: on success
            type: str
            sample: lifecycle_details_example
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
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "description": "description_example",
        "mesh_id": "ocid1.mesh.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "hosts": [{
            "name": "name_example",
            "hostnames": [],
            "listeners": [{
                "protocol": "HTTP",
                "port": 56,
                "tls": {
                    "mode": "DISABLED",
                    "server_certificate": {
                        "secret_name": "secret_name_example",
                        "type": "OCI_CERTIFICATES",
                        "certificate_id": "ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx"
                    },
                    "client_validation": {
                        "trusted_ca_bundle": {
                            "secret_name": "secret_name_example",
                            "type": "OCI_CERTIFICATES",
                            "ca_bundle_id": "ocid1.cabundle.oc1..xxxxxxEXAMPLExxxxxx"
                        },
                        "subject_alternate_names": []
                    }
                }
            }]
        }],
        "mtls": {
            "certificate_id": "ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx",
            "maximum_validity": 56
        },
        "access_logging": {
            "is_enabled": true
        },
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
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
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.service_mesh import ServiceMeshClient
    from oci.service_mesh.models import ChangeIngressGatewayCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class IngressGatewayActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "ingress_gateway_id"

    def get_module_resource_id(self):
        return self.module.params.get("ingress_gateway_id")

    def get_get_fn(self):
        return self.client.get_ingress_gateway

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_ingress_gateway,
            ingress_gateway_id=self.module.params.get("ingress_gateway_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeIngressGatewayCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_ingress_gateway_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                ingress_gateway_id=self.module.params.get("ingress_gateway_id"),
                change_ingress_gateway_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


IngressGatewayActionsHelperCustom = get_custom_class(
    "IngressGatewayActionsHelperCustom"
)


class ResourceHelper(IngressGatewayActionsHelperCustom, IngressGatewayActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            ingress_gateway_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="ingress_gateway",
        service_client_class=ServiceMeshClient,
        namespace="service_mesh",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
