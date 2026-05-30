from datetime import (
    datetime,
    UTC,
    timedelta
)

import json
import os
import time
import uuid

from orchestration.orchestrator import (
    Orchestrator
)

from core.schemas.message_object import (
    MessageObject
)

from runtime.input.message_assembler import (
    MessageAssembler
)

RUNTIME_LOG = (
    "state/runtime_state.json"
)

AUDIT_LOG = (
    "state/operational_audit.json"
)

SCHEDULER_INTERVAL_SECONDS = 300
MAX_PROCESSING_DURATION = 10
MAX_AUDIT_LOG_SIZE = 500

ANOMALY_THRESHOLDS = {
    "processing_duration":
        MAX_PROCESSING_DURATION,

    "heartbeat_staleness_seconds":
        600,

    "scheduler_delay_seconds":
        900
}

INFRASTRUCTURE_SCORE_THRESHOLDS = {
    "excellent":
        95,

    "stable":
        80,

    "warning":
        60,

    "critical":
        40
}

DEFAULT_MONITORING_ROUTINES = [
    {
        "routine_name":
            "runtime_health_monitor",

        "category":
            "infrastructure",

        "enabled":
            True
    },

    {
        "routine_name":
            "scheduler_integrity_monitor",

        "category":
            "scheduler",

        "enabled":
            True
    },

    {
        "routine_name":
            "cycle_stability_monitor",

        "category":
            "operations",

        "enabled":
            True
    }
]

DEFAULT_RUNTIME_STATE = {
    "session_count":
        0,

    "last_session_start":
        None,

    "last_user_message":
        None,

    "last_runtime_status":
        "initialized",

    "heartbeat_timestamp":
        None,

    "runtime_health":
        "stable",

    "cycle_id":
        None,

    "cycle_status":
        "idle",

    "cycle_started_at":
        None,

    "cycle_completed_at":
        None,

    "scheduler_enabled":
        True,

    "scheduler_health":
        "stable",

    "scheduler_interval_seconds":
        SCHEDULER_INTERVAL_SECONDS,

    "next_scheduled_cycle":
        None,

    "last_scheduler_check":
        None,

    "monitoring_routines":
        DEFAULT_MONITORING_ROUTINES,

    "last_monitoring_cycle":
        None,

    "monitoring_health":
        "stable",

    "executive_governance":
        True,

    "verification_layer":
        True,

    "correction_loops":
        True,

    "runtime_cognition":
        True,

    "pipeline_connected":
        False,

    "watchtower_bridge_active":
        False,

    "pipeline_status":
        "inactive",

    "active_pipeline":
        None,

    "active_engine":
        None,

    "reflection_analysis":
        {},

    "enrichment_layer_count":
        0,

    "current_wave":
        0
}

def initialize_runtime_state():
    if not os.path.exists(
        "state"
    ):
        os.mkdir(
            "state"
        )

    if not os.path.exists(
        RUNTIME_LOG
    ):
        with open(
            RUNTIME_LOG,
            "w"
        ) as file:
            json.dump(
                DEFAULT_RUNTIME_STATE,
                file,
                indent=4
            )

    if not os.path.exists(
        AUDIT_LOG
    ):
        with open(
            AUDIT_LOG,
            "w"
        ) as file:
            json.dump(
                [],
                file,
                indent=4
            )

def load_runtime_state():
    with open(
        RUNTIME_LOG,
        "r"
    ) as file:
        return json.load(
            file
        )

def save_runtime_state(
    runtime_state
):
    with open(
        RUNTIME_LOG,
        "w"
    ) as file:
        json.dump(
            runtime_state,
            file,
            indent=4
        )

def load_audit_log():
    with open(
        AUDIT_LOG,
        "r"
    ) as file:
        return json.load(
            file
        )

def save_audit_log(
    audit_log
):
    with open(
        AUDIT_LOG,
        "w"
    ) as file:
        json.dump(
            audit_log,
            file,
            indent=4
        )

def record_audit_event(
    event_type,
    details
):
    audit_log = (
        load_audit_log()
    )

    audit_event = {
        "event_id":
            str(
                uuid.uuid4()
            ),

        "event_type":
            event_type,

        "timestamp":
            datetime.now(
                UTC
            ).isoformat(),

        "details":
            details
    }

    audit_log.append(
        audit_event
    )

    if len(
        audit_log
    ) > MAX_AUDIT_LOG_SIZE:
        audit_log = (
            audit_log[
                -MAX_AUDIT_LOG_SIZE:
            ]
        )

    save_audit_log(
        audit_log
    )

def record_anomaly_event(
    anomaly_type,
    severity,
    details
):
    anomaly_event = {
        "anomaly_id":
            str(
                uuid.uuid4()
            ),

        "anomaly_type":
            anomaly_type,

        "severity":
            severity,

        "timestamp":
            datetime.now(
                UTC
            ).isoformat(),

        "details":
            details
    }

    record_audit_event(
        "operational_anomaly",
        anomaly_event
    )

def evaluate_runtime_anomalies(
    runtime_state
):
    processing_duration = (
        runtime_state.get(
            "last_processing_duration",
            0
        )
    )

    if (
        processing_duration
        > ANOMALY_THRESHOLDS[
            "processing_duration"
        ]
    ):
        record_anomaly_event(
            "processing_duration_exceeded",
            "medium",
            {
                "processing_duration":
                    processing_duration
            }
        )

