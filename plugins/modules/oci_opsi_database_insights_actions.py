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
module: oci_opsi_database_insights_actions
short_description: Perform actions on a DatabaseInsights resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a DatabaseInsights resource in Oracle Cloud Infrastructure
    - For I(action=change_autonomous_database_insight_advanced_features), update connection detail for advanced features of Autonomous Database in Operations
      Insights.
    - For I(action=change), moves a DatabaseInsight resource from one compartment identifier to another. When provided, If-Match is checked against ETag values
      of the resource.
    - For I(action=change_pe_comanaged), change the connection details of a co-managed  database insight. When provided, If-Match is checked against ETag values
      of the resource.
    - For I(action=disable_autonomous_database_insight_advanced_features), disable advanced features for an Autonomous Database in Operations Insights. The
      connection detail and advanced features will be removed.
    - For I(action=disable), disables a database in Operations Insights. Database metric collection and analysis will be stopped.
    - For I(action=enable_autonomous_database_insight_advanced_features), enables advanced features for an Autonomous Database in Operations Insights. A direct
      connection will be available for further collection.
    - For I(action=enable), enables a database in Operations Insights. Database metric collection and analysis will be started.
    - For I(action=ingest_addm_reports), this endpoint takes in a JSON payload, persists it in Operation Insights ingest pipeline.
      Either databaseId or id must be specified.
    - For I(action=ingest_database_configuration), this is a generic ingest endpoint for all database configuration metrics.
    - For I(action=ingest_sql_bucket), the sqlbucket endpoint takes in a JSON payload, persists it in Operations Insights ingest pipeline.
      Either databaseId or id must be specified.
    - For I(action=ingest_sql_plan_lines), the SqlPlanLines endpoint takes in a JSON payload, persists it in Operation Insights ingest pipeline.
      Either databaseId or id must be specified.
    - For I(action=ingest_sql_stats), the SQL Stats endpoint takes in a JSON payload, persists it in Operations Insights ingest pipeline.
      Either databaseId or id must be specified.
    - "For I(action=ingest_sql_text), the SqlText endpoint takes in a JSON payload, persists it in Operation Insights ingest pipeline.
      Either databaseId or id must be specified.
      Disclaimer: SQL text being uploaded explicitly via APIs is not masked. Any sensitive literals contained in the sqlFullText column should be masked prior
      to ingestion."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    entity_source:
        description:
            - Source of the database entity.
            - Required for I(action=enable).
        type: str
        choices:
            - "EM_MANAGED_EXTERNAL_DATABASE"
            - "PE_COMANAGED_DATABASE"
    opsi_private_endpoint_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the OPSI private endpoint
            - Required for I(action=change_pe_comanaged).
            - Required when $p.relatedDiscriminatorFieldName is 'PE_COMANAGED_DATABASE'
        type: str
    service_name:
        description:
            - Database service name used for connection requests.
            - Required for I(action=change_pe_comanaged).
            - Required when $p.relatedDiscriminatorFieldName is 'PE_COMANAGED_DATABASE'
        type: str
    credential_details:
        description:
            - ""
            - Required for I(action=change_autonomous_database_insight_advanced_features), I(action=change_pe_comanaged),
              I(action=enable_autonomous_database_insight_advanced_features).
            - Required when $p.relatedDiscriminatorFieldName is 'PE_COMANAGED_DATABASE'
        type: dict
        suboptions:
            credential_source_name:
                description:
                    - Credential source name that had been added in Management Agent wallet. This is supplied in the External Database Service.
                type: str
                required: true
            credential_type:
                description:
                    - Credential type.
                type: str
                choices:
                    - "CREDENTIALS_BY_SOURCE"
                    - "CREDENTIALS_BY_VAULT"
                required: true
            user_name:
                description:
                    - database user name.
                    - Applicable when credential_type is 'CREDENTIALS_BY_VAULT'
                type: str
            password_secret_id:
                description:
                    - The secret L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) mapping to the database credentials.
                    - Applicable when credential_type is 'CREDENTIALS_BY_VAULT'
                type: str
            wallet_secret_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Secret where the database keystore contents are
                      stored. This is used for TCPS support in BM/VM/ExaCS cases.
                    - Applicable when credential_type is 'CREDENTIALS_BY_VAULT'
                type: str
            role:
                description:
                    - database user role.
                    - Applicable when credential_type is 'CREDENTIALS_BY_VAULT'
                type: str
                choices:
                    - "NORMAL"
    connection_details:
        description:
            - ""
            - Required for I(action=change_autonomous_database_insight_advanced_features), I(action=enable_autonomous_database_insight_advanced_features).
            - Applicable when $p.relatedDiscriminatorFieldName is 'PE_COMANAGED_DATABASE'
        type: dict
        suboptions:
            host_name:
                description:
                    - Name of the listener host that will be used to create the connect string to the database.
                type: str
            port:
                description:
                    - Listener port number used for connection requests.
                type: int
            hosts:
                description:
                    - List of hosts and port for private endpoint accessed database resource.
                    - Required when $p.relatedDiscriminatorFieldName is 'PE_COMANAGED_DATABASE'
                type: list
                elements: dict
                suboptions:
                    host_ip:
                        description:
                            - Host IP used for connection requests for Cloud DB resource.
                        type: str
                    port:
                        description:
                            - Listener port number used for connection requests for rivate endpoint accessed db resource.
                        type: int
            protocol:
                description:
                    - Protocol used for connection requests.
                    - Applicable when $p.relatedDiscriminatorFieldName is 'PE_COMANAGED_DATABASE'
                type: str
                choices:
                    - "TCP"
                    - "TCPS"
            service_name:
                description:
                    - Database service name used for connection requests.
                    - Applicable when $p.relatedDiscriminatorFieldName is 'PE_COMANAGED_DATABASE'
                type: str
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - Applicable only for I(action=enable).
            - Applicable when entity_source is 'PE_COMANAGED_DATABASE'
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - Applicable only for I(action=enable).
            - Applicable when entity_source is 'PE_COMANAGED_DATABASE'
        type: dict
    system_tags:
        description:
            - "System tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            - Applicable only for I(action=enable).
            - Applicable when entity_source is 'PE_COMANAGED_DATABASE'
        type: dict
    database_insight_id:
        description:
            - Unique database insight identifier
            - Required for I(action=change_autonomous_database_insight_advanced_features), I(action=change), I(action=change_pe_comanaged),
              I(action=disable_autonomous_database_insight_advanced_features), I(action=disable),
              I(action=enable_autonomous_database_insight_advanced_features), I(action=enable).
        type: str
    items:
        description:
            - List of Addm reports
            - Required for I(action=ingest_addm_reports), I(action=ingest_database_configuration).
        type: list
        elements: dict
        suboptions:
            time_interval_start:
                description:
                    - The start timestamp that was passed into the request.
                type: str
            time_interval_end:
                description:
                    - The end timestamp that was passed into the request.
                type: str
            task_identifier:
                description:
                    - TASK_ID in the oracle database view DBA_ADDM_TASKS
                type: str
            database_identifier:
                description:
                    - Internal id of the database.
                type: str
            snapshot_interval_start:
                description:
                    - AWR snapshot id.
                type: str
            snapshot_interval_end:
                description:
                    - AWR snapshot id.
                type: str
            addm_report:
                description:
                    - The complete ADDM report
                type: str
            num_cp_us:
                description:
                    - Total number of CPUs available.
                    - Applicable when metric_name is 'DB_OS_CONFIG_INSTANCE'
                type: int
            num_cpu_cores:
                description:
                    - Number of CPU cores available (includes subcores of multicore CPUs as well as single-core CPUs).
                    - Applicable when metric_name is 'DB_OS_CONFIG_INSTANCE'
                type: int
            num_cpu_sockets:
                description:
                    - Number of CPU Sockets available.
                    - Applicable when metric_name is 'DB_OS_CONFIG_INSTANCE'
                type: int
            physical_memory_bytes:
                description:
                    - Total number of bytes of physical memory.
                    - Applicable when metric_name is 'DB_OS_CONFIG_INSTANCE'
                type: float
            host_name:
                description:
                    - Host name of the database instance.
                    - Required when metric_name is one of ['DB_EXTERNAL_INSTANCE', 'DB_OS_CONFIG_INSTANCE']
                type: str
            cpu_count:
                description:
                    - Total number of CPUs allocated for the host.
                    - Applicable when metric_name is 'DB_EXTERNAL_INSTANCE'
                type: int
            host_memory_capacity:
                description:
                    - Total amount of usable Physical RAM Memory available in gigabytes.
                    - Applicable when metric_name is 'DB_EXTERNAL_INSTANCE'
                type: float
            db_external_instance_version:
                description:
                    - Database version.
                    - Applicable when metric_name is 'DB_EXTERNAL_INSTANCE'
                type: str
            parallel:
                description:
                    - Indicates whether the instance is mounted in cluster database mode (YES) or not (NO).
                    - Applicable when metric_name is 'DB_EXTERNAL_INSTANCE'
                type: str
            instance_role:
                description:
                    - Role (permissions) of the database instance.
                    - Applicable when metric_name is 'DB_EXTERNAL_INSTANCE'
                type: str
            logins:
                description:
                    - Indicates if logins are allowed or restricted.
                    - Applicable when metric_name is 'DB_EXTERNAL_INSTANCE'
                type: str
            database_status:
                description:
                    - Status of the database.
                    - Applicable when metric_name is 'DB_EXTERNAL_INSTANCE'
                type: str
            status:
                description:
                    - Status of the instance.
                    - Applicable when metric_name is 'DB_EXTERNAL_INSTANCE'
                type: str
            edition:
                description:
                    - The edition of the database.
                    - Applicable when metric_name is 'DB_EXTERNAL_INSTANCE'
                type: str
            startup_time:
                description:
                    - Start up time of the database instance.
                    - Applicable when metric_name is 'DB_EXTERNAL_INSTANCE'
                type: str
            instance_number:
                description:
                    - Database instance number.
                    - Required when metric_name is 'DB_PARAMETERS'
                type: int
            parameter_name:
                description:
                    - Database parameter name.
                    - Required when metric_name is 'DB_PARAMETERS'
                type: str
            parameter_value:
                description:
                    - Database parameter value.
                    - Required when metric_name is 'DB_PARAMETERS'
                type: str
            snapshot_id:
                description:
                    - AWR snapshot id for the parameter value
                    - Applicable when metric_name is 'DB_PARAMETERS'
                type: int
            is_changed:
                description:
                    - Indicates whether the parameter's value changed in given snapshot or not.
                    - Applicable when metric_name is 'DB_PARAMETERS'
                type: str
            is_default:
                description:
                    - Indicates whether this value is the default value or not.
                    - Applicable when metric_name is 'DB_PARAMETERS'
                type: str
            metric_name:
                description:
                    - Name of the metric group.
                type: str
                choices:
                    - "DB_OS_CONFIG_INSTANCE"
                    - "DB_EXTERNAL_INSTANCE"
                    - "DB_PARAMETERS"
                    - "DB_EXTERNAL_PROPERTIES"
            name:
                description:
                    - Name of the database.
                    - Applicable when metric_name is 'DB_EXTERNAL_PROPERTIES'
                type: str
            log_mode:
                description:
                    - Archive log mode.
                    - Applicable when metric_name is 'DB_EXTERNAL_PROPERTIES'
                type: str
            cdb:
                description:
                    - Indicates if it is a CDB or not. This would be 'yes' or 'no'.
                    - Applicable when metric_name is 'DB_EXTERNAL_PROPERTIES'
                type: str
            open_mode:
                description:
                    - Open mode information.
                    - Applicable when metric_name is 'DB_EXTERNAL_PROPERTIES'
                type: str
            database_role:
                description:
                    - Current role of the database.
                    - Applicable when metric_name is 'DB_EXTERNAL_PROPERTIES'
                type: str
            guard_status:
                description:
                    - Data protection policy.
                    - Applicable when metric_name is 'DB_EXTERNAL_PROPERTIES'
                type: str
            platform_name:
                description:
                    - Platform name of the database, OS with architecture.
                    - Applicable when metric_name is 'DB_EXTERNAL_PROPERTIES'
                type: str
            control_file_type:
                description:
                    - Type of control file.
                    - Applicable when metric_name is 'DB_EXTERNAL_PROPERTIES'
                type: str
            switchover_status:
                description:
                    - Indicates whether switchover is allowed.
                    - Applicable when metric_name is 'DB_EXTERNAL_PROPERTIES'
                type: str
            created:
                description:
                    - Creation time.
                    - Applicable when metric_name is 'DB_EXTERNAL_PROPERTIES'
                type: str
            database_type:
                description:
                    - Operations Insights internal representation of the database type.
                type: str
            bucket_id:
                description:
                    - "SQL Bucket ID, examples <= 3 secs, 3-10 secs, 10-60 secs, 1-5 min, > 5 min
                      Example: `\\"<= 3 secs\\"`"
                type: str
            executions_count:
                description:
                    - "Total number of executions
                      Example: `60`"
                type: int
            cpu_time_in_sec:
                description:
                    - "Total CPU time
                      Example: `1046`"
                type: float
            io_time_in_sec:
                description:
                    - "Total IO time
                      Example: `5810`"
                type: float
            other_wait_time_in_sec:
                description:
                    - "Total other wait time
                      Example: `24061`"
                type: float
            total_time_in_sec:
                description:
                    - "Total time
                      Example: `30917`"
                type: float
            plan_hash:
                description:
                    - Plan hash value for the SQL Execution Plan
                type: int
            operation:
                description:
                    - "Operation
                      Example: `\\"SELECT STATEMENT\\"`"
                type: str
            remark:
                description:
                    - "Remark
                      Example: `\\"\\"`"
                type: str
            options:
                description:
                    - "Options
                      Example: `\\"RANGE SCAN\\"`"
                type: str
            object_node:
                description:
                    - "Object Node
                      Example: `\\"Q4000\\"`"
                type: str
            object_owner:
                description:
                    - "Object Owner
                      Example: `\\"TENANT_A#SCHEMA\\"`"
                type: str
            object_name:
                description:
                    - "Object Name
                      Example: `\\"PLAN_LINES_PK\\"`"
                type: str
            object_alias:
                description:
                    - "Object Alias
                      Example: `\\"PLAN_LINES@SEL$1\\"`"
                type: str
            object_instance:
                description:
                    - "Object Instance
                      Example: `37472`"
                type: int
            object_type:
                description:
                    - "Object Type
                      Example: `\\"INDEX (UNIQUE)\\"`"
                type: str
            optimizer:
                description:
                    - "Optimizer
                      Example: `\\"CLUSTER\\"`"
                type: str
            search_columns:
                description:
                    - "Search Columns
                      Example: `3`"
                type: int
            identifier:
                description:
                    - "Identifier
                      Example: `3`"
                type: int
            parent_identifier:
                description:
                    - "Parent Identifier
                      Example: `2`"
                type: int
            depth:
                description:
                    - "Depth
                      Example: `3`"
                type: int
            position:
                description:
                    - "Position
                      Example: `1`"
                type: int
            cost:
                description:
                    - "Cost
                      Example: `1`"
                type: int
            cardinality:
                description:
                    - "Cardinality
                      Example: `1`"
                type: int
            bytes:
                description:
                    - "Bytes
                      Example: `150`"
                type: int
            other:
                description:
                    - "Other
                      Example: ``"
                type: str
            other_tag:
                description:
                    - "Other Tag
                      Example: `\\"PARALLEL_COMBINED_WITH_PARENT\\"`"
                type: str
            partition_start:
                description:
                    - "Partition start
                      Example: `1`"
                type: str
            partition_stop:
                description:
                    - "Partition stop
                      Example: `2`"
                type: str
            partition_identifier:
                description:
                    - "Partition identifier
                      Example: `8`"
                type: int
            distribution:
                description:
                    - "Distribution
                      Example: `\\"QC (RANDOM)\\"`"
                type: str
            cpu_cost:
                description:
                    - "CPU cost
                      Example: `7321`"
                type: int
            io_cost:
                description:
                    - "IO cost
                      Example: `1`"
                type: int
            temp_space:
                description:
                    - "Time space
                      Example: `15614000`"
                type: int
            access_predicates:
                description:
                    - "Access predicates
                      Example: `\\"\\\\\\"RESOURCE_ID\\\\\\"=:1 AND \\\\\\"QUERY_ID\\\\\\"=:2\\"`"
                type: str
            filter_predicates:
                description:
                    - "Filter predicates
                      Example: `\\"(INTERNAL_FUNCTION(\\\\\\"J\\\\\\".\\\\\\"DATABASE_ROLE\\\\\\") OR (\\\\\\"J\\\\\\".\\\\\\"DATABASE_ROLE\\\\\\" IS NULL AND
                      SYS_CONTEXT('userenv','database_role')='PRIMARY'))\\"`"
                type: str
            projection:
                description:
                    - "Projection
                      Example: `\\"COUNT(*)[22]\\"`"
                type: str
            qblock_name:
                description:
                    - "Qblock Name
                      Example: `\\"SEL$1\\"`"
                type: str
            elapsed_time_in_sec:
                description:
                    - "Total elapsed time
                      Example: `1.2`"
                type: float
            other_xml:
                description:
                    - "Other SQL
                      Example: `\\"<other_xml><info type=\\\\\\"db_version\\\\\\">18.0.0.0</info><info
                      type=\\\\\\"parse_schema\\\\\\"><![CDATA[\\\\\\"SYS\\\\\\"]]></info><info type=\\\\\\"plan_hash_full\\\\\\">483892784</info><info
                      type=\\\\\\"plan_hash\\\\\\">2709293936</info><info type=\\\\\\"plan_hash_2\\\\\\">483892784</info><outline_data><hint><![CDATA[IGNORE_OPT
                      IM_EMBEDDED_HINTS]]></hint><hint><![CDATA[OPTIMIZER_FEATURES_ENABLE('18.1.0')]]></hint><hint><![CDATA[DB_VERSION('18.1.0')]]></hint><hint>
                      <![CDATA[OPT_PARAM('_b_tree_bitmap_plans' 'false')]]></hint><hint><![CDATA[OPT_PARAM('_optim_peek_user_binds'
                      'false')]]></hint><hint><![CDATA[OPT_PARAM('result_cache_mode' 'FORCE')]]></hint><hint><![CDATA[OPT_PARAM('_fix_control' '20648883:0
                      27745220:1 30001331:1 30142527:1
                      30539126:1')]]></hint><hint><![CDATA[OUTLINE_LEAF(@\\\\\\"SEL$1\\\\\\")]]></hint><hint><![CDATA[INDEX(@\\\\\\"SEL$1\\\\\\"
                      \\\\\\"USER$\\\\\\"@\\\\\\"SEL$1\\\\\\" \\\\\\"I_USER#\\\\\\")]]></hint></outline_data></other_xml>\\"`"
                type: str
            plan_hash_value:
                description:
                    - Plan hash value for the SQL Execution Plan
                type: int
            instance_name:
                description:
                    - Name of the database instance.
                    - Required when metric_name is one of ['DB_EXTERNAL_INSTANCE', 'DB_OS_CONFIG_INSTANCE']
                type: str
            last_active_time:
                description:
                    - "last_active_time
                      Example: `\\"0000000099CCE300\\"`"
                type: str
            parse_calls:
                description:
                    - "Total integer of parse calls
                       Example: `60`"
                type: int
            disk_reads:
                description:
                    - Number of disk reads
                type: int
            direct_reads:
                description:
                    - Number of direct reads
                type: int
            direct_writes:
                description:
                    - Number of Direct writes
                type: int
            buffer_gets:
                description:
                    - Number of Buffer Gets
                type: int
            rows_processed:
                description:
                    - Number of row processed
                type: int
            serializable_aborts:
                description:
                    - Number of serializable aborts
                type: int
            fetches:
                description:
                    - Number of fetches
                type: int
            executions:
                description:
                    - Number of executions
                type: int
            avoided_executions:
                description:
                    - Number of executions attempted on this object, but prevented due to the SQL statement being in quarantine
                type: int
            end_of_fetch_count:
                description:
                    - Number of times this cursor was fully executed since the cursor was brought into the library cache
                type: int
            loads:
                description:
                    - Number of times the object was either loaded or reloaded
                type: int
            version_count:
                description:
                    - Number of cursors present in the cache with this SQL text and plan
                type: int
            invalidations:
                description:
                    - Number of times this child cursor has been invalidated
                type: int
            obsolete_count:
                description:
                    - Number of times that a parent cursor became obsolete
                type: int
            px_servers_executions:
                description:
                    - Total number of executions performed by parallel execution servers (0 when the statement has never been executed in parallel)
                type: int
            cpu_time_in_us:
                description:
                    - CPU time (in microseconds) used by this cursor for parsing, executing, and fetching
                type: int
            elapsed_time_in_us:
                description:
                    - Elapsed time (in microseconds) used by this cursor for parsing, executing, and fetching.
                type: int
            avg_hard_parse_time_in_us:
                description:
                    - Average hard parse time (in microseconds) used by this cursor
                type: int
            concurrency_wait_time_in_us:
                description:
                    - Concurrency wait time (in microseconds)
                type: int
            application_wait_time_in_us:
                description:
                    - Application wait time (in microseconds)
                type: int
            cluster_wait_time_in_us:
                description:
                    - Cluster wait time (in microseconds). This value is specific to Oracle RAC
                type: int
            user_io_wait_time_in_us:
                description:
                    - User I/O wait time (in microseconds)
                type: int
            plsql_exec_time_in_us:
                description:
                    - PL/SQL execution time (in microseconds)
                type: int
            java_exec_time_in_us:
                description:
                    - Java execution time (in microseconds)
                type: int
            sorts:
                description:
                    - Number of sorts that were done for the child cursor
                type: int
            sharable_mem:
                description:
                    - Total shared memory (in bytes) currently occupied by all cursors with this SQL text and plan
                type: int
            total_sharable_mem:
                description:
                    - Total shared memory (in bytes) occupied by all cursors with this SQL text and plan if they were to be fully loaded in the shared pool
                      (that is, cursor size)
                type: int
            type_check_mem:
                description:
                    - Typecheck memory
                type: int
            io_cell_offload_eligible_bytes:
                description:
                    - Number of I/O bytes which can be filtered by the Exadata storage system
                type: int
            io_interconnect_bytes:
                description:
                    - Number of I/O bytes exchanged between Oracle Database and the storage system. Typically used for Cache Fusion or parallel queries
                type: int
            physical_read_requests:
                description:
                    - Number of physical read I/O requests issued by the monitored SQL. The requests may not be disk reads
                type: int
            physical_read_bytes:
                description:
                    - Number of bytes read from disks by the monitored SQL
                type: int
            physical_write_requests:
                description:
                    - Number of physical write I/O requests issued by the monitored SQL
                type: int
            physical_write_bytes:
                description:
                    - Number of bytes written to disks by the monitored SQL
                type: int
            io_cell_uncompressed_bytes:
                description:
                    - Number of uncompressed bytes (that is, size after decompression) that are offloaded to the Exadata cells
                type: int
            io_cell_offload_returned_bytes:
                description:
                    - Number of bytes that are returned by Exadata cell through the regular I/O path
                type: int
            child_number:
                description:
                    - Number of this child cursor
                type: int
            command_type:
                description:
                    - Oracle command type definition
                type: int
            users_opening:
                description:
                    - Number of users that have any of the child cursors open
                type: int
            users_executing:
                description:
                    - Number of users executing the statement
                type: int
            optimizer_cost:
                description:
                    - Cost of this query given by the optimizer
                type: int
            full_plan_hash_value:
                description:
                    - Total Number of rows in SQLStats table
                type: str
            module:
                description:
                    - Module name
                type: str
            service:
                description:
                    - Service name
                type: str
            action:
                description:
                    - Contains the name of the action that was executing when the SQL statement was first parsed, which is set by calling
                      DBMS_APPLICATION_INFO.SET_ACTION
                type: str
            sql_profile:
                description:
                    - SQL profile used for this statement, if any
                type: str
            sql_patch:
                description:
                    - SQL patch used for this statement, if any
                type: str
            sql_plan_baseline:
                description:
                    - SQL plan baseline used for this statement, if any
                type: str
            delta_execution_count:
                description:
                    - Number of executions for the cursor since the last AWR snapshot
                type: int
            delta_cpu_time:
                description:
                    - CPU time (in microseconds) for the cursor since the last AWR snapshot
                type: int
            delta_io_bytes:
                description:
                    - Number of I/O bytes exchanged between the Oracle database and the storage system for the cursor since the last AWR snapshot
                type: int
            delta_cpu_rank:
                description:
                    - Rank based on CPU Consumption
                type: int
            delta_execs_rank:
                description:
                    - Rank based on number of execution
                type: int
            sharable_mem_rank:
                description:
                    - Rank based on sharable memory
                type: int
            delta_io_rank:
                description:
                    - Rank based on I/O Consumption
                type: int
            harmonic_sum:
                description:
                    - Harmonic sum based on ranking parameters
                type: int
            wt_harmonic_sum:
                description:
                    - Weight based harmonic sum of ranking parameters
                type: int
            total_sql_count:
                description:
                    - Total number of rows in SQLStats table
                type: int
            version:
                description:
                    - "Version
                      Example: `1`"
                type: float
            sql_identifier:
                description:
                    - Unique SQL_ID for a SQL Statement.
                type: str
            time_collected:
                description:
                    - "Collection timestamp
                      Example: `\\"2020-05-06T00:00:00.000Z\\"`"
                type: str
            sql_command:
                description:
                    - "SQL command
                      Example: `\\"SELECT\\"`"
                type: str
            exact_matching_signature:
                description:
                    - "exact_matching_signature
                      Example: `\\"18067345456756876713\\"`"
                type: str
            force_matching_signature:
                description:
                    - "force_matching_signature
                      Example: `\\"18067345456756876713\\"`"
                type: str
            sql_full_text:
                description:
                    - "Full SQL Text
                      Example: `\\"SELECT username,profile,default_tablespace,temporary_tablespace FROM dba_users\\"`
                      Disclaimer: SQL text being uploaded explicitly via APIs is not masked. Any sensitive literals contained in the sqlFullText column should
                      be masked prior to ingestion."
                type: str
    compartment_id:
        description:
            - The OCID of the compartment into which the resource should be moved.
            - Required for I(action=change).
            - Required when $p.relatedDiscriminatorFieldName is 'PE_COMANAGED_DATABASE'
        type: str
    database_id:
        description:
            - Optional L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the associated DBaaS entity.
            - Applicable only for I(action=ingest_addm_reports)I(action=ingest_database_configuration)I(action=ingest_sql_bucket)I(action=ingest_sql_plan_lines)
              I(action=ingest_sql_stats)I(action=ingest_sql_text).
        type: str
    id:
        description:
            - L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the database insight resource.
            - Applicable only for I(action=ingest_addm_reports)I(action=ingest_database_configuration)I(action=ingest_sql_bucket)I(action=ingest_sql_plan_lines)
              I(action=ingest_sql_stats)I(action=ingest_sql_text).
        type: str
    action:
        description:
            - The action to perform on the DatabaseInsights.
        type: str
        required: true
        choices:
            - "change_autonomous_database_insight_advanced_features"
            - "change"
            - "change_pe_comanaged"
            - "disable_autonomous_database_insight_advanced_features"
            - "disable"
            - "enable_autonomous_database_insight_advanced_features"
            - "enable"
            - "ingest_addm_reports"
            - "ingest_database_configuration"
            - "ingest_sql_bucket"
            - "ingest_sql_plan_lines"
            - "ingest_sql_stats"
            - "ingest_sql_text"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_autonomous_database_insight_advanced_features on database_insights
  oci_opsi_database_insights_actions:
    # required
    credential_details:
      # required
      credential_source_name: credential_source_name_example
      credential_type: CREDENTIALS_BY_SOURCE
    connection_details:
      # optional
      host_name: host_name_example
      port: 56
      hosts:
      - # optional
        host_ip: host_ip_example
        port: 56
      protocol: TCP
      service_name: service_name_example
    database_insight_id: "ocid1.databaseinsight.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_autonomous_database_insight_advanced_features

    # optional
    opsi_private_endpoint_id: "ocid1.opsiprivateendpoint.oc1..xxxxxxEXAMPLExxxxxx"

