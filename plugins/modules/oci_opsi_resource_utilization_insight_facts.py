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
module: oci_opsi_resource_utilization_insight_facts
short_description: Fetches details about a ResourceUtilizationInsight resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a ResourceUtilizationInsight resource in Oracle Cloud Infrastructure
    - Gets resources with current utilization (high and low) and projected utilization (high and low) for a resource type over specified time period.
      If compartmentIdInSubtree is specified, aggregates resources in a compartment and in all sub-compartments.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        type: str
        required: true
    resource_metric:
        description:
            - Filter by resource metric.
              Supported values are CPU , STORAGE, MEMORY and IO.
        type: str
        required: true
    analysis_time_interval:
        description:
            - Specify time period in ISO 8601 format with respect to current time.
              Default is last 30 days represented by P30D.
              If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored.
              Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to
              current time (P25M).
        type: str
    time_interval_start:
        description:
            - Analysis start time in UTC in ISO 8601 format(inclusive).
              Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
              The minimum allowed value is 2 years prior to the current day.
              timeIntervalStart and timeIntervalEnd parameters are used together.
              If analysisTimeInterval is specified, this parameter is ignored.
        type: str
    time_interval_end:
        description:
            - Analysis end time in UTC in ISO 8601 format(exclusive).
              Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
              timeIntervalStart and timeIntervalEnd are used together.
              If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.
        type: str
    database_type:
        description:
            - Filter by one or more database type.
              Possible values are ADW-S, ATP-S, ADW-D, ATP-D, EXTERNAL-PDB, EXTERNAL-NONCDB.
        type: list
        elements: str
        choices:
            - "ADW-S"
            - "ATP-S"
            - "ADW-D"
            - "ATP-D"
            - "EXTERNAL-PDB"
            - "EXTERNAL-NONCDB"
            - "COMANAGED-VM-CDB"
            - "COMANAGED-VM-PDB"
            - "COMANAGED-VM-NONCDB"
            - "COMANAGED-BM-CDB"
            - "COMANAGED-BM-PDB"
            - "COMANAGED-BM-NONCDB"
            - "COMANAGED-EXACS-CDB"
            - "COMANAGED-EXACS-PDB"
            - "COMANAGED-EXACS-NONCDB"
    database_id:
        description:
            - Optional list of database L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the associated DBaaS entity.
        type: list
        elements: str
    id:
        description:
            - Optional list of database insight resource L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        type: list
        elements: str
    exadata_insight_id:
        description:
            - Optional list of exadata insight resource L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        type: list
        elements: str
    forecast_days:
        description:
            - Number of days used for utilization forecast analysis.
        type: int
    host_name:
        description:
            - Filter by one or more hostname.
        type: list
        elements: str
    is_database_instance_level_metrics:
        description:
            - Flag to indicate if database instance level metrics should be returned. The flag is ignored when a host name filter is not applied.
              When a hostname filter is applied this flag will determine whether to return metrics for the instances located on the specified host or for the
              whole database which contains an instance on this host.
        type: bool
    defined_tag_equals:
        description:
            - "A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned.
              Each item in the list has the format \\"{namespace}.{tagName}.{value}\\".  All inputs are case-insensitive.
              Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \\"OR\\".
              Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \\"AND\\"."
        type: list
        elements: str
    freeform_tag_equals:
        description:
            - "A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned.
              The key for each tag is \\"{tagName}.{value}\\".  All inputs are case-insensitive.
              Multiple values for the same tag name are interpreted as \\"OR\\".  Values for different tag names are interpreted as \\"AND\\"."
        type: list
        elements: str
    defined_tag_exists:
        description:
            - "A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned.
              Each item in the list has the format \\"{namespace}.{tagName}.true\\" (for checking existence of a defined tag)
              or \\"{namespace}.true\\".  All inputs are case-insensitive.
              Currently, only existence (\\"true\\" at the end) is supported. Absence (\\"false\\" at the end) is not supported.
              Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \\"OR\\".
              Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \\"AND\\"."
        type: list
        elements: str
    freeform_tag_exists:
        description:
            - "A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned.
              The key for each tag is \\"{tagName}.true\\".  All inputs are case-insensitive.
              Currently, only existence (\\"true\\" at the end) is supported. Absence (\\"false\\" at the end) is not supported.
              Multiple values for different tag names are interpreted as \\"AND\\"."
        type: list
        elements: str
    compartment_id_in_subtree:
        description:
            - A flag to search all resources within a given compartment and all sub-compartments.
        type: bool
    vmcluster_name:
        description:
            - Optional list of Exadata Insight VM cluster name.
        type: list
        elements: str
    cdb_name:
        description:
            - Filter by one or more cdb name.
        type: list
        elements: str
    high_utilization_threshold:
        description:
            - Percent value in which a resource metric is considered highly utilized.
        type: int
    low_utilization_threshold:
        description:
            - Percent value in which a resource metric is considered low utilized.
        type: int
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific resource_utilization_insight
  oci_opsi_resource_utilization_insight_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    resource_metric: resource_metric_example

    # optional
    analysis_time_interval: analysis_time_interval_example
    time_interval_start: 2013-10-20T19:20:30+01:00
    time_interval_end: 2013-10-20T19:20:30+01:00
    database_type: [ "ADW-S" ]
    database_id: [ "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx" ]
    id: [ "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx" ]
    exadata_insight_id: [ "ocid1.exadatainsight.oc1..xxxxxxEXAMPLExxxxxx" ]
    forecast_days: 30
    host_name: [ "host_name_example" ]
    is_database_instance_level_metrics: true
    defined_tag_equals: [ "defined_tag_equals_example" ]
    freeform_tag_equals: [ "freeform_tag_equals_example" ]
    defined_tag_exists: [ "defined_tag_exists_example" ]
    freeform_tag_exists: [ "freeform_tag_exists_example" ]
    compartment_id_in_subtree: true
    vmcluster_name: [ "vmcluster_name_example" ]
    cdb_name: [ "cdb_name_example" ]
    high_utilization_threshold: 1
    low_utilization_threshold: 0

