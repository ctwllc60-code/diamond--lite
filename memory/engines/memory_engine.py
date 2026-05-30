from memory.engines.memory_bridge import (
    MemoryBridge
)


class MemoryEngine:

    def __init__(self):

        self.memory_bridge = (
            MemoryBridge()
        )

    def process(
        self,
        message_object,
        final_response=None
    ):

        message_object = (
            self.memory_bridge.inject_memory(
                message_object
            )
        )

        if final_response:

            self.memory_bridge.process_cycle(

                message_object.raw_message,

                final_response
            )

        return message_object
