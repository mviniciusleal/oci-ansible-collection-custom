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
module: oci_ai_language_batch_detect_language_pii_entities_actions
short_description: Perform actions on a BatchDetectLanguagePiiEntities resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a BatchDetectLanguagePiiEntities resource in Oracle Cloud Infrastructure
    - "For I(action=batch_detect_language_pii_entities), the API extracts pii entities in text records. For each entity, its type and confidence score (between
      0 and 1) is returned.  It supports passing a batch of records.
      Limitations:
      - A batch may have up to 100 records.
      - A record may be up to 5000 characters long.
      - The total of characters to process in a request can be up to 20,000 characters."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment that calls the API, inference will be served
              from pre trained model
        type: str
    documents:
        description:
            - List of documents to detect personal identification information.
        type: list
        elements: dict
        required: true
        suboptions:
            key:
                description:
                    - Document unique identifier defined by the user.
                type: str
                required: true
            text:
                description:
                    - Document text for language service call.
                type: str
                required: true
            language_code:
                description:
                    - Language code of the document. Please refer to respective model L(API
                      documentation,https://docs.cloud.oracle.com/iaas/language/using/overview.htm) for supported languages.
                type: str
    masking:
        description:
            - Mask recognized PII entities with different modes.
        type: dict
        suboptions:
            replace_with:
                description:
                    - Replace entities with given sequence of characters. By default PII entity will be replaced with <ENTITY_TYPE>.
                    - Applicable when mode is 'REPLACE'
                type: str
            mode:
                description:
                    - The type of masking mode.
                type: str
                choices:
                    - "REPLACE"
                    - "REMOVE"
                    - "MASK"
                required: true
            masking_character:
                description:
                    - "Masking character. By default, the character is an asterisk (*)"
                    - Applicable when mode is 'MASK'
                type: str
            leave_characters_unmasked:
                description:
                    - Number of characters to leave unmasked. By default, the whole entity is masked.
                    - Applicable when mode is 'MASK'
                type: int
            is_unmasked_from_end:
                description:
                    - "Unmask from the end. By default, the whole entity is masked. This field works in concert with
                      leaveCharactersUnmasked. For example, leaveCharactersUnmasked is 3 and isUnmaskedFromEnd is true,
                      then if the entity is India the masked entity/result is **dia."
                    - Applicable when mode is 'MASK'
                type: bool
    action:
        description:
            - The action to perform on the BatchDetectLanguagePiiEntities.
        type: str
        required: true
        choices:
            - "batch_detect_language_pii_entities"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action batch_detect_language_pii_entities on batch_detect_language_pii_entities
  oci_ai_language_batch_detect_language_pii_entities_actions:
    # required
    documents:
    - # required
      key: key_example
      text: text_example

      # optional
      language_code: language_code_example
    action: batch_detect_language_pii_entities

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    masking:
      # required
      mode: REPLACE

      # optional
      replace_with: replace_with_example

"""

RETURN = """
batch_detect_language_pii_entities_result:
    description:
        - Details of the BatchDetectLanguagePiiEntities resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        documents:
            description:
                - List of succeeded document response.
            returned: on success
            type: complex
            contains:
                key:
                    description:
                        - Document unique identifier defined by the user.
                    returned: on success
                    type: str
                    sample: key_example
                entities:
                    description:
                        - List of batch detect personal identification.
                    returned: on success
                    type: complex
                    contains:
                        offset:
                            description:
                                - The number of Unicode code points preceding this entity in the submitted text.
                            returned: on success
                            type: int
                            sample: 56
                        length:
                            description:
                                - Length of PII entity text.
                            returned: on success
                            type: int
                            sample: 56
                        text:
                            description:
                                - Entity text like name of person, Organization and so on.
                            returned: on success
                            type: str
                            sample: text_example
                        type:
                            description:
                                - Type of PII entity text like PER, LOC.
                            returned: on success
                            type: str
                            sample: type_example
                        score:
                            description:
                                - Score or confidence for detected PII entity.
                            returned: on success
                            type: float
                            sample: 1.2
                masked_text:
                    description:
                        - Masked text per given mask mode.
                    returned: on success
                    type: str
                    sample: masked_text_example
                language_code:
                    description:
                        - "Language code supported
                          - auto : Automatically detect language
                          - ar : Arabic
                          - pt-BR : Brazilian Portuguese
                          - cs : Czech
                          - da : Danish
                          - nl : Dutch
                          - en : English
                          - fi : Finnish
                          - fr : French
                          - fr-CA : Canadian French
                          - de : German
                          - it : Italian
                          - ja : Japanese
                          - ko : Korean
                          - no : Norwegian
                          - pl : Polish
                          - ro : Romanian
                          - zh-CN : Simplified Chinese
                          - es : Spanish
                          - sv : Swedish
                          - zh-TW : Traditional Chinese
                          - tr : Turkish
                          - el : Greek
                          - he : Hebrew"
                    returned: on success
                    type: str
                    sample: language_code_example
        errors:
            description:
                - List of failed document response.
            returned: on success
            type: complex
            contains:
                key:
                    description:
                        - Document unique identifier defined by the user.
                    returned: on success
                    type: str
                    sample: key_example
                error:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        code:
                            description:
                                - A short error code that defines the error, meant for programmatic parsing.
                            returned: on success
                            type: str
                            sample: code_example
                        message:
                            description:
                                - A human-readable error string.
                            returned: on success
                            type: str
                            sample: message_example
    sample: {
        "documents": [{
            "key": "key_example",
            "entities": [{
                "offset": 56,
                "length": 56,
                "text": "text_example",
                "type": "type_example",
                "score": 1.2
            }],
            "masked_text": "masked_text_example",
            "language_code": "language_code_example"
        }],
        "errors": [{
            "key": "key_example",
            "error": {
                "code": "code_example",
                "message": "message_example"
            }
        }]
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
    from oci.ai_language import AIServiceLanguageClient
    from oci.ai_language.models import BatchDetectLanguagePiiEntitiesDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AiLanguageBatchDetectLanguagePiiEntitiesActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        batch_detect_language_pii_entities
    """

    def batch_detect_language_pii_entities(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, BatchDetectLanguagePiiEntitiesDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.batch_detect_language_pii_entities,
            call_fn_args=(),
            call_fn_kwargs=dict(
                batch_detect_language_pii_entities_details=action_details,
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


AiLanguageBatchDetectLanguagePiiEntitiesActionsHelperCustom = get_custom_class(
    "AiLanguageBatchDetectLanguagePiiEntitiesActionsHelperCustom"
)


class ResourceHelper(
    AiLanguageBatchDetectLanguagePiiEntitiesActionsHelperCustom,
    AiLanguageBatchDetectLanguagePiiEntitiesActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            documents=dict(
                type="list",
                elements="dict",
                required=True,
                options=dict(
                    key=dict(type="str", required=True, no_log=True),
                    text=dict(type="str", required=True),
                    language_code=dict(type="str"),
                ),
            ),
            masking=dict(type="dict"),
            action=dict(
                type="str",
                required=True,
                choices=["batch_detect_language_pii_entities"],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="batch_detect_language_pii_entities",
        service_client_class=AIServiceLanguageClient,
        namespace="ai_language",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
