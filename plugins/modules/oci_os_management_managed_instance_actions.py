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
module: oci_os_management_managed_instance_actions
short_description: Perform actions on a ManagedInstance resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a ManagedInstance resource in Oracle Cloud Infrastructure
    - For I(action=attach_child_software_source), adds a child software source to a managed instance. After the software
      source has been added, then packages from that software source can be
      installed on the managed instance.
    - For I(action=attach_parent_software_source), adds a parent software source to a managed instance. After the software
      source has been added, then packages from that software source can be
      installed on the managed instance. Software sources that have this
      software source as a parent will be able to be added to this managed instance.
    - For I(action=detach_child_software_source), removes a child software source from a managed instance. Packages will no longer be able to be
      installed from these software sources.
    - For I(action=detach_parent_software_source), removes a software source from a managed instance. All child software sources will also be removed
      from the managed instance. Packages will no longer be able to be installed from these software sources.
    - For I(action=disable_module_stream), disables a module stream on a managed instance.  After the stream is
      disabled, it is no longer possible to install the profiles that are
      contained by the stream.  All installed profiles must be removed prior
      to disabling a module stream.
    - For I(action=enable_module_stream), enables a module stream on a managed instance.  After the stream is
      enabled, it is possible to install the profiles that are contained
      by the stream.  Enabling a stream that is already enabled will
      succeed.  Attempting to enable a different stream for a module that
      already has a stream enabled results in an error.
    - For I(action=install_all_package_updates), install all of the available package updates for the managed instance.
    - For I(action=install_all_windows_updates), install all of the available Windows updates for the managed instance.
    - For I(action=install_module_stream_profile), installs a profile for an module stream.  The stream must be
      enabled before a profile can be installed.  If a module stream
      defines multiple profiles, each one can be installed independently.
    - For I(action=install_package), installs a package on a managed instance.
    - For I(action=install_package_update), updates a package on a managed instance.
    - For I(action=install_windows_update), installs a Windows update on a managed instance.
    - "For I(action=manage_module_streams), perform an operation involving modules, streams, and profiles on a
      managed instance.  Each operation may enable or disable an arbitrary
      amount of module streams, and install or remove an arbitrary number
      of module stream profiles.  When the operation is complete, the
      state of the modules, streams, and profiles on the managed instance
      will match the state indicated in the operation.
      Each module stream specified in the list of module streams to enable
      will be in the \\"ENABLED\\" state upon completion of the operation.
      If there was already a stream of that module enabled, any work
      required to switch from the current stream to the new stream is
      performed implicitly.
      Each module stream specified in the list of module streams to disable
      will be in the \\"DISABLED\\" state upon completion of the operation.
      Any profiles that are installed for the module stream will be removed
      as part of the operation.
      Each module stream profile specified in the list of profiles to install
      will be in the \\"INSTALLED\\" state upon completion of the operation,
      indicating that any packages that are part of the profile are installed
      on the managed instance.  If the module stream containing the profile
      is not enabled, it will be enabled as part of the operation.  There
      is an exception when attempting to install a stream of a profile when
      another stream of the same module is enabled.  It is an error to attempt
      to install a profile of another module stream, unless enabling the
      new module stream is explicitly included in this operation.
      Each module stream profile specified in the list of profiles to remove
      will be in the \\"AVAILABLE\\" state upon completion of the operation.
      The status of packages within the profile after the operation is
      complete is defined by the package manager on the managed instance.
      Operations that contain one or more elements that are not allowed
      are rejected.
      The result of this request is a WorkRequest object.  The returned
      WorkRequest is the parent of a structure of other WorkRequests.  Taken
      as a whole, this structure indicates the entire set of work to be
      performed to complete the operation.
      This interface can also be used to perform a dry run of the operation
      rather than committing it to a managed instance.  If a dry run is
      requested, the OS Management Service will evaluate the operation
      against the current module, stream, and profile state on the managed
      instance.  It will calculate the impact of the operation on all
      modules, streams, and profiles on the managed instance, including those
      that are implicitly impacted by the operation.
      The WorkRequest resulting from a dry run behaves differently than
      a WorkRequest resulting from a committable operation.  Dry run
      WorkRequests are always singletons and never have children.  The
      impact of the operation is returned using the log and error
      facilities of WorkRequests.  The impact of operations that are
      allowed by the OS Management Service are communicated as one or
      more work request log entries.  Operations that are not allowed
      by the OS Management Service are communicated as one or more
      work requst error entries.  Each entry, for either logs or errors,
      contains a structured message containing the results of one
      or more operations."
    - For I(action=remove_module_stream_profile), removes a profile for a module stream that is installed on a managed instance.
      If a module stream is provided, rather than a fully qualified profile, all
      profiles that have been installed for the module stream will be removed.
    - For I(action=remove_package), removes an installed package from a managed instance.
    - For I(action=switch_module_stream), enables a new stream for a module that already has a stream enabled.
      If any profiles or packages from the original module are installed,
      switching to a new stream will remove the existing packages and
      install their counterparts in the new stream.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    software_source_id:
        description:
            - OCID for the Software Source
            - Required for I(action=attach_child_software_source), I(action=attach_parent_software_source), I(action=detach_child_software_source),
              I(action=detach_parent_software_source).
        type: str
    update_type:
        description:
            - The type of updates to be applied
            - Applicable only for I(action=install_all_package_updates)I(action=install_all_windows_updates).
        type: str
        choices:
            - "SECURITY"
            - "BUGFIX"
            - "ENHANCEMENT"
            - "OTHER"
            - "KSPLICE"
            - "ALL"
    windows_update_name:
        description:
            - "Unique identifier for the Windows update. NOTE - This is not an OCID,
              but is a unique identifier assigned by Microsoft.
              Example: `6981d463-cd91-4a26-b7c4-ea4ded9183ed`"
            - Required for I(action=install_windows_update).
        type: str
    is_dry_run:
        description:
            - Indicates if this operation is a dry run or if the operation
              should be commited.  If set to true, the result of the operation
              will be evaluated but not committed.  If set to false, the
              operation is committed to the managed instance.  The default is
              false.
            - Applicable only for I(action=manage_module_streams).
        type: bool
    enable:
        description:
            - The set of module streams to enable.
            - Applicable only for I(action=manage_module_streams).
        type: list
        elements: dict
        suboptions:
            module_name:
                description:
                    - The name of a module
                type: str
                required: true
            stream_name:
                description:
                    - The name of a stream of the specified module
                type: str
                required: true
    disable:
        description:
            - The set of module streams to disable.
            - Applicable only for I(action=manage_module_streams).
        type: list
        elements: dict
        suboptions:
            module_name:
                description:
                    - The name of a module
                type: str
                required: true
            stream_name:
                description:
                    - The name of a stream of the specified module
                type: str
                required: true
    install:
        description:
            - The set of module stream profiles to install.
            - Applicable only for I(action=manage_module_streams).
        type: list
        elements: dict
        suboptions:
            module_name:
                description:
                    - The name of a module
                type: str
                required: true
            stream_name:
                description:
                    - The name of a stream of the specified module
                type: str
                required: true
            profile_name:
                description:
                    - The name of a profile of the specified module stream
                type: str
                required: true
    remove:
        description:
            - The set of module stream profiles to remove.
            - Applicable only for I(action=manage_module_streams).
        type: list
        elements: dict
        suboptions:
            module_name:
                description:
                    - The name of a module
                type: str
                required: true
            stream_name:
                description:
                    - The name of a stream of the specified module
                type: str
                required: true
            profile_name:
                description:
                    - The name of a profile of the specified module stream
                type: str
                required: true
    profile_name:
        description:
            - The name of the profile of the containing module stream
            - Applicable only for I(action=install_module_stream_profile)I(action=remove_module_stream_profile).
        type: str
    software_package_name:
        description:
            - Package name
            - Required for I(action=install_package), I(action=install_package_update), I(action=remove_package).
        type: str
    managed_instance_id:
        description:
            - OCID for the managed instance
        type: str
        aliases: ["id"]
        required: true
    module_name:
        description:
            - The name of a module.
            - Required for I(action=disable_module_stream), I(action=enable_module_stream), I(action=install_module_stream_profile),
              I(action=remove_module_stream_profile), I(action=switch_module_stream).
        type: str
    stream_name:
        description:
            - The name of the stream of the containing module.  This parameter
              is required if a profileName is specified.
            - Applicable only for I(action=disable_module_stream)I(action=enable_module_stream)I(action=install_module_stream_profile)I(action=remove_module_str
              eam_profile)I(action=switch_module_stream).
        type: str
    action:
        description:
            - The action to perform on the ManagedInstance.
        type: str
        required: true
        choices:
            - "attach_child_software_source"
            - "attach_parent_software_source"
            - "detach_child_software_source"
            - "detach_parent_software_source"
            - "disable_module_stream"
            - "enable_module_stream"
            - "install_all_package_updates"
            - "install_all_windows_updates"
            - "install_module_stream_profile"
            - "install_package"
            - "install_package_update"
            - "install_windows_update"
            - "manage_module_streams"
            - "remove_module_stream_profile"
            - "remove_package"
            - "switch_module_stream"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action attach_child_software_source on managed_instance
  oci_os_management_managed_instance_actions:
    # required
    software_source_id: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
    action: attach_child_software_source