- name: Perform action change on database_insights
  oci_opsi_database_insights_actions:
    # required
    database_insight_id: "ocid1.databaseinsight.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change

- name: Perform action change_pe_comanaged on database_insights
  oci_opsi_database_insights_actions:
    # required
    opsi_private_endpoint_id: "ocid1.opsiprivateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
    service_name: service_name_example
    credential_details:
      # required
      credential_source_name: credential_source_name_example
      credential_type: CREDENTIALS_BY_SOURCE
    database_insight_id: "ocid1.databaseinsight.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_pe_comanaged

    # optional
    connection_details:
      # optional
      host_name: host_name_example
      port: 56
      hosts:
      - # optional
        host_ip: host_ip_example
        port: 56
      protocol: TCP
      service_name: service_name_example

- name: Perform action disable_autonomous_database_insight_advanced_features on database_insights
  oci_opsi_database_insights_actions:
    # required
    database_insight_id: "ocid1.databaseinsight.oc1..xxxxxxEXAMPLExxxxxx"
    action: disable_autonomous_database_insight_advanced_features

- name: Perform action disable on database_insights
  oci_opsi_database_insights_actions:
    # required
    database_insight_id: "ocid1.databaseinsight.oc1..xxxxxxEXAMPLExxxxxx"
    action: disable

