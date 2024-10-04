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
module: oci_golden_gate_deployment
short_description: Manage a Deployment resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Deployment resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new Deployment.
    - "This resource has the following action operations in the M(oracle.oci.oci_golden_gate_deployment_actions) module: add_deployment_lock,
      change_compartment, collect_deployment_diagnostic, deployment_wallet_exists, export_deployment_wallet, generate_library_url, import_deployment_wallet,
      remove_deployment_lock, start, stop, upgrade."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment being referenced.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    locks:
        description:
            - Locks associated with this resource.
        type: list
        elements: dict
        suboptions:
            type:
                description:
                    - Type of the lock.
                type: str
                choices:
                    - "FULL"
                    - "DELETE"
                    - "DEFAULT"
                    - "SPECIFIC_RELEASE"
                    - "CURRENT_RELEASE"
                required: true
            message:
                description:
                    - A message added by the creator of the lock. This is typically used to give an
                      indication of why the resource is locked.
                type: str
    deployment_backup_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the backup being referenced.
        type: str
    deployment_type:
        description:
            - "The type of deployment, which can be any one of the Allowed values.
              NOTE: Use of the value 'OGG' is maintained for backward compatibility purposes.
                  Its use is discouraged in favor of 'DATABASE_ORACLE'."
            - Required for create using I(state=present).
        type: str
        choices:
            - "OGG"
            - "DATABASE_ORACLE"
            - "BIGDATA"
            - "DATABASE_MICROSOFT_SQLSERVER"
            - "DATABASE_MYSQL"
            - "DATABASE_POSTGRESQL"
            - "DATABASE_DB2ZOS"
            - "GGSA"
            - "DATA_TRANSFORMS"
    display_name:
        description:
            - An object's Display Name.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    license_model:
        description:
            - The Oracle license model that applies to a Deployment.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
        choices:
            - "LICENSE_INCLUDED"
            - "BRING_YOUR_OWN_LICENSE"
    description:
        description:
            - Metadata about this specific object.
            - This parameter is updatable.
        type: str
    freeform_tags:
        description:
            - A simple key-value pair that is applied without any predefined name, type, or scope. Exists
              for cross-compatibility only.
            - "Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - Tags defined for this resource. Each key is predefined and scoped to a namespace.
            - "Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    nsg_ids:
        description:
            - An array of Network Security Group OCIDs used to define network access for either Deployments or Connections.
            - This parameter is updatable.
        type: list
        elements: str
    subnet_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the subnet of the deployment's private endpoint.
              The subnet must be a private subnet. For backward compatibility, public subnets are allowed until May 31 2025,
              after which the private subnet will be enforced.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    load_balancer_subnet_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of a public subnet in the customer tenancy.
              Can be provided only for public deployments. If provided, the loadbalancer will be created in this subnet instead of the service tenancy.
              For backward compatibility, this is an optional property. It will become mandatory for public deployments after October 1, 2024.
            - This parameter is updatable.
        type: str
    is_public:
        description:
            - True if this object is publicly available.
            - This parameter is updatable.
        type: bool
    fqdn:
        description:
            - A three-label Fully Qualified Domain Name (FQDN) for a resource.
            - This parameter is updatable.
        type: str
    cpu_core_count:
        description:
            - The Minimum number of OCPUs to be made available for this Deployment.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: int
    is_auto_scaling_enabled:
        description:
            - Indicates if auto scaling is enabled for the Deployment's CPU core count.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: bool
    ogg_data:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            deployment_name:
                description:
                    - The name given to the GoldenGate service deployment.
                      The name must be 1 to 32 characters long, must contain only alphanumeric characters and must start with a letter.
                type: str
            ogg_version:
                description:
                    - Version of OGG
                type: str
            credential_store:
                description:
                    - The type of credential store for OGG.
                    - This parameter is updatable.
                type: str
                choices:
                    - "GOLDENGATE"
                    - "IAM"
            identity_domain_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Identity Domain when IAM credential store is
                      used.
                    - This parameter is updatable.
                type: str
            password_secret_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Secret where the deployment password is stored.
                    - This parameter is updatable.
                type: str
            admin_username:
                description:
                    - The GoldenGate deployment console username.
                    - This parameter is updatable.
                type: str
            admin_password:
                description:
                    - "The password associated with the GoldenGate deployment console username.
                      The password must be 8 to 30 characters long and must contain at least 1 uppercase, 1 lowercase, 1 numeric,
                      and 1 special character. Special characters such as '$', '^', or '?' are not allowed.
                      This field will be deprecated and replaced by \\"passwordSecretId\\"."
                    - This parameter is updatable.
                type: str
            certificate:
                description:
                    - The base64 encoded content of the PEM file containing the SSL certificate.
                    - This parameter is updatable.
                type: str
            key:
                description:
                    - The base64 encoded content of the PEM file containing the private key.
                    - This parameter is updatable.
                type: str
    maintenance_window:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            day:
                description:
                    - Days of the week.
                    - This parameter is updatable.
                type: str
                choices:
                    - "MONDAY"
                    - "TUESDAY"
                    - "WEDNESDAY"
                    - "THURSDAY"
                    - "FRIDAY"
                    - "SATURDAY"
                    - "SUNDAY"
                required: true
            start_hour:
                description:
                    - Start hour for maintenance period. Hour is in UTC.
                    - This parameter is updatable.
                type: int
                required: true
    maintenance_configuration:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            is_interim_release_auto_upgrade_enabled:
                description:
                    - By default auto upgrade for interim releases are not enabled. If auto-upgrade is enabled for interim release,
                      you have to specify interimReleaseUpgradePeriodInDays too.
                    - This parameter is updatable.
                type: bool
            interim_release_upgrade_period_in_days:
                description:
                    - Defines auto upgrade period for interim releases. This period must be shorter or equal to bundle release upgrade period.
                    - This parameter is updatable.
                type: int
            bundle_release_upgrade_period_in_days:
                description:
                    - Defines auto upgrade period for bundle releases. Manually configured period cannot be longer than service defined period for bundle
                      releases.
                      This period must be shorter or equal to major release upgrade period. Not passing this field during create will equate to using the
                      service default.
                    - This parameter is updatable.
                type: int
            major_release_upgrade_period_in_days:
                description:
                    - Defines auto upgrade period for major releases. Manually configured period cannot be longer than service defined period for major
                      releases.
                      Not passing this field during create will equate to using the service default.
                    - This parameter is updatable.
                type: int
            security_patch_upgrade_period_in_days:
                description:
                    - Defines auto upgrade period for releases with security fix. Manually configured period cannot be longer than service defined period for
                      security releases.
                      Not passing this field during create will equate to using the service default.
                    - This parameter is updatable.
                type: int
    deployment_id:
        description:
            - A unique Deployment identifier.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    is_lock_override:
        description:
            - Whether to override locks (if any exist).
            - This parameter is updatable.
        type: bool
    state:
        description:
            - The state of the Deployment.
            - Use I(state=present) to create or update a Deployment.
            - Use I(state=absent) to delete a Deployment.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create deployment
  oci_golden_gate_deployment:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    deployment_type: OGG
    display_name: display_name_example
    license_model: LICENSE_INCLUDED
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    cpu_core_count: 56
    is_auto_scaling_enabled: true

    # optional
    locks:
    - # required
      type: FULL

      # optional
      message: message_example
    deployment_backup_id: "ocid1.deploymentbackup.oc1..xxxxxxEXAMPLExxxxxx"
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    nsg_ids: [ "nsg_ids_example" ]
    load_balancer_subnet_id: "ocid1.loadbalancersubnet.oc1..xxxxxxEXAMPLExxxxxx"
    is_public: true
    fqdn: fqdn_example
    ogg_data:
      # optional
      deployment_name: deployment_name_example
      ogg_version: ogg_version_example
      credential_store: GOLDENGATE
      identity_domain_id: "ocid1.identitydomain.oc1..xxxxxxEXAMPLExxxxxx"
      password_secret_id: "ocid1.passwordsecret.oc1..xxxxxxEXAMPLExxxxxx"
      admin_username: admin_username_example
      admin_password: example-password
      certificate: "-----BEGIN CERTIFICATE----MIIBIjANBgkqhkiG9w0BA..-----END PUBLIC KEY-----"
      key: key_example
    maintenance_window:
      # required
      day: MONDAY
      start_hour: 56
    maintenance_configuration:
      # optional
      is_interim_release_auto_upgrade_enabled: true
      interim_release_upgrade_period_in_days: 56
      bundle_release_upgrade_period_in_days: 56
      major_release_upgrade_period_in_days: 56
      security_patch_upgrade_period_in_days: 56