- name: Perform action attach_parent_software_source on managed_instance
  oci_os_management_managed_instance_actions:
    # required
    software_source_id: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
    action: attach_parent_software_source

- name: Perform action detach_child_software_source on managed_instance
  oci_os_management_managed_instance_actions:
    # required
    software_source_id: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
    action: detach_child_software_source

- name: Perform action detach_parent_software_source on managed_instance
  oci_os_management_managed_instance_actions:
    # required
    software_source_id: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
    action: detach_parent_software_source

- name: Perform action disable_module_stream on managed_instance
  oci_os_management_managed_instance_actions:
    # required
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
    module_name: module_name_example
    action: disable_module_stream

    # optional
    stream_name: stream_name_example

- name: Perform action enable_module_stream on managed_instance
  oci_os_management_managed_instance_actions:
    # required
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
    module_name: module_name_example
    action: enable_module_stream

    # optional
    stream_name: stream_name_example

- name: Perform action install_all_package_updates on managed_instance
  oci_os_management_managed_instance_actions:
    # required
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
    action: install_all_package_updates

    # optional
    update_type: SECURITY

- name: Perform action install_all_windows_updates on managed_instance
  oci_os_management_managed_instance_actions:
    # required
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
    action: install_all_windows_updates

    # optional
    update_type: SECURITY

