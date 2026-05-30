from memory.engines.memory_pipeline_connector import (
    MemoryPipelineConnector
)


class MemoryRuntime:

    def __init__(self):

        self.pipeline_connector = (
            MemoryPipelineConnector()
        )

    def initialize(
        self
    ):

        return {

            "memory_runtime":
                "active",

            "pipeline_connected":
                True
        }

    def inject_before_cycle(
        self,
        message_object
    ):

        return (

            self.pipeline_connector.before_processing(
                message_object
            )
        )

    def finalize_after_cycle(
        self,
        message_object,
        final_response
    ):

        self.pipeline_connector.after_processing(

            message_object,

            final_response
        )