- name: Update deployment
  oci_golden_gate_deployment:
    # required
    deployment_id: "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    license_model: LICENSE_INCLUDED
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    nsg_ids: [ "nsg_ids_example" ]
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    load_balancer_subnet_id: "ocid1.loadbalancersubnet.oc1..xxxxxxEXAMPLExxxxxx"
    is_public: true
    fqdn: fqdn_example
    cpu_core_count: 56
    is_auto_scaling_enabled: true
    ogg_data:
      # optional
      deployment_name: deployment_name_example
      ogg_version: ogg_version_example
      credential_store: GOLDENGATE
      identity_domain_id: "ocid1.identitydomain.oc1..xxxxxxEXAMPLExxxxxx"
      password_secret_id: "ocid1.passwordsecret.oc1..xxxxxxEXAMPLExxxxxx"
      admin_username: admin_username_example
      admin_password: example-password
      certificate: "-----BEGIN CERTIFICATE----MIIBIjANBgkqhkiG9w0BA..-----END PUBLIC KEY-----"
      key: key_example
    maintenance_window:
      # required
      day: MONDAY
      start_hour: 56
    maintenance_configuration:
      # optional
      is_interim_release_auto_upgrade_enabled: true
      interim_release_upgrade_period_in_days: 56
      bundle_release_upgrade_period_in_days: 56
      major_release_upgrade_period_in_days: 56
      security_patch_upgrade_period_in_days: 56
    is_lock_override: true