- name: Perform action install_module_stream_profile on managed_instance
  oci_os_management_managed_instance_actions:
    # required
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
    module_name: module_name_example
    action: install_module_stream_profile

    # optional
    profile_name: profile_name_example
    stream_name: stream_name_example

- name: Perform action install_package on managed_instance
  oci_os_management_managed_instance_actions:
    # required
    software_package_name: software_package_name_example
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
    action: install_package

- name: Perform action install_package_update on managed_instance
  oci_os_management_managed_instance_actions:
    # required
    software_package_name: software_package_name_example
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
    action: install_package_update

- name: Perform action install_windows_update on managed_instance
  oci_os_management_managed_instance_actions:
    # required
    windows_update_name: windows_update_name_example
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
    action: install_windows_update

- name: Perform action manage_module_streams on managed_instance
  oci_os_management_managed_instance_actions:
    # required
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
    action: manage_module_streams

    # optional
    is_dry_run: true
    enable:
    - # required
      module_name: module_name_example
      stream_name: stream_name_example
    disable:
    - # required
      module_name: module_name_example
      stream_name: stream_name_example
    install:
    - # required
      module_name: module_name_example
      stream_name: stream_name_example
      profile_name: profile_name_example
    remove:
    - # required
      module_name: module_name_example
      stream_name: stream_name_example
      profile_name: profile_name_example

