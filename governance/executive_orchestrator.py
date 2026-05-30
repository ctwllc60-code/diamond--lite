from datetime import datetime

from core.identity.diamond_lite_identity import (
    DIAMOND_LITE_IDENTITY
)

from core.architecture.mental_model import (
    MENTAL_MODEL
)

from core.architecture.thinking_model import (
    THINKING_MODEL
)

from governance.rules_and_constraints import (
    RULES_AND_CONSTRAINTS
)

from governance.risk_analysis import (
    RISK_ANALYSIS
)

from governance.feedback_loop import (
    FEEDBACK_LOOP
)

from memory.identity.learning_and_internalization_model import (
    LEARNING_AND_INTERNALIZATION_MODEL
)

from manifestation.voice_guidance import (
    VOICE_GUIDANCE
)

from philosophy.experience_preservation import (
    EXPERIENCE_PRESERVATION
)

from philosophy.human_centered_architecture import (
    HUMAN_CENTERED_ARCHITECTURE
)


def build_orchestration_state():

    return {

        "active_engine":
            None,

        "execution_mode":
            "structured",

        "priority_level":
            "standard",

        "orchestration_pressure":
            "stable",

        "active_routes":
            [],

        "protected_routes":
            [],

        "blocked_routes":
            [],

        "routing_history":
            [],

        "last_updated":
            None
    }


def determine_execution_mode(
    payload
):

    payload_text = str(
        payload
    ).lower()

    if any(

        signal in payload_text

        for signal in [

            "error",

            "failure",

            "confused",

            "unstable",

            "frustrated"
        ]
    ):

        return "stabilization"

    if any(

        signal in payload_text

        for signal in [

            "build",

            "wire",

            "execute",

            "implement",

            "architecture"
        ]
    ):

        return "execution"

    return "structured"


def determine_priority_level(
    payload
):

    payload_text = str(
        payload
    ).lower()

    critical_signals = [

        "collapse",

        "corruption",

        "failure",

        "broken",

        "unstable"
    ]

    elevated_signals = [

        "build",

        "upgrade",

        "expand",

        "system"
    ]

    if any(

        signal in payload_text

        for signal in critical_signals
    ):

        return "critical"

    if any(

        signal in payload_text

        for signal in elevated_signals
    ):

        return "elevated"

    return "standard"


def determine_active_routes(
    execution_mode
):

    route_map = {

        "stabilization": [

            "continuity_stabilizer",

            "behavioral_harmony",

            "validation_layer",

            "surface_integrity_verification"
        ],

        "execution": [

            "retrieval_engine",

            "relationship_awareness_engine",

            "validation_layer"
        ],

        "structured": [

            "retrieval_engine",

            "validation_layer"
        ]
    }

    return route_map.get(
        execution_mode,
        []
    )


def determine_protected_routes(
    priority_level
):

    if priority_level == "critical":

        return [

            "validation_layer",

            "surface_integrity_verification",

            "continuity_stabilizer"
        ]

    return [
        "validation_layer"
    ]


def determine_blocked_routes(
    execution_mode
):

    if execution_mode == "stabilization":

        return [

            "aggressive_expansion",

            "unverified_execution"
        ]

    return []


def load_foundation_layers():

    return {

        "diamond_lite_identity":
            DIAMOND_LITE_IDENTITY,

        "mental_model":
            MENTAL_MODEL,

        "thinking_model":
            THINKING_MODEL,

        "rules_and_constraints":
            RULES_AND_CONSTRAINTS,

        "risk_analysis":
            RISK_ANALYSIS,

        "feedback_loop":
            FEEDBACK_LOOP,

        "learning_model":
            LEARNING_AND_INTERNALIZATION_MODEL,

        "voice_guidance":
            VOICE_GUIDANCE,

        "experience_preservation":
            EXPERIENCE_PRESERVATION,

        "human_centered_architecture":
            HUMAN_CENTERED_ARCHITECTURE
    }


def build_orchestration_profile(
    payload
):

    orchestration_state = (
        build_orchestration_state()
    )

    execution_mode = (
        determine_execution_mode(
            payload
        )
    )

    priority_level = (
        determine_priority_level(
            payload
        )
    )

    active_routes = (
        determine_active_routes(
            execution_mode
        )
    )

    protected_routes = (
        determine_protected_routes(
            priority_level
        )
    )

    blocked_routes = (
        determine_blocked_routes(
            execution_mode
        )
    )

    orchestration_state[
        "execution_mode"
    ] = execution_mode

    orchestration_state[
        "priority_level"
    ] = priority_level

    orchestration_state[
        "active_routes"
    ] = active_routes

    orchestration_state[
        "protected_routes"
    ] = protected_routes

    orchestration_state[
        "blocked_routes"
    ] = blocked_routes

    orchestration_state[
        "foundation_layers"
    ] = load_foundation_layers()

    orchestration_state[
        "last_updated"
    ] = datetime.utcnow().isoformat()

    return orchestration_state


def orchestrate_execution(
    payload
):

    orchestration_profile = (
        build_orchestration_profile(
            payload
        )
    )

    payload[
        "executive_orchestration"
    ] = orchestration_profile

    return payload


def get_orchestration_snapshot(
    payload
):

    profile = (
        build_orchestration_profile(
            payload
        )
    )

    return {

        "execution_mode":
            profile.get(
                "execution_mode"
            ),

        "priority_level":
            profile.get(
                "priority_level"
            ),

        "active_routes":
            profile.get(
                "active_routes"
            ),

        "protected_routes":
            profile.get(
                "protected_routes"
            ),

        "blocked_routes":
            profile.get(
                "blocked_routes"
            )
    }
