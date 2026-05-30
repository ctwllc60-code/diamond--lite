from core.base_engine import BaseEngine

from memory.cognitive_memory import (
    CognitiveMemory
)

class MemoryIntegration(BaseEngine):

    def __init__(self):

        super().__init__(
            "memory_integration"
        )

        self.memory = CognitiveMemory()

    def process(self, message_object):

        recent_reflections = (
            self.memory
            .retrieve_recent_reflections()
        )

        continuity_signals = []

        for reflection in recent_reflections:

            notes = reflection.get(
                "reflection_notes",
                []
            )

            continuity_signals.extend(notes)

        continuity_analysis = {
            "recent_reflection_count":
                len(recent_reflections),

            "continuity_signals":
                continuity_signals,

            "memory_influence_active":
                True
        }

        message_object.cognitive_state[
            "continuity_signals"
        ] = continuity_signals

        message_object.enrichment_layers.append({
            "engine": self.engine_name,
            "wave":
                message_object.recursion_state[
                    "current_wave"
                ],
            "type": "memory_continuity",
            "content": continuity_analysis
        })

        return message_object
