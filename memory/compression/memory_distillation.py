from datetime import (
    datetime,
    UTC
)


DISTILLATION_LIMIT = 400

DISTILLATION_VERSION = (
    "diamond_distillation_v3"
)


def normalize_text(
    text
):

    return str(
        text or ""
    ).strip()


def detect_core_patterns(
    text
):

    lowered = text.lower()

    detected_patterns = []

    pattern_map = {

        "clarity_preference": [

            "clarity",

            "structured",

            "full response",

            "complete answer",

            "clean explanation"
        ],

        "continuity_preference": [

            "continuity",

            "connected",

            "flow",

            "progression",

            "remember"
        ],

        "experience_preference": [

            "experience",

            "feeling",

            "smooth",

            "natural",

            "immersive"
        ],

        "systems_thinking": [

            "system",

            "architecture",

            "pipeline",

            "engine",

            "structure"
        ],

        "relationship_signal": [

            "trust",

            "understand me",

            "alignment",

            "together",

            "connection"
        ],

        "governance_awareness": [

            "validation",

            "governance",

            "rules",

            "stability",

            "protection"
        ],

        "retrieval_awareness": [

            "memory",

            "retrieve",

            "vault",

            "continuity tags",

            "framework"
        ],

        "creative_variation_preference": [

            "creative",

            "variation",

            "non repetitive",

            "not repetitive",

            "switch it up",

            "different response"
        ]
    }

    for category, patterns in (

        pattern_map.items()
    ):

        if any(

            pattern in lowered

            for pattern in patterns
        ):

            detected_patterns.append(
                category
            )

    return detected_patterns


def extract_distilled_understanding(
    entry
):

    input_text = normalize_text(

        entry.get(
            "input",
            ""
        )
    )

    output_text = normalize_text(

        entry.get(
            "output",
            ""
        )
    )

    combined = (

        input_text
        + "\n"
        + output_text
    )

    detected_patterns = (

        detect_core_patterns(
            combined
        )
    )

    distilled_points = []

    if (
        "clarity_preference"
        in detected_patterns
    ):

        distilled_points.append(

            "User values clarity, structure, and complete responses."
        )

    if (
        "continuity_preference"
        in detected_patterns
    ):

        distilled_points.append(

            "User prefers connected continuity and progression awareness."
        )

    if (
        "experience_preference"
        in detected_patterns
    ):

        distilled_points.append(

            "User prioritizes smooth and immersive interaction flow."
        )

    if (
        "systems_thinking"
        in detected_patterns
    ):

        distilled_points.append(

            "User thinks through systems, structure, and architecture."
        )

    if (
        "relationship_signal"
        in detected_patterns
    ):

        distilled_points.append(

            "Relationship alignment and understanding are important."
        )

    if (
        "governance_awareness"
        in detected_patterns
    ):

        distilled_points.append(

            "Governance, validation, and stability systems are important."
        )

    if (
        "retrieval_awareness"
        in detected_patterns
    ):

        distilled_points.append(

            "Memory retrieval and continuity-aware cognition are prioritized."
        )

    if (
        "creative_variation_preference"
        in detected_patterns
    ):

        distilled_points.append(

            "User prefers creative conversational variation while preserving meaning continuity."
        )

    if not distilled_points:

        distilled_points.append(

            "General continuity signal preserved."
        )

    return distilled_points


def build_distillation_metadata():

    return {

        "distillation_version":
            DISTILLATION_VERSION,

        "distillation_timestamp":

            datetime.now(
                UTC
            ).isoformat()
    }


def compress_memory_entry(
    entry
):

    distilled_understanding = (

        extract_distilled_understanding(
            entry
        )
    )

    compressed_text = " ".join(
        distilled_understanding
    )

    if len(
        compressed_text
    ) > DISTILLATION_LIMIT:

        compressed_text = (

            compressed_text[
                :DISTILLATION_LIMIT
            ]

            + "..."
        )

    return {

        "distilled_understanding":
            distilled_understanding,

        "continuity_tags":

            entry.get(
                "continuity_tags",
                []
            ),

        "relationship_groups":

            entry.get(
                "relationship_groups",
                []
            ),

        "memory_type":

            entry.get(
                "memory_type",
                "general_memory"
            ),

        "retrieval_priority":

            entry.get(
                "retrieval_priority",
                1
            ),

        "recurring_strength":

            entry.get(
                "recurring_strength",
                1
            ),

        "creative_variation_preference":

            "creative_variation_preference"
            in distilled_understanding,

        "distillation_metadata":
            build_distillation_metadata()
    }


def distill_memory(
    entry
):

    compressed_entry = (

        compress_memory_entry(
            entry
        )
    )

    return {

        "distilled_memory":
            compressed_entry,

        "distillation_complete":
            True
    }


def get_distillation_snapshot(
    entry
):

    result = distill_memory(
        entry
    )

    distilled = result.get(
        "distilled_memory",
        {}
    )

    return {

        "distilled_points":

            distilled.get(
                "distilled_understanding",
                []
            ),

        "continuity_tags":

            distilled.get(
                "continuity_tags",
                []
            ),

        "relationship_groups":

            distilled.get(
                "relationship_groups",
                []
            ),

        "memory_type":

            distilled.get(
                "memory_type",
                "general_memory"
            ),

        "distillation_metadata":

            distilled.get(
                "distillation_metadata",
                {}
            ),

        "distillation_complete":

            result.get(
                "distillation_complete",
                False
            )
    }
