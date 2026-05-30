from core.base.base_engine import (
    BaseEngine
)

from memory.cognitive_memory import (
    CognitiveMemory
)


class MemoryIntegration(BaseEngine):

    def __init__(self):

        super().__init__(
            "memory_integration"
        )

        self.memory = (
            CognitiveMemory()
        )

    def process(
        self,
        message_object
    ):

        raw_message = (

            message_object.raw_message
            or ""

        ).strip().lower()

        current_wave = (

            message_object.recursion_state[
                "current_wave"
            ]
        )

        recent_reflections = (

            self.memory
            .retrieve_recent_reflections()
        )

        continuity_signals = []

        historical_topics = []

        matched_topics = []

        repetition_detected = False

        adaptive_variation_required = False

        for reflection in recent_reflections:

            reflection_message = (

                reflection.get(
                    "raw_message",
                    ""
                )
            )

            reflection_response = (

                reflection.get(
                    "final_response",
                    ""
                )
            )

            reflection_notes = (

                reflection.get(
                    "reflection_notes",
                    []
                )
            )

            if reflection_notes:

                continuity_signals.extend(
                    reflection_notes
                )

            if reflection_message:

                historical_topics.append(
                    reflection_message[:120]
                )

            lowered_reflection = (

                reflection_message
                .lower()
            )

            if (
                raw_message
                == lowered_reflection.strip()
            ):

                repetition_detected = True

            for word in raw_message.split():

                if (

                    len(word) > 4

                    and word in lowered_reflection
                ):

                    matched_topics.append(
                        word
                    )

        if repetition_detected:

            adaptive_variation_required = True

        continuity_relevance = (
            "low"
        )

        if len(
            matched_topics
        ) >= 3:

            continuity_relevance = (
                "moderate"
            )

        if len(
            matched_topics
        ) >= 7:

            continuity_relevance = (
                "high"
            )

        memory_analysis = {

            "recent_reflection_count":

                len(
                    recent_reflections
                ),

            "continuity_signals":
                continuity_signals,

            "historical_topics":
                historical_topics,

            "matched_topics":

                list(
                    set(
                        matched_topics
                    )
                ),

            "continuity_relevance":
                continuity_relevance,

            "repetition_detected":
                repetition_detected,

            "adaptive_variation_required":
                adaptive_variation_required,

            "memory_influence_active":
                True
        }

        message_object.cognitive_state[
            "memory_integration"
        ] = memory_analysis

        message_object.enrichment_layers.append({

            "engine":
                self.engine_name,

            "wave":
                current_wave,

            "type":
                "memory_continuity",

            "content":
                memory_analysis
        })

        return message_object
