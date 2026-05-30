def detect_conversation_energy(
    adapted_reasoning
):

    atmosphere_profile = (
        adapted_reasoning.get(
            "atmosphere_profile",
            {}
        )
    )

    harmony_profile = (
        adapted_reasoning.get(
            "harmony_profile",
            {}
        )
    )

    behavioral_pressures = (
        harmony_profile.get(
            "behavioral_pressures",
            {}
        )
    )

    response_temperature = (
        behavioral_pressures.get(
            "response_temperature",
            "adaptive"
        )
    )

    pacing_style = (
        behavioral_pressures.get(
            "pacing_style",
            "natural"
        )
    )

    reasoning_mode = (
        behavioral_pressures.get(
            "reasoning_mode",
            "adaptive_reasoning"
        )
    )

    grounded_presence_active = (
        response_temperature == "grounded"
    )

    guided_pacing_active = (
        pacing_style == "guided"
    )

    structured_reasoning_active = (
        reasoning_mode == "structured_reasoning"
    )

    grounded_presence_active and (
        response_energy := "focused_grounded"
    )

    guided_pacing_active and (
        response_energy := "careful_collaborative"
    )

    structured_reasoning_active and (
        response_energy := "active_participation"
    )

    response_energy = locals().get(
        "response_energy",
        "natural_guided"
    )

    return response_energy


def detect_relational_presence(
    adapted_reasoning
):

    harmony_profile = (
        adapted_reasoning.get(
            "harmony_profile",
            {}
        )
    )

    behavioral_pressures = (
        harmony_profile.get(
            "behavioral_pressures",
            {}
        )
    )

    execution_alignment_active = (
        behavioral_pressures.get(
            "execution_alignment_active",
            False
        )
    )

    execution_alignment_active and (
        relational_presence := "immersive_with_user"
    )

    relational_presence = locals().get(
        "relational_presence",
        "direct_conversational"
    )

    return relational_presence


def build_retrieval_queries(
    atmosphere_profile
):

    return [{

        "access_type":
            "conversation_presence",

        "query": {

            "conversation_energy":
                atmosphere_profile.get(
                    "conversation_energy"
                ),

            "relational_presence":
                atmosphere_profile.get(
                    "relational_presence"
                ),

            "talking_style":
                atmosphere_profile.get(
                    "talking_style"
                ),

            "retrieval_focus": [

                "human_connection",
                "conversation_flow",
                "interaction_stability",
                "relational_continuity",
                "experience_enrichment"
            ]
        }
    }]


def build_conversation_state(
    atmosphere_profile
):

    return {

        "conversational_presence_active":
            True,

        "grounded_presence_preserved":
            atmosphere_profile.get(
                "maintain_grounded_presence",
                False
            ),

        "conversational_flow_preserved":
            atmosphere_profile.get(
                "maintain_conversational_flow",
                False
            ),

        "adaptive_breathing_preserved":
            atmosphere_profile.get(
                "preserve_adaptive_breathing",
                False
            ),

        "with_user_presence_active":
            atmosphere_profile.get(
                "talking_style"
            ) == "with_user_not_at_user",

        "experience_alignment_active":
            True,

        "vault_resonance_active":
            bool(
                atmosphere_profile.get(
                    "vault_resonance",
                    {}
                )
            )
    }


def build_conversation_router():

    return {

        "routing_identity":
            "conversation_presence",

        "routing_active":
            True,

        "vault_access":
            True,

        "retrieval_enabled":
            True,

        "enrichment_targets": [

            "nervous_system",
            "behavioral_harmony",
            "continuity_support",
            "voice"
        ]
    }


def build_atmosphere_profile(
    adapted_reasoning,
    vault_resonance=None
):

    atmosphere_profile = {

        "conversation_energy":
            detect_conversation_energy(
                adapted_reasoning
            ),

        "relational_presence":
            detect_relational_presence(
                adapted_reasoning
            ),

        "talking_style":
            "with_user_not_at_user",

        "maintain_grounded_presence":
            True,

        "maintain_conversational_flow":
            True,

        "preserve_adaptive_breathing":
            True,

        "vault_resonance":
            vault_resonance or {},

        "north_star_alignment":
            True,

        "experience_enrichment":
            True,

        "adaptive_presence":
            True
    }

    atmosphere_profile[
        "conversation_state"
    ] = build_conversation_state(
        atmosphere_profile
    )

    atmosphere_profile[
        "nervous_system_queries"
    ] = build_retrieval_queries(
        atmosphere_profile
    )

    atmosphere_profile[
        "mini_router"
    ] = build_conversation_router()

    return atmosphere_profile


def apply_conversation_atmosphere(
    adapted_reasoning,
    vault_resonance=None
):

    atmosphere_profile = (
        build_atmosphere_profile(
            adapted_reasoning,
            vault_resonance=vault_resonance
        )
    )

    return {

        "adapted_reasoning":
            adapted_reasoning,

        "atmosphere_profile":
            atmosphere_profile,

        "conversation_presence_active":
            True
    }


def get_atmosphere_snapshot(
    adapted_reasoning
):

    enriched = (
        apply_conversation_atmosphere(
            adapted_reasoning
        )
    )

    profile = enriched.get(
        "atmosphere_profile",
        {}
    )

    return {

        "conversation_energy":
            profile.get(
                "conversation_energy"
            ),

        "relational_presence":
            profile.get(
                "relational_presence"
            ),

        "talking_style":
            profile.get(
                "talking_style"
            ),

        "conversation_state":
            profile.get(
                "conversation_state"
            ),

        "experience_enrichment":
            profile.get(
                "experience_enrichment"
            ),

        "north_star_alignment":
            profile.get(
                "north_star_alignment"
            ),

        "nervous_system_queries":
            profile.get(
                "nervous_system_queries"
            ),

        "mini_router":
            profile.get(
                "mini_router"
            )
    }
