from abc import ABC, abstractmethod
import traceback


class BaseEngine(ABC):

    def __init__(
        self,
        engine_name
    ):

        self.engine_name = (
            engine_name
        )

    @abstractmethod
    def process(
        self,
        message_object
    ):

        pass

    def protected_process(
        self,
        message_object
    ):

        try:

            result = (
                self.process(
                    message_object
                )
            )

            return result

        except Exception as error:

            failure_trace = (
                traceback.format_exc()
            )

            failure_layer = {

                "engine":
                    self.engine_name,

                "wave":
                    message_object.recursion_state.get(
                        "current_wave",
                        0
                    ),

                "type":
                    "engine_failure",

                "content": {

                    "failure_detected":
                        True,

                    "engine_name":
                        self.engine_name,

                    "error":
                        str(error),

                    "trace":
                        failure_trace,

                    "pipeline_continuation":
                        True,

                    "resilience_layer_active":
                        True
                }
            }

            message_object.enrichment_layers.append(
                failure_layer
            )

            if not getattr(
                message_object,
                "final_response",
                None
            ):

                message_object.final_response = (

                    "A temporary internal processing disruption occurred, but the system remained operational."
                )

            return message_object
