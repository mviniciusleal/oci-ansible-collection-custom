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
module: oci_monitoring_alarm_actions
short_description: Perform actions on an Alarm resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an Alarm resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves an alarm into a different compartment within the same tenancy.
      For more information, see
      L(Moving an Alarm,https://docs.cloud.oracle.com/iaas/Content/Monitoring/Tasks/change-compartment-alarm.htm).
    - For I(action=remove_alarm_suppression), removes any existing suppression for the specified alarm.
      For more information, see
      L(Removing Suppression from an Alarm,https://docs.cloud.oracle.com/iaas/Content/Monitoring/Tasks/remove-alarm-suppression.htm).
      For important limits information, see
      L(Limits on Monitoring,https://docs.cloud.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#limits).
      This call is subject to a Monitoring limit that applies to the total number of requests across all alarm operations.
      Monitoring might throttle this call to reject an otherwise valid request when the total rate of alarm operations exceeds 10 requests,
      or transactions, per second (TPS) for a given tenancy.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the alarm to.
            - Required for I(action=change_compartment).
        type: str
    alarm_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of an alarm.
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the Alarm.
        type: str
        required: true
        choices:
            - "change_compartment"
            - "remove_alarm_suppression"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on alarm
  oci_monitoring_alarm_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    alarm_id: "ocid1.alarm.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action remove_alarm_suppression on alarm
  oci_monitoring_alarm_actions:
    # required
    alarm_id: "ocid1.alarm.oc1..xxxxxxEXAMPLExxxxxx"
    action: remove_alarm_suppression

"""

RETURN = """
alarm:
    description:
        - Details of the Alarm resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the alarm.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name for the alarm. It does not have to be unique, and it's changeable.
                - This value determines the title of each alarm notification.
                - "Example: `High CPU Utilization`"
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the alarm.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        metric_compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the metric
                  being evaluated by the alarm.
            returned: on success
            type: str
            sample: "ocid1.metriccompartment.oc1..xxxxxxEXAMPLExxxxxx"
        metric_compartment_id_in_subtree:
            description:
                - When true, the alarm evaluates metrics from all compartments and subcompartments. The parameter can
                  only be set to true when metricCompartmentId is the tenancy OCID (the tenancy is the root compartment).
                  A true value requires the user to have tenancy-level permissions. If this requirement is not met,
                  then the call is rejected. When false, the alarm evaluates metrics from only the compartment specified
                  in metricCompartmentId. Default is false.
                - "Example: `true`"
            returned: on success
            type: bool
            sample: true
        namespace:
            description:
                - The source service or application emitting the metric that is evaluated by the alarm.
                - "Example: `oci_computeagent`"
            returned: on success
            type: str
            sample: namespace_example
        resource_group:
            description:
                - Resource group to match for metric data retrieved by the alarm. A resource group is a custom string that you can match when retrieving custom
                  metrics. Only one resource group can be applied per metric.
                  A valid resourceGroup value starts with an alphabetical character and includes only alphanumeric characters, periods (.), underscores (_),
                  hyphens (-), and dollar signs ($).
                - "Example: `frontend-fleet`"
            returned: on success
            type: str
            sample: resource_group_example
        query:
            description:
                - "The Monitoring Query Language (MQL) expression to evaluate for the alarm. The Alarms feature of
                  the Monitoring service interprets results for each returned time series as Boolean values,
                  where zero represents false and a non-zero value represents true. A true value means that the trigger
                  rule condition has been met. The query must specify a metric, statistic, interval, and trigger
                  rule (threshold or absence). Supported values for interval depend on the specified time range. More
                  interval values are supported for smaller time ranges. You can optionally
                  specify dimensions and grouping functions.
                  Also, you can customize the
                  L(absence detection period,https://docs.cloud.oracle.com/iaas/Content/Monitoring/Tasks/create-edit-alarm-query-absence-detection-period.htm).
                  Supported grouping functions: `grouping()`, `groupBy()`.
                  For information about writing MQL expressions, see
                  L(Editing the MQL Expression for a Query,https://docs.cloud.oracle.com/iaas/Content/Monitoring/Tasks/query-metric-mql.htm).
                  For details about MQL, see
                  L(Monitoring Query Language (MQL) Reference,https://docs.cloud.oracle.com/iaas/Content/Monitoring/Reference/mql.htm).
                  For available dimensions, review the metric definition for the supported service. See
                  L(Supported Services,https://docs.cloud.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#SupportedServices)."
                - "Example of threshold alarm:"
                -   -----
                - "   CpuUtilization[1m]{availabilityDomain=\\"cumS:PHX-AD-1\\"}.groupBy(availabilityDomain).percentile(0.9) > 85"
                -   -----
                - "Example of absence alarm:"
                -   -----
                - "   CpuUtilization[1m]{availabilityDomain=\\"cumS:PHX-AD-1\\"}.absent()"
                - " -----
                  Example of absence alarm with custom absence detection period of 20 hours:"
                -   -----
                - "   CpuUtilization[1m]{availabilityDomain=\\"cumS:PHX-AD-1\\"}.absent(20h)"
                -   -----
            returned: on success
            type: str
            sample: query_example
        resolution:
            description:
                - "The time between calculated aggregation windows for the alarm. Supported value: `1m`"
            returned: on success
            type: str
            sample: resolution_example
        pending_duration:
            description:
                - "The period of time that the condition defined in the alarm must persist before the alarm state
                  changes from \\"OK\\" to \\"FIRING\\". For example, a value of 5 minutes means that the
                  alarm must persist in breaching the condition for five minutes before the alarm updates its
                  state to \\"FIRING\\"."
                - "The duration is specified as a string in ISO 8601 format (`PT10M` for ten minutes or `PT1H`
                  for one hour). Minimum: PT1M. Maximum: PT1H. Default: PT1M."
                - "Under the default value of PT1M, the first evaluation that breaches the alarm updates the
                  state to \\"FIRING\\"."
                - "The alarm updates its status to \\"OK\\" when the breaching condition has been clear for
                  the most recent minute."
                - "Example: `PT5M`"
            returned: on success
            type: str
            sample: pending_duration_example
        severity:
            description:
                - "The perceived type of response required when the alarm is in the \\"FIRING\\" state."
                - "Example: `CRITICAL`"
            returned: on success
            type: str
            sample: CRITICAL
        body:
            description:
                - The human-readable content of the delivered alarm notification.
                  Optionally include L(dynamic variables,https://docs.cloud.oracle.com/iaas/Content/Monitoring/Tasks/update-alarm-dynamic-variables.htm).
                  Oracle recommends providing guidance
                  to operators for resolving the alarm condition. Consider adding links to standard runbook
                  practices. Avoid entering confidential information.
                - "Example: `High CPU usage alert. Follow runbook instructions for resolution.`"
            returned: on success
            type: str
            sample: body_example
        is_notifications_per_metric_dimension_enabled:
            description:
                - When set to `true`, splits alarm notifications per metric stream.
                  When set to `false`, groups alarm notifications across metric streams.
            returned: on success
            type: bool
            sample: true
        message_format:
            description:
                - "The format to use for alarm notifications. The formats are:
                  * `RAW` - Raw JSON blob. Default value. When the `destinations` attribute specifies `Streaming`, all alarm notifications use this format.
                  * `PRETTY_JSON`: JSON with new lines and indents. Available when the `destinations` attribute specifies `Notifications` only.
                  * `ONS_OPTIMIZED`: Simplified, user-friendly layout. Available when the `destinations` attribute specifies `Notifications` only. Applies to
                  Email subscription types only."
            returned: on success
            type: str
            sample: RAW
        destinations:
            description:
                - "A list of destinations for alarm notifications.
                  Each destination is represented by the L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm)
                  of a related resource, such as a L(topic,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/notification/latest/NotificationTopic).
                  Supported destination services: Notifications, Streaming.
                  Limit: One destination per supported destination service."
            returned: on success
            type: list
            sample: []
        repeat_notification_duration:
            description:
                - "The frequency for re-submitting alarm notifications, if the alarm keeps firing without
                  interruption. Format defined by ISO 8601. For example, `PT4H` indicates four hours.
                  Minimum: PT1M. Maximum: P30D."
                - "Default value: null (notifications are not re-submitted)."
                - "Example: `PT2H`"
            returned: on success
            type: str
            sample: repeat_notification_duration_example
        suppression:
            description:
                - The configuration details for suppressing an alarm.
            returned: on success
            type: complex
            contains:
                description:
                    description:
                        - Human-readable reason for suppressing alarm notifications.
                          It does not have to be unique, and it's changeable.
                          Avoid entering confidential information.
                        - Oracle recommends including tracking information for the event or associated work,
                          such as a ticket number.
                        - "Example: `Planned outage due to change IT-1234.`"
                    returned: on success
                    type: str
                    sample: description_example
                time_suppress_from:
                    description:
                        - The start date and time for the suppression to take place, inclusive. Format defined by RFC3339.
                        - "Example: `2023-02-01T01:02:29.600Z`"
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_suppress_until:
                    description:
                        - The end date and time for the suppression to take place, inclusive. Format defined by RFC3339.
                        - "Example: `2023-02-01T02:02:29.600Z`"
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
        is_enabled:
            description:
                - Whether the alarm is enabled.
                - "Example: `true`"
            returned: on success
            type: bool
            sample: true
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Usage of predefined tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        overrides:
            description:
                - A set of overrides that control evaluations of the alarm.
                - Each override can specify values for query, severity, body, and pending duration.
                  When an alarm contains overrides, the Monitoring service evaluates each override in order, beginning with the first override in the array
                  (index position `0`),
                  and then evaluates the alarm's base values (`ruleName` value of `BASE`).
            returned: on success
            type: complex
            contains:
                pending_duration:
                    description:
                        - "The period of time that the condition defined in the alarm must persist before the alarm state
                          changes from \\"OK\\" to \\"FIRING\\". For example, a value of 5 minutes means that the
                          alarm must persist in breaching the condition for five minutes before the alarm updates its
                          state to \\"FIRING\\"."
                        - "The duration is specified as a string in ISO 8601 format (`PT10M` for ten minutes or `PT1H`
                          for one hour). Minimum: PT1M. Maximum: PT1H. Default: PT1M."
                        - "Under the default value of PT1M, the first evaluation that breaches the alarm updates the
                          state to \\"FIRING\\"."
                        - "The alarm updates its status to \\"OK\\" when the breaching condition has been clear for
                          the most recent minute."
                        - "Example: `PT5M`"
                    returned: on success
                    type: str
                    sample: pending_duration_example
                severity:
                    description:
                        - The perceived severity of the alarm with regard to the affected system.
                        - "Example: `CRITICAL`"
                    returned: on success
                    type: str
                    sample: severity_example
                body:
                    description:
                        - The human-readable content of the delivered alarm notification.
                          Optionally include L(dynamic variables,https://docs.cloud.oracle.com/iaas/Content/Monitoring/Tasks/update-alarm-dynamic-
                          variables.htm).
                          Oracle recommends providing guidance
                          to operators for resolving the alarm condition. Consider adding links to standard runbook
                          practices. Avoid entering confidential information.
                        - "Example: `High CPU usage alert. Follow runbook instructions for resolution.`"
                    returned: on success
                    type: str
                    sample: body_example
                rule_name:
                    description:
                        - A user-friendly description for this alarm override. Must be unique across all `ruleName` values for the alarm.
                    returned: on success
                    type: str
                    sample: rule_name_example
                query:
                    description:
                        - "The Monitoring Query Language (MQL) expression to evaluate for the alarm. The Alarms feature of
                          the Monitoring service interprets results for each returned time series as Boolean values,
                          where zero represents false and a non-zero value represents true. A true value means that the trigger
                          rule condition has been met. The query must specify a metric, statistic, interval, and trigger
                          rule (threshold or absence). Supported values for interval depend on the specified time range. More
                          interval values are supported for smaller time ranges. You can optionally
                          specify dimensions and grouping functions.
                          Also, you can customize the
                          L(absence detection period,https://docs.cloud.oracle.com/iaas/Content/Monitoring/Tasks/create-edit-alarm-query-absence-detection-
                          period.htm).
                          Supported grouping functions: `grouping()`, `groupBy()`.
                          For information about writing MQL expressions, see
                          L(Editing the MQL Expression for a Query,https://docs.cloud.oracle.com/iaas/Content/Monitoring/Tasks/query-metric-mql.htm).
                          For details about MQL, see
                          L(Monitoring Query Language (MQL) Reference,https://docs.cloud.oracle.com/iaas/Content/Monitoring/Reference/mql.htm).
                          For available dimensions, review the metric definition for the supported service. See
                          L(Supported Services,https://docs.cloud.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#SupportedServices)."
                        - "Example of threshold alarm:"
                        -   -----
                        - "   CpuUtilization[1m]{availabilityDomain=\\"cumS:PHX-AD-1\\"}.groupBy(availabilityDomain).percentile(0.9) > 85"
                        -   -----
                        - "Example of absence alarm:"
                        -   -----
                        - "   CpuUtilization[1m]{availabilityDomain=\\"cumS:PHX-AD-1\\"}.absent()"
                        - " -----
                          Example of absence alarm with custom absence detection period of 20 hours:"
                        -   -----
                        - "   CpuUtilization[1m]{availabilityDomain=\\"cumS:PHX-AD-1\\"}.absent(20h)"
                        -   -----
                    returned: on success
                    type: str
                    sample: query_example
        rule_name:
            description:
                - Identifier of the alarm's base values for alarm evaluation, for use when the alarm contains overrides.
                  Default value is `BASE`. For information about alarm overrides, see L(AlarmOverride,https://docs.cloud.oracle.com/en-
                  us/iaas/api/#/en/monitoring/latest/datatypes/AlarmOverride).
            returned: on success
            type: str
            sample: rule_name_example
        notification_version:
            description:
                - "The version of the alarm notification to be delivered. Allowed value: `1.X`
                  The value must start with a number (up to four digits), followed by a period and an uppercase X."
            returned: on success
            type: str
            sample: notification_version_example
        notification_title:
            description:
                - Customizable notification title (`title` L(alarm message parameter,https://docs.cloud.oracle.com/iaas/Content/Monitoring/alarm-message-
                  format.htm)).
                  Optionally include L(dynamic variables,https://docs.cloud.oracle.com/iaas/Content/Monitoring/Tasks/update-alarm-dynamic-variables.htm).
                  The notification title appears as the subject line in a formatted email message and as the title in a Slack message.
            returned: on success
            type: str
            sample: notification_title_example
        evaluation_slack_duration:
            description:
                - "Customizable slack period to wait for metric ingestion before evaluating the alarm.
                  Specify a string in ISO 8601 format (`PT10M` for ten minutes or `PT1H`
                  for one hour). Minimum: PT3M. Maximum: PT2H. Default: PT3M.
                  For more information about the slack period, see
                  L(About the Internal Reset Period,https://docs.cloud.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#reset)."
            returned: on success
            type: str
            sample: evaluation_slack_duration_example
        alarm_summary:
            description:
                - Customizable alarm summary (`alarmSummary` L(alarm message parameter,https://docs.cloud.oracle.com/iaas/Content/Monitoring/alarm-message-
                  format.htm)).
                  Optionally include L(dynamic variables,https://docs.cloud.oracle.com/iaas/Content/Monitoring/Tasks/update-alarm-dynamic-variables.htm).
                  The alarm summary appears within the body of the alarm message and in responses to
                  L(ListAlarmStatus,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/monitoring/latest/AlarmStatusSummary/ListAlarmsStatus)
                  L(GetAlarmHistory,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/monitoring/latest/AlarmHistoryCollection/GetAlarmHistory) and
                  L(RetrieveDimensionStates,https://docs.cloud.oracle.com/en-
                  us/iaas/api/#/en/monitoring/latest/AlarmDimensionStatesCollection/RetrieveDimensionStates).
            returned: on success
            type: str
            sample: alarm_summary_example
        lifecycle_state:
            description:
                - The current lifecycle state of the alarm.
                - "Example: `DELETED`"
            returned: on success
            type: str
            sample: ACTIVE
        time_created:
            description:
                - The date and time the alarm was created. Format defined by RFC3339.
                - "Example: `2023-02-01T01:02:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the alarm was last updated. Format defined by RFC3339.
                - "Example: `2023-02-03T01:02:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "metric_compartment_id": "ocid1.metriccompartment.oc1..xxxxxxEXAMPLExxxxxx",
        "metric_compartment_id_in_subtree": true,
        "namespace": "namespace_example",
        "resource_group": "resource_group_example",
        "query": "query_example",
        "resolution": "resolution_example",
        "pending_duration": "pending_duration_example",
        "severity": "CRITICAL",
        "body": "body_example",
        "is_notifications_per_metric_dimension_enabled": true,
        "message_format": "RAW",
        "destinations": [],
        "repeat_notification_duration": "repeat_notification_duration_example",
        "suppression": {
            "description": "description_example",
            "time_suppress_from": "2013-10-20T19:20:30+01:00",
            "time_suppress_until": "2013-10-20T19:20:30+01:00"
        },
        "is_enabled": true,
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "overrides": [{
            "pending_duration": "pending_duration_example",
            "severity": "severity_example",
            "body": "body_example",
            "rule_name": "rule_name_example",
            "query": "query_example"
        }],
        "rule_name": "rule_name_example",
        "notification_version": "notification_version_example",
        "notification_title": "notification_title_example",
        "evaluation_slack_duration": "evaluation_slack_duration_example",
        "alarm_summary": "alarm_summary_example",
        "lifecycle_state": "ACTIVE",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00"
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
    from oci.monitoring import MonitoringClient
    from oci.monitoring.models import ChangeAlarmCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AlarmActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
        remove_alarm_suppression
    """

    @staticmethod
    def get_module_resource_id_param():
        return "alarm_id"

    def get_module_resource_id(self):
        return self.module.params.get("alarm_id")

    def get_get_fn(self):
        return self.client.get_alarm

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_alarm, alarm_id=self.module.params.get("alarm_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeAlarmCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_alarm_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                alarm_id=self.module.params.get("alarm_id"),
                change_alarm_compartment_details=action_details,
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

    def remove_alarm_suppression(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.remove_alarm_suppression,
            call_fn_args=(),
            call_fn_kwargs=dict(alarm_id=self.module.params.get("alarm_id"),),
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


AlarmActionsHelperCustom = get_custom_class("AlarmActionsHelperCustom")


class ResourceHelper(AlarmActionsHelperCustom, AlarmActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            alarm_id=dict(aliases=["id"], type="str", required=True),
            action=dict(
                type="str",
                required=True,
                choices=["change_compartment", "remove_alarm_suppression"],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="alarm",
        service_client_class=MonitoringClient,
        namespace="monitoring",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