def calculate_infrastructure_score(
    runtime_state
):
    infrastructure_score = 100
    anomaly_penalty = 0

    processing_duration = (
        runtime_state.get(
            "last_processing_duration",
            0
        )
    )

    if (
        processing_duration
        > MAX_PROCESSING_DURATION
    ):
        anomaly_penalty += 15

    scheduler_health = (
        runtime_state.get(
            "scheduler_health",
            "stable"
        )
    )

    if (
        scheduler_health
        != "stable"
    ):
        anomaly_penalty += 20

    runtime_health = (
        runtime_state.get(
            "runtime_health",
            "stable"
        )
    )

    if (
        runtime_health
        != "stable"
    ):
        anomaly_penalty += 20

    infrastructure_score -= (
        anomaly_penalty
    )

    if infrastructure_score < 0:
        infrastructure_score = 0

    runtime_state[
        "infrastructure_score"
    ] = infrastructure_score

    runtime_state[
        "infrastructure_status"
    ] = (
        "excellent"
        if infrastructure_score >= 95
        else "stable"
    )

def update_heartbeat(
    runtime_state
):
    runtime_state[
        "heartbeat_timestamp"
    ] = (
        datetime.now(
            UTC
        ).isoformat()
    )

    runtime_state[
        "runtime_health"
    ] = "stable"

def update_scheduler_state(
    runtime_state
):
    current_time = (
        datetime.now(
            UTC
        )
    )

    next_cycle = (
        current_time
        + timedelta(
            seconds=SCHEDULER_INTERVAL_SECONDS
        )
    )

    runtime_state[
        "last_scheduler_check"
    ] = (
        current_time.isoformat()
    )

    runtime_state[
        "next_scheduled_cycle"
    ] = (
        next_cycle.isoformat()
    )

    runtime_state[
        "scheduler_health"
    ] = "stable"

def begin_operational_cycle(
    runtime_state
):
    runtime_state[
        "cycle_id"
    ] = str(
        uuid.uuid4()
    )

    runtime_state[
        "cycle_status"
    ] = "running"

    runtime_state[
        "cycle_started_at"
    ] = (
        datetime.now(
            UTC
        ).isoformat()
    )

def complete_operational_cycle(
    runtime_state
):
    runtime_state[
        "cycle_status"
    ] = "completed"

    runtime_state[
        "cycle_completed_at"
    ] = (
        datetime.now(
            UTC
        ).isoformat()
    )

# --------------------------------------------------
# INITIALIZATION
# --------------------------------------------------

initialize_runtime_state()

runtime_state = (
    load_runtime_state()
)

runtime_state[
    "session_count"
] += 1

runtime_state[
    "last_session_start"
] = (
    datetime.now(
        UTC
    ).isoformat()
)

runtime_state[
    "last_runtime_status"
] = "active"

save_runtime_state(
    runtime_state
)

record_audit_event(
    "runtime_session_started",
    {
        "session_count":
            runtime_state[
                "session_count"
            ]
    }
)

orchestrator = (
    Orchestrator()
)

assembler = (
    MessageAssembler()
)

# --------------------------------------------------
# MAIN OPERATIONAL LOOP
# --------------------------------------------------

while True:

    update_heartbeat(
        runtime_state
    )

    update_scheduler_state(
        runtime_state
    )

    evaluate_runtime_anomalies(
        runtime_state
    )

    calculate_infrastructure_score(
        runtime_state
    )

    save_runtime_state(
        runtime_state
    )

    lines = []

    while True:

        line = input(
            "\nUser: "
            if not lines
            else ""
        )

        if (
            line.lower().strip()
            == "exit"
        ):

            runtime_state[
                "last_runtime_status"
            ] = "closed"

            save_runtime_state(
                runtime_state
            )

            record_audit_event(
                "runtime_closed",
                {
                    "status":
                        "closed"
                }
            )

            exit()

        if (
            line.lower().strip()
            == "/send"
        ):
            break

        lines.append(
            line
        )

    user_input = (
        "\n".join(
            lines
        ).strip()
    )

    if not user_input:
        continue

    begin_operational_cycle(
        runtime_state
    )

    runtime_state[
        "last_user_message"
    ] = user_input

    runtime_state[
        "last_runtime_status"
    ] = "processing"

    save_runtime_state(
        runtime_state
    )

    processing_start = (
        time.time()
    )

    message = MessageObject(
        raw_message=user_input,
        developer_mode=False
    )

    result = orchestrator.run(
        message
    )

    processing_end = (
        time.time()
    )

    cleaned_response = (
        result.final_response.strip()
    )

    runtime_state[
        "last_runtime_status"
    ] = "response_generated"

    runtime_state[
        "last_response_timestamp"
    ] = (
        datetime.now(
            UTC
        ).isoformat()
    )

    runtime_state[
        "last_processing_duration"
    ] = round(
        processing_end
        - processing_start,
        4
    )

    runtime_state[
        "enrichment_layer_count"
    ] = len(
        result.enrichment_layers
    )

    runtime_state[
        "current_wave"
    ] = (
        result.recursion_state.get(
            "current_wave",
            0
        )
    )

    runtime_state[
        "pipeline_connected"
    ] = True

    runtime_state[
        "pipeline_status"
    ] = "active"

    complete_operational_cycle(
        runtime_state
    )

    update_heartbeat(
        runtime_state
    )

    update_scheduler_state(
        runtime_state
    )

    evaluate_runtime_anomalies(
        runtime_state
    )

    calculate_infrastructure_score(
        runtime_state
    )

    save_runtime_state(
        runtime_state
    )

    record_audit_event(
        "response_generated",
        {
            "processing_duration":
                runtime_state[
                    "last_processing_duration"
                ],

            "enrichment_layers":
                runtime_state[
                    "enrichment_layer_count"
                ]
        }
    )

    print(
        f"\nDiamond Lite: {cleaned_response}"
    )