"""

RETURN = """
resource_utilization_insight:
    description:
        - ResourceUtilizationInsight resource
    returned: on success
    type: complex
    contains:
        time_interval_start:
            description:
                - The start timestamp that was passed into the request.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_interval_end:
            description:
                - The end timestamp that was passed into the request.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        high_utilization_threshold:
            description:
                - Percent value in which a resource metric is considered highly utilized.
            returned: on success
            type: int
            sample: 56
        low_utilization_threshold:
            description:
                - Percent value in which a resource metric is considered lowly utilized.
            returned: on success
            type: int
            sample: 56
        resource_metric:
            description:
                - "Defines the type of resource metric (example: CPU, STORAGE)"
            returned: on success
            type: str
            sample: CPU
        projected_utilization:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                low:
                    description:
                        - List of db ids with low usage
                    returned: on success
                    type: complex
                    contains:
                        id:
                            description:
                                - Db id
                            returned: on success
                            type: str
                            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                        days_to_reach:
                            description:
                                - Days to reach projected utilization
                            returned: on success
                            type: int
                            sample: 56
                high:
                    description:
                        - List of db ids with high usage
                    returned: on success
                    type: complex
                    contains:
                        id:
                            description:
                                - Db id
                            returned: on success
                            type: str
                            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                        days_to_reach:
                            description:
                                - Days to reach projected utilization
                            returned: on success
                            type: int
                            sample: 56
        current_utilization:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                low:
                    description:
                        - List of db ids with low usage
                    returned: on success
                    type: list
                    sample: []
                high:
                    description:
                        - List of db ids with high usage
                    returned: on success
                    type: list
                    sample: []
    sample: {
        "time_interval_start": "2013-10-20T19:20:30+01:00",
        "time_interval_end": "2013-10-20T19:20:30+01:00",
        "high_utilization_threshold": 56,
        "low_utilization_threshold": 56,
        "resource_metric": "CPU",
        "projected_utilization": {
            "low": [{
                "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
                "days_to_reach": 56
            }],
            "high": [{
                "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
                "days_to_reach": 56
            }]
        },
        "current_utilization": {
            "low": [],
            "high": []
        }
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.opsi import OperationsInsightsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ResourceUtilizationInsightFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "compartment_id",
            "resource_metric",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "database_type",
            "database_id",
            "id",
            "exadata_insight_id",
            "forecast_days",
            "host_name",
            "is_database_instance_level_metrics",
            "defined_tag_equals",
            "freeform_tag_equals",
            "defined_tag_exists",
            "freeform_tag_exists",
            "compartment_id_in_subtree",
            "vmcluster_name",
            "cdb_name",
            "high_utilization_threshold",
            "low_utilization_threshold",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.summarize_database_insight_resource_utilization_insight,
            compartment_id=self.module.params.get("compartment_id"),
            resource_metric=self.module.params.get("resource_metric"),
            **optional_kwargs
        )


ResourceUtilizationInsightFactsHelperCustom = get_custom_class(
    "ResourceUtilizationInsightFactsHelperCustom"
)


class ResourceFactsHelper(
    ResourceUtilizationInsightFactsHelperCustom,
    ResourceUtilizationInsightFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            resource_metric=dict(type="str", required=True),
            analysis_time_interval=dict(type="str"),
            time_interval_start=dict(type="str"),
            time_interval_end=dict(type="str"),
            database_type=dict(
                type="list",
                elements="str",
                choices=[
                    "ADW-S",
                    "ATP-S",
                    "ADW-D",
                    "ATP-D",
                    "EXTERNAL-PDB",
                    "EXTERNAL-NONCDB",
                    "COMANAGED-VM-CDB",
                    "COMANAGED-VM-PDB",
                    "COMANAGED-VM-NONCDB",
                    "COMANAGED-BM-CDB",
                    "COMANAGED-BM-PDB",
                    "COMANAGED-BM-NONCDB",
                    "COMANAGED-EXACS-CDB",
                    "COMANAGED-EXACS-PDB",
                    "COMANAGED-EXACS-NONCDB",
                ],
            ),
            database_id=dict(type="list", elements="str"),
            id=dict(type="list", elements="str"),
            exadata_insight_id=dict(type="list", elements="str"),
            forecast_days=dict(type="int"),
            host_name=dict(type="list", elements="str"),
            is_database_instance_level_metrics=dict(type="bool"),
            defined_tag_equals=dict(type="list", elements="str"),
            freeform_tag_equals=dict(type="list", elements="str"),
            defined_tag_exists=dict(type="list", elements="str"),
            freeform_tag_exists=dict(type="list", elements="str"),
            compartment_id_in_subtree=dict(type="bool"),
            vmcluster_name=dict(type="list", elements="str"),
            cdb_name=dict(type="list", elements="str"),
            high_utilization_threshold=dict(type="int"),
            low_utilization_threshold=dict(type="int"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="resource_utilization_insight",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(resource_utilization_insight=result)


if __name__ == "__main__":
    main()
