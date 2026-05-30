from memory.engines.memory_engine import (
    MemoryEngine
)

from memory.engines.memory_state_manager import (
    MemoryStateManager
)


class MemoryIntegration:

    def __init__(self):

        self.memory_engine = (
            MemoryEngine()
        )

        self.state_manager = (
            MemoryStateManager()
        )

    def process(
        self,
        message_object
    ):

        message_object = (

            self.memory_engine.process(
                message_object
            )
        )

        memory_state = (
            self.state_manager.retrieve_state()
        )

        message_object.cognitive_state[
            "memory_state"
        ] = memory_state

        enrichment_content = {

            "memory_connected":
                True,

            "continuity_enrichment_active":
                True
        }

        if memory_state:

            enrichment_content[
                "memory_state_available"
            ] = True

        message_object.enrichment_layers.append({

            "engine":
                "memory_integration",

            "wave":
                message_object.recursion_state[
                    "current_wave"
                ],

            "type":
                "memory_enrichment",

            "content":
                enrichment_content
        })

        return message_object

    def finalize_cycle(
        self,
        message_object,
        final_response
    ):

        self.memory_engine.process(
            message_object,
            final_response
        )
