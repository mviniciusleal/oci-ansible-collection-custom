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
module: oci_devops_connection
short_description: Manage a Connection resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Connection resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new connection.
    - "This resource has the following action operations in the M(oracle.oci.oci_devops_connection_actions) module: validate."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    project_id:
        description:
            - The OCID of the DevOps project.
            - Required for create using I(state=present).
        type: str
    username:
        description:
            - Public Bitbucket Cloud Username in plain text(not more than 30 characters)
            - This parameter is updatable.
            - Applicable when connection_type is 'BITBUCKET_CLOUD_APP_PASSWORD'
            - Required when connection_type is 'BITBUCKET_CLOUD_APP_PASSWORD'
        type: str
    app_password:
        description:
            - OCID of personal Bitbucket Cloud AppPassword saved in secret store
            - This parameter is updatable.
            - Applicable when connection_type is 'BITBUCKET_CLOUD_APP_PASSWORD'
            - Required when connection_type is 'BITBUCKET_CLOUD_APP_PASSWORD'
        type: str
    description:
        description:
            - Optional description about the connection.
            - This parameter is updatable.
        type: str
    display_name:
        description:
            - Optional connection display name. Avoid entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    connection_type:
        description:
            - The type of connection.
            - Required for create using I(state=present), update using I(state=present) with connection_id present.
        type: str
        choices:
            - "VBS_ACCESS_TOKEN"
            - "GITLAB_SERVER_ACCESS_TOKEN"
            - "BITBUCKET_SERVER_ACCESS_TOKEN"
            - "GITHUB_ACCESS_TOKEN"
            - "BITBUCKET_CLOUD_APP_PASSWORD"
            - "GITLAB_ACCESS_TOKEN"
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace. See L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    access_token:
        description:
            - The OCID of personal access token saved in secret store.
            - This parameter is updatable.
            - Applicable when connection_type is one of ['GITLAB_ACCESS_TOKEN', 'GITHUB_ACCESS_TOKEN', 'VBS_ACCESS_TOKEN', 'BITBUCKET_SERVER_ACCESS_TOKEN',
              'GITLAB_SERVER_ACCESS_TOKEN']
            - Required when connection_type is one of ['GITLAB_ACCESS_TOKEN', 'VBS_ACCESS_TOKEN', 'GITHUB_ACCESS_TOKEN', 'BITBUCKET_SERVER_ACCESS_TOKEN',
              'GITLAB_SERVER_ACCESS_TOKEN']
        type: str
    base_url:
        description:
            - The Base URL of the hosted VBS server.
            - This parameter is updatable.
            - Required when connection_type is one of ['VBS_ACCESS_TOKEN', 'BITBUCKET_SERVER_ACCESS_TOKEN', 'GITLAB_SERVER_ACCESS_TOKEN']
        type: str
    tls_verify_config:
        description:
            - ""
            - This parameter is updatable.
            - Applicable when connection_type is one of ['BITBUCKET_SERVER_ACCESS_TOKEN', 'GITLAB_SERVER_ACCESS_TOKEN']
        type: dict
        suboptions:
            tls_verify_mode:
                description:
                    - The type of TLS verification.
                type: str
                choices:
                    - "CA_CERTIFICATE_VERIFY"
                required: true
            ca_certificate_bundle_id:
                description:
                    - The OCID of OCI certificate service CA bundle.
                type: str
                required: true
    connection_id:
        description:
            - Unique connection identifier.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Connection.
            - Use I(state=present) to create or update a Connection.
            - Use I(state=absent) to delete a Connection.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create connection with connection_type = VBS_ACCESS_TOKEN
  oci_devops_connection:
    # required
    project_id: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
    connection_type: VBS_ACCESS_TOKEN

    # optional
    description: description_example
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    access_token: access_token_example
    base_url: base_url_example

- name: Create connection with connection_type = GITLAB_SERVER_ACCESS_TOKEN
  oci_devops_connection:
    # required
    project_id: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
    connection_type: GITLAB_SERVER_ACCESS_TOKEN

    # optional
    description: description_example
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    access_token: access_token_example
    base_url: base_url_example
    tls_verify_config:
      # required
      tls_verify_mode: CA_CERTIFICATE_VERIFY
      ca_certificate_bundle_id: "ocid1.cacertificatebundle.oc1..xxxxxxEXAMPLExxxxxx"

- name: Create connection with connection_type = BITBUCKET_SERVER_ACCESS_TOKEN
  oci_devops_connection:
    # required
    project_id: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
    connection_type: BITBUCKET_SERVER_ACCESS_TOKEN

    # optional
    description: description_example
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    access_token: access_token_example
    base_url: base_url_example
    tls_verify_config:
      # required
      tls_verify_mode: CA_CERTIFICATE_VERIFY
      ca_certificate_bundle_id: "ocid1.cacertificatebundle.oc1..xxxxxxEXAMPLExxxxxx"

- name: Create connection with connection_type = GITHUB_ACCESS_TOKEN
  oci_devops_connection:
    # required
    project_id: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
    connection_type: GITHUB_ACCESS_TOKEN

    # optional
    description: description_example
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    access_token: access_token_example

