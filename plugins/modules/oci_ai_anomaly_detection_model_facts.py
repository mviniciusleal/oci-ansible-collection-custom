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
module: oci_ai_anomaly_detection_model_facts
short_description: Fetches details about one or multiple Model resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Model resources in Oracle Cloud Infrastructure
    - Returns a list of Models.
    - If I(model_id) is specified, the details of a single Model will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    model_id:
        description:
            - The OCID of the Model.
            - Required to get a specific model.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required to list multiple models.
        type: str
    project_id:
        description:
            - The ID of the project for which to list the objects.
        type: str
    lifecycle_state:
        description:
            - <b>Filter</b> results by the specified lifecycle state. Must be a valid
              state for the resource type.
        type: str
        choices:
            - "DELETING"
            - "DELETED"
            - "FAILED"
            - "CREATING"
            - "ACTIVE"
            - "UPDATING"
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
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
            - Specifies the field to sort by. Accepts only one field.
              By default, when you sort by `timeCreated`, the results are shown
              in descending order. When you sort by `displayName`, the results are
              shown in ascending order. Sort order for the `displayName` field is case sensitive.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific model
  oci_ai_anomaly_detection_model_facts:
    # required
    model_id: "ocid1.model.oc1..xxxxxxEXAMPLExxxxxx"