- name: Perform action enable_autonomous_database_insight_advanced_features on database_insights
  oci_opsi_database_insights_actions:
    # required
    credential_details:
      # required
      credential_source_name: credential_source_name_example
      credential_type: CREDENTIALS_BY_SOURCE
    connection_details:
      # optional
      host_name: host_name_example
      port: 56
      hosts:
      - # optional
        host_ip: host_ip_example
        port: 56
      protocol: TCP
      service_name: service_name_example
    database_insight_id: "ocid1.databaseinsight.oc1..xxxxxxEXAMPLExxxxxx"
    action: enable_autonomous_database_insight_advanced_features

    # optional
    opsi_private_endpoint_id: "ocid1.opsiprivateendpoint.oc1..xxxxxxEXAMPLExxxxxx"

- name: Perform action enable on database_insights with entity_source = EM_MANAGED_EXTERNAL_DATABASE
  oci_opsi_database_insights_actions:
    # required
    entity_source: EM_MANAGED_EXTERNAL_DATABASE

- name: Perform action enable on database_insights with entity_source = PE_COMANAGED_DATABASE
  oci_opsi_database_insights_actions:
    # required
    entity_source: PE_COMANAGED_DATABASE
    opsi_private_endpoint_id: "ocid1.opsiprivateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
    service_name: service_name_example
    credential_details:
      # required
      credential_source_name: credential_source_name_example
      credential_type: CREDENTIALS_BY_SOURCE
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    connection_details:
      # optional
      host_name: host_name_example
      port: 56
      hosts:
      - # optional
        host_ip: host_ip_example
        port: 56
      protocol: TCP
      service_name: service_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    system_tags: null

