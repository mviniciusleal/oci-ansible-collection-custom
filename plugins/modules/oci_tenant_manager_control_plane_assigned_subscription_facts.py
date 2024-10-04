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
module: oci_tenant_manager_control_plane_assigned_subscription_facts
short_description: Fetches details about one or multiple AssignedSubscription resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AssignedSubscription resources in Oracle Cloud Infrastructure
    - Lists subscriptions that are consumed by the compartment. Only the root compartment is allowed.
    - If I(assigned_subscription_id) is specified, the details of a single AssignedSubscription will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    assigned_subscription_id:
        description:
            - OCID of the assigned Oracle Cloud Subscription.
            - Required to get a specific assigned_subscription.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required to list multiple assigned_subscriptions.
        type: str
    subscription_id:
        description:
            - The ID of the subscription to which the tenancy is associated.
        type: str
    sort_order:
        description:
            - The sort order to use, whether 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - "The field to sort by. Only one sort order can be provided.
              * The default order for timeCreated is descending.
              * The default order for displayName is ascending.
              * If no value is specified, timeCreated is the default."
        type: str
        choices:
            - "timeCreated"
            - "displayName"
    entity_version:
        description:
            - The version of the subscription entity.
        type: str
        choices:
            - "V1"
            - "V2"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific assigned_subscription
  oci_tenant_manager_control_plane_assigned_subscription_facts:
    # required
    assigned_subscription_id: "ocid1.assignedsubscription.oc1..xxxxxxEXAMPLExxxxxx"

- name: List assigned_subscriptions
  oci_tenant_manager_control_plane_assigned_subscription_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    subscription_id: "ocid1.subscription.oc1..xxxxxxEXAMPLExxxxxx"
    sort_order: ASC
    sort_by: timeCreated
    entity_version: V1

