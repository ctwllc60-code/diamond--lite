from core.base.base_engine import (
    BaseEngine
)


class RelationshipContent(BaseEngine):

    def __init__(self):

        super().__init__(
            "relationship_content"
        )

    def process(
        self,
        message_object
    ):

        raw_message = (
            message_object.raw_message
            or ""
        ).lower()

        current_wave = (

            message_object.recursion_state[
                "current_wave"
            ]
        )

        relationship_signals = []

        contextual_reference_hits = []

        recurring_patterns = [

            "diamond",
            "wagg",
            "memory",
            "continuity",
            "identity",
            "architecture",
            "system",
            "pipeline",
            "orchestration",
            "cognition",
            "alignment",
            "relationship",
            "building",
            "retrieval",
            "manifestation"
        ]

        contextual_references = [

            "we",
            "us",
            "together",
            "she",
            "her",
            "done"
        ]

        for pattern in recurring_patterns:

            if pattern in raw_message:

                relationship_signals.append(
                    pattern
                )

        for reference in contextual_references:

            if reference in raw_message:

                contextual_reference_hits.append(
                    reference
                )

        relationship_analysis = {

            "relationship_signals":
                relationship_signals,

            "contextual_references":
                contextual_reference_hits,

            "conceptual_resonance":
                len(
                    relationship_signals
                ),

            "relationship_alignment_active":
                True
        }

        if relationship_signals:

            relationship_analysis[
                "resonance_presence"
            ] = "active"

        message_object.cognitive_state[
            "relationship_content"
        ] = relationship_analysis

        message_object.enrichment_layers.append({

            "engine":
                self.engine_name,

            "wave":
                current_wave,

            "type":
                "relationship_alignment",

            "content":
                relationship_analysis
        })

        return message_object
