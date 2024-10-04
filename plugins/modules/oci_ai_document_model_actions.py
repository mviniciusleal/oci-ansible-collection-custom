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
module: oci_ai_document_model_actions
short_description: Perform actions on a Model resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Model resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a model from one compartment to another. When provided, If-Match is checked against the ETag values of the
      resource.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    model_id:
        description:
            - A unique model identifier.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The compartment identifier.
        type: str
        required: true
    action:
        description:
            - The action to perform on the Model.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on model
  oci_ai_document_model_actions:
    # required
    model_id: "ocid1.model.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
model:
    description:
        - Details of the Model resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - A unique identifier that is immutable after creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A human-friendly name for the model, which can be changed.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - An optional description of the model.
            returned: on success
            type: str
            sample: description_example
        compartment_id:
            description:
                - The compartment identifier.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        model_type:
            description:
                - The type of the Document model.
            returned: on success
            type: str
            sample: KEY_VALUE_EXTRACTION
        tenancy_id:
            description:
                - The tenancy id of the model.
            returned: on success
            type: str
            sample: "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx"
        alias_name:
            description:
                - the alias name of the model.
            returned: on success
            type: str
            sample: alias_name_example
        labels:
            description:
                - The collection of labels used to train the custom model.
            returned: on success
            type: list
            sample: []
        is_quick_mode:
            description:
                - Set to true when experimenting with a new model type or dataset, so model training is quick, with a predefined low number of passes through
                  the training data.
            returned: on success
            type: bool
            sample: true
        max_training_time_in_hours:
            description:
                - The maximum model training time in hours, expressed as a decimal fraction.
            returned: on success
            type: float
            sample: 1.2
        trained_time_in_hours:
            description:
                - The total hours actually used for model training.
            returned: on success
            type: float
            sample: 1.2
        training_dataset:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                dataset_id:
                    description:
                        - OCID of the Data Labeling dataset.
                    returned: on success
                    type: str
                    sample: "ocid1.dataset.oc1..xxxxxxEXAMPLExxxxxx"
                dataset_type:
                    description:
                        - The dataset type, based on where it is stored.
                    returned: on success
                    type: str
                    sample: DATA_SCIENCE_LABELING
                namespace_name:
                    description:
                        - The namespace name of the Object Storage bucket that contains the input data file.
                    returned: on success
                    type: str
                    sample: namespace_name_example
                bucket_name:
                    description:
                        - The name of the Object Storage bucket that contains the input data file.
                    returned: on success
                    type: str
                    sample: bucket_name_example
                object_name:
                    description:
                        - The object name of the input data file.
                    returned: on success
                    type: str
                    sample: object_name_example
        testing_dataset:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                dataset_id:
                    description:
                        - OCID of the Data Labeling dataset.
                    returned: on success
                    type: str
                    sample: "ocid1.dataset.oc1..xxxxxxEXAMPLExxxxxx"
                dataset_type:
                    description:
                        - The dataset type, based on where it is stored.
                    returned: on success
                    type: str
                    sample: DATA_SCIENCE_LABELING
                namespace_name:
                    description:
                        - The namespace name of the Object Storage bucket that contains the input data file.
                    returned: on success
                    type: str
                    sample: namespace_name_example
                bucket_name:
                    description:
                        - The name of the Object Storage bucket that contains the input data file.
                    returned: on success
                    type: str
                    sample: bucket_name_example
                object_name:
                    description:
                        - The object name of the input data file.
                    returned: on success
                    type: str
                    sample: object_name_example
        validation_dataset:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                dataset_id:
                    description:
                        - OCID of the Data Labeling dataset.
                    returned: on success
                    type: str
                    sample: "ocid1.dataset.oc1..xxxxxxEXAMPLExxxxxx"
                dataset_type:
                    description:
                        - The dataset type, based on where it is stored.
                    returned: on success
                    type: str
                    sample: DATA_SCIENCE_LABELING
                namespace_name:
                    description:
                        - The namespace name of the Object Storage bucket that contains the input data file.
                    returned: on success
                    type: str
                    sample: namespace_name_example
                bucket_name:
                    description:
                        - The name of the Object Storage bucket that contains the input data file.
                    returned: on success
                    type: str
                    sample: bucket_name_example
                object_name:
                    description:
                        - The object name of the input data file.
                    returned: on success
                    type: str
                    sample: object_name_example
        component_models:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) collection of active custom Key Value models that need
                  to be composed.
            returned: on success
            type: complex
            contains:
                model_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of active custom Key Value model that need to
                          be composed.
                    returned: on success
                    type: str
                    sample: "ocid1.model.oc1..xxxxxxEXAMPLExxxxxx"
        is_composed_model:
            description:
                - Set to true when the model is created by using multiple key value extraction models.
            returned: on success
            type: bool
            sample: true
        model_version:
            description:
                - The version of the model.
            returned: on success
            type: str
            sample: model_version_example
        project_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the project that contains the model.
            returned: on success
            type: str
            sample: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - When the model was created, as an RFC3339 datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - When the model was updated, as an RFC3339 datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the model.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail, that can provide actionable information if training failed.
            returned: on success
            type: str
            sample: lifecycle_details_example
        metrics:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                model_type:
                    description:
                        - The type of custom model trained.
                    returned: on success
                    type: str
                    sample: KEY_VALUE_EXTRACTION
                dataset_summary:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        training_sample_count:
                            description:
                                - Number of samples used for training the model.
                            returned: on success
                            type: int
                            sample: 56
                        validation_sample_count:
                            description:
                                - Number of samples used for validating the model.
                            returned: on success
                            type: int
                            sample: 56
                        test_sample_count:
                            description:
                                - Number of samples used for testing the model.
                            returned: on success
                            type: int
                            sample: 56
                label_metrics_report:
                    description:
                        - List of metrics entries per label.
                    returned: on success
                    type: complex
                    contains:
                        label:
                            description:
                                - Label name
                            returned: on success
                            type: str
                            sample: label_example
                        mean_average_precision:
                            description:
                                - Mean average precision under different thresholds
                            returned: on success
                            type: float
                            sample: 3.4
                        confidence_entries:
                            description:
                                - List of document classification confidence report.
                            returned: on success
                            type: complex
                            contains:
                                threshold:
                                    description:
                                        - Threshold used to calculate precision and recall.
                                    returned: on success
                                    type: float
                                    sample: 3.4
                                precision:
                                    description:
                                        - Precision under the threshold
                                    returned: on success
                                    type: float
                                    sample: 3.4
                                recall:
                                    description:
                                        - Recall under the threshold
                                    returned: on success
                                    type: float
                                    sample: 3.4
                                f1_score:
                                    description:
                                        - f1Score under the threshold
                                    returned: on success
                                    type: float
                                    sample: 3.4
                                accuracy:
                                    description:
                                        - accuracy under the threshold
                                    returned: on success
                                    type: float
                                    sample: 3.4
                        document_count:
                            description:
                                - Total test documents in the label.
                            returned: on success
                            type: int
                            sample: 56
                overall_metrics_report:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        mean_average_precision:
                            description:
                                - Mean average precision under different thresholds
                            returned: on success
                            type: float
                            sample: 3.4
                        confidence_entries:
                            description:
                                - List of document classification confidence report.
                            returned: on success
                            type: complex
                            contains:
                                threshold:
                                    description:
                                        - Threshold used to calculate precision and recall.
                                    returned: on success
                                    type: float
                                    sample: 3.4
                                precision:
                                    description:
                                        - Precision under the threshold
                                    returned: on success
                                    type: float
                                    sample: 3.4
                                recall:
                                    description:
                                        - Recall under the threshold
                                    returned: on success
                                    type: float
                                    sample: 3.4
                                f1_score:
                                    description:
                                        - f1Score under the threshold
                                    returned: on success
                                    type: float
                                    sample: 3.4
                                accuracy:
                                    description:
                                        - accuracy under the threshold
                                    returned: on success
                                    type: float
                                    sample: 3.4
                        document_count:
                            description:
                                - Total test documents in the label.
                            returned: on success
                            type: int
                            sample: 56
        freeform_tags:
            description:
                - "A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only.
                  For example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  For example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "model_type": "KEY_VALUE_EXTRACTION",
        "tenancy_id": "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx",
        "alias_name": "alias_name_example",
        "labels": [],
        "is_quick_mode": true,
        "max_training_time_in_hours": 1.2,
        "trained_time_in_hours": 1.2,
        "training_dataset": {
            "dataset_id": "ocid1.dataset.oc1..xxxxxxEXAMPLExxxxxx",
            "dataset_type": "DATA_SCIENCE_LABELING",
            "namespace_name": "namespace_name_example",
            "bucket_name": "bucket_name_example",
            "object_name": "object_name_example"
        },
        "testing_dataset": {
            "dataset_id": "ocid1.dataset.oc1..xxxxxxEXAMPLExxxxxx",
            "dataset_type": "DATA_SCIENCE_LABELING",
            "namespace_name": "namespace_name_example",
            "bucket_name": "bucket_name_example",
            "object_name": "object_name_example"
        },
        "validation_dataset": {
            "dataset_id": "ocid1.dataset.oc1..xxxxxxEXAMPLExxxxxx",
            "dataset_type": "DATA_SCIENCE_LABELING",
            "namespace_name": "namespace_name_example",
            "bucket_name": "bucket_name_example",
            "object_name": "object_name_example"
        },
        "component_models": [{
            "model_id": "ocid1.model.oc1..xxxxxxEXAMPLExxxxxx"
        }],
        "is_composed_model": true,
        "model_version": "model_version_example",
        "project_id": "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "metrics": {
            "model_type": "KEY_VALUE_EXTRACTION",
            "dataset_summary": {
                "training_sample_count": 56,
                "validation_sample_count": 56,
                "test_sample_count": 56
            },
            "label_metrics_report": [{
                "label": "label_example",
                "mean_average_precision": 3.4,
                "confidence_entries": [{
                    "threshold": 3.4,
                    "precision": 3.4,
                    "recall": 3.4,
                    "f1_score": 3.4,
                    "accuracy": 3.4
                }],
                "document_count": 56
            }],
            "overall_metrics_report": {
                "mean_average_precision": 3.4,
                "confidence_entries": [{
                    "threshold": 3.4,
                    "precision": 3.4,
                    "recall": 3.4,
                    "f1_score": 3.4,
                    "accuracy": 3.4
                }],
                "document_count": 56
            }
        },
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
    from oci.ai_document import AIServiceDocumentClient
    from oci.ai_document.models import ChangeModelCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AiDocumentModelActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "model_id"

    def get_module_resource_id(self):
        return self.module.params.get("model_id")

    def get_get_fn(self):
        return self.client.get_model

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_model, model_id=self.module.params.get("model_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeModelCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_model_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                model_id=self.module.params.get("model_id"),
                change_model_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
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


AiDocumentModelActionsHelperCustom = get_custom_class(
    "AiDocumentModelActionsHelperCustom"
)


class ResourceHelper(
    AiDocumentModelActionsHelperCustom, AiDocumentModelActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            model_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="model",
        service_client_class=AIServiceDocumentClient,
        namespace="ai_document",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