- name: Perform action ingest_addm_reports on database_insights
  oci_opsi_database_insights_actions:
    # required
    items:
    - # required
      host_name: host_name_example
      metric_name: DB_OS_CONFIG_INSTANCE
      instance_name: instance_name_example

      # optional
      num_cp_us: 56
      num_cpu_cores: 56
      num_cpu_sockets: 56
      physical_memory_bytes: 3.4
      time_collected: time_collected_example
    action: ingest_addm_reports

    # optional
    database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
    id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"

- name: Perform action ingest_database_configuration on database_insights
  oci_opsi_database_insights_actions:
    # required
    items:
    - # required
      host_name: host_name_example
      metric_name: DB_OS_CONFIG_INSTANCE
      instance_name: instance_name_example

      # optional
      num_cp_us: 56
      num_cpu_cores: 56
      num_cpu_sockets: 56
      physical_memory_bytes: 3.4
      time_collected: time_collected_example
    action: ingest_database_configuration

    # optional
    database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
    id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"

- name: Perform action ingest_sql_bucket on database_insights
  oci_opsi_database_insights_actions:
    # required
    action: ingest_sql_bucket

    # optional
    items:
    - # required
      host_name: host_name_example
      metric_name: DB_OS_CONFIG_INSTANCE
      instance_name: instance_name_example

      # optional
      num_cp_us: 56
      num_cpu_cores: 56
      num_cpu_sockets: 56
      physical_memory_bytes: 3.4
      time_collected: time_collected_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
    id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"