- name: Update deployment using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_golden_gate_deployment:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    license_model: LICENSE_INCLUDED
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    nsg_ids: [ "nsg_ids_example" ]
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    load_balancer_subnet_id: "ocid1.loadbalancersubnet.oc1..xxxxxxEXAMPLExxxxxx"
    is_public: true
    fqdn: fqdn_example
    cpu_core_count: 56
    is_auto_scaling_enabled: true
    ogg_data:
      # optional
      deployment_name: deployment_name_example
      ogg_version: ogg_version_example
      credential_store: GOLDENGATE
      identity_domain_id: "ocid1.identitydomain.oc1..xxxxxxEXAMPLExxxxxx"
      password_secret_id: "ocid1.passwordsecret.oc1..xxxxxxEXAMPLExxxxxx"
      admin_username: admin_username_example
      admin_password: example-password
      certificate: "-----BEGIN CERTIFICATE----MIIBIjANBgkqhkiG9w0BA..-----END PUBLIC KEY-----"
      key: key_example
    maintenance_window:
      # required
      day: MONDAY
      start_hour: 56
    maintenance_configuration:
      # optional
      is_interim_release_auto_upgrade_enabled: true
      interim_release_upgrade_period_in_days: 56
      bundle_release_upgrade_period_in_days: 56
      major_release_upgrade_period_in_days: 56
      security_patch_upgrade_period_in_days: 56
    is_lock_override: true

- name: Delete deployment
  oci_golden_gate_deployment:
    # required
    deployment_id: "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

    # optional
    is_lock_override: true

