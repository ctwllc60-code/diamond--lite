from core.base.base_engine import (
    BaseEngine
)


class SynthesisCoordinator(BaseEngine):

    def __init__(self):

        super().__init__(
            "synthesis_coordinator"
        )

    def process(
        self,
        message_object
    ):

        current_wave = (

            message_object.recursion_state[
                "current_wave"
            ]
        )

        raw_message = (
            message_object.raw_message
            or ""
        )

        enrichment_layers = (
            message_object.enrichment_layers
        )

        active_reasoning_stream = []

        synthesis_signals = []

        for layer in enrichment_layers:

            layer_engine = (

                layer.get(
                    "engine",
                    "unknown_engine"
                )
            )

            layer_type = (

                layer.get(
                    "type",
                    "general"
                )
            )

            layer_content = (

                layer.get(
                    "content",
                    {}
                )
            )

            active_reasoning_stream.append({

                "engine":
                    layer_engine,

                "type":
                    layer_type,

                "content":
                    layer_content
            })

            content_string = str(
                layer_content
            ).lower()

            if (
                "continuity"
                in content_string
            ):

                synthesis_signals.append(
                    "continuity"
                )

            if (
                "relationship"
                in content_string
            ):

                synthesis_signals.append(
                    "relationship"
                )

            if (
                "depth"
                in content_string
            ):

                synthesis_signals.append(
                    "depth"
                )

            if (
                "reasoning"
                in content_string
            ):

                synthesis_signals.append(
                    "reasoning"
                )

            if (
                "pipeline"
                in content_string
            ):

                synthesis_signals.append(
                    "pipeline"
                )

        synthesis_package = {

            "raw_message":
                raw_message,

            "wave":
                current_wave,

            "active_reasoning_stream":
                active_reasoning_stream,

            "synthesis_signals":
                synthesis_signals,

            "living_cognition":
                True
        }

        message_object.cognitive_state[
            "synthesis_coordinator"
        ] = synthesis_package

        message_object.enrichment_layers.append({

            "engine":
                self.engine_name,

            "wave":
                current_wave,

            "type":
                "cognition_synthesis",

            "content": {

                "living_cognition":
                    True,

                "synthesis_signals":
                    synthesis_signals
            }
        })

        return message_object
