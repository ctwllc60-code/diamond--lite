from datetime import (
    datetime,
    UTC
)


RELATIONSHIP_ENGINE_VERSION = (
    "diamond_relationship_v2"
)


def build_relationship_state():
    return {
        "recognized_patterns": [],
        "active_journeys": [],
        "unfinished_paths": [],
        "recurring_topics": [],
        "continuity_links": [],
        "relationship_strength": 0,
        "journey_continuity": "emerging",
        "continuity_pressure": "stable",
        "relationship_temperature": "open",
        "relationship_alignment": "stable",
        "last_interaction": None
    }


def normalize_text(
    text
):
    return str(
        text or ""
    ).lower().strip()


def extract_relationship_terms(
    text
):
    return [
        word.strip(
            ".,!?()[]{}:;"
        )

        for word in normalize_text(
            text
        ).split()

        if len(word) > 4
    ]


def detect_relationship_patterns(
    current_input,
    previous_entries
):
    current_terms = (
        extract_relationship_terms(
            current_input
        )
    )

    relationship_patterns = []

    for entry in previous_entries:

        previous_text = normalize_text(
            entry.get(
                "input",
                ""
            )
        )

        if not previous_text:
            continue

        shared_terms = []

        for term in current_terms:

            if term in previous_text:
                shared_terms.append(
                    term
                )

        if shared_terms:

            relationship_patterns.append({
                "shared_terms": (
                    list(
                        set(
                            shared_terms
                        )
                    )
                ),

                "previous_topic": (
                    entry.get(
                        "input",
                        ""
                    )
                ),

                "timestamp": (
                    entry.get(
                        "timestamp"
                    )
                ),

                "continuity_detected": (
                    True
                ),

                "relationship_resonance": (
                    len(
                        shared_terms
                    )
                )
            })

    return relationship_patterns


def identify_unfinished_paths(
    relationship_patterns
):
    unfinished_paths = []

    for pattern in relationship_patterns:

        continuity_strength = len(
            pattern.get(
                "shared_terms",
                []
            )
        )

        unfinished_paths.append({
            "pathway": (
                pattern.get(
                    "previous_topic",
                    ""
                )
            ),

            "continuity_strength": (
                continuity_strength
            ),

            "continuation_ready": (
                continuity_strength >= 2
            ),

            "relationship_weight": (
                "high"
                if continuity_strength >= 4
                else "moderate"
            )
        })

    return unfinished_paths


def detect_recurring_topics(
    relationship_patterns
):
    recurring_topics = []

    for pattern in relationship_patterns:

        recurring_topics.extend(
            pattern.get(
                "shared_terms",
                []
            )
        )

    return list(
        set(
            recurring_topics
        )
    )


def determine_relationship_depth(
    relationship_strength
):
    if relationship_strength >= 6:
        return "deeply_established"

    if relationship_strength >= 3:
        return "established"

    if relationship_strength >= 1:
        return "developing"

    return "new"


def determine_relationship_temperature(
    relationship_strength
):
    if relationship_strength >= 6:
        return "deeply_connected"

    if relationship_strength >= 3:
        return "warm"

    if relationship_strength >= 1:
        return "open"

    return "neutral"


def determine_continuity_pressure(
    unfinished_paths
):
    if len(
        unfinished_paths
    ) >= 5:
        return "high"

    if len(
        unfinished_paths
    ) >= 2:
        return "active"

    return "stable"


def determine_relationship_alignment(
    relationship_strength,
    continuity_pressure
):
    if (
        relationship_strength >= 5
        and continuity_pressure != "high"
    ):
        return "strong_alignment"

    if relationship_strength >= 2:
        return "stable_alignment"

    return "emerging_alignment"