- name: Delete deployment using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_golden_gate_deployment:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
deployment:
    description:
        - Details of the Deployment resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the deployment being referenced.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - An object's Display Name.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - Metadata about this specific object.
            returned: on success
            type: str
            sample: description_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment being referenced.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        deployment_backup_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the backup being referenced.
            returned: on success
            type: str
            sample: "ocid1.deploymentbackup.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The time the resource was created. The format is defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the resource was last updated. The format is defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - Possible lifecycle states.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_sub_state:
            description:
                - Possible GGS lifecycle sub-states.
            returned: on success
            type: str
            sample: RECOVERING
        lifecycle_details:
            description:
                - Describes the object's current state in detail. For example, it can be used to provide
                  actionable information for a resource in a Failed state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        freeform_tags:
            description:
                - A simple key-value pair that is applied without any predefined name, type, or scope. Exists
                  for cross-compatibility only.
                - "Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Tags defined for this resource. Each key is predefined and scoped to a namespace.
                - "Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        locks:
            description:
                - Locks associated with this resource.
            returned: on success
            type: complex
            contains:
                type:
                    description:
                        - Type of the lock.
                    returned: on success
                    type: str
                    sample: FULL
                related_resource_id:
                    description:
                        - The id of the resource that is locking this resource. Indicates that deleting this resource will remove the lock.
                    returned: on success
                    type: str
                    sample: "ocid1.relatedresource.oc1..xxxxxxEXAMPLExxxxxx"
                message:
                    description:
                        - A message added by the creator of the lock. This is typically used to give an
                          indication of why the resource is locked.
                    returned: on success
                    type: str
                    sample: message_example
                time_created:
                    description:
                        - When the lock was created.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
        is_healthy:
            description:
                - True if all of the aggregate resources are working correctly.
            returned: on success
            type: bool
            sample: true
        subnet_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the subnet of the deployment's private endpoint.
                  The subnet must be a private subnet. For backward compatibility, public subnets are allowed until May 31 2025,
                  after which the private subnet will be enforced.
            returned: on success
            type: str
            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        load_balancer_subnet_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of a public subnet in the customer tenancy.
                  Can be provided only for public deployments. If provided, the loadbalancer will be created in this subnet instead of the service tenancy.
                  For backward compatibility, this is an optional property. It will become mandatory for public deployments after October 1, 2024.
            returned: on success
            type: str
            sample: "ocid1.loadbalancersubnet.oc1..xxxxxxEXAMPLExxxxxx"
        load_balancer_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the loadbalancer in the customer's subnet.
                  The loadbalancer of the public deployment created in the customer subnet.
            returned: on success
            type: str
            sample: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
        fqdn:
            description:
                - A three-label Fully Qualified Domain Name (FQDN) for a resource.
            returned: on success
            type: str
            sample: fqdn_example
        license_model:
            description:
                - The Oracle license model that applies to a Deployment.
            returned: on success
            type: str
            sample: LICENSE_INCLUDED
        cpu_core_count:
            description:
                - The Minimum number of OCPUs to be made available for this Deployment.
            returned: on success
            type: int
            sample: 56
        is_auto_scaling_enabled:
            description:
                - Indicates if auto scaling is enabled for the Deployment's CPU core count.
            returned: on success
            type: bool
            sample: true
        nsg_ids:
            description:
                - An array of Network Security Group OCIDs used to define network access for either Deployments or Connections.
            returned: on success
            type: list
            sample: []
        is_public:
            description:
                - True if this object is publicly available.
            returned: on success
            type: bool
            sample: true
        public_ip_address:
            description:
                - The public IP address representing the access point for the Deployment.
            returned: on success
            type: str
            sample: public_ip_address_example
        private_ip_address:
            description:
                - The private IP address in the customer's VCN representing the access point for the
                  associated endpoint service in the GoldenGate service VCN.
            returned: on success
            type: str
            sample: private_ip_address_example
        deployment_url:
            description:
                - The URL of a resource.
            returned: on success
            type: str
            sample: deployment_url_example
        system_tags:
            description:
                - The system tags associated with this resource, if any. The system tags are set by Oracle
                  Cloud Infrastructure services. Each key is predefined and scoped to namespaces.  For more
                  information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{orcl-cloud: {free-tier-retain: true}}`"
            returned: on success
            type: dict
            sample: {}
        is_latest_version:
            description:
                - Indicates if the resource is the the latest available version.
            returned: on success
            type: bool
            sample: true
        time_upgrade_required:
            description:
                - "Note: Deprecated: Use timeOfNextMaintenance instead, or related upgrade records
                  to check, when deployment will be forced to upgrade to a newer version.
                  Old description:
                  The date the existing version in use will no longer be considered as usable
                  and an upgrade will be required.  This date is typically 6 months after the
                  version was released for use by GGS.  The format is defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`."
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        storage_utilization_in_bytes:
            description:
                - The amount of storage being utilized (in bytes)
            returned: on success
            type: int
            sample: 56
        is_storage_utilization_limit_exceeded:
            description:
                - Indicator will be true if the amount of storage being utilized exceeds the allowable storage utilization limit.  Exceeding the limit may be an
                  indication of a misconfiguration of the deployment's GoldenGate service.
            returned: on success
            type: bool
            sample: true
        deployment_type:
            description:
                - "The type of deployment, which can be any one of the Allowed values.
                  NOTE: Use of the value 'OGG' is maintained for backward compatibility purposes.
                      Its use is discouraged in favor of 'DATABASE_ORACLE'."
            returned: on success
            type: str
            sample: OGG
        ogg_data:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                deployment_name:
                    description:
                        - The name given to the GoldenGate service deployment.
                          The name must be 1 to 32 characters long, must contain only alphanumeric characters and must start with a letter.
                    returned: on success
                    type: str
                    sample: deployment_name_example
                admin_username:
                    description:
                        - The GoldenGate deployment console username.
                    returned: on success
                    type: str
                    sample: admin_username_example
                ogg_version:
                    description:
                        - Version of OGG
                    returned: on success
                    type: str
                    sample: ogg_version_example
                certificate:
                    description:
                        - The base64 encoded content of the PEM file containing the SSL certificate.
                    returned: on success
                    type: str
                    sample: "-----BEGIN CERTIFICATE----MIIBIjANBgkqhkiG9w0BA..-----END PUBLIC KEY-----"
                credential_store:
                    description:
                        - The type of credential store for OGG.
                    returned: on success
                    type: str
                    sample: GOLDENGATE
                identity_domain_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Identity Domain when IAM credential store is
                          used.
                    returned: on success
                    type: str
                    sample: "ocid1.identitydomain.oc1..xxxxxxEXAMPLExxxxxx"
                password_secret_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Secret where the deployment password is
                          stored.
                    returned: on success
                    type: str
                    sample: "ocid1.passwordsecret.oc1..xxxxxxEXAMPLExxxxxx"
        deployment_diagnostic_data:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                namespace_name:
                    description:
                        - Name of namespace that serves as a container for all of your buckets
                    returned: on success
                    type: str
                    sample: namespace_name_example
                bucket_name:
                    description:
                        - Name of the bucket where the object is to be uploaded in the object storage
                    returned: on success
                    type: str
                    sample: bucket_name_example
                object_name:
                    description:
                        - Name of the diagnostic collected and uploaded to object storage
                    returned: on success
                    type: str
                    sample: object_name_example
                diagnostic_state:
                    description:
                        - The state of the deployment diagnostic collection.
                    returned: on success
                    type: str
                    sample: IN_PROGRESS
                time_diagnostic_start:
                    description:
                        - The time from which the diagnostic collection should collect the logs. The format is defined by
                          L(RFC3339,https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_diagnostic_end:
                    description:
                        - The time until which the diagnostic collection should collect the logs. The format is defined by
                          L(RFC3339,https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
        maintenance_window:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                day:
                    description:
                        - Days of the week.
                    returned: on success
                    type: str
                    sample: MONDAY
                start_hour:
                    description:
                        - Start hour for maintenance period. Hour is in UTC.
                    returned: on success
                    type: int
                    sample: 56
        time_of_next_maintenance:
            description:
                - The time of next maintenance schedule. The format is defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        next_maintenance_action_type:
            description:
                - Type of the next maintenance.
            returned: on success
            type: str
            sample: UPGRADE
        next_maintenance_description:
            description:
                - Description of the next maintenance.
            returned: on success
            type: str
            sample: next_maintenance_description_example
        maintenance_configuration:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                is_interim_release_auto_upgrade_enabled:
                    description:
                        - By default auto upgrade for interim releases are not enabled. If auto-upgrade is enabled for interim release,
                          you have to specify interimReleaseUpgradePeriodInDays too.
                    returned: on success
                    type: bool
                    sample: true
                interim_release_upgrade_period_in_days:
                    description:
                        - Defines auto upgrade period for interim releases. This period must be shorter or equal to bundle release upgrade period.
                    returned: on success
                    type: int
                    sample: 56
                bundle_release_upgrade_period_in_days:
                    description:
                        - Defines auto upgrade period for bundle releases. Manually configured period cannot be longer than service defined period for bundle
                          releases.
                          This period must be shorter or equal to major release upgrade period. Not passing this field during create will equate to using the
                          service default.
                    returned: on success
                    type: int
                    sample: 56
                major_release_upgrade_period_in_days:
                    description:
                        - Defines auto upgrade period for major releases. Manually configured period cannot be longer than service defined period for major
                          releases.
                          Not passing this field during create will equate to using the service default.
                    returned: on success
                    type: int
                    sample: 56
                security_patch_upgrade_period_in_days:
                    description:
                        - Defines auto upgrade period for releases with security fix. Manually configured period cannot be longer than service defined period
                          for security releases.
                          Not passing this field during create will equate to using the service default.
                    returned: on success
                    type: int
                    sample: 56
        time_ogg_version_supported_until:
            description:
                - The time until OGG version is supported. After this date has passed OGG version will not be available anymore. The format is defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        ingress_ips:
            description:
                - List of ingress IP addresses from where the GoldenGate deployment connects to this connection's privateIp.
                  Customers may optionally set up ingress security rules to restrict traffic from these IP addresses.
            returned: on success
            type: complex
            contains:
                ingress_ip:
                    description:
                        - A Private Endpoint IPv4 or IPv6 Address created in the customer's subnet.
                    returned: on success
                    type: str
                    sample: ingress_ip_example
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "deployment_backup_id": "ocid1.deploymentbackup.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_sub_state": "RECOVERING",
        "lifecycle_details": "lifecycle_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "locks": [{
            "type": "FULL",
            "related_resource_id": "ocid1.relatedresource.oc1..xxxxxxEXAMPLExxxxxx",
            "message": "message_example",
            "time_created": "2013-10-20T19:20:30+01:00"
        }],
        "is_healthy": true,
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "load_balancer_subnet_id": "ocid1.loadbalancersubnet.oc1..xxxxxxEXAMPLExxxxxx",
        "load_balancer_id": "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx",
        "fqdn": "fqdn_example",
        "license_model": "LICENSE_INCLUDED",
        "cpu_core_count": 56,
        "is_auto_scaling_enabled": true,
        "nsg_ids": [],
        "is_public": true,
        "public_ip_address": "public_ip_address_example",
        "private_ip_address": "private_ip_address_example",
        "deployment_url": "deployment_url_example",
        "system_tags": {},
        "is_latest_version": true,
        "time_upgrade_required": "2013-10-20T19:20:30+01:00",
        "storage_utilization_in_bytes": 56,
        "is_storage_utilization_limit_exceeded": true,
        "deployment_type": "OGG",
        "ogg_data": {
            "deployment_name": "deployment_name_example",
            "admin_username": "admin_username_example",
            "ogg_version": "ogg_version_example",
            "certificate": "-----BEGIN CERTIFICATE----MIIBIjANBgkqhkiG9w0BA..-----END PUBLIC KEY-----",
            "credential_store": "GOLDENGATE",
            "identity_domain_id": "ocid1.identitydomain.oc1..xxxxxxEXAMPLExxxxxx",
            "password_secret_id": "ocid1.passwordsecret.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "deployment_diagnostic_data": {
            "namespace_name": "namespace_name_example",
            "bucket_name": "bucket_name_example",
            "object_name": "object_name_example",
            "diagnostic_state": "IN_PROGRESS",
            "time_diagnostic_start": "2013-10-20T19:20:30+01:00",
            "time_diagnostic_end": "2013-10-20T19:20:30+01:00"
        },
        "maintenance_window": {
            "day": "MONDAY",
            "start_hour": 56
        },
        "time_of_next_maintenance": "2013-10-20T19:20:30+01:00",
        "next_maintenance_action_type": "UPGRADE",
        "next_maintenance_description": "next_maintenance_description_example",
        "maintenance_configuration": {
            "is_interim_release_auto_upgrade_enabled": true,
            "interim_release_upgrade_period_in_days": 56,
            "bundle_release_upgrade_period_in_days": 56,
            "major_release_upgrade_period_in_days": 56,
            "security_patch_upgrade_period_in_days": 56
        },
        "time_ogg_version_supported_until": "2013-10-20T19:20:30+01:00",
        "ingress_ips": [{
            "ingress_ip": "ingress_ip_example"
        }]
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
    from oci.golden_gate import GoldenGateClient
    from oci.golden_gate.models import CreateDeploymentDetails
    from oci.golden_gate.models import UpdateDeploymentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DeploymentHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_default_module_wait_timeout(self):
        return 3600

    def get_possible_entity_types(self):
        return super(DeploymentHelperGen, self).get_possible_entity_types() + [
            "deployment",
            "deployments",
            "goldenGatedeployment",
            "goldenGatedeployments",
            "deploymentresource",
            "deploymentsresource",
            "goldengate",
        ]

    def get_module_resource_id_param(self):
        return "deployment_id"

    def get_module_resource_id(self):
        return self.module.params.get("deployment_id")

    def get_get_fn(self):
        return self.client.get_deployment

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_deployment, deployment_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_deployment,
            deployment_id=self.module.params.get("deployment_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = (
            ["display_name"]
            if self._use_name_as_identifier()
            else ["display_name", "fqdn"]
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
            self.client.list_deployments, **kwargs
        )

    def get_create_model_class(self):
        return CreateDeploymentDetails

    def get_exclude_attributes(self):
        return ["ogg_data.admin_password", "ogg_data.key"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_deployment,
            call_fn_args=(),
            call_fn_kwargs=dict(create_deployment_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateDeploymentDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_deployment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                deployment_id=self.module.params.get("deployment_id"),
                update_deployment_details=update_details,
                is_lock_override=self.module.params.get("is_lock_override"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_deployment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                deployment_id=self.module.params.get("deployment_id"),
                is_lock_override=self.module.params.get("is_lock_override"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DeploymentHelperCustom = get_custom_class("DeploymentHelperCustom")


class ResourceHelper(DeploymentHelperCustom, DeploymentHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            locks=dict(
                type="list",
                elements="dict",
                options=dict(
                    type=dict(
                        type="str",
                        required=True,
                        choices=[
                            "FULL",
                            "DELETE",
                            "DEFAULT",
                            "SPECIFIC_RELEASE",
                            "CURRENT_RELEASE",
                        ],
                    ),
                    message=dict(type="str"),
                ),
            ),
            deployment_backup_id=dict(type="str"),
            deployment_type=dict(
                type="str",
                choices=[
                    "OGG",
                    "DATABASE_ORACLE",
                    "BIGDATA",
                    "DATABASE_MICROSOFT_SQLSERVER",
                    "DATABASE_MYSQL",
                    "DATABASE_POSTGRESQL",
                    "DATABASE_DB2ZOS",
                    "GGSA",
                    "DATA_TRANSFORMS",
                ],
            ),
            display_name=dict(aliases=["name"], type="str"),
            license_model=dict(
                type="str", choices=["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]
            ),
            description=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            nsg_ids=dict(type="list", elements="str"),
            subnet_id=dict(type="str"),
            load_balancer_subnet_id=dict(type="str"),
            is_public=dict(type="bool"),
            fqdn=dict(type="str"),
            cpu_core_count=dict(type="int"),
            is_auto_scaling_enabled=dict(type="bool"),
            ogg_data=dict(
                type="dict",
                options=dict(
                    deployment_name=dict(type="str"),
                    ogg_version=dict(type="str"),
                    credential_store=dict(type="str", choices=["GOLDENGATE", "IAM"]),
                    identity_domain_id=dict(type="str"),
                    password_secret_id=dict(type="str"),
                    admin_username=dict(type="str"),
                    admin_password=dict(type="str", no_log=True),
                    certificate=dict(type="str"),
                    key=dict(type="str", no_log=True),
                ),
            ),
            maintenance_window=dict(
                type="dict",
                options=dict(
                    day=dict(
                        type="str",
                        required=True,
                        choices=[
                            "MONDAY",
                            "TUESDAY",
                            "WEDNESDAY",
                            "THURSDAY",
                            "FRIDAY",
                            "SATURDAY",
                            "SUNDAY",
                        ],
                    ),
                    start_hour=dict(type="int", required=True),
                ),
            ),
            maintenance_configuration=dict(
                type="dict",
                options=dict(
                    is_interim_release_auto_upgrade_enabled=dict(type="bool"),
                    interim_release_upgrade_period_in_days=dict(type="int"),
                    bundle_release_upgrade_period_in_days=dict(type="int"),
                    major_release_upgrade_period_in_days=dict(type="int"),
                    security_patch_upgrade_period_in_days=dict(type="int"),
                ),
            ),
            deployment_id=dict(aliases=["id"], type="str"),
            is_lock_override=dict(type="bool"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="deployment",
        service_client_class=GoldenGateClient,
        namespace="golden_gate",
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
