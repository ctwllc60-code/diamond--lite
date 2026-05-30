import json
from datetime import (
    datetime,
    UTC
)

MEMORY_PATH = (
    "memory/foundation_memory.json"
)

DEFAULT_TOP_K = 10

RETRIEVAL_VERSION = (
    "diamond_retrieval_v2"
)


def load_memory():
    try:
        with open(
            MEMORY_PATH,
            "r"
        ) as file:
            return json.load(
                file
            )

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []

    except Exception:
        return []


def save_memory(
    memory
):
    with open(
        MEMORY_PATH,
        "w"
    ) as file:
        json.dump(
            memory,
            file,
            indent=4
        )


def normalize_text(
    text
):
    return (
        str(
            text or ""
        )
        .lower()
        .strip()
    )


def extract_nested_values(
    value
):
    extracted = []

    if isinstance(
        value,
        str
    ):
        extracted.append(
            value
        )

    elif isinstance(
        value,
        list
    ):
        for item in value:
            extracted.extend(
                extract_nested_values(
                    item
                )
            )

    elif isinstance(
        value,
        dict
    ):
        for nested in value.values():
            extracted.extend(
                extract_nested_values(
                    nested
                )
            )

    return extracted


def build_search_field(
    entry
):
    searchable = []

    for key, value in entry.items():
        searchable.extend(
            extract_nested_values(
                value
            )
        )

    return " ".join(
        [
            str(item)
            for item in searchable
        ]
    ).lower()


def score_memory_entry(
    entry,
    user_input,
    engine=None,
    continuity_context=None
):
    text = normalize_text(
        user_input
    )

    keywords = text.split()

    search_field = build_search_field(
        entry
    )

    score = 0

    for keyword in keywords:
        if keyword in search_field:
            score += 1

    score += entry.get(
        "retrieval_priority",
        1
    )

    score += entry.get(
        "recurring_strength",
        1
    )

    engine_routes = entry.get(
        "engine_routes",
        []
    )

    if (
        engine
        and engine in engine_routes
    ):
        score += 5

    continuity_tags = entry.get(
        "continuity_tags",
        []
    )

    for keyword in keywords:
        if keyword in continuity_tags:
            score += 3

    relationship_groups = entry.get(
        "relationship_groups",
        []
    )

    for keyword in keywords:
        if keyword in relationship_groups:
            score += 2

    if continuity_context:
        active_tags = continuity_context.get(
            "active_tags",
            []
        )

        for tag in active_tags:
            if tag in continuity_tags:
                score += 4

    return score


def retrieve_relevant_memory(
    user_input,
    engine=None,
    top_k=DEFAULT_TOP_K,
    continuity_context=None
):
    memory = load_memory()

    scored = []

    for entry in memory:

        score = score_memory_entry(
            entry=entry,
            user_input=user_input,
            engine=engine,
            continuity_context=continuity_context
        )

        if score > 0:
            scored.append(
                (
                    score,
                    entry
                )
            )

    scored.sort(
        key=lambda x: x[0],
        reverse=True
    )

    return [
        item[1]
        for item in scored[:top_k]
    ]


def deduplicate(
    values
):
    return list(
        dict.fromkeys(
            [
                str(v)
                for v in values
            ]
        )
    )


def build_cognitive_context(
    user_input,
    engine=None,
    continuity_context=None
):
    retrieved = retrieve_relevant_memory(
        user_input=user_input,
        engine=engine,
        continuity_context=continuity_context
    )

    cognitive_context = {
        "retrieved_frameworks": [],
        "identity_principles": [],
        "behavioral_reinforcements": [],
        "continuity_tags": [],
        "experience_enrichment": [],
        "governance_principles": [],
        "assistant_role": [],
        "operational_requirements": [],
        "communication_preferences": [],
        "clarity_rules": [],
        "preservation_rules": [],
        "execution_flow_rules": [],
        "voice_characteristics": [],
        "foundational_insights": [],
        "systems_alignment": [],
        "relationship_model": [],
        "engine_access_guidance": [],
        "retrieval_boundaries": [],
        "state_adaptation": [],
        "feedback_triggers": [],
        "stabilization_patterns": [],
        "pressure_patterns": [],
        "voice_patterns": [],
        "experience_categories": [],
        "failure_handling": [],
        "success_handling": [],
        "strategic_queries": [],
        "layer_architecture": [],
        "application_domains": [],
        "system_behaviors": [],
        "design_philosophy": [],
        "core_objectives": [],
        "experience_preservation_principles": [],
        "cooperative_specialization_model": [],
        "system_constraints": [],
        "relationship_groups": [],
        "identity_examples": [],
        "execution_examples": [],
        "communication_examples": [],
        "reasoning_examples": []
    }

    for entry in retrieved:

        cognitive_context[
            "retrieved_frameworks"
        ].append(
            entry.get(
                "input",
                ""
            )
        )

        for key in cognitive_context.keys():

            if key == "retrieved_frameworks":
                continue

            if key in entry:

                extracted = extract_nested_values(
                    entry[key]
                )

                cognitive_context[
                    key
                ].extend(
                    extracted
                )

        if "output" in entry:
            cognitive_context[
                "reasoning_examples"
            ].append(
                entry[
                    "output"
                ]
            )

        if "voice_patterns" in entry:
            cognitive_context[
                "communication_examples"
            ].extend(
                extract_nested_values(
                    entry[
                        "voice_patterns"
                    ]
                )
            )

        if "behavioral_reinforcements" in entry:
            cognitive_context[
                "execution_examples"
            ].extend(
                entry[
                    "behavioral_reinforcements"
                ]
            )

        if "identity_principles" in entry:
            cognitive_context[
                "identity_examples"
            ].extend(
                entry[
                    "identity_principles"
                ]
            )

    for key in cognitive_context.keys():

        cognitive_context[
            key
        ] = deduplicate(
            cognitive_context[
                key
            ]
        )

    cognitive_context[
        "retrieval_metadata"
    ] = {
        "retrieval_version": (
            RETRIEVAL_VERSION
        ),
        "retrieval_timestamp": (
            datetime.now(
                UTC
            ).isoformat()
        ),
        "retrieved_count": (
            len(
                retrieved
            )
        ),
        "engine": (
            engine
        )
    }

    return cognitive_context


def inject_cognitive_context(
    payload,
    user_input,
    engine,
    continuity_context=None
):
    cognitive_context = build_cognitive_context(
        user_input=user_input,
        engine=engine,
        continuity_context=continuity_context
    )

    payload[
        "cognitive_context"
    ] = cognitive_context

    payload[
        "retrieval_active"
    ] = True

    payload[
        "retrieval_engine"
    ] = engine

    payload[
        "retrieved_frameworks"
    ] = cognitive_context.get(
        "retrieved_frameworks",
        []
    )

    payload[
        "retrieval_metadata"
    ] = cognitive_context.get(
        "retrieval_metadata",
        {}
    )

    return payload