"""

RETURN = """
assigned_subscriptions:
    description:
        - List of AssignedSubscription resources
    returned: on success
    type: complex
    contains:
        classic_subscription_id:
            description:
                - Subscription ID.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.classicsubscription.oc1..xxxxxxEXAMPLExxxxxx"
        is_classic_subscription:
            description:
                - Specifies whether or not the subscription is legacy.
                - Returned for get operation
            returned: on success
            type: bool
            sample: true
        region_assignment:
            description:
                - Region for the subscription.
                - Returned for get operation
            returned: on success
            type: str
            sample: region_assignment_example
        skus:
            description:
                - List of SKUs linked to the subscription.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                sku:
                    description:
                        - Stock Keeping Unit (SKU) ID.
                    returned: on success
                    type: str
                    sample: sku_example
                quantity:
                    description:
                        - Quantity of the stock units.
                    returned: on success
                    type: int
                    sample: 56
                description:
                    description:
                        - Description of the stock units.
                    returned: on success
                    type: str
                    sample: description_example
                gsi_order_line_id:
                    description:
                        - Sales order line identifier.
                    returned: on success
                    type: str
                    sample: "ocid1.gsiorderline.oc1..xxxxxxEXAMPLExxxxxx"
                license_part_description:
                    description:
                        - Description of the covered product belonging to this SKU.
                    returned: on success
                    type: str
                    sample: license_part_description_example
                metric_name:
                    description:
                        - Base metric for billing the service.
                    returned: on success
                    type: str
                    sample: metric_name_example
                is_base_service_component:
                    description:
                        - Specifies if the SKU is considered as a parent or child.
                    returned: on success
                    type: bool
                    sample: true
                is_additional_instance:
                    description:
                        - Specifies if an additional test instance can be provisioned by the SaaS application.
                    returned: on success
                    type: bool
                    sample: true
                start_date:
                    description:
                        - Date and time when the SKU was created.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                end_date:
                    description:
                        - Date and time when the SKU ended.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
        order_ids:
            description:
                - List of subscription order OCIDs that contributed to this subscription.
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        program_type:
            description:
                - Specifies any program that is associated with the subscription.
                - Returned for get operation
            returned: on success
            type: str
            sample: program_type_example
        customer_country_code:
            description:
                - The country code for the customer associated with the subscription.
                - Returned for get operation
            returned: on success
            type: str
            sample: customer_country_code_example
        cloud_amount_currency:
            description:
                - The currency code for the customer associated with the subscription.
                - Returned for get operation
            returned: on success
            type: str
            sample: cloud_amount_currency_example
        csi_number:
            description:
                - Customer service identifier for the customer associated with the subscription.
                - Returned for get operation
            returned: on success
            type: str
            sample: csi_number_example
        subscription_tier:
            description:
                - Tier for the subscription, whether a free promotion subscription or a paid subscription.
                - Returned for get operation
            returned: on success
            type: str
            sample: subscription_tier_example
        is_government_subscription:
            description:
                - Specifies whether or not the subscription is a government subscription.
                - Returned for get operation
            returned: on success
            type: bool
            sample: true
        promotion:
            description:
                - List of promotions related to the subscription.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                duration:
                    description:
                        - Specifies how long the promotion related to the subscription, if any, is valid in duration units.
                    returned: on success
                    type: int
                    sample: 56
                duration_unit:
                    description:
                        - Unit for the duration.
                    returned: on success
                    type: str
                    sample: duration_unit_example
                amount:
                    description:
                        - If a subscription is present, indicates the total amount of promotional subscription credits.
                    returned: on success
                    type: float
                    sample: 3.4
                status:
                    description:
                        - If a subscription is present, indicates the current status of the subscription promotion.
                    returned: on success
                    type: str
                    sample: INITIALIZED
                is_intent_to_pay:
                    description:
                        - Speficies whether or not the customer intends to pay after the promotion has expired.
                    returned: on success
                    type: bool
                    sample: true
                currency_unit:
                    description:
                        - Currency unit associated with the promotion.
                    returned: on success
                    type: str
                    sample: currency_unit_example
                time_started:
                    description:
                        - Date and time when the promotion starts.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_expired:
                    description:
                        - Date and time when the promotion ends.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
        purchase_entitlement_id:
            description:
                - Purchase entitlement ID associated with the subscription.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.purchaseentitlement.oc1..xxxxxxEXAMPLExxxxxx"
        start_date:
            description:
                - Subscription start time.
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        end_date:
            description:
                - Subscription end time.
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        subscription_number:
            description:
                - Unique Oracle Cloud Subscriptions identifier that is immutable on creation.
                - Returned for get operation
            returned: on success
            type: str
            sample: subscription_number_example
        currency_code:
            description:
                - Currency code. For example USD, MXN.
                - Returned for get operation
            returned: on success
            type: str
            sample: currency_code_example
        lifecycle_state:
            description:
                - Lifecycle state of the subscription.
                - Returned for get operation
            returned: on success
            type: str
            sample: CREATING
        entity_version:
            description:
                - The entity version of the subscription, whether V1 (the legacy schema version), or V2 (the latest 20230401 API version).
            returned: on success
            type: str
            sample: V1
        id:
            description:
                - The Oracle ID (L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)) of the subscription.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The Oracle ID (L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)) of the owning compartment. Always a tenancy
                  OCID.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        service_name:
            description:
                - The type of subscription, such as 'UCM', 'SAAS', 'ERP', 'CRM'.
            returned: on success
            type: str
            sample: service_name_example
        time_created:
            description:
                - The date and time of creation, as described in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339), section 14.29.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time of update, as described in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339), section 14.29.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
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
    sample: [{
        "classic_subscription_id": "ocid1.classicsubscription.oc1..xxxxxxEXAMPLExxxxxx",
        "is_classic_subscription": true,
        "region_assignment": "region_assignment_example",
        "skus": [{
            "sku": "sku_example",
            "quantity": 56,
            "description": "description_example",
            "gsi_order_line_id": "ocid1.gsiorderline.oc1..xxxxxxEXAMPLExxxxxx",
            "license_part_description": "license_part_description_example",
            "metric_name": "metric_name_example",
            "is_base_service_component": true,
            "is_additional_instance": true,
            "start_date": "2013-10-20T19:20:30+01:00",
            "end_date": "2013-10-20T19:20:30+01:00"
        }],
        "order_ids": [],
        "program_type": "program_type_example",
        "customer_country_code": "customer_country_code_example",
        "cloud_amount_currency": "cloud_amount_currency_example",
        "csi_number": "csi_number_example",
        "subscription_tier": "subscription_tier_example",
        "is_government_subscription": true,
        "promotion": [{
            "duration": 56,
            "duration_unit": "duration_unit_example",
            "amount": 3.4,
            "status": "INITIALIZED",
            "is_intent_to_pay": true,
            "currency_unit": "currency_unit_example",
            "time_started": "2013-10-20T19:20:30+01:00",
            "time_expired": "2013-10-20T19:20:30+01:00"
        }],
        "purchase_entitlement_id": "ocid1.purchaseentitlement.oc1..xxxxxxEXAMPLExxxxxx",
        "start_date": "2013-10-20T19:20:30+01:00",
        "end_date": "2013-10-20T19:20:30+01:00",
        "subscription_number": "subscription_number_example",
        "currency_code": "currency_code_example",
        "lifecycle_state": "CREATING",
        "entity_version": "V1",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "service_name": "service_name_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.tenant_manager_control_plane import SubscriptionClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AssignedSubscriptionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "assigned_subscription_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_assigned_subscription,
            assigned_subscription_id=self.module.params.get("assigned_subscription_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "subscription_id",
            "sort_order",
            "sort_by",
            "entity_version",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_assigned_subscriptions,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


AssignedSubscriptionFactsHelperCustom = get_custom_class(
    "AssignedSubscriptionFactsHelperCustom"
)


class ResourceFactsHelper(
    AssignedSubscriptionFactsHelperCustom, AssignedSubscriptionFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            assigned_subscription_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            subscription_id=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
            entity_version=dict(type="str", choices=["V1", "V2"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="assigned_subscription",
        service_client_class=SubscriptionClient,
        namespace="tenant_manager_control_plane",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(assigned_subscriptions=result)


if __name__ == "__main__":
    main()
