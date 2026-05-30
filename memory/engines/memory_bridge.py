from memory.engines.memory_coordinator import (
    MemoryCoordinator
)


class MemoryBridge:

    def __init__(self):

        self.memory_coordinator = (
            MemoryCoordinator()
        )

    def inject_memory(
        self,
        message_object
    ):

        memory_state = (

            self.memory_coordinator.retrieve_memory_state()
        )

        message_object.cognitive_state[
            "memory"
        ] = memory_state

        return message_object

    def process_cycle(
        self,
        raw_message,
        final_response
    ):

        self.memory_coordinator.process_interaction(

            raw_message,

            final_response
        )
