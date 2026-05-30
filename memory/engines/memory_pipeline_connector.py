from memory.engines.memory_integration import (
    MemoryIntegration
)


class MemoryPipelineConnector:

    def __init__(self):

        self.memory_integration = (
            MemoryIntegration()
        )

    def before_processing(
        self,
        message_object
    ):

        return (

            self.memory_integration.inject(
                message_object
            )
        )

    def after_processing(
        self,
        message_object,
        final_response
    ):

        self.memory_integration.finalize_cycle(

            message_object,

            final_response
        )