- name: Create connection with connection_type = BITBUCKET_CLOUD_APP_PASSWORD
  oci_devops_connection:
    # required
    project_id: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
    connection_type: BITBUCKET_CLOUD_APP_PASSWORD

    # optional
    username: username_example
    app_password: example-password
    description: description_example
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Create connection with connection_type = GITLAB_ACCESS_TOKEN
  oci_devops_connection:
    # required
    project_id: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
    connection_type: GITLAB_ACCESS_TOKEN

    # optional
    description: description_example
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    access_token: access_token_example

- name: Update connection with connection_type = VBS_ACCESS_TOKEN
  oci_devops_connection:
    # required
    connection_type: VBS_ACCESS_TOKEN

    # optional
    description: description_example
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    access_token: access_token_example
    base_url: base_url_example

- name: Update connection with connection_type = GITLAB_SERVER_ACCESS_TOKEN
  oci_devops_connection:
    # required
    connection_type: GITLAB_SERVER_ACCESS_TOKEN

    # optional
    description: description_example
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    access_token: access_token_example
    base_url: base_url_example
    tls_verify_config:
      # required
      tls_verify_mode: CA_CERTIFICATE_VERIFY
      ca_certificate_bundle_id: "ocid1.cacertificatebundle.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update connection with connection_type = BITBUCKET_SERVER_ACCESS_TOKEN
  oci_devops_connection:
    # required
    connection_type: BITBUCKET_SERVER_ACCESS_TOKEN

    # optional
    description: description_example
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    access_token: access_token_example
    base_url: base_url_example
    tls_verify_config:
      # required
      tls_verify_mode: CA_CERTIFICATE_VERIFY
      ca_certificate_bundle_id: "ocid1.cacertificatebundle.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update connection with connection_type = GITHUB_ACCESS_TOKEN
  oci_devops_connection:
    # required
    connection_type: GITHUB_ACCESS_TOKEN

    # optional
    description: description_example
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    access_token: access_token_example

- name: Update connection with connection_type = BITBUCKET_CLOUD_APP_PASSWORD
  oci_devops_connection:
    # required
    connection_type: BITBUCKET_CLOUD_APP_PASSWORD

    # optional
    username: username_example
    app_password: example-password
    description: description_example
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update connection with connection_type = GITLAB_ACCESS_TOKEN
  oci_devops_connection:
    # required
    connection_type: GITLAB_ACCESS_TOKEN

    # optional
    description: description_example
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    access_token: access_token_example

- name: Update connection using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with connection_type = VBS_ACCESS_TOKEN
  oci_devops_connection:
    # required
    connection_type: VBS_ACCESS_TOKEN

    # optional
    description: description_example
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    access_token: access_token_example
    base_url: base_url_example

- name: Update connection using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with connection_type = GITLAB_SERVER_ACCESS_TOKEN
  oci_devops_connection:
    # required
    connection_type: GITLAB_SERVER_ACCESS_TOKEN

    # optional
    description: description_example
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    access_token: access_token_example
    base_url: base_url_example
    tls_verify_config:
      # required
      tls_verify_mode: CA_CERTIFICATE_VERIFY
      ca_certificate_bundle_id: "ocid1.cacertificatebundle.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update connection using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with connection_type = BITBUCKET_SERVER_ACCESS_TOKEN
  oci_devops_connection:
    # required
    connection_type: BITBUCKET_SERVER_ACCESS_TOKEN

    # optional
    description: description_example
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    access_token: access_token_example
    base_url: base_url_example
    tls_verify_config:
      # required
      tls_verify_mode: CA_CERTIFICATE_VERIFY
      ca_certificate_bundle_id: "ocid1.cacertificatebundle.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update connection using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with connection_type = GITHUB_ACCESS_TOKEN
  oci_devops_connection:
    # required
    connection_type: GITHUB_ACCESS_TOKEN

    # optional
    description: description_example
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    access_token: access_token_example

- name: Update connection using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with connection_type = BITBUCKET_CLOUD_APP_PASSWORD
  oci_devops_connection:
    # required
    connection_type: BITBUCKET_CLOUD_APP_PASSWORD

    # optional
    username: username_example
    app_password: example-password
    description: description_example
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update connection using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with connection_type = GITLAB_ACCESS_TOKEN
  oci_devops_connection:
    # required
    connection_type: GITLAB_ACCESS_TOKEN

    # optional
    description: description_example
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    access_token: access_token_example

- name: Delete connection
  oci_devops_connection:
    # required
    connection_id: "ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete connection using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_devops_connection:
    # required
    display_name: display_name_example
    state: absent

