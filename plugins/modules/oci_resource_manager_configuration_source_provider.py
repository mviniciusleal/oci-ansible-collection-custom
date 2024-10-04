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
module: oci_resource_manager_configuration_source_provider
short_description: Manage a ConfigurationSourceProvider resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a ConfigurationSourceProvider resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a configuration source provider in the specified compartment.
      For more information, see
      L(To create a configuration source
      provider,https://docs.cloud.oracle.com/iaas/Content/ResourceManager/Tasks/managingconfigurationsourceproviders.htm#CreateConfigurationSourceProvider).
    - "This resource has the following action operations in the M(oracle.oci.oci_resource_manager_configuration_source_provider_actions) module:
      change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment where
              you want to create the configuration source provider.
        type: str
    username:
        description:
            - The username for the user of the Bitbucket cloud repository.
            - This parameter is updatable.
            - Applicable when config_source_provider_type is 'BITBUCKET_CLOUD_USERNAME_APPPASSWORD'
            - Required when config_source_provider_type is 'BITBUCKET_CLOUD_USERNAME_APPPASSWORD'
        type: str
    secret_id:
        description:
            - The secret ocid which is used to authorize the user.
            - This parameter is updatable.
            - Required when config_source_provider_type is one of ['BITBUCKET_SERVER_ACCESS_TOKEN', 'BITBUCKET_CLOUD_USERNAME_APPPASSWORD']
        type: str
    display_name:
        description:
            - Human-readable name of the configuration source provider. Avoid entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    description:
        description:
            - Description of the configuration source provider. Avoid entering confidential information.
            - This parameter is updatable.
        type: str
    config_source_provider_type:
        description:
            - The type of configuration source provider.
              The `GITLAB_ACCESS_TOKEN` type corresponds to GitLab.
              The `GITHUB_ACCESS_TOKEN` type corresponds to GitHub.
              The `BITBUCKET_CLOUD_USERNAME_APPPASSWORD` type corresponds to Bitbucket Cloud.
              The `BITBUCKET_SERVER_ACCESS_TOKEN` type corresponds to Bitbucket Server.
            - Required for create using I(state=present), update using I(state=present) with configuration_source_provider_id present.
            - Applicable when config_source_provider_type is one of ['GITLAB_ACCESS_TOKEN', 'GITHUB_ACCESS_TOKEN', 'BITBUCKET_SERVER_ACCESS_TOKEN',
              'BITBUCKET_CLOUD_USERNAME_APPPASSWORD']
        type: str
        choices:
            - "GITLAB_ACCESS_TOKEN"
            - "BITBUCKET_CLOUD_USERNAME_APPPASSWORD"
            - "GITHUB_ACCESS_TOKEN"
            - "BITBUCKET_SERVER_ACCESS_TOKEN"
    private_server_config_details:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            private_endpoint_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of a private endpoint associated with the
                      configuration source provider.
                    - Required when config_source_provider_type is 'GITLAB_ACCESS_TOKEN'
                type: str
                required: true
            certificate_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of a certificate associated with the configuration
                      source provider.
                    - Required when config_source_provider_type is 'GITLAB_ACCESS_TOKEN'
                type: str
                required: true
    freeform_tags:
        description:
            - "Free-form tags associated with the resource. Each tag is a key-value pair with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    api_endpoint:
        description:
            - "The Git service endpoint.
              Example: `https://gitlab.com`"
            - Required for create using I(state=present).
            - This parameter is updatable.
            - Applicable when config_source_provider_type is one of ['GITLAB_ACCESS_TOKEN', 'GITHUB_ACCESS_TOKEN', 'BITBUCKET_SERVER_ACCESS_TOKEN',
              'BITBUCKET_CLOUD_USERNAME_APPPASSWORD']
        type: str
    access_token:
        description:
            - The personal access token to be configured on the GitLab repository. Avoid entering confidential information.
            - This parameter is updatable.
            - Required when config_source_provider_type is one of ['GITLAB_ACCESS_TOKEN', 'GITHUB_ACCESS_TOKEN']
        type: str
    configuration_source_provider_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the configuration source provider.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the ConfigurationSourceProvider.
            - Use I(state=present) to create or update a ConfigurationSourceProvider.
            - Use I(state=absent) to delete a ConfigurationSourceProvider.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create configuration_source_provider with config_source_provider_type = GITLAB_ACCESS_TOKEN
  oci_resource_manager_configuration_source_provider:
    # required
    config_source_provider_type: GITLAB_ACCESS_TOKEN

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    description: description_example
    private_server_config_details:
      # required
      private_endpoint_id: "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
      certificate_id: "ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    api_endpoint: api_endpoint_example
    access_token: access_token_example

- name: Create configuration_source_provider with config_source_provider_type = BITBUCKET_CLOUD_USERNAME_APPPASSWORD
  oci_resource_manager_configuration_source_provider:
    # required
    config_source_provider_type: BITBUCKET_CLOUD_USERNAME_APPPASSWORD

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    username: username_example
    secret_id: "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    description: description_example
    private_server_config_details:
      # required
      private_endpoint_id: "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
      certificate_id: "ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    api_endpoint: api_endpoint_example

- name: Create configuration_source_provider with config_source_provider_type = GITHUB_ACCESS_TOKEN
  oci_resource_manager_configuration_source_provider:
    # required
    config_source_provider_type: GITHUB_ACCESS_TOKEN

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    description: description_example
    private_server_config_details:
      # required
      private_endpoint_id: "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
      certificate_id: "ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    api_endpoint: api_endpoint_example
    access_token: access_token_example

- name: Create configuration_source_provider with config_source_provider_type = BITBUCKET_SERVER_ACCESS_TOKEN
  oci_resource_manager_configuration_source_provider:
    # required
    config_source_provider_type: BITBUCKET_SERVER_ACCESS_TOKEN

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    secret_id: "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    description: description_example
    private_server_config_details:
      # required
      private_endpoint_id: "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
      certificate_id: "ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    api_endpoint: api_endpoint_example

- name: Update configuration_source_provider with config_source_provider_type = GITLAB_ACCESS_TOKEN
  oci_resource_manager_configuration_source_provider:
    # required
    config_source_provider_type: GITLAB_ACCESS_TOKEN

    # optional
    display_name: display_name_example
    description: description_example
    private_server_config_details:
      # required
      private_endpoint_id: "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
      certificate_id: "ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    api_endpoint: api_endpoint_example
    access_token: access_token_example

- name: Update configuration_source_provider with config_source_provider_type = BITBUCKET_CLOUD_USERNAME_APPPASSWORD
  oci_resource_manager_configuration_source_provider:
    # required
    config_source_provider_type: BITBUCKET_CLOUD_USERNAME_APPPASSWORD

    # optional
    username: username_example
    secret_id: "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    description: description_example
    private_server_config_details:
      # required
      private_endpoint_id: "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
      certificate_id: "ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    api_endpoint: api_endpoint_example

- name: Update configuration_source_provider with config_source_provider_type = GITHUB_ACCESS_TOKEN
  oci_resource_manager_configuration_source_provider:
    # required
    config_source_provider_type: GITHUB_ACCESS_TOKEN

    # optional
    display_name: display_name_example
    description: description_example
    private_server_config_details:
      # required
      private_endpoint_id: "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
      certificate_id: "ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    api_endpoint: api_endpoint_example
    access_token: access_token_example

- name: Update configuration_source_provider with config_source_provider_type = BITBUCKET_SERVER_ACCESS_TOKEN
  oci_resource_manager_configuration_source_provider:
    # required
    config_source_provider_type: BITBUCKET_SERVER_ACCESS_TOKEN

    # optional
    secret_id: "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    description: description_example
    private_server_config_details:
      # required
      private_endpoint_id: "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
      certificate_id: "ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    api_endpoint: api_endpoint_example

- name: >
    Update configuration_source_provider using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
    with config_source_provider_type = GITLAB_ACCESS_TOKEN
  oci_resource_manager_configuration_source_provider:
    # required
    config_source_provider_type: GITLAB_ACCESS_TOKEN

    # optional
    display_name: display_name_example
    description: description_example
    private_server_config_details:
      # required
      private_endpoint_id: "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
      certificate_id: "ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    api_endpoint: api_endpoint_example
    access_token: access_token_example

- name: >
    Update configuration_source_provider using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
    with config_source_provider_type = BITBUCKET_CLOUD_USERNAME_APPPASSWORD
  oci_resource_manager_configuration_source_provider:
    # required
    config_source_provider_type: BITBUCKET_CLOUD_USERNAME_APPPASSWORD

    # optional
    username: username_example
    secret_id: "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    description: description_example
    private_server_config_details:
      # required
      private_endpoint_id: "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
      certificate_id: "ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    api_endpoint: api_endpoint_example

- name: >
    Update configuration_source_provider using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
    with config_source_provider_type = GITHUB_ACCESS_TOKEN
  oci_resource_manager_configuration_source_provider:
    # required
    config_source_provider_type: GITHUB_ACCESS_TOKEN

    # optional
    display_name: display_name_example
    description: description_example
    private_server_config_details:
      # required
      private_endpoint_id: "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
      certificate_id: "ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    api_endpoint: api_endpoint_example
    access_token: access_token_example

- name: >
    Update configuration_source_provider using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
    with config_source_provider_type = BITBUCKET_SERVER_ACCESS_TOKEN
  oci_resource_manager_configuration_source_provider:
    # required
    config_source_provider_type: BITBUCKET_SERVER_ACCESS_TOKEN

    # optional
    secret_id: "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    description: description_example
    private_server_config_details:
      # required
      private_endpoint_id: "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
      certificate_id: "ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    api_endpoint: api_endpoint_example

- name: Delete configuration_source_provider
  oci_resource_manager_configuration_source_provider:
    # required
    configuration_source_provider_id: "ocid1.configurationsourceprovider.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete configuration_source_provider using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_resource_manager_configuration_source_provider:
    # required
    display_name: display_name_example
    state: absent

"""

RETURN = """
configuration_source_provider:
    description:
        - Details of the ConfigurationSourceProvider resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the configuration source provider.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment where the configuration source
                  provider is located.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Human-readable display name for the configuration source provider.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - Description of the configuration source provider.
            returned: on success
            type: str
            sample: description_example
        time_created:
            description:
                - "The date and time when the configuration source provider was created.
                  Format is defined by RFC3339.
                  Example: `2020-01-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current lifecycle state of the configuration source provider.
                  For more information about configuration source provider lifecycle states in Resource Manager, see
                  L(Key Concepts,https://docs.cloud.oracle.com/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#concepts__CSPStates).
            returned: on success
            type: str
            sample: ACTIVE
        config_source_provider_type:
            description:
                - The type of configuration source provider.
                  The `BITBUCKET_CLOUD_USERNAME_APPPASSWORD` type corresponds to Bitbucket Cloud.
                  The `BITBUCKET_SERVER_ACCESS_TOKEN` type corresponds to Bitbucket Server.
                  The `GITLAB_ACCESS_TOKEN` type corresponds to GitLab.
                  The `GITHUB_ACCESS_TOKEN` type corresponds to GitHub.
            returned: on success
            type: str
            sample: BITBUCKET_CLOUD_USERNAME_APPPASSWORD
        private_server_config_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                private_endpoint_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of a private endpoint associated with the
                          configuration source provider.
                    returned: on success
                    type: str
                    sample: "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
                certificate_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of a certificate associated with the
                          configuration source provider.
                    returned: on success
                    type: str
                    sample: "ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx"
        username:
            description:
                - Username which is used to authorize the user.
            returned: on success
            type: str
            sample: username_example
        secret_id:
            description:
                - Secret ocid which is used to authorize the user.
            returned: on success
            type: str
            sample: "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags:
            description:
                - "Free-form tags associated with this resource. Each tag is a key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        api_endpoint:
            description:
                - "The Bitbucket cloud service endpoint.
                  Example: `https://bitbucket.org/`"
            returned: on success
            type: str
            sample: api_endpoint_example
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACTIVE",
        "config_source_provider_type": "BITBUCKET_CLOUD_USERNAME_APPPASSWORD",
        "private_server_config_details": {
            "private_endpoint_id": "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx",
            "certificate_id": "ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "username": "username_example",
        "secret_id": "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "api_endpoint": "api_endpoint_example"
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
    from oci.resource_manager import ResourceManagerClient
    from oci.resource_manager.models import CreateConfigurationSourceProviderDetails
    from oci.resource_manager.models import UpdateConfigurationSourceProviderDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ConfigurationSourceProviderHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(
            ConfigurationSourceProviderHelperGen, self
        ).get_possible_entity_types() + [
            "ormconfigsourceprovider",
            "ormconfigsourceproviders",
            "resourceManagerormconfigsourceprovider",
            "resourceManagerormconfigsourceproviders",
            "ormconfigsourceproviderresource",
            "ormconfigsourceprovidersresource",
            "configurationsourceprovider",
            "configurationsourceproviders",
            "resourceManagerconfigurationsourceprovider",
            "resourceManagerconfigurationsourceproviders",
            "configurationsourceproviderresource",
            "configurationsourceprovidersresource",
            "resourcemanager",
        ]

    def get_module_resource_id_param(self):
        return "configuration_source_provider_id"

    def get_module_resource_id(self):
        return self.module.params.get("configuration_source_provider_id")

    def get_get_fn(self):
        return self.client.get_configuration_source_provider

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_configuration_source_provider,
            configuration_source_provider_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_configuration_source_provider,
            configuration_source_provider_id=self.module.params.get(
                "configuration_source_provider_id"
            ),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = (
            ["compartment_id", "configuration_source_provider_id", "display_name"]
            if self._use_name_as_identifier()
            else [
                "compartment_id",
                "configuration_source_provider_id",
                "display_name",
                "config_source_provider_type",
            ]
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
            self.client.list_configuration_source_providers, **kwargs
        )

    def get_create_model_class(self):
        return CreateConfigurationSourceProviderDetails

    def get_exclude_attributes(self):
        return ["access_token"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_configuration_source_provider,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_configuration_source_provider_details=create_details,
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
        return UpdateConfigurationSourceProviderDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_configuration_source_provider,
            call_fn_args=(),
            call_fn_kwargs=dict(
                configuration_source_provider_id=self.module.params.get(
                    "configuration_source_provider_id"
                ),
                update_configuration_source_provider_details=update_details,
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
            call_fn=self.client.delete_configuration_source_provider,
            call_fn_args=(),
            call_fn_kwargs=dict(
                configuration_source_provider_id=self.module.params.get(
                    "configuration_source_provider_id"
                ),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


ConfigurationSourceProviderHelperCustom = get_custom_class(
    "ConfigurationSourceProviderHelperCustom"
)


class ResourceHelper(
    ConfigurationSourceProviderHelperCustom, ConfigurationSourceProviderHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            username=dict(type="str"),
            secret_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            config_source_provider_type=dict(
                type="str",
                choices=[
                    "GITLAB_ACCESS_TOKEN",
                    "BITBUCKET_CLOUD_USERNAME_APPPASSWORD",
                    "GITHUB_ACCESS_TOKEN",
                    "BITBUCKET_SERVER_ACCESS_TOKEN",
                ],
            ),
            private_server_config_details=dict(
                type="dict",
                options=dict(
                    private_endpoint_id=dict(type="str", required=True),
                    certificate_id=dict(type="str", required=True),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            api_endpoint=dict(type="str"),
            access_token=dict(type="str", no_log=True),
            configuration_source_provider_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="configuration_source_provider",
        service_client_class=ResourceManagerClient,
        namespace="resource_manager",
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
