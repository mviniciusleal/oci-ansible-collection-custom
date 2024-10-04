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
module: oci_nosql_table
short_description: Manage a Table resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Table resource in Oracle Cloud Infrastructure
    - For I(state=present), create a new table.
    - "This resource has the following action operations in the M(oracle.oci.oci_nosql_table_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    name:
        description:
            - Table name.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    is_auto_reclaimable:
        description:
            - True if table can be reclaimed after an idle period.
        type: bool
    ddl_statement:
        description:
            - Complete CREATE TABLE DDL statement.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    table_limits:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            max_read_units:
                description:
                    - Maximum sustained read throughput limit for the table.
                type: int
                required: true
            max_write_units:
                description:
                    - Maximum sustained write throughput limit for the table.
                type: int
                required: true
            max_storage_in_g_bs:
                description:
                    - Maximum size of storage used by the table.
                type: int
                required: true
            capacity_mode:
                description:
                    - The capacity mode of the table.  If capacityMode = ON_DEMAND,
                      maxReadUnits and maxWriteUnits are not used, and both will have
                      the value of zero.
                type: str
                choices:
                    - "PROVISIONED"
                    - "ON_DEMAND"
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined
              name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and
              scoped to a namespace.  Example: `{\\"foo-namespace\\":
              {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    table_name_or_id:
        description:
            - A table name within the compartment, or a table OCID.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - Compartment Identifier.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable.
        type: str
    is_if_exists:
        description:
            - "Set as true to select \\"if exists\\" behavior."
        type: bool
    state:
        description:
            - The state of the Table.
            - Use I(state=present) to create or update a Table.
            - Use I(state=absent) to delete a Table.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create table
  oci_nosql_table:
    # required
    name: name_example
    ddl_statement: ddl_statement_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    is_auto_reclaimable: true
    table_limits:
      # required
      max_read_units: 56
      max_write_units: 56
      max_storage_in_g_bs: 56

      # optional
      capacity_mode: PROVISIONED
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update table
  oci_nosql_table:
    # required
    table_name_or_id: "ocid1.tablenameor.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    ddl_statement: ddl_statement_example
    table_limits:
      # required
      max_read_units: 56
      max_write_units: 56
      max_storage_in_g_bs: 56

      # optional
      capacity_mode: PROVISIONED
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update table using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_nosql_table:
    # required
    name: name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    ddl_statement: ddl_statement_example
    table_limits:
      # required
      max_read_units: 56
      max_write_units: 56
      max_storage_in_g_bs: 56

      # optional
      capacity_mode: PROVISIONED
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete table
  oci_nosql_table:
    # required
    table_name_or_id: "ocid1.tablenameor.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    is_if_exists: true

- name: Delete table using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_nosql_table:
    # required
    name: name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
table:
    description:
        - Details of the Table resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Unique identifier that is immutable.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - Human-friendly table name, immutable.
            returned: on success
            type: str
            sample: name_example
        compartment_id:
            description:
                - Compartment Identifier.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The time the the table was created. An RFC3339 formatted
                  datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the the table's metadata was last updated. An
                  RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        table_limits:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                max_read_units:
                    description:
                        - Maximum sustained read throughput limit for the table.
                    returned: on success
                    type: int
                    sample: 56
                max_write_units:
                    description:
                        - Maximum sustained write throughput limit for the table.
                    returned: on success
                    type: int
                    sample: 56
                max_storage_in_g_bs:
                    description:
                        - Maximum size of storage used by the table.
                    returned: on success
                    type: int
                    sample: 56
                capacity_mode:
                    description:
                        - The capacity mode of the table.  If capacityMode = ON_DEMAND,
                          maxReadUnits and maxWriteUnits are not used, and both will have
                          the value of zero.
                    returned: on success
                    type: str
                    sample: PROVISIONED
        lifecycle_state:
            description:
                - The state of a table.
            returned: on success
            type: str
            sample: CREATING
        is_auto_reclaimable:
            description:
                - True if this table can be reclaimed after an idle period.
            returned: on success
            type: bool
            sample: true
        time_of_expiration:
            description:
                - If lifecycleState is INACTIVE, indicates when
                  this table will be automatically removed.
                  An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_details:
            description:
                - A message describing the current state in more detail.
            returned: on success
            type: str
            sample: lifecycle_details_example
        schema:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                columns:
                    description:
                        - The columns of a table.
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - The column name.
                            returned: on success
                            type: str
                            sample: name_example
                        type:
                            description:
                                - The column type.
                            returned: on success
                            type: str
                            sample: type_example
                        is_nullable:
                            description:
                                - The column nullable flag.
                            returned: on success
                            type: bool
                            sample: true
                        default_value:
                            description:
                                - The column default value.
                            returned: on success
                            type: str
                            sample: default_value_example
                        is_as_uuid:
                            description:
                                - True if the STRING column was declared AS UUID.
                            returned: on success
                            type: bool
                            sample: true
                        is_generated:
                            description:
                                - True if the STRING AS UUID column is also GENERATED BY DEFAULT.
                            returned: on success
                            type: bool
                            sample: true
                primary_key:
                    description:
                        - A list of column names that make up a key.
                    returned: on success
                    type: list
                    sample: []
                shard_key:
                    description:
                        - A list of column names that make up a key.
                    returned: on success
                    type: list
                    sample: []
                ttl:
                    description:
                        - The default Time-to-Live for the table, in days.
                    returned: on success
                    type: int
                    sample: 56
                identity:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        column_name:
                            description:
                                - The name of the identity column.
                            returned: on success
                            type: str
                            sample: column_name_example
                        is_always:
                            description:
                                - True if the identity value is GENERATED ALWAYS.
                            returned: on success
                            type: bool
                            sample: true
                        is_null:
                            description:
                                - True if the identity value is GENERATED BY DEFAULT ON NULL.
                            returned: on success
                            type: bool
                            sample: true
        ddl_statement:
            description:
                - A DDL statement representing the schema.
            returned: on success
            type: str
            sample: ddl_statement_example
        schema_state:
            description:
                - "The current state of this table's schema. Available states are
                  MUTABLE - The schema can be changed. The table is not eligible for replication.
                  FROZEN - The schema is immutable. The table is eligible for replication."
            returned: on success
            type: str
            sample: MUTABLE
        is_multi_region:
            description:
                - True if this table is currently a member of a replication set.
            returned: on success
            type: bool
            sample: true
        local_replica_initialization_in_percent:
            description:
                - If this table is in a replication set, this value represents
                  the progress of the initialization of the replica's data.  A
                  value of 100 indicates that initialization has completed.
            returned: on success
            type: int
            sample: 56
        replicas:
            description:
                - An array of Replica listing this table's replicas, if any
            returned: on success
            type: complex
            contains:
                region:
                    description:
                        - A customer-facing region identifier
                    returned: on success
                    type: str
                    sample: us-phoenix-1
                table_id:
                    description:
                        - The OCID of the replica table
                    returned: on success
                    type: str
                    sample: "ocid1.table.oc1..xxxxxxEXAMPLExxxxxx"
                max_write_units:
                    description:
                        - Maximum sustained write throughput limit of the replica table.
                    returned: on success
                    type: int
                    sample: 56
                capacity_mode:
                    description:
                        - The capacity mode of the replica.
                    returned: on success
                    type: str
                    sample: PROVISIONED
                lifecycle_state:
                    description:
                        - The state of the replica.
                    returned: on success
                    type: str
                    sample: CREATING
                lifecycle_details:
                    description:
                        - A message describing the current state in more detail.
                    returned: on success
                    type: str
                    sample: lifecycle_details_example
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined
                  name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and
                  scoped to a namespace.  Example: `{\\"foo-namespace\\":
                  {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "Read-only system tag. These predefined keys are scoped to
                  namespaces.  At present the only supported namespace is
                  `\\"orcl-cloud\\"`; and the only key in that namespace is
                  `\\"free-tier-retained\\"`.
                  Example: `{\\"orcl-cloud\\"\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "table_limits": {
            "max_read_units": 56,
            "max_write_units": 56,
            "max_storage_in_g_bs": 56,
            "capacity_mode": "PROVISIONED"
        },
        "lifecycle_state": "CREATING",
        "is_auto_reclaimable": true,
        "time_of_expiration": "2013-10-20T19:20:30+01:00",
        "lifecycle_details": "lifecycle_details_example",
        "schema": {
            "columns": [{
                "name": "name_example",
                "type": "type_example",
                "is_nullable": true,
                "default_value": "default_value_example",
                "is_as_uuid": true,
                "is_generated": true
            }],
            "primary_key": [],
            "shard_key": [],
            "ttl": 56,
            "identity": {
                "column_name": "column_name_example",
                "is_always": true,
                "is_null": true
            }
        },
        "ddl_statement": "ddl_statement_example",
        "schema_state": "MUTABLE",
        "is_multi_region": true,
        "local_replica_initialization_in_percent": 56,
        "replicas": [{
            "region": "us-phoenix-1",
            "table_id": "ocid1.table.oc1..xxxxxxEXAMPLExxxxxx",
            "max_write_units": 56,
            "capacity_mode": "PROVISIONED",
            "lifecycle_state": "CREATING",
            "lifecycle_details": "lifecycle_details_example"
        }],
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
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.nosql import NosqlClient
    from oci.nosql.models import CreateTableDetails
    from oci.nosql.models import UpdateTableDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TableHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(TableHelperGen, self).get_possible_entity_types() + [
            "table",
            "tables",
            "nosqltable",
            "nosqltables",
            "tableresource",
            "tablesresource",
            "nosql",
        ]

    def get_module_resource_id_param(self):
        return "table_name_or_id"

    def get_module_resource_id(self):
        return self.module.params.get("table_name_or_id")

    def get_get_fn(self):
        return self.client.get_table

    def get_resource(self):
        optional_params = [
            "compartment_id",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_table,
            table_name_or_id=self.module.params.get("table_name_or_id"),
            **optional_kwargs
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["name"]

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
        return oci_common_utils.list_all_resources(self.client.list_tables, **kwargs)

    def get_create_model_class(self):
        return CreateTableDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_table,
            call_fn_args=(),
            call_fn_kwargs=dict(create_table_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateTableDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_table,
            call_fn_args=(),
            call_fn_kwargs=dict(
                table_name_or_id=self.module.params.get("table_name_or_id"),
                update_table_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_table,
            call_fn_args=(),
            call_fn_kwargs=dict(
                table_name_or_id=self.module.params.get("table_name_or_id"),
                compartment_id=self.module.params.get("compartment_id"),
                is_if_exists=self.module.params.get("is_if_exists"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


TableHelperCustom = get_custom_class("TableHelperCustom")


class ResourceHelper(TableHelperCustom, TableHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            name=dict(type="str"),
            is_auto_reclaimable=dict(type="bool"),
            ddl_statement=dict(type="str"),
            table_limits=dict(
                type="dict",
                options=dict(
                    max_read_units=dict(type="int", required=True),
                    max_write_units=dict(type="int", required=True),
                    max_storage_in_g_bs=dict(type="int", required=True),
                    capacity_mode=dict(
                        type="str", choices=["PROVISIONED", "ON_DEMAND"]
                    ),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            table_name_or_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            is_if_exists=dict(type="bool"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="table",
        service_client_class=NosqlClient,
        namespace="nosql",
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