def build_relationship_router(
    relationship_state
):
    enrichment_routes = []

    relationship_strength = (
        relationship_state.get(
            "relationship_strength",
            0
        )
    )

    unfinished_paths = (
        relationship_state.get(
            "unfinished_paths",
            []
        )
    )

    recurring_topics = (
        relationship_state.get(
            "recurring_topics",
            []
        )
    )

    continuity_pressure = (
        relationship_state.get(
            "continuity_pressure",
            "stable"
        )
    )

    if relationship_strength >= 3:

        enrichment_routes.extend([
            "memory_reasoning",
            "continuity_stabilizer",
            "conversation_atmosphere"
        ])

    if unfinished_paths:
        enrichment_routes.append(
            "meaning_builder"
        )

    if recurring_topics:
        enrichment_routes.append(
            "memory_flow"
        )

    if continuity_pressure in [
        "active",
        "high"
    ]:
        enrichment_routes.append(
            "behavioral_harmony"
        )

    return {
        "enrichment_routes": (
            enrichment_routes
        ),

        "routing_active": (
            bool(
                enrichment_routes
            )
        ),

        "relationship_priority": (
            "high"
            if relationship_strength >= 5
            else "standard"
        ),

        "continuity_support_active": (
            True
        )
    }


def build_relationship_metadata():
    return {
        "relationship_engine_version": (
            RELATIONSHIP_ENGINE_VERSION
        ),

        "relationship_timestamp": (
            datetime.now(
                UTC
            ).isoformat()
        )
    }


def build_relationship_awareness(
    current_input,
    previous_entries
):
    relationship_state = (
        build_relationship_state()
    )

    relationship_patterns = (
        detect_relationship_patterns(
            current_input,
            previous_entries
        )
    )

    unfinished_paths = (
        identify_unfinished_paths(
            relationship_patterns
        )
    )

    recurring_topics = (
        detect_recurring_topics(
            relationship_patterns
        )
    )

    relationship_strength = len(
        relationship_patterns
    )

    relationship_state[
        "recognized_patterns"
    ] = relationship_patterns

    relationship_state[
        "unfinished_paths"
    ] = unfinished_paths

    relationship_state[
        "recurring_topics"
    ] = recurring_topics

    relationship_state[
        "relationship_strength"
    ] = relationship_strength

    relationship_state[
        "journey_continuity"
    ] = determine_relationship_depth(
        relationship_strength
    )

    relationship_state[
        "relationship_temperature"
    ] = determine_relationship_temperature(
        relationship_strength
    )

    relationship_state[
        "continuity_pressure"
    ] = determine_continuity_pressure(
        unfinished_paths
    )

    relationship_state[
        "relationship_alignment"
    ] = determine_relationship_alignment(
        relationship_strength,
        relationship_state.get(
            "continuity_pressure"
        )
    )

    relationship_state[
        "last_interaction"
    ] = datetime.now(
        UTC
    ).isoformat()

    relationship_state[
        "relationship_metadata"
    ] = build_relationship_metadata()

    relationship_state[
        "mini_router"
    ] = build_relationship_router(
        relationship_state
    )

    return relationship_state


def get_relationship_snapshot(
    relationship_state
):
    return {
        "recognized_patterns": (
            len(
                relationship_state.get(
                    "recognized_patterns",
                    []
                )
            )
        ),

        "unfinished_paths": (
            len(
                relationship_state.get(
                    "unfinished_paths",
                    []
                )
            )
        ),

        "relationship_strength": (
            relationship_state.get(
                "relationship_strength",
                0
            )
        ),

        "journey_continuity": (
            relationship_state.get(
                "journey_continuity"
            )
        ),

        "relationship_temperature": (
            relationship_state.get(
                "relationship_temperature"
            )
        ),

        "relationship_alignment": (
            relationship_state.get(
                "relationship_alignment"
            )
        ),

        "continuity_pressure": (
            relationship_state.get(
                "continuity_pressure"
            )
        ),

        "relationship_metadata": (
            relationship_state.get(
                "relationship_metadata"
            )
        ),

        "mini_router": (
            relationship_state.get(
                "mini_router"
            )
        )
    }