"""

RETURN = """
connection:
    description:
        - Details of the Connection resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        username:
            description:
                - Public Bitbucket Cloud Username in plain text
            returned: on success
            type: str
            sample: username_example
        app_password:
            description:
                - OCID of personal Bitbucket Cloud AppPassword saved in secret store
            returned: on success
            type: str
            sample: example-password
        tls_verify_config:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                tls_verify_mode:
                    description:
                        - The type of TLS verification.
                    returned: on success
                    type: str
                    sample: CA_CERTIFICATE_VERIFY
                ca_certificate_bundle_id:
                    description:
                        - The OCID of OCI certificate service CA bundle.
                    returned: on success
                    type: str
                    sample: "ocid1.cacertificatebundle.oc1..xxxxxxEXAMPLExxxxxx"
        id:
            description:
                - Unique identifier that is immutable on creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        description:
            description:
                - Optional description about the connection.
            returned: on success
            type: str
            sample: description_example
        display_name:
            description:
                - Connection display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The OCID of the compartment containing the connection.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        project_id:
            description:
                - The OCID of the DevOps project.
            returned: on success
            type: str
            sample: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
        connection_type:
            description:
                - The type of connection.
            returned: on success
            type: str
            sample: GITHUB_ACCESS_TOKEN
        time_created:
            description:
                - The time the connection was created. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the connection was updated. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        last_connection_validation_result:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                result:
                    description:
                        - The latest result of whether the credentials pass the validation.
                    returned: on success
                    type: str
                    sample: PASS
                time_validated:
                    description:
                        - The latest timestamp when the connection was validated. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                message:
                    description:
                        - A message describing the result of connection validation in more detail.
                    returned: on success
                    type: str
                    sample: message_example
        lifecycle_details:
            description:
                - A detailed message describing the current state. For example, can be used to provide actionable information for a resource in Failed state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        lifecycle_state:
            description:
                - The current state of the connection.
            returned: on success
            type: str
            sample: ACTIVE
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
        access_token:
            description:
                - The OCID of personal access token saved in secret store.
            returned: on success
            type: str
            sample: access_token_example
        base_url:
            description:
                - The Base URL of the hosted BitbucketServer.
            returned: on success
            type: str
            sample: base_url_example
    sample: {
        "username": "username_example",
        "app_password": "example-password",
        "tls_verify_config": {
            "tls_verify_mode": "CA_CERTIFICATE_VERIFY",
            "ca_certificate_bundle_id": "ocid1.cacertificatebundle.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "description": "description_example",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "project_id": "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx",
        "connection_type": "GITHUB_ACCESS_TOKEN",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "last_connection_validation_result": {
            "result": "PASS",
            "time_validated": "2013-10-20T19:20:30+01:00",
            "message": "message_example"
        },
        "lifecycle_details": "lifecycle_details_example",
        "lifecycle_state": "ACTIVE",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "access_token": "access_token_example",
        "base_url": "base_url_example"
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
    from oci.devops import DevopsClient
    from oci.devops.models import CreateConnectionDetails
    from oci.devops.models import UpdateConnectionDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DevopsConnectionHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(DevopsConnectionHelperGen, self).get_possible_entity_types() + [
            "devopsconnection",
            "devopsconnections",
            "devopsdevopsconnection",
            "devopsdevopsconnections",
            "devopsconnectionresource",
            "devopsconnectionsresource",
            "connection",
            "connections",
            "connectionresource",
            "connectionsresource",
            "devops",
        ]

    def get_module_resource_id_param(self):
        return "connection_id"

    def get_module_resource_id(self):
        return self.module.params.get("connection_id")

    def get_get_fn(self):
        return self.client.get_connection

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_connection, connection_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_connection,
            connection_id=self.module.params.get("connection_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = (
            ["project_id", "display_name"]
            if self._use_name_as_identifier()
            else ["project_id", "display_name", "connection_type"]
        )

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
            self.client.list_connections, **kwargs
        )

    def get_create_model_class(self):
        return CreateConnectionDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_connection,
            call_fn_args=(),
            call_fn_kwargs=dict(create_connection_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateConnectionDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_connection,
            call_fn_args=(),
            call_fn_kwargs=dict(
                connection_id=self.module.params.get("connection_id"),
                update_connection_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_connection,
            call_fn_args=(),
            call_fn_kwargs=dict(connection_id=self.module.params.get("connection_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DevopsConnectionHelperCustom = get_custom_class("DevopsConnectionHelperCustom")


class ResourceHelper(DevopsConnectionHelperCustom, DevopsConnectionHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            project_id=dict(type="str"),
            username=dict(type="str"),
            app_password=dict(type="str", no_log=True),
            description=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            connection_type=dict(
                type="str",
                choices=[
                    "VBS_ACCESS_TOKEN",
                    "GITLAB_SERVER_ACCESS_TOKEN",
                    "BITBUCKET_SERVER_ACCESS_TOKEN",
                    "GITHUB_ACCESS_TOKEN",
                    "BITBUCKET_CLOUD_APP_PASSWORD",
                    "GITLAB_ACCESS_TOKEN",
                ],
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            access_token=dict(type="str", no_log=True),
            base_url=dict(type="str"),
            tls_verify_config=dict(
                type="dict",
                options=dict(
                    tls_verify_mode=dict(
                        type="str", required=True, choices=["CA_CERTIFICATE_VERIFY"]
                    ),
                    ca_certificate_bundle_id=dict(type="str", required=True),
                ),
            ),
            connection_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="connection",
        service_client_class=DevopsClient,
        namespace="devops",
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