- name: List models
  oci_ai_anomaly_detection_model_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    project_id: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_state: DELETING
    display_name: display_name_example
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
models:
    description:
        - List of Model resources
    returned: on success
    type: complex
    contains:
        time_updated:
            description:
                - The time the Model was updated. An RFC3339 formatted datetime string.
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
                - Returned for get operation
            returned: on success
            type: str
            sample: lifecycle_details_example
        id:
            description:
                - The OCID of the model that is immutable on creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - A short description of the Model.
            returned: on success
            type: str
            sample: description_example
        compartment_id:
            description:
                - The OCID for the model's compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        model_training_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                algorithm_hint:
                    description:
                        - User can choose specific algorithm for training.
                    returned: on success
                    type: str
                    sample: MULTIVARIATE_MSET
                target_fap:
                    description:
                        - A target model accuracy metric user provides as their requirement
                    returned: on success
                    type: float
                    sample: 3.4
                training_fraction:
                    description:
                        - Fraction of total data that is used for training the model. The remaining is used for validation of the model.
                    returned: on success
                    type: float
                    sample: 3.4
                window_size:
                    description:
                        - This value would determine the window size of the training algorithm.
                    returned: on success
                    type: int
                    sample: 56
                data_asset_ids:
                    description:
                        - The list of OCIDs of the data assets to train the model. The dataAssets have to be in the same project where the ai model would
                          reside.
                    returned: on success
                    type: list
                    sample: []
        model_training_results:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                fap:
                    description:
                        - The final-achieved model accuracy metric on individual value level
                    returned: on success
                    type: float
                    sample: 3.4
                multivariate_fap:
                    description:
                        - The model accuracy metric on timestamp level.
                    returned: on success
                    type: float
                    sample: 3.4
                algorithm:
                    description:
                        - Actual algorithm used to train the model
                    returned: on success
                    type: str
                    sample: MULTIVARIATE_MSET
                window_size:
                    description:
                        - Window size defined during training or deduced by the algorithm.
                    returned: on success
                    type: int
                    sample: 56
                is_training_goal_achieved:
                    description:
                        - A boolean value to indicate if train goal/targetFap is achieved for trained model
                    returned: on success
                    type: bool
                    sample: true
                warning:
                    description:
                        - A warning message to explain the reason when targetFap cannot be achieved for trained model
                    returned: on success
                    type: str
                    sample: warning_example
                signal_details:
                    description:
                        - The list of signal details.
                    returned: on success
                    type: complex
                    contains:
                        signal_name:
                            description:
                                - The name of a signal.
                            returned: on success
                            type: str
                            sample: signal_name_example
                        mvi_ratio:
                            description:
                                - The ratio of missing values in a signal filled/imputed by the IDP algorithm.
                            returned: on success
                            type: float
                            sample: 1.2
                        is_quantized:
                            description:
                                - A boolean value to indicate if a signal is quantized or not.
                            returned: on success
                            type: bool
                            sample: true
                        fap:
                            description:
                                - Accuracy metric for a signal.
                            returned: on success
                            type: float
                            sample: 3.4
                        min:
                            description:
                                - Min value within a signal.
                            returned: on success
                            type: float
                            sample: 1.2
                        max:
                            description:
                                - Max value within a signal.
                            returned: on success
                            type: float
                            sample: 1.2
                        std:
                            description:
                                - Standard deviation of values within a signal.
                            returned: on success
                            type: float
                            sample: 1.2
                        status:
                            description:
                                - "Status of the signal:
                                   * ACCEPTED - the signal is used for training the model
                                   * DROPPED - the signal does not meet requirement, and is dropped before training the model.
                                   * OTHER - placeholder for other status"
                            returned: on success
                            type: str
                            sample: ACCEPTED
                        details:
                            description:
                                - detailed information for a signal.
                            returned: on success
                            type: str
                            sample: details_example
                row_reduction_details:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        is_reduction_enabled:
                            description:
                                - A boolean value to indicate if row reduction is applied
                            returned: on success
                            type: bool
                            sample: true
                        reduction_percentage:
                            description:
                                - A percentage to reduce data size down to on top of original data
                            returned: on success
                            type: float
                            sample: 1.2
                        reduction_method:
                            description:
                                - "Method for row reduction:
                                    * DELETE_ROW - delete rows with equal intervals
                                    * AVERAGE_ROW - average multiple rows to one row"
                            returned: on success
                            type: str
                            sample: DELETE_ROW
        time_created:
            description:
                - The time the the Model was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The state of the model.
            returned: on success
            type: str
            sample: DELETING
        project_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the project to associate with the model.
            returned: on success
            type: str
            sample: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
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
                  Example: `{ \\"orcl-cloud\\": { \\"free-tier-retained\\": \\"true\\" } }`"
            returned: on success
            type: dict
            sample: {}
    sample: [{
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_details": "lifecycle_details_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "model_training_details": {
            "algorithm_hint": "MULTIVARIATE_MSET",
            "target_fap": 3.4,
            "training_fraction": 3.4,
            "window_size": 56,
            "data_asset_ids": []
        },
        "model_training_results": {
            "fap": 3.4,
            "multivariate_fap": 3.4,
            "algorithm": "MULTIVARIATE_MSET",
            "window_size": 56,
            "is_training_goal_achieved": true,
            "warning": "warning_example",
            "signal_details": [{
                "signal_name": "signal_name_example",
                "mvi_ratio": 1.2,
                "is_quantized": true,
                "fap": 3.4,
                "min": 1.2,
                "max": 1.2,
                "std": 1.2,
                "status": "ACCEPTED",
                "details": "details_example"
            }],
            "row_reduction_details": {
                "is_reduction_enabled": true,
                "reduction_percentage": 1.2,
                "reduction_method": "DELETE_ROW"
            }
        },
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "DELETING",
        "project_id": "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.ai_anomaly_detection import AnomalyDetectionClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ModelFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "model_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_model, model_id=self.module.params.get("model_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "project_id",
            "lifecycle_state",
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
            self.client.list_models,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ModelFactsHelperCustom = get_custom_class("ModelFactsHelperCustom")


class ResourceFactsHelper(ModelFactsHelperCustom, ModelFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            model_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            project_id=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "DELETING",
                    "DELETED",
                    "FAILED",
                    "CREATING",
                    "ACTIVE",
                    "UPDATING",
                ],
            ),
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
        resource_type="model",
        service_client_class=AnomalyDetectionClient,
        namespace="ai_anomaly_detection",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(models=result)


if __name__ == "__main__":
    main()