- name: Perform action ingest_sql_plan_lines on database_insights
  oci_opsi_database_insights_actions:
    # required
    action: ingest_sql_plan_lines

    # optional
    items:
    - # required
      host_name: host_name_example
      metric_name: DB_OS_CONFIG_INSTANCE
      instance_name: instance_name_example

      # optional
      num_cp_us: 56
      num_cpu_cores: 56
      num_cpu_sockets: 56
      physical_memory_bytes: 3.4
      time_collected: time_collected_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
    id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"

- name: Perform action ingest_sql_stats on database_insights
  oci_opsi_database_insights_actions:
    # required
    action: ingest_sql_stats

    # optional
    items:
    - # required
      host_name: host_name_example
      metric_name: DB_OS_CONFIG_INSTANCE
      instance_name: instance_name_example

      # optional
      num_cp_us: 56
      num_cpu_cores: 56
      num_cpu_sockets: 56
      physical_memory_bytes: 3.4
      time_collected: time_collected_example
    database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
    id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"

- name: Perform action ingest_sql_text on database_insights
  oci_opsi_database_insights_actions:
    # required
    action: ingest_sql_text

    # optional
    items:
    - # required
      host_name: host_name_example
      metric_name: DB_OS_CONFIG_INSTANCE
      instance_name: instance_name_example

      # optional
      num_cp_us: 56
      num_cpu_cores: 56
      num_cpu_sockets: 56
      physical_memory_bytes: 3.4
      time_collected: time_collected_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
    id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
