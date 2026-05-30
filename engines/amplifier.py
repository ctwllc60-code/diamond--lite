from core.base.base_engine import (
    BaseEngine
)


class Amplifier(BaseEngine):

    def __init__(self):

        super().__init__(
            "amplifier"
        )

    def process(
        self,
        message_object
    ):

        raw = (
            message_object.raw_message
            or ""
        )

        previous_layers = len(
            message_object.enrichment_layers
        )

        amplification_analysis = {
            "word_count":
                len(raw.split()),

            "emotional_intensity":
                "medium",

            "depth_pressure":
                "increased",

            "previous_enrichment_layers_detected":
                previous_layers
        }

        message_object.enrichment_layers.append({
            "engine":
                self.engine_name,

            "wave":
                message_object.recursion_state[
                    "current_wave"
                ],

            "type":
                "cognitive_amplification",

            "content":
                amplification_analysis
        })

        return message_object
