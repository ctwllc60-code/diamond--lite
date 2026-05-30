from datetime import (
    datetime,
    UTC
)


BEHAVIORAL_HARMONY_VERSION = (
    "diamond_behavioral_harmony_v2"
)


def detect_behavioral_pressures(
    atmosphere_enriched
):
    adapted_reasoning = (
        atmosphere_enriched.get(
            "adapted_reasoning",
            {}
        )
    )

    behavioral_directives = (
        adapted_reasoning.get(
            "behavioral_directives",
            {}
        )
    )

    atmosphere_profile = (
        atmosphere_enriched.get(
            "atmosphere_profile",
            {}
        )
    )

    pressures = {
        "execution_pressure": (
            behavioral_directives.get(
                "preserve_execution_momentum",
                False
            )
        ),

        "narrative_drift_pressure": (
            behavioral_directives.get(
                "reduce_narrative_drift",
                False
            )
        ),

        "depth_pressure": (
            behavioral_directives.get(
                "depth_intensity",
                "standard"
            )
        ),

        "response_temperature": (
            atmosphere_profile.get(
                "response_temperature",
                "balanced"
            )
        ),

        "pacing_style": (
            atmosphere_profile.get(
                "pacing_style",
                "natural"
            )
        ),

        "breathing_room": (
            atmosphere_profile.get(
                "breathing_room",
                "balanced"
            )
        ),

        "reasoning_mode": (
            behavioral_directives.get(
                "reasoning_mode",
                "adaptive_general"
            )
        )
    }

    return pressures


def balance_behavioral_pressures(
    pressures
):
    harmony_rules = {
        "preserve_emergence": True,
        "preserve_behavioral_identity": True,
        "prevent_behavioral_domination": True,
        "maintain_experiential_balance": True,
        "maintain_reasoning_balance": True,
        "maintain_narrative_breathing_room": True,
        "preserve_grounded_delivery": True,
        "preserve_response_cohesion": True
    }

    if pressures.get(
        "depth_pressure"
    ) == "deep":

        harmony_rules[
            "prevent_over_expansion"
        ] = True

    if pressures.get(
        "execution_pressure"
    ):

        harmony_rules[
            "preserve_natural_flow"
        ] = True

    if pressures.get(
        "narrative_drift_pressure"
    ):

        harmony_rules[
            "preserve_structural_alignment"
        ] = True

    if pressures.get(
        "breathing_room"
    ) == "protective":

        harmony_rules[
            "reduce_response_overload"
        ] = True

    return harmony_rules


def build_nervous_system_queries(
    pressures,
    harmony_rules
):
    nervous_system_queries = []

    nervous_system_queries.append({
        "resonance_type": (
            "behavioral_stabilization"
        ),

        "query": {
            "depth_pressure": (
                pressures.get(
                    "depth_pressure"
                )
            ),

            "response_temperature": (
                pressures.get(
                    "response_temperature"
                )
            ),

            "pacing_style": (
                pressures.get(
                    "pacing_style"
                )
            ),

            "breathing_room": (
                pressures.get(
                    "breathing_room"
                )
            ),

            "execution_pressure": (
                pressures.get(
                    "execution_pressure"
                )
            ),

            "narrative_drift_pressure": (
                pressures.get(
                    "narrative_drift_pressure"
                )
            ),

            "active_harmony_rules": (
                list(
                    harmony_rules.keys()
                )
            )
        }
    })

    return nervous_system_queries


def build_harmony_state(
    pressures,
    harmony_rules
):
    return {
        "behavioral_balance_active": (
            True
        ),

        "preserve_behavioral_identity": (
            harmony_rules.get(
                "preserve_behavioral_identity",
                False
            )
        ),

        "preserve_natural_flow": (
            harmony_rules.get(
                "preserve_natural_flow",
                False
            )
        ),

        "preserve_structural_alignment": (
            harmony_rules.get(
                "preserve_structural_alignment",
                False
            )
        ),

        "reduce_response_overload": (
            harmony_rules.get(
                "reduce_response_overload",
                False
            )
        ),

        "maintain_narrative_breathing_room": (
            harmony_rules.get(
                "maintain_narrative_breathing_room",
                False
            )
        ),

        "preserve_response_cohesion": (
            harmony_rules.get(
                "preserve_response_cohesion",
                False
            )
        )
    }


def build_harmony_router(
    harmony_rules
):
    enrichment_routes = []

    if harmony_rules.get(
        "preserve_structural_alignment"
    ):
        enrichment_routes.append(
            "continuity_stabilizer"
        )

    if harmony_rules.get(
        "reduce_response_overload"
    ):
        enrichment_routes.append(
            "atmosphere_condition"
        )

    if harmony_rules.get(
        "preserve_response_cohesion"
    ):
        enrichment_routes.append(
            "surface_integrity_verification"
        )

    return {
        "routing_active": (
            bool(
                enrichment_routes
            )
        ),

        "enrichment_routes": (
            enrichment_routes
        ),

        "behavioral_supervision_active": (
            True
        )
    }


def build_harmony_metadata():
    return {
        "behavioral_harmony_version": (
            BEHAVIORAL_HARMONY_VERSION
        ),

        "behavioral_harmony_timestamp": (
            datetime.now(
                UTC
            ).isoformat()
        )
    }


def build_harmony_profile(
    atmosphere_enriched
):
    pressures = (
        detect_behavioral_pressures(
            atmosphere_enriched
        )
    )

    harmony_rules = (
        balance_behavioral_pressures(
            pressures
        )
    )

    nervous_system_queries = (
        build_nervous_system_queries(
            pressures,
            harmony_rules
        )
    )

    harmony_state = (
        build_harmony_state(
            pressures,
            harmony_rules
        )
    )

    harmony_profile = {
        "behavioral_pressures": (
            pressures
        ),

        "harmony_rules": (
            harmony_rules
        ),

        "harmony_state": (
            harmony_state
        ),

        "nervous_system_queries": (
            nervous_system_queries
        ),

        "mini_router": (
            build_harmony_router(
                harmony_rules
            )
        ),

        "harmony_metadata": (
            build_harmony_metadata()
        )
    }

    return harmony_profile


def apply_behavioral_harmony(
    atmosphere_enriched
):
    harmony_profile = (
        build_harmony_profile(
            atmosphere_enriched
        )
    )

    return {
        "atmosphere_enriched": (
            atmosphere_enriched
        ),

        "harmony_profile": (
            harmony_profile
        )
    }


def get_harmony_snapshot(
    atmosphere_enriched
):
    harmonized = (
        apply_behavioral_harmony(
            atmosphere_enriched
        )
    )

    harmony_profile = harmonized.get(
        "harmony_profile",
        {}
    )

    return {
        "behavioral_pressures": (
            harmony_profile.get(
                "behavioral_pressures"
            )
        ),

        "harmony_rules": (
            harmony_profile.get(
                "harmony_rules"
            )
        ),

        "harmony_state": (
            harmony_profile.get(
                "harmony_state"
            )
        ),

        "nervous_system_queries": (
            harmony_profile.get(
                "nervous_system_queries"
            )
        ),

        "harmony_metadata": (
            harmony_profile.get(
                "harmony_metadata"
            )
        ),

        "mini_router": (
            harmony_profile.get(
                "mini_router"
            )
        )
    }