database_insights:
    description:
        - Details of the DatabaseInsights resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        is_advanced_features_enabled:
            description:
                - Flag is to identify if advanced features for autonomous database is enabled or not
            returned: on success
            type: bool
            sample: true
        enterprise_manager_identifier:
            description:
                - Enterprise Manager Unique Identifier
            returned: on success
            type: str
            sample: enterprise_manager_identifier_example
        enterprise_manager_entity_name:
            description:
                - Enterprise Manager Entity Name
            returned: on success
            type: str
            sample: enterprise_manager_entity_name_example
        enterprise_manager_entity_type:
            description:
                - Enterprise Manager Entity Type
            returned: on success
            type: str
            sample: enterprise_manager_entity_type_example
        enterprise_manager_entity_identifier:
            description:
                - Enterprise Manager Entity Unique Identifier
            returned: on success
            type: str
            sample: enterprise_manager_entity_identifier_example
        enterprise_manager_entity_display_name:
            description:
                - Enterprise Manager Entity Display Name
            returned: on success
            type: str
            sample: enterprise_manager_entity_display_name_example
        enterprise_manager_bridge_id:
            description:
                - OPSI Enterprise Manager Bridge OCID
            returned: on success
            type: str
            sample: "ocid1.enterprisemanagerbridge.oc1..xxxxxxEXAMPLExxxxxx"
        exadata_insight_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Exadata insight.
            returned: on success
            type: str
            sample: "ocid1.exadatainsight.oc1..xxxxxxEXAMPLExxxxxx"
        management_agent_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Management Agent
            returned: on success
            type: str
            sample: "ocid1.managementagent.oc1..xxxxxxEXAMPLExxxxxx"
        connector_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of External Database Connector
            returned: on success
            type: str
            sample: "ocid1.connector.oc1..xxxxxxEXAMPLExxxxxx"
        connection_credential_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                credential_source_name:
                    description:
                        - Credential source name that had been added in Management Agent wallet. This is supplied in the External Database Service.
                    returned: on success
                    type: str
                    sample: credential_source_name_example
                credential_type:
                    description:
                        - Credential type.
                    returned: on success
                    type: str
                    sample: CREDENTIALS_BY_SOURCE
                user_name:
                    description:
                        - database user name.
                    returned: on success
                    type: str
                    sample: user_name_example
                password_secret_id:
                    description:
                        - The secret L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) mapping to the database credentials.
                    returned: on success
                    type: str
                    sample: "ocid1.passwordsecret.oc1..xxxxxxEXAMPLExxxxxx"
                wallet_secret_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Secret where the database keystore contents
                          are stored. This is used for TCPS support in BM/VM/ExaCS cases.
                    returned: on success
                    type: str
                    sample: "ocid1.walletsecret.oc1..xxxxxxEXAMPLExxxxxx"
                role:
                    description:
                        - database user role.
                    returned: on success
                    type: str
                    sample: NORMAL
        db_additional_details:
            description:
                - Additional details of a database in JSON format. For autonomous databases, this is the AutonomousDatabase object serialized as a JSON string
                  as defined in https://docs.cloud.oracle.com/en-us/iaas/api/#/en/database/20160918/AutonomousDatabase/. For EM, pass in null or an empty
                  string. Note that this string needs to be escaped when specified in the curl command.
            returned: on success
            type: dict
            sample: {}
        entity_source:
            description:
                - Source of the database entity.
            returned: on success
            type: str
            sample: AUTONOMOUS_DATABASE
        id:
            description:
                - Database insight identifier
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - Compartment identifier of the database
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        status:
            description:
                - Indicates the status of a database insight in Operations Insights
            returned: on success
            type: str
            sample: DISABLED
        database_type:
            description:
                - Operations Insights internal representation of the database type.
            returned: on success
            type: str
            sample: database_type_example
        database_version:
            description:
                - The version of the database.
            returned: on success
            type: str
            sample: database_version_example
        processor_count:
            description:
                - Processor count. This is the OCPU count for Autonomous Database and CPU core count for other database types.
            returned: on success
            type: int
            sample: 56
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
                - "System tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
        time_created:
            description:
                - The time the the database insight was first enabled. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the database insight was updated. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the database.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        database_connection_status_details:
            description:
                - A message describing the status of the database connection of this resource. For example, it can be used to provide actionable information
                  about the permission and content validity of the database connection.
            returned: on success
            type: str
            sample: database_connection_status_details_example
        opsi_private_endpoint_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the OPSI private endpoint
            returned: on success
            type: str
            sample: "ocid1.opsiprivateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
        connection_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                host_name:
                    description:
                        - Name of the listener host that will be used to create the connect string to the database.
                    returned: on success
                    type: str
                    sample: host_name_example
                protocol:
                    description:
                        - Protocol used for connection requests.
                    returned: on success
                    type: str
                    sample: TCP
                port:
                    description:
                        - Listener port number used for connection requests.
                    returned: on success
                    type: int
                    sample: 56
                service_name:
                    description:
                        - Database service name used for connection requests.
                    returned: on success
                    type: str
                    sample: service_name_example
                hosts:
                    description:
                        - List of hosts and port for private endpoint accessed database resource.
                    returned: on success
                    type: complex
                    contains:
                        host_ip:
                            description:
                                - Host IP used for connection requests for Cloud DB resource.
                            returned: on success
                            type: str
                            sample: host_ip_example
                        port:
                            description:
                                - Listener port number used for connection requests for rivate endpoint accessed db resource.
                            returned: on success
                            type: int
                            sample: 56
        credential_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                credential_source_name:
                    description:
                        - Credential source name that had been added in Management Agent wallet. This is supplied in the External Database Service.
                    returned: on success
                    type: str
                    sample: credential_source_name_example
                credential_type:
                    description:
                        - Credential type.
                    returned: on success
                    type: str
                    sample: CREDENTIALS_BY_SOURCE
                user_name:
                    description:
                        - database user name.
                    returned: on success
                    type: str
                    sample: user_name_example
                password_secret_id:
                    description:
                        - The secret L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) mapping to the database credentials.
                    returned: on success
                    type: str
                    sample: "ocid1.passwordsecret.oc1..xxxxxxEXAMPLExxxxxx"
                wallet_secret_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Secret where the database keystore contents
                          are stored. This is used for TCPS support in BM/VM/ExaCS cases.
                    returned: on success
                    type: str
                    sample: "ocid1.walletsecret.oc1..xxxxxxEXAMPLExxxxxx"
                role:
                    description:
                        - database user role.
                    returned: on success
                    type: str
                    sample: NORMAL
        database_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the database.
            returned: on success
            type: str
            sample: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
        database_name:
            description:
                - Name of database
            returned: on success
            type: str
            sample: database_name_example
        database_display_name:
            description:
                - Display name of database
            returned: on success
            type: str
            sample: database_display_name_example
        database_resource_type:
            description:
                - OCI database resource type
            returned: on success
            type: str
            sample: database_resource_type_example
        parent_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VM Cluster or DB System ID, depending on which
                  configuration the resource belongs to.
            returned: on success
            type: str
            sample: "ocid1.parent.oc1..xxxxxxEXAMPLExxxxxx"
        root_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Exadata Infrastructure.
            returned: on success
            type: str
            sample: "ocid1.root.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
        "is_advanced_features_enabled": true,
        "enterprise_manager_identifier": "enterprise_manager_identifier_example",
        "enterprise_manager_entity_name": "enterprise_manager_entity_name_example",
        "enterprise_manager_entity_type": "enterprise_manager_entity_type_example",
        "enterprise_manager_entity_identifier": "enterprise_manager_entity_identifier_example",
        "enterprise_manager_entity_display_name": "enterprise_manager_entity_display_name_example",
        "enterprise_manager_bridge_id": "ocid1.enterprisemanagerbridge.oc1..xxxxxxEXAMPLExxxxxx",
        "exadata_insight_id": "ocid1.exadatainsight.oc1..xxxxxxEXAMPLExxxxxx",
        "management_agent_id": "ocid1.managementagent.oc1..xxxxxxEXAMPLExxxxxx",
        "connector_id": "ocid1.connector.oc1..xxxxxxEXAMPLExxxxxx",
        "connection_credential_details": {
            "credential_source_name": "credential_source_name_example",
            "credential_type": "CREDENTIALS_BY_SOURCE",
            "user_name": "user_name_example",
            "password_secret_id": "ocid1.passwordsecret.oc1..xxxxxxEXAMPLExxxxxx",
            "wallet_secret_id": "ocid1.walletsecret.oc1..xxxxxxEXAMPLExxxxxx",
            "role": "NORMAL"
        },
        "db_additional_details": {},
        "entity_source": "AUTONOMOUS_DATABASE",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "status": "DISABLED",
        "database_type": "database_type_example",
        "database_version": "database_version_example",
        "processor_count": 56,
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "database_connection_status_details": "database_connection_status_details_example",
        "opsi_private_endpoint_id": "ocid1.opsiprivateendpoint.oc1..xxxxxxEXAMPLExxxxxx",
        "connection_details": {
            "host_name": "host_name_example",
            "protocol": "TCP",
            "port": 56,
            "service_name": "service_name_example",
            "hosts": [{
                "host_ip": "host_ip_example",
                "port": 56
            }]
        },
        "credential_details": {
            "credential_source_name": "credential_source_name_example",
            "credential_type": "CREDENTIALS_BY_SOURCE",
            "user_name": "user_name_example",
            "password_secret_id": "ocid1.passwordsecret.oc1..xxxxxxEXAMPLExxxxxx",
            "wallet_secret_id": "ocid1.walletsecret.oc1..xxxxxxEXAMPLExxxxxx",
            "role": "NORMAL"
        },
        "database_id": "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx",
        "database_name": "database_name_example",
        "database_display_name": "database_display_name_example",
        "database_resource_type": "database_resource_type_example",
        "parent_id": "ocid1.parent.oc1..xxxxxxEXAMPLExxxxxx",
        "root_id": "ocid1.root.oc1..xxxxxxEXAMPLExxxxxx"
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
    from oci.opsi import OperationsInsightsClient
    from oci.opsi.models import ChangeAutonomousDatabaseInsightAdvancedFeaturesDetails
    from oci.opsi.models import ChangeDatabaseInsightCompartmentDetails
    from oci.opsi.models import ChangePeComanagedDatabaseInsightDetails
    from oci.opsi.models import EnableAutonomousDatabaseInsightAdvancedFeaturesDetails
    from oci.opsi.models import EnableDatabaseInsightDetails
    from oci.opsi.models import IngestAddmReportsDetails
    from oci.opsi.models import IngestDatabaseConfigurationDetails
    from oci.opsi.models import IngestSqlBucketDetails
    from oci.opsi.models import IngestSqlPlanLinesDetails
    from oci.opsi.models import IngestSqlStatsDetails
    from oci.opsi.models import IngestSqlTextDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DatabaseInsightsActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_autonomous_database_insight_advanced_features
        change
        change_pe_comanaged
        disable_autonomous_database_insight_advanced_features
        disable
        enable_autonomous_database_insight_advanced_features
        enable
        ingest_addm_reports
        ingest_database_configuration
        ingest_sql_bucket
        ingest_sql_plan_lines
        ingest_sql_stats
        ingest_sql_text
    """

    def get_get_fn(self):
        return self.client.get_database_insight

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_database_insight,
            database_insight_id=self.module.params.get("database_insight_id"),
        )

    def change_autonomous_database_insight_advanced_features(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeAutonomousDatabaseInsightAdvancedFeaturesDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_autonomous_database_insight_advanced_features,
            call_fn_args=(),
            call_fn_kwargs=dict(
                change_autonomous_database_insight_advanced_features_details=action_details,
                database_insight_id=self.module.params.get("database_insight_id"),
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

    def change(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeDatabaseInsightCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_database_insight_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                database_insight_id=self.module.params.get("database_insight_id"),
                change_database_insight_compartment_details=action_details,
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

    def change_pe_comanaged(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangePeComanagedDatabaseInsightDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_pe_comanaged_database_insight,
            call_fn_args=(),
            call_fn_kwargs=dict(
                database_insight_id=self.module.params.get("database_insight_id"),
                change_pe_comanaged_database_insight_details=action_details,
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

    def disable_autonomous_database_insight_advanced_features(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.disable_autonomous_database_insight_advanced_features,
            call_fn_args=(),
            call_fn_kwargs=dict(
                database_insight_id=self.module.params.get("database_insight_id"),
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

    def disable(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.disable_database_insight,
            call_fn_args=(),
            call_fn_kwargs=dict(
                database_insight_id=self.module.params.get("database_insight_id"),
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

    def enable_autonomous_database_insight_advanced_features(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, EnableAutonomousDatabaseInsightAdvancedFeaturesDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.enable_autonomous_database_insight_advanced_features,
            call_fn_args=(),
            call_fn_kwargs=dict(
                enable_autonomous_database_insight_advanced_features_details=action_details,
                database_insight_id=self.module.params.get("database_insight_id"),
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

    def enable(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, EnableDatabaseInsightDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.enable_database_insight,
            call_fn_args=(),
            call_fn_kwargs=dict(
                enable_database_insight_details=action_details,
                database_insight_id=self.module.params.get("database_insight_id"),
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

    def ingest_addm_reports(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, IngestAddmReportsDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.ingest_addm_reports,
            call_fn_args=(),
            call_fn_kwargs=dict(
                ingest_addm_reports_details=action_details,
                database_id=self.module.params.get("database_id"),
                id=self.module.params.get("id"),
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

    def ingest_database_configuration(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, IngestDatabaseConfigurationDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.ingest_database_configuration,
            call_fn_args=(),
            call_fn_kwargs=dict(
                ingest_database_configuration_details=action_details,
                database_id=self.module.params.get("database_id"),
                id=self.module.params.get("id"),
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

    def ingest_sql_bucket(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, IngestSqlBucketDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.ingest_sql_bucket,
            call_fn_args=(),
            call_fn_kwargs=dict(
                ingest_sql_bucket_details=action_details,
                compartment_id=self.module.params.get("compartment_id"),
                database_id=self.module.params.get("database_id"),
                id=self.module.params.get("id"),
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

    def ingest_sql_plan_lines(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, IngestSqlPlanLinesDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.ingest_sql_plan_lines,
            call_fn_args=(),
            call_fn_kwargs=dict(
                ingest_sql_plan_lines_details=action_details,
                compartment_id=self.module.params.get("compartment_id"),
                database_id=self.module.params.get("database_id"),
                id=self.module.params.get("id"),
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

    def ingest_sql_stats(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, IngestSqlStatsDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.ingest_sql_stats,
            call_fn_args=(),
            call_fn_kwargs=dict(
                ingest_sql_stats_details=action_details,
                database_id=self.module.params.get("database_id"),
                id=self.module.params.get("id"),
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

    def ingest_sql_text(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, IngestSqlTextDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.ingest_sql_text,
            call_fn_args=(),
            call_fn_kwargs=dict(
                ingest_sql_text_details=action_details,
                compartment_id=self.module.params.get("compartment_id"),
                database_id=self.module.params.get("database_id"),
                id=self.module.params.get("id"),
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


DatabaseInsightsActionsHelperCustom = get_custom_class(
    "DatabaseInsightsActionsHelperCustom"
)


class ResourceHelper(
    DatabaseInsightsActionsHelperCustom, DatabaseInsightsActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            entity_source=dict(
                type="str",
                choices=["EM_MANAGED_EXTERNAL_DATABASE", "PE_COMANAGED_DATABASE"],
            ),
            opsi_private_endpoint_id=dict(type="str"),
            service_name=dict(type="str"),
            credential_details=dict(
                type="dict",
                options=dict(
                    credential_source_name=dict(type="str", required=True),
                    credential_type=dict(
                        type="str",
                        required=True,
                        choices=["CREDENTIALS_BY_SOURCE", "CREDENTIALS_BY_VAULT"],
                    ),
                    user_name=dict(type="str"),
                    password_secret_id=dict(type="str"),
                    wallet_secret_id=dict(type="str"),
                    role=dict(type="str", choices=["NORMAL"]),
                ),
            ),
            connection_details=dict(
                type="dict",
                options=dict(
                    host_name=dict(type="str"),
                    port=dict(type="int"),
                    hosts=dict(
                        type="list",
                        elements="dict",
                        options=dict(host_ip=dict(type="str"), port=dict(type="int")),
                    ),
                    protocol=dict(type="str", choices=["TCP", "TCPS"]),
                    service_name=dict(type="str"),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            system_tags=dict(type="dict"),
            database_insight_id=dict(type="str"),
            items=dict(
                type="list",
                elements="dict",
                options=dict(
                    time_interval_start=dict(type="str"),
                    time_interval_end=dict(type="str"),
                    task_identifier=dict(type="str"),
                    database_identifier=dict(type="str"),
                    snapshot_interval_start=dict(type="str"),
                    snapshot_interval_end=dict(type="str"),
                    addm_report=dict(type="str"),
                    num_cp_us=dict(type="int"),
                    num_cpu_cores=dict(type="int"),
                    num_cpu_sockets=dict(type="int"),
                    physical_memory_bytes=dict(type="float"),
                    host_name=dict(type="str"),
                    cpu_count=dict(type="int"),
                    host_memory_capacity=dict(type="float"),
                    db_external_instance_version=dict(type="str"),
                    parallel=dict(type="str"),
                    instance_role=dict(type="str"),
                    logins=dict(type="str"),
                    database_status=dict(type="str"),
                    status=dict(type="str"),
                    edition=dict(type="str"),
                    startup_time=dict(type="str"),
                    instance_number=dict(type="int"),
                    parameter_name=dict(type="str"),
                    parameter_value=dict(type="str"),
                    snapshot_id=dict(type="int"),
                    is_changed=dict(type="str"),
                    is_default=dict(type="str"),
                    metric_name=dict(
                        type="str",
                        choices=[
                            "DB_OS_CONFIG_INSTANCE",
                            "DB_EXTERNAL_INSTANCE",
                            "DB_PARAMETERS",
                            "DB_EXTERNAL_PROPERTIES",
                        ],
                    ),
                    name=dict(type="str"),
                    log_mode=dict(type="str"),
                    cdb=dict(type="str"),
                    open_mode=dict(type="str"),
                    database_role=dict(type="str"),
                    guard_status=dict(type="str"),
                    platform_name=dict(type="str"),
                    control_file_type=dict(type="str"),
                    switchover_status=dict(type="str"),
                    created=dict(type="str"),
                    database_type=dict(type="str"),
                    bucket_id=dict(type="str"),
                    executions_count=dict(type="int"),
                    cpu_time_in_sec=dict(type="float"),
                    io_time_in_sec=dict(type="float"),
                    other_wait_time_in_sec=dict(type="float"),
                    total_time_in_sec=dict(type="float"),
                    plan_hash=dict(type="int"),
                    operation=dict(type="str"),
                    remark=dict(type="str"),
                    options=dict(type="str"),
                    object_node=dict(type="str"),
                    object_owner=dict(type="str"),
                    object_name=dict(type="str"),
                    object_alias=dict(type="str"),
                    object_instance=dict(type="int"),
                    object_type=dict(type="str"),
                    optimizer=dict(type="str"),
                    search_columns=dict(type="int"),
                    identifier=dict(type="int"),
                    parent_identifier=dict(type="int"),
                    depth=dict(type="int"),
                    position=dict(type="int"),
                    cost=dict(type="int"),
                    cardinality=dict(type="int"),
                    bytes=dict(type="int"),
                    other=dict(type="str"),
                    other_tag=dict(type="str"),
                    partition_start=dict(type="str"),
                    partition_stop=dict(type="str"),
                    partition_identifier=dict(type="int"),
                    distribution=dict(type="str"),
                    cpu_cost=dict(type="int"),
                    io_cost=dict(type="int"),
                    temp_space=dict(type="int"),
                    access_predicates=dict(type="str"),
                    filter_predicates=dict(type="str"),
                    projection=dict(type="str"),
                    qblock_name=dict(type="str"),
                    elapsed_time_in_sec=dict(type="float"),
                    other_xml=dict(type="str"),
                    plan_hash_value=dict(type="int"),
                    instance_name=dict(type="str"),
                    last_active_time=dict(type="str"),
                    parse_calls=dict(type="int"),
                    disk_reads=dict(type="int"),
                    direct_reads=dict(type="int"),
                    direct_writes=dict(type="int"),
                    buffer_gets=dict(type="int"),
                    rows_processed=dict(type="int"),
                    serializable_aborts=dict(type="int"),
                    fetches=dict(type="int"),
                    executions=dict(type="int"),
                    avoided_executions=dict(type="int"),
                    end_of_fetch_count=dict(type="int"),
                    loads=dict(type="int"),
                    version_count=dict(type="int"),
                    invalidations=dict(type="int"),
                    obsolete_count=dict(type="int"),
                    px_servers_executions=dict(type="int"),
                    cpu_time_in_us=dict(type="int"),
                    elapsed_time_in_us=dict(type="int"),
                    avg_hard_parse_time_in_us=dict(type="int"),
                    concurrency_wait_time_in_us=dict(type="int"),
                    application_wait_time_in_us=dict(type="int"),
                    cluster_wait_time_in_us=dict(type="int"),
                    user_io_wait_time_in_us=dict(type="int"),
                    plsql_exec_time_in_us=dict(type="int"),
                    java_exec_time_in_us=dict(type="int"),
                    sorts=dict(type="int"),
                    sharable_mem=dict(type="int"),
                    total_sharable_mem=dict(type="int"),
                    type_check_mem=dict(type="int"),
                    io_cell_offload_eligible_bytes=dict(type="int"),
                    io_interconnect_bytes=dict(type="int"),
                    physical_read_requests=dict(type="int"),
                    physical_read_bytes=dict(type="int"),
                    physical_write_requests=dict(type="int"),
                    physical_write_bytes=dict(type="int"),
                    io_cell_uncompressed_bytes=dict(type="int"),
                    io_cell_offload_returned_bytes=dict(type="int"),
                    child_number=dict(type="int"),
                    command_type=dict(type="int"),
                    users_opening=dict(type="int"),
                    users_executing=dict(type="int"),
                    optimizer_cost=dict(type="int"),
                    full_plan_hash_value=dict(type="str"),
                    module=dict(type="str"),
                    service=dict(type="str"),
                    action=dict(type="str"),
                    sql_profile=dict(type="str"),
                    sql_patch=dict(type="str"),
                    sql_plan_baseline=dict(type="str"),
                    delta_execution_count=dict(type="int"),
                    delta_cpu_time=dict(type="int"),
                    delta_io_bytes=dict(type="int"),
                    delta_cpu_rank=dict(type="int"),
                    delta_execs_rank=dict(type="int"),
                    sharable_mem_rank=dict(type="int"),
                    delta_io_rank=dict(type="int"),
                    harmonic_sum=dict(type="int"),
                    wt_harmonic_sum=dict(type="int"),
                    total_sql_count=dict(type="int"),
                    version=dict(type="float"),
                    sql_identifier=dict(type="str"),
                    time_collected=dict(type="str"),
                    sql_command=dict(type="str"),
                    exact_matching_signature=dict(type="str"),
                    force_matching_signature=dict(type="str"),
                    sql_full_text=dict(type="str"),
                ),
            ),
            compartment_id=dict(type="str"),
            database_id=dict(type="str"),
            id=dict(type="str"),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "change_autonomous_database_insight_advanced_features",
                    "change",
                    "change_pe_comanaged",
                    "disable_autonomous_database_insight_advanced_features",
                    "disable",
                    "enable_autonomous_database_insight_advanced_features",
                    "enable",
                    "ingest_addm_reports",
                    "ingest_database_configuration",
                    "ingest_sql_bucket",
                    "ingest_sql_plan_lines",
                    "ingest_sql_stats",
                    "ingest_sql_text",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="database_insights",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
