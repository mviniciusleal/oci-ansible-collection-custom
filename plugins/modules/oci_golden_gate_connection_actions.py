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
module: oci_golden_gate_connection_actions
short_description: Perform actions on a Connection resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Connection resource in Oracle Cloud Infrastructure
    - For I(action=add_connection_lock), adds a lock to a Connection resource.
    - For I(action=change_compartment), moves the Connection into a different compartment within the same tenancy. When
      provided, If-Match is checked against ETag values of the resource.  For information about
      moving resources between compartments, see L(Moving Resources Between
      Compartments,https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
    - For I(action=remove_connection_lock), removes a lock from a Connection resource.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    msg:
        description:
            - A message added by the creator of the lock. This is typically used to give an
              indication of why the resource is locked.
            - Applicable only for I(action=add_connection_lock).
        type: str
        aliases: ["message"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment being referenced.
            - Required for I(action=change_compartment).
        type: str
    is_lock_override:
        description:
            - Whether to override locks (if any exist).
            - Applicable only for I(action=change_compartment).
        type: bool
    connection_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of a Connection.
        type: str
        aliases: ["id"]
        required: true
    type:
        description:
            - Type of the lock.
            - Required for I(action=add_connection_lock), I(action=remove_connection_lock).
        type: str
        choices:
            - "FULL"
            - "DELETE"
            - "DEFAULT"
            - "SPECIFIC_RELEASE"
            - "CURRENT_RELEASE"
    action:
        description:
            - The action to perform on the Connection.
        type: str
        required: true
        choices:
            - "add_connection_lock"
            - "change_compartment"
            - "remove_connection_lock"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action add_connection_lock on connection
  oci_golden_gate_connection_actions:
    # required
    connection_id: "ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx"
    type: FULL
    action: add_connection_lock

    # optional
    msg: msg_example

- name: Perform action change_compartment on connection
  oci_golden_gate_connection_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    connection_id: "ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

    # optional
    is_lock_override: true

- name: Perform action remove_connection_lock on connection
  oci_golden_gate_connection_actions:
    # required
    connection_id: "ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx"
    type: FULL
    action: remove_connection_lock

"""

RETURN = """
connection:
    description:
        - Details of the Connection resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        access_key_id:
            description:
                - Access key ID to access the Amazon Kinesis.
            returned: on success
            type: str
            sample: "ocid1.accesskey.oc1..xxxxxxEXAMPLExxxxxx"
        account_name:
            description:
                - Sets the Azure storage account name.
            returned: on success
            type: str
            sample: account_name_example
        azure_tenant_id:
            description:
                - "Azure tenant ID of the application. This property is required when 'authenticationType' is set to 'AZURE_ACTIVE_DIRECTORY'.
                  e.g.: 14593954-d337-4a61-a364-9f758c64f97f"
            returned: on success
            type: str
            sample: "ocid1.azuretenant.oc1..xxxxxxEXAMPLExxxxxx"
        client_id:
            description:
                - "Azure client ID of the application. This property is required when 'authenticationType' is set to 'AZURE_ACTIVE_DIRECTORY'.
                  e.g.: 06ecaabf-8b80-4ec8-a0ec-20cbf463703d"
            returned: on success
            type: str
            sample: "ocid1.client.oc1..xxxxxxEXAMPLExxxxxx"
        endpoint:
            description:
                - "Azure Storage service endpoint.
                  e.g: https://test.blob.core.windows.net"
            returned: on success
            type: str
            sample: endpoint_example
        deployment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the deployment being referenced.
            returned: on success
            type: str
            sample: "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"
        should_use_jndi:
            description:
                - If set to true, Java Naming and Directory Interface (JNDI) properties should be provided.
            returned: on success
            type: bool
            sample: true
        jndi_connection_factory:
            description:
                - "The Connection Factory can be looked up using this name.
                  e.g.: 'ConnectionFactory'"
            returned: on success
            type: str
            sample: jndi_connection_factory_example
        jndi_provider_url:
            description:
                - "The URL that Java Message Service will use to contact the JNDI provider.
                  e.g.: 'tcp://myjms.host.domain:61616?jms.prefetchPolicy.all=1000'"
            returned: on success
            type: str
            sample: jndi_provider_url_example
        jndi_initial_context_factory:
            description:
                - "The implementation of javax.naming.spi.InitialContextFactory interface
                  that the client uses to obtain initial naming context.
                  e.g.: 'org.apache.activemq.jndi.ActiveMQInitialContextFactory'"
            returned: on success
            type: str
            sample: jndi_initial_context_factory_example
        jndi_security_principal:
            description:
                - "Specifies the identity of the principal (user) to be authenticated.
                  e.g.: 'admin2'"
            returned: on success
            type: str
            sample: jndi_security_principal_example
        connection_factory:
            description:
                - "The of Java class implementing javax.jms.ConnectionFactory interface
                  supplied by the Java Message Service provider.
                  e.g.: 'com.stc.jmsjca.core.JConnectionFactoryXA'"
            returned: on success
            type: str
            sample: connection_factory_example
        stream_pool_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the stream pool being referenced.
            returned: on success
            type: str
            sample: "ocid1.streampool.oc1..xxxxxxEXAMPLExxxxxx"
        bootstrap_servers:
            description:
                - "Kafka bootstrap. Equivalent of bootstrap.servers configuration property in Kafka:
                  list of KafkaBootstrapServer objects specified by host/port.
                  Used for establishing the initial connection to the Kafka cluster.
                  Example: `\\"server1.example.com:9092,server2.example.com:9092\\"`"
            returned: on success
            type: complex
            contains:
                host:
                    description:
                        - The name or address of a host.
                    returned: on success
                    type: str
                    sample: host_example
                port:
                    description:
                        - The port of an endpoint usually specified for a connection.
                    returned: on success
                    type: int
                    sample: 56
                private_ip:
                    description:
                        - "Deprecated: this field will be removed in future versions. Either specify the private IP in the connectionString or host
                          field, or make sure the host name is resolvable in the target VCN."
                        - The private IP address of the connection's endpoint in the customer's VCN, typically a
                          database endpoint or a big data endpoint (e.g. Kafka bootstrap server).
                          In case the privateIp is provided, the subnetId must also be provided.
                          In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible.
                          In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.
                    returned: on success
                    type: str
                    sample: private_ip_example
        url:
            description:
                - "Kafka Schema Registry URL.
                  e.g.: 'https://server1.us.oracle.com:8081'"
            returned: on success
            type: str
            sample: url_example
        ssl_ca:
            description:
                - "Database Certificate - The base64 encoded content of a .pem or .crt file.
                  containing the server public key (for 1-way SSL)."
            returned: on success
            type: str
            sample: ssl_ca_example
        should_validate_server_certificate:
            description:
                - If set to true, the driver validates the certificate that is sent by the database server.
            returned: on success
            type: bool
            sample: true
        connection_string:
            description:
                - "JDBC connection string.
                  e.g.: 'jdbc:sqlserver://<synapse-workspace>.sql.azuresynapse.net:1433;database=<db-
                  name>;encrypt=true;trustServerCertificate=false;hostNameInCertificate=*.sql.azuresynapse.net;loginTimeout=300;'"
            returned: on success
            type: str
            sample: connection_string_example
        authentication_mode:
            description:
                - Authentication mode. It can be provided at creation of Oracle Autonomous Database Serverless connections,
                  when a databaseId is provided. The default value is MTLS.
            returned: on success
            type: str
            sample: TLS
        session_mode:
            description:
                - "The mode of the database connection session to be established by the data client.
                  'REDIRECT' - for a RAC database, 'DIRECT' - for a non-RAC database.
                  Connection to a RAC database involves a redirection received from the SCAN listeners
                  to the database node to connect to. By default the mode would be DIRECT."
            returned: on success
            type: str
            sample: DIRECT
        database_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Oracle Autonomous Json Database.
            returned: on success
            type: str
            sample: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
        tenancy_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the related OCI tenancy.
            returned: on success
            type: str
            sample: "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx"
        region:
            description:
                - "The name of the region. e.g.: us-ashburn-1"
            returned: on success
            type: str
            sample: us-phoenix-1
        user_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the OCI user who will access the Object Storage.
                  The user must have write access to the bucket they want to connect to.
            returned: on success
            type: str
            sample: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"
        database_name:
            description:
                - The name of the database.
            returned: on success
            type: str
            sample: database_name_example
        host:
            description:
                - The name or address of a host.
            returned: on success
            type: str
            sample: host_example
        port:
            description:
                - The port of an endpoint usually specified for a connection.
            returned: on success
            type: int
            sample: 56
        additional_attributes:
            description:
                - An array of name-value pair attribute entries.
                  Used as additional parameters in connection string.
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - The name of the property entry.
                    returned: on success
                    type: str
                    sample: name_example
                value:
                    description:
                        - The value of the property entry.
                    returned: on success
                    type: str
                    sample: value_example
        ssl_mode:
            description:
                - SSL modes for MySQL.
            returned: on success
            type: str
            sample: DISABLED
        private_ip:
            description:
                - "Deprecated: this field will be removed in future versions. Either specify the private IP in the connectionString or host
                  field, or make sure the host name is resolvable in the target VCN."
                - The private IP address of the connection's endpoint in the customer's VCN, typically a
                  database endpoint or a big data endpoint (e.g. Kafka bootstrap server).
                  In case the privateIp is provided, the subnetId must also be provided.
                  In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible.
                  In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.
            returned: on success
            type: str
            sample: private_ip_example
        db_system_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the database system being referenced.
            returned: on success
            type: str
            sample: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"
        servers:
            description:
                - "Comma separated list of Elasticsearch server addresses, specified as host:port entries, where :port is optional.
                  If port is not specified, it defaults to 9200.
                  Used for establishing the initial connection to the Elasticsearch cluster.
                  Example: `\\"server1.example.com:4000,server2.example.com:4000\\"`"
            returned: on success
            type: str
            sample: servers_example
        security_protocol:
            description:
                - Security Protocol for the DB2 database.
            returned: on success
            type: str
            sample: PLAIN
        redis_cluster_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Redis cluster.
            returned: on success
            type: str
            sample: "ocid1.rediscluster.oc1..xxxxxxEXAMPLExxxxxx"
        connection_type:
            description:
                - The connection type.
            returned: on success
            type: str
            sample: GOLDENGATE
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the connection being
                  referenced.
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
        system_tags:
            description:
                - The system tags associated with this resource, if any. The system tags are set by Oracle
                  Cloud Infrastructure services. Each key is predefined and scoped to namespaces.  For more
                  information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{orcl-cloud: {free-tier-retain: true}}`"
            returned: on success
            type: dict
            sample: {}
        lifecycle_state:
            description:
                - Possible lifecycle states for connection.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - Describes the object's current state in detail. For example, it can be used to provide
                  actionable information for a resource in a Failed state.
            returned: on success
            type: str
            sample: lifecycle_details_example
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
        vault_id:
            description:
                - Refers to the customer's vault OCID.
                  If provided, it references a vault where GoldenGate can manage secrets. Customers must add policies to permit GoldenGate
                  to manage secrets contained within this vault.
            returned: on success
            type: str
            sample: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
        key_id:
            description:
                - Refers to the customer's master key OCID.
                  If provided, it references a key to manage secrets. Customers must add policies to permit GoldenGate to use this key.
            returned: on success
            type: str
            sample: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
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
        nsg_ids:
            description:
                - An array of Network Security Group OCIDs used to define network access for either Deployments or Connections.
            returned: on success
            type: list
            sample: []
        subnet_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the target subnet of the dedicated connection.
            returned: on success
            type: str
            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        routing_method:
            description:
                - "Controls the network traffic direction to the target:
                  SHARED_SERVICE_ENDPOINT: Traffic flows through the Goldengate Service's network to public hosts. Cannot be used for private targets.
                  SHARED_DEPLOYMENT_ENDPOINT: Network traffic flows from the assigned deployment's private endpoint through the deployment's subnet.
                  DEDICATED_ENDPOINT: A dedicated private endpoint is created in the target VCN subnet for the connection. The subnetId is required when
                  DEDICATED_ENDPOINT networking is selected."
            returned: on success
            type: str
            sample: SHARED_SERVICE_ENDPOINT
        technology_type:
            description:
                - The Amazon Kinesis technology type.
            returned: on success
            type: str
            sample: AMAZON_KINESIS
        connection_url:
            description:
                - "Connection URL.
                  e.g.: 'jdbc:redshift://aws-redshift-instance.aaaaaaaaaaaa.us-east-2.redshift.amazonaws.com:5439/mydb'"
            returned: on success
            type: str
            sample: connection_url_example
        authentication_type:
            description:
                - Used authentication mechanism to access Azure Data Lake Storage.
            returned: on success
            type: str
            sample: SHARED_KEY
        username:
            description:
                - The username Oracle GoldenGate uses to connect the associated system of the given technology.
                  This username must already exist and be available by the system/application to be connected to
                  and must conform to the case sensitivty requirments defined in it.
            returned: on success
            type: str
            sample: username_example
    sample: {
        "access_key_id": "ocid1.accesskey.oc1..xxxxxxEXAMPLExxxxxx",
        "account_name": "account_name_example",
        "azure_tenant_id": "ocid1.azuretenant.oc1..xxxxxxEXAMPLExxxxxx",
        "client_id": "ocid1.client.oc1..xxxxxxEXAMPLExxxxxx",
        "endpoint": "endpoint_example",
        "deployment_id": "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx",
        "should_use_jndi": true,
        "jndi_connection_factory": "jndi_connection_factory_example",
        "jndi_provider_url": "jndi_provider_url_example",
        "jndi_initial_context_factory": "jndi_initial_context_factory_example",
        "jndi_security_principal": "jndi_security_principal_example",
        "connection_factory": "connection_factory_example",
        "stream_pool_id": "ocid1.streampool.oc1..xxxxxxEXAMPLExxxxxx",
        "bootstrap_servers": [{
            "host": "host_example",
            "port": 56,
            "private_ip": "private_ip_example"
        }],
        "url": "url_example",
        "ssl_ca": "ssl_ca_example",
        "should_validate_server_certificate": true,
        "connection_string": "connection_string_example",
        "authentication_mode": "TLS",
        "session_mode": "DIRECT",
        "database_id": "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx",
        "tenancy_id": "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx",
        "region": "us-phoenix-1",
        "user_id": "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx",
        "database_name": "database_name_example",
        "host": "host_example",
        "port": 56,
        "additional_attributes": [{
            "name": "name_example",
            "value": "value_example"
        }],
        "ssl_mode": "DISABLED",
        "private_ip": "private_ip_example",
        "db_system_id": "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx",
        "servers": "servers_example",
        "security_protocol": "PLAIN",
        "redis_cluster_id": "ocid1.rediscluster.oc1..xxxxxxEXAMPLExxxxxx",
        "connection_type": "GOLDENGATE",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "locks": [{
            "type": "FULL",
            "related_resource_id": "ocid1.relatedresource.oc1..xxxxxxEXAMPLExxxxxx",
            "message": "message_example",
            "time_created": "2013-10-20T19:20:30+01:00"
        }],
        "vault_id": "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx",
        "key_id": "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx",
        "ingress_ips": [{
            "ingress_ip": "ingress_ip_example"
        }],
        "nsg_ids": [],
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "routing_method": "SHARED_SERVICE_ENDPOINT",
        "technology_type": "AMAZON_KINESIS",
        "connection_url": "connection_url_example",
        "authentication_type": "SHARED_KEY",
        "username": "username_example"
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
    from oci.golden_gate import GoldenGateClient
    from oci.golden_gate.models import AddResourceLockDetails
    from oci.golden_gate.models import ChangeConnectionCompartmentDetails
    from oci.golden_gate.models import RemoveResourceLockDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ConnectionActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        add_connection_lock
        change_compartment
        remove_connection_lock
    """

    @staticmethod
    def get_module_resource_id_param():
        return "connection_id"

    def get_module_resource_id(self):
        return self.module.params.get("connection_id")

    def get_get_fn(self):
        return self.client.get_connection

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_connection,
            connection_id=self.module.params.get("connection_id"),
        )

    def add_connection_lock(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AddResourceLockDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.add_connection_lock,
            call_fn_args=(),
            call_fn_kwargs=dict(
                connection_id=self.module.params.get("connection_id"),
                add_resource_lock_details=action_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeConnectionCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_connection_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                connection_id=self.module.params.get("connection_id"),
                change_connection_compartment_details=action_details,
                is_lock_override=self.module.params.get("is_lock_override"),
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

    def remove_connection_lock(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RemoveResourceLockDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.remove_connection_lock,
            call_fn_args=(),
            call_fn_kwargs=dict(
                connection_id=self.module.params.get("connection_id"),
                remove_resource_lock_details=action_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


ConnectionActionsHelperCustom = get_custom_class("ConnectionActionsHelperCustom")


class ResourceHelper(ConnectionActionsHelperCustom, ConnectionActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            msg=dict(aliases=["message"], type="str"),
            compartment_id=dict(type="str"),
            is_lock_override=dict(type="bool"),
            connection_id=dict(aliases=["id"], type="str", required=True),
            type=dict(
                type="str",
                choices=[
                    "FULL",
                    "DELETE",
                    "DEFAULT",
                    "SPECIFIC_RELEASE",
                    "CURRENT_RELEASE",
                ],
            ),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "add_connection_lock",
                    "change_compartment",
                    "remove_connection_lock",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="connection",
        service_client_class=GoldenGateClient,
        namespace="golden_gate",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
