import re

from datetime import (
    datetime,
    UTC
)


CONTINUITY_VERSION = (
    "diamond_continuity_v2"
)


def normalize_response(
    response
):
    return str(
        response or ""
    ).strip()


def detect_response_collapse(
    response
):
    text = normalize_response(
        response
    )

    response_length = len(
        text
    )

    collapse_patterns = [
        "you get the idea",
        "and so on",
        "etc.",
        "whatever",
        "something like that"
    ]

    collapse_detected = (
        response_length < 40
    )

    collapse_pattern_detected = any(
        pattern in text.lower()
        for pattern in collapse_patterns
    )

    return (
        collapse_detected
        or collapse_pattern_detected
    )


def detect_transition_instability(
    response
):
    text = normalize_response(
        response
    )

    transition_patterns = [
        "anyway",
        "moving on",
        "in conclusion",
        "basically",
        "long story short"
    ]

    transition_instability_score = sum(
        1
        for pattern in transition_patterns
        if pattern in text.lower()
    )

    transition_instability_detected = (
        transition_instability_score >= 2
    )

    return transition_instability_detected


def detect_pacing_fragmentation(
    response
):
    text = normalize_response(
        response
    )

    sentences = re.split(
        r"[.!?]",
        text
    )

    sentence_lengths = [
        len(sentence.strip())
        for sentence in sentences
        if sentence.strip()
    ]

    fragmentation_score = sum(
        1
        for length in sentence_lengths
        if length < 8
    )

    pacing_fragmentation_detected = (
        fragmentation_score >= 6
    )

    return pacing_fragmentation_detected


def detect_continuity_pressure(
    continuity_signals
):
    collapse_detected = (
        continuity_signals.get(
            "response_collapse_detected",
            False
        )
    )

    transition_instability_detected = (
        continuity_signals.get(
            "transition_instability_detected",
            False
        )
    )

    pacing_fragmentation_detected = (
        continuity_signals.get(
            "pacing_fragmentation_detected",
            False
        )
    )

    orchestration_fragmentation = (
        continuity_signals.get(
            "orchestration_fragmentation",
            False
        )
    )

    if (
        collapse_detected
        or transition_instability_detected
        or orchestration_fragmentation
    ):
        return "high"

    if pacing_fragmentation_detected:
        return "moderate"

    return "stable"


def build_retrieval_queries(
    continuity_profile
):
    return [{
        "access_type": (
            "continuity_stabilization"
        ),

        "query": {
            "continuity_pressure": (
                continuity_profile.get(
                    "continuity_pressure"
                )
            ),

            "response_collapse_detected": (
                continuity_profile.get(
                    "response_collapse_detected"
                )
            ),

            "transition_instability_detected": (
                continuity_profile.get(
                    "transition_instability_detected"
                )
            ),

            "pacing_fragmentation_detected": (
                continuity_profile.get(
                    "pacing_fragmentation_detected"
                )
            ),

            "retrieval_focus": [
                "continuity_preservation",
                "response_stability",
                "conversation_flow",
                "pacing_balance",
                "experience_enrichment",
                "behavioral_harmony"
            ]
        }
    }]


def build_stability_state(
    continuity_profile
):
    return {
        "continuity_stable": (
            continuity_profile.get(
                "continuity_pressure"
            ) == "stable"
        ),

        "transition_flow_preserved": (
            not continuity_profile.get(
                "transition_instability_detected",
                False
            )
        ),

        "pacing_balance_preserved": (
            not continuity_profile.get(
                "pacing_fragmentation_detected",
                False
            )
        ),

        "collapse_protection_active": (
            not continuity_profile.get(
                "response_collapse_detected",
                False
            )
        ),

        "continuity_monitoring_active": (
            True
        ),

        "experience_stability_active": (
            True
        ),

        "north_star_alignment": (
            True
        ),

        "retrieval_stability_active": (
            True
        ),

        "orchestration_stability_active": (
            True
        )
    }


def build_continuity_router():
    return {
        "routing_identity": (
            "continuity_stabilization"
        ),

        "routing_active": (
            True
        ),

        "vault_access": (
            True
        ),

        "retrieval_enabled": (
            True
        ),

        "continuity_supervision": (
            True
        ),

        "enrichment_targets": [
            "nervous_system",
            "voice",
            "conversation_atmosphere",
            "behavioral_harmony",
            "relationship_awareness_engine",
            "surface_integrity_verification"
        ]
    }


def build_continuity_metadata():
    return {
        "continuity_version": (
            CONTINUITY_VERSION
        ),

        "continuity_timestamp": (
            datetime.now(
                UTC
            ).isoformat()
        )
    }


def stabilize_continuity(
    response,
    vault_resonance=None,
    continuity_context=None
):
    continuity_profile = {
        "response_collapse_detected": (
            detect_response_collapse(
                response
            )
        ),

        "transition_instability_detected": (
            detect_transition_instability(
                response
            )
        ),

        "pacing_fragmentation_detected": (
            detect_pacing_fragmentation(
                response
            )
        ),

        "orchestration_fragmentation": (
            False
        ),

        "vault_resonance": (
            vault_resonance or {}
        ),

        "continuity_context": (
            continuity_context or {}
        ),

        "experience_enrichment": (
            True
        ),

        "adaptive_stabilization": (
            True
        ),

        "north_star_alignment": (
            True
        )
    }

    continuity_profile[
        "continuity_pressure"
    ] = detect_continuity_pressure(
        continuity_profile
    )

    continuity_profile[
        "stability_state"
    ] = build_stability_state(
        continuity_profile
    )

    continuity_profile[
        "nervous_system_queries"
    ] = build_retrieval_queries(
        continuity_profile
    )

    continuity_profile[
        "mini_router"
    ] = build_continuity_router()

    continuity_profile[
        "continuity_metadata"
    ] = build_continuity_metadata()

    return {
        "response": (
            response
        ),

        "continuity_profile": (
            continuity_profile
        ),

        "stabilization_active": (
            True
        )
    }


def get_continuity_snapshot(
    response
):
    stabilized = (
        stabilize_continuity(
            response
        )
    )

    continuity_profile = stabilized.get(
        "continuity_profile",
        {}
    )

    return {
        "continuity_pressure": (
            continuity_profile.get(
                "continuity_pressure"
            )
        ),

        "stability_state": (
            continuity_profile.get(
                "stability_state"
            )
        ),

        "experience_enrichment": (
            continuity_profile.get(
                "experience_enrichment"
            )
        ),

        "north_star_alignment": (
            continuity_profile.get(
                "north_star_alignment"
            )
        ),

        "nervous_system_queries": (
            continuity_profile.get(
                "nervous_system_queries"
            )
        ),

        "mini_router": (
            continuity_profile.get(
                "mini_router"
            )
        ),

        "continuity_metadata": (
            continuity_profile.get(
                "continuity_metadata"
            )
        ),

        "response_length": (
            len(
                stabilized.get(
                    "response",
                    ""
                )
            )
        )
    }
