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
module: oci_monitoring_alarm
short_description: Manage an Alarm resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an Alarm resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new alarm in the specified compartment.
      For more information, see
      L(Creating an Alarm,https://docs.cloud.oracle.com/iaas/Content/Monitoring/Tasks/create-alarm.htm).
      For important limits information, see
      L(Limits on Monitoring,https://docs.cloud.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#limits).
    - This call is subject to a Monitoring limit that applies to the total number of requests across all alarm operations.
      Monitoring might throttle this call to reject an otherwise valid request when the total rate of alarm operations exceeds 10 requests,
      or transactions, per second (TPS) for a given tenancy.
    - "This resource has the following action operations in the M(oracle.oci.oci_monitoring_alarm_actions) module: change_compartment,
      remove_alarm_suppression."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    display_name:
        description:
            - A user-friendly name for the alarm. It does not have to be unique, and it's changeable.
              Avoid entering confidential information.
            - This value determines the title of each alarm notification.
            - "Example: `High CPU Utilization`"
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the alarm.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable.
        type: str
    metric_compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the metric
              being evaluated by the alarm.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    metric_compartment_id_in_subtree:
        description:
            - When true, the alarm evaluates metrics from all compartments and subcompartments. The parameter can
              only be set to true when metricCompartmentId is the tenancy OCID (the tenancy is the root compartment).
              A true value requires the user to have tenancy-level permissions. If this requirement is not met,
              then the call is rejected. When false, the alarm evaluates metrics from only the compartment specified
              in metricCompartmentId. Default is false.
            - "Example: `true`"
            - This parameter is updatable.
        type: bool
    namespace:
        description:
            - The source service or application emitting the metric that is evaluated by the alarm.
            - "Example: `oci_computeagent`"
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    resource_group:
        description:
            - Resource group that you want to match. A null value returns only metric data that has no resource groups. The alarm retrieves metric data
              associated with the specified resource group only. Only one resource group can be applied per metric.
              A valid resourceGroup value starts with an alphabetical character and includes only alphanumeric characters, periods (.), underscores (_), hyphens
              (-), and dollar signs ($).
              Avoid entering confidential information.
            - "Example: `frontend-fleet`"
            - This parameter is updatable.
        type: str
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
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    resolution:
        description:
            - "The time between calculated aggregation windows for the alarm. Supported value: `1m`"
            - This parameter is updatable.
        type: str
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
            - This parameter is updatable.
        type: str
    severity:
        description:
            - "The perceived type of response required when the alarm is in the \\"FIRING\\" state."
            - "Example: `CRITICAL`"
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    body:
        description:
            - The human-readable content of the delivered alarm notification.
              Optionally include L(dynamic variables,https://docs.cloud.oracle.com/iaas/Content/Monitoring/Tasks/update-alarm-dynamic-variables.htm).
              Oracle recommends providing guidance
              to operators for resolving the alarm condition. Consider adding links to standard runbook
              practices. Avoid entering confidential information.
            - "Example: `High CPU usage alert. Follow runbook instructions for resolution.`"
            - This parameter is updatable.
        type: str
    is_notifications_per_metric_dimension_enabled:
        description:
            - "When set to `true`, splits alarm notifications per metric stream.
              When set to `false`, groups alarm notifications across metric streams.
              Example: `true`"
            - This parameter is updatable.
        type: bool
    message_format:
        description:
            - "The format to use for alarm notifications. The formats are:
              * `RAW` - Raw JSON blob. Default value. When the `destinations` attribute specifies `Streaming`, all alarm notifications use this format.
              * `PRETTY_JSON`: JSON with new lines and indents. Available when the `destinations` attribute specifies `Notifications` only.
              * `ONS_OPTIMIZED`: Simplified, user-friendly layout. Available when the `destinations` attribute specifies `Notifications` only. Applies to Email
              subscription types only."
            - This parameter is updatable.
        type: str
        choices:
            - "RAW"
            - "PRETTY_JSON"
            - "ONS_OPTIMIZED"
    destinations:
        description:
            - "A list of destinations for alarm notifications.
              Each destination is represented by the L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm)
              of a related resource, such as a L(topic,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/notification/latest/NotificationTopic).
              Supported destination services: Notifications, Streaming.
              Limit: One destination per supported destination service."
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: list
        elements: str
    repeat_notification_duration:
        description:
            - "The frequency for re-submitting alarm notifications, if the alarm keeps firing without
              interruption. Format defined by ISO 8601. For example, `PT4H` indicates four hours.
              Minimum: PT1M. Maximum: P30D."
            - "Default value: null (notifications are not re-submitted)."
            - "Example: `PT2H`"
            - This parameter is updatable.
        type: str
    suppression:
        description:
            - The configuration details for suppressing an alarm.
            - This parameter is updatable.
        type: dict
        suboptions:
            description:
                description:
                    - Human-readable reason for suppressing alarm notifications.
                      It does not have to be unique, and it's changeable.
                      Avoid entering confidential information.
                    - Oracle recommends including tracking information for the event or associated work,
                      such as a ticket number.
                    - "Example: `Planned outage due to change IT-1234.`"
                type: str
            time_suppress_from:
                description:
                    - The start date and time for the suppression to take place, inclusive. Format defined by RFC3339.
                    - "Example: `2023-02-01T01:02:29.600Z`"
                type: str
                required: true
            time_suppress_until:
                description:
                    - The end date and time for the suppression to take place, inclusive. Format defined by RFC3339.
                    - "Example: `2023-02-01T02:02:29.600Z`"
                type: str
                required: true
    is_enabled:
        description:
            - Whether the alarm is enabled.
            - "Example: `true`"
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: bool
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Usage of predefined tag keys. These predefined keys are scoped to namespaces.
              Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    overrides:
        description:
            - A set of overrides that control evaluations of the alarm.
            - Each override can specify values for query, severity, body, and pending duration.
              When an alarm contains overrides, the Monitoring service evaluates each override in order, beginning with the first override in the array (index
              position `0`),
              and then evaluates the alarm's base values (`ruleName` value of `BASE`).
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
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
                type: str
            severity:
                description:
                    - The perceived severity of the alarm with regard to the affected system.
                    - "Example: `CRITICAL`"
                type: str
            body:
                description:
                    - The human-readable content of the delivered alarm notification.
                      Optionally include L(dynamic variables,https://docs.cloud.oracle.com/iaas/Content/Monitoring/Tasks/update-alarm-dynamic-variables.htm).
                      Oracle recommends providing guidance
                      to operators for resolving the alarm condition. Consider adding links to standard runbook
                      practices. Avoid entering confidential information.
                    - "Example: `High CPU usage alert. Follow runbook instructions for resolution.`"
                type: str
            rule_name:
                description:
                    - A user-friendly description for this alarm override. Must be unique across all `ruleName` values for the alarm.
                type: str
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
                type: str
    rule_name:
        description:
            - Identifier of the alarm's base values for alarm evaluation, for use when the alarm contains overrides.
              Default value is `BASE`. For information about alarm overrides, see L(AlarmOverride,https://docs.cloud.oracle.com/en-
              us/iaas/api/#/en/monitoring/latest/datatypes/AlarmOverride).
            - This parameter is updatable.
        type: str
    notification_version:
        description:
            - "The version of the alarm notification to be delivered. Allowed value: `1.X`
              The value must start with a number (up to four digits), followed by a period and an uppercase X."
            - This parameter is updatable.
        type: str
    notification_title:
        description:
            - Customizable notification title (`title` L(alarm message parameter,https://docs.cloud.oracle.com/iaas/Content/Monitoring/alarm-message-
              format.htm)).
              Optionally include L(dynamic variables,https://docs.cloud.oracle.com/iaas/Content/Monitoring/Tasks/update-alarm-dynamic-variables.htm).
              The notification title appears as the subject line in a formatted email message and as the title in a Slack message.
            - This parameter is updatable.
        type: str
    evaluation_slack_duration:
        description:
            - "Customizable slack period to wait for metric ingestion before evaluating the alarm.
              Specify a string in ISO 8601 format (`PT10M` for ten minutes or `PT1H`
              for one hour). Minimum: PT3M. Maximum: PT2H. Default: PT3M.
              For more information about the slack period, see
              L(About the Internal Reset Period,https://docs.cloud.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#reset)."
            - This parameter is updatable.
        type: str
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
            - This parameter is updatable.
        type: str
    alarm_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of an alarm.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Alarm.
            - Use I(state=present) to create or update an Alarm.
            - Use I(state=absent) to delete an Alarm.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create alarm
  oci_monitoring_alarm:
    # required
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    metric_compartment_id: "ocid1.metriccompartment.oc1..xxxxxxEXAMPLExxxxxx"
    namespace: namespace_example
    query: query_example
    severity: severity_example
    destinations: [ "destinations_example" ]
    is_enabled: true

    # optional
    metric_compartment_id_in_subtree: true
    resource_group: resource_group_example
    resolution: resolution_example
    pending_duration: pending_duration_example
    body: body_example
    is_notifications_per_metric_dimension_enabled: true
    message_format: RAW
    repeat_notification_duration: repeat_notification_duration_example
    suppression:
      # required
      time_suppress_from: time_suppress_from_example
      time_suppress_until: time_suppress_until_example

      # optional
      description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    overrides:
    - # optional
      pending_duration: pending_duration_example
      severity: severity_example
      body: body_example
      rule_name: rule_name_example
      query: query_example
    rule_name: rule_name_example
    notification_version: notification_version_example
    notification_title: notification_title_example
    evaluation_slack_duration: evaluation_slack_duration_example
    alarm_summary: alarm_summary_example

- name: Update alarm
  oci_monitoring_alarm:
    # required
    alarm_id: "ocid1.alarm.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    metric_compartment_id: "ocid1.metriccompartment.oc1..xxxxxxEXAMPLExxxxxx"
    metric_compartment_id_in_subtree: true
    namespace: namespace_example
    resource_group: resource_group_example
    query: query_example
    resolution: resolution_example
    pending_duration: pending_duration_example
    severity: severity_example
    body: body_example
    is_notifications_per_metric_dimension_enabled: true
    message_format: RAW
    destinations: [ "destinations_example" ]
    repeat_notification_duration: repeat_notification_duration_example
    suppression:
      # required
      time_suppress_from: time_suppress_from_example
      time_suppress_until: time_suppress_until_example

      # optional
      description: description_example
    is_enabled: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    overrides:
    - # optional
      pending_duration: pending_duration_example
      severity: severity_example
      body: body_example
      rule_name: rule_name_example
      query: query_example
    rule_name: rule_name_example
    notification_version: notification_version_example
    notification_title: notification_title_example
    evaluation_slack_duration: evaluation_slack_duration_example
    alarm_summary: alarm_summary_example

- name: Update alarm using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_monitoring_alarm:
    # required
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    metric_compartment_id: "ocid1.metriccompartment.oc1..xxxxxxEXAMPLExxxxxx"
    metric_compartment_id_in_subtree: true
    namespace: namespace_example
    resource_group: resource_group_example
    query: query_example
    resolution: resolution_example
    pending_duration: pending_duration_example
    severity: severity_example
    body: body_example
    is_notifications_per_metric_dimension_enabled: true
    message_format: RAW
    destinations: [ "destinations_example" ]
    repeat_notification_duration: repeat_notification_duration_example
    suppression:
      # required
      time_suppress_from: time_suppress_from_example
      time_suppress_until: time_suppress_until_example

      # optional
      description: description_example
    is_enabled: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    overrides:
    - # optional
      pending_duration: pending_duration_example
      severity: severity_example
      body: body_example
      rule_name: rule_name_example
      query: query_example
    rule_name: rule_name_example
    notification_version: notification_version_example
    notification_title: notification_title_example
    evaluation_slack_duration: evaluation_slack_duration_example
    alarm_summary: alarm_summary_example

- name: Delete alarm
  oci_monitoring_alarm:
    # required
    alarm_id: "ocid1.alarm.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete alarm using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_monitoring_alarm:
    # required
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

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
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.monitoring import MonitoringClient
    from oci.monitoring.models import CreateAlarmDetails
    from oci.monitoring.models import UpdateAlarmDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AlarmHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(AlarmHelperGen, self).get_possible_entity_types() + [
            "alarm",
            "alarms",
            "monitoringalarm",
            "monitoringalarms",
            "alarmresource",
            "alarmsresource",
            "monitoring",
        ]

    def get_module_resource_id_param(self):
        return "alarm_id"

    def get_module_resource_id(self):
        return self.module.params.get("alarm_id")

    def get_get_fn(self):
        return self.client.get_alarm

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_alarm, alarm_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_alarm, alarm_id=self.module.params.get("alarm_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["display_name"]

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
        return oci_common_utils.list_all_resources(self.client.list_alarms, **kwargs)

    def get_create_model_class(self):
        return CreateAlarmDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_alarm,
            call_fn_args=(),
            call_fn_kwargs=dict(create_alarm_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateAlarmDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_alarm,
            call_fn_args=(),
            call_fn_kwargs=dict(
                alarm_id=self.module.params.get("alarm_id"),
                update_alarm_details=update_details,
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
            call_fn=self.client.delete_alarm,
            call_fn_args=(),
            call_fn_kwargs=dict(alarm_id=self.module.params.get("alarm_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


AlarmHelperCustom = get_custom_class("AlarmHelperCustom")


class ResourceHelper(AlarmHelperCustom, AlarmHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            display_name=dict(aliases=["name"], type="str"),
            compartment_id=dict(type="str"),
            metric_compartment_id=dict(type="str"),
            metric_compartment_id_in_subtree=dict(type="bool"),
            namespace=dict(type="str"),
            resource_group=dict(type="str"),
            query=dict(type="str"),
            resolution=dict(type="str"),
            pending_duration=dict(type="str"),
            severity=dict(type="str"),
            body=dict(type="str"),
            is_notifications_per_metric_dimension_enabled=dict(type="bool"),
            message_format=dict(
                type="str", choices=["RAW", "PRETTY_JSON", "ONS_OPTIMIZED"]
            ),
            destinations=dict(type="list", elements="str"),
            repeat_notification_duration=dict(type="str"),
            suppression=dict(
                type="dict",
                options=dict(
                    description=dict(type="str"),
                    time_suppress_from=dict(type="str", required=True),
                    time_suppress_until=dict(type="str", required=True),
                ),
            ),
            is_enabled=dict(type="bool"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            overrides=dict(
                type="list",
                elements="dict",
                options=dict(
                    pending_duration=dict(type="str"),
                    severity=dict(type="str"),
                    body=dict(type="str"),
                    rule_name=dict(type="str"),
                    query=dict(type="str"),
                ),
            ),
            rule_name=dict(type="str"),
            notification_version=dict(type="str"),
            notification_title=dict(type="str"),
            evaluation_slack_duration=dict(type="str"),
            alarm_summary=dict(type="str"),
            alarm_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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