- name: Perform action remove_module_stream_profile on managed_instance
  oci_os_management_managed_instance_actions:
    # required
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
    module_name: module_name_example
    action: remove_module_stream_profile

    # optional
    profile_name: profile_name_example
    stream_name: stream_name_example

- name: Perform action remove_package on managed_instance
  oci_os_management_managed_instance_actions:
    # required
    software_package_name: software_package_name_example
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
    action: remove_package

- name: Perform action switch_module_stream on managed_instance
  oci_os_management_managed_instance_actions:
    # required
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
    module_name: module_name_example
    action: switch_module_stream

    # optional
    stream_name: stream_name_example

"""

RETURN = """
managed_instance:
    description:
        - Details of the ManagedInstance resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        display_name:
            description:
                - Managed Instance identifier
            returned: on success
            type: str
            sample: display_name_example
        id:
            description:
                - OCID for the managed instance
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        description:
            description:
                - Information specified by the user about the managed instance
            returned: on success
            type: str
            sample: description_example
        last_checkin:
            description:
                - Time at which the instance last checked in
            returned: on success
            type: str
            sample: last_checkin_example
        last_boot:
            description:
                - Time at which the instance last booted
            returned: on success
            type: str
            sample: last_boot_example
        updates_available:
            description:
                - Number of updates available to be installed
            returned: on success
            type: int
            sample: 56
        os_name:
            description:
                - Operating System Name
            returned: on success
            type: str
            sample: os_name_example
        os_version:
            description:
                - Operating System Version
            returned: on success
            type: str
            sample: os_version_example
        os_kernel_version:
            description:
                - Operating System Kernel Version
            returned: on success
            type: str
            sample: os_kernel_version_example
        compartment_id:
            description:
                - OCID for the Compartment
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        status:
            description:
                - status of the managed instance.
            returned: on success
            type: str
            sample: NORMAL
        parent_software_source:
            description:
                - the parent (base) Software Source attached to the Managed Instance
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - software source name
                    returned: on success
                    type: str
                    sample: name_example
                id:
                    description:
                        - software source identifier
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        child_software_sources:
            description:
                - list of child Software Sources attached to the Managed Instance
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - software source name
                    returned: on success
                    type: str
                    sample: name_example
                id:
                    description:
                        - software source identifier
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        managed_instance_groups:
            description:
                - The ids of the managed instance groups of which this instance is a
                  member.
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - unique identifier that is immutable on creation
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                display_name:
                    description:
                        - User friendly name
                    returned: on success
                    type: str
                    sample: display_name_example
        os_family:
            description:
                - The Operating System type of the managed instance.
            returned: on success
            type: str
            sample: LINUX
        is_reboot_required:
            description:
                - Indicates whether a reboot is required to complete installation of updates.
            returned: on success
            type: bool
            sample: true
        notification_topic_id:
            description:
                - OCID of the ONS topic used to send notification to users
            returned: on success
            type: str
            sample: "ocid1.notificationtopic.oc1..xxxxxxEXAMPLExxxxxx"
        ksplice_effective_kernel_version:
            description:
                - The ksplice effective kernel version
            returned: on success
            type: str
            sample: ksplice_effective_kernel_version_example
        is_data_collection_authorized:
            description:
                - True if user allow data collection for this instance
            returned: on success
            type: bool
            sample: true
        autonomous:
            description:
                - if present, indicates the Managed Instance is an autonomous instance. Holds all the Autonomous specific information
            returned: on success
            type: complex
            contains:
                is_auto_update_enabled:
                    description:
                        - True if daily updates are enabled
                    returned: on success
                    type: bool
                    sample: true
        security_updates_available:
            description:
                - Number of security type updates available to be installed
            returned: on success
            type: int
            sample: 56
        bug_updates_available:
            description:
                - Number of bug fix type updates available to be installed
            returned: on success
            type: int
            sample: 56
        enhancement_updates_available:
            description:
                - Number of enhancement type updates available to be installed
            returned: on success
            type: int
            sample: 56
        other_updates_available:
            description:
                - Number of non-classified updates available to be installed
            returned: on success
            type: int
            sample: 56
        scheduled_job_count:
            description:
                - Number of scheduled jobs associated with this instance
            returned: on success
            type: int
            sample: 56
        work_request_count:
            description:
                - Number of work requests associated with this instance
            returned: on success
            type: int
            sample: 56
    sample: {
        "display_name": "display_name_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "description": "description_example",
        "last_checkin": "last_checkin_example",
        "last_boot": "last_boot_example",
        "updates_available": 56,
        "os_name": "os_name_example",
        "os_version": "os_version_example",
        "os_kernel_version": "os_kernel_version_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "status": "NORMAL",
        "parent_software_source": {
            "name": "name_example",
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "child_software_sources": [{
            "name": "name_example",
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        }],
        "managed_instance_groups": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example"
        }],
        "os_family": "LINUX",
        "is_reboot_required": true,
        "notification_topic_id": "ocid1.notificationtopic.oc1..xxxxxxEXAMPLExxxxxx",
        "ksplice_effective_kernel_version": "ksplice_effective_kernel_version_example",
        "is_data_collection_authorized": true,
        "autonomous": {
            "is_auto_update_enabled": true
        },
        "security_updates_available": 56,
        "bug_updates_available": 56,
        "enhancement_updates_available": 56,
        "other_updates_available": 56,
        "scheduled_job_count": 56,
        "work_request_count": 56
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
    from oci.os_management import OsManagementClient
    from oci.os_management.models import (
        AttachChildSoftwareSourceToManagedInstanceDetails,
    )
    from oci.os_management.models import (
        AttachParentSoftwareSourceToManagedInstanceDetails,
    )
    from oci.os_management.models import (
        DetachChildSoftwareSourceFromManagedInstanceDetails,
    )
    from oci.os_management.models import (
        DetachParentSoftwareSourceFromManagedInstanceDetails,
    )
    from oci.os_management.models import ManageModuleStreamsOnManagedInstanceDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ManagedInstanceActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        attach_child_software_source
        attach_parent_software_source
        detach_child_software_source
        detach_parent_software_source
        disable_module_stream
        enable_module_stream
        install_all_package_updates
        install_all_windows_updates
        install_module_stream_profile
        install_package
        install_package_update
        install_windows_update
        manage_module_streams
        remove_module_stream_profile
        remove_package
        switch_module_stream
    """

    def get_default_module_wait_timeout(self):
        return 3600

    @staticmethod
    def get_module_resource_id_param():
        return "managed_instance_id"

    def get_module_resource_id(self):
        return self.module.params.get("managed_instance_id")

    def get_get_fn(self):
        return self.client.get_managed_instance

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_managed_instance,
            managed_instance_id=self.module.params.get("managed_instance_id"),
        )

    def attach_child_software_source(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AttachChildSoftwareSourceToManagedInstanceDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.attach_child_software_source_to_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                attach_child_software_source_to_managed_instance_details=action_details,
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

    def attach_parent_software_source(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AttachParentSoftwareSourceToManagedInstanceDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.attach_parent_software_source_to_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                attach_parent_software_source_to_managed_instance_details=action_details,
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

    def detach_child_software_source(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, DetachChildSoftwareSourceFromManagedInstanceDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.detach_child_software_source_from_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                detach_child_software_source_from_managed_instance_details=action_details,
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

    def detach_parent_software_source(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, DetachParentSoftwareSourceFromManagedInstanceDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.detach_parent_software_source_from_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                detach_parent_software_source_from_managed_instance_details=action_details,
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

    def disable_module_stream(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.disable_module_stream_on_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                module_name=self.module.params.get("module_name"),
                stream_name=self.module.params.get("stream_name"),
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

    def enable_module_stream(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.enable_module_stream_on_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                module_name=self.module.params.get("module_name"),
                stream_name=self.module.params.get("stream_name"),
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

    def install_all_package_updates(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.install_all_package_updates_on_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                update_type=self.module.params.get("update_type"),
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

    def install_all_windows_updates(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.install_all_windows_updates_on_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                update_type=self.module.params.get("update_type"),
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

    def install_module_stream_profile(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.install_module_stream_profile_on_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                module_name=self.module.params.get("module_name"),
                stream_name=self.module.params.get("stream_name"),
                profile_name=self.module.params.get("profile_name"),
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

    def install_package(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.install_package_on_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                software_package_name=self.module.params.get("software_package_name"),
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

    def install_package_update(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.install_package_update_on_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                software_package_name=self.module.params.get("software_package_name"),
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

    def install_windows_update(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.install_windows_update_on_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                windows_update_name=self.module.params.get("windows_update_name"),
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

    def manage_module_streams(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ManageModuleStreamsOnManagedInstanceDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.manage_module_streams_on_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                manage_module_streams_on_managed_instance_details=action_details,
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

    def remove_module_stream_profile(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.remove_module_stream_profile_from_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                module_name=self.module.params.get("module_name"),
                stream_name=self.module.params.get("stream_name"),
                profile_name=self.module.params.get("profile_name"),
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

    def remove_package(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.remove_package_from_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                software_package_name=self.module.params.get("software_package_name"),
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

    def switch_module_stream(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.switch_module_stream_on_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                module_name=self.module.params.get("module_name"),
                stream_name=self.module.params.get("stream_name"),
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


ManagedInstanceActionsHelperCustom = get_custom_class(
    "ManagedInstanceActionsHelperCustom"
)


class ResourceHelper(
    ManagedInstanceActionsHelperCustom, ManagedInstanceActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            software_source_id=dict(type="str"),
            update_type=dict(
                type="str",
                choices=[
                    "SECURITY",
                    "BUGFIX",
                    "ENHANCEMENT",
                    "OTHER",
                    "KSPLICE",
                    "ALL",
                ],
            ),
            windows_update_name=dict(type="str"),
            is_dry_run=dict(type="bool"),
            enable=dict(
                type="list",
                elements="dict",
                options=dict(
                    module_name=dict(type="str", required=True),
                    stream_name=dict(type="str", required=True),
                ),
            ),
            disable=dict(
                type="list",
                elements="dict",
                options=dict(
                    module_name=dict(type="str", required=True),
                    stream_name=dict(type="str", required=True),
                ),
            ),
            install=dict(
                type="list",
                elements="dict",
                options=dict(
                    module_name=dict(type="str", required=True),
                    stream_name=dict(type="str", required=True),
                    profile_name=dict(type="str", required=True),
                ),
            ),
            remove=dict(
                type="list",
                elements="dict",
                options=dict(
                    module_name=dict(type="str", required=True),
                    stream_name=dict(type="str", required=True),
                    profile_name=dict(type="str", required=True),
                ),
            ),
            profile_name=dict(type="str"),
            software_package_name=dict(type="str"),
            managed_instance_id=dict(aliases=["id"], type="str", required=True),
            module_name=dict(type="str"),
            stream_name=dict(type="str"),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "attach_child_software_source",
                    "attach_parent_software_source",
                    "detach_child_software_source",
                    "detach_parent_software_source",
                    "disable_module_stream",
                    "enable_module_stream",
                    "install_all_package_updates",
                    "install_all_windows_updates",
                    "install_module_stream_profile",
                    "install_package",
                    "install_package_update",
                    "install_windows_update",
                    "manage_module_streams",
                    "remove_module_stream_profile",
                    "remove_package",
                    "switch_module_stream",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="managed_instance",
        service_client_class=OsManagementClient,
        namespace="os_management",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
