from core.base.base_engine import (
    BaseEngine
)


class ConvictionIgniter(BaseEngine):

    def __init__(self):

        super().__init__(
            "conviction_igniter"
        )

    def process(
        self,
        message_object
    ):

        raw_message = (
            message_object.raw_message
            or ""
        ).lower()

        conviction_profile = {

            "level":
                "grounded",

            "voice_alignment":
                "assertive",

            "presence_alignment":
                "grounded",

            "confidence_alignment_active":
                True,

            "certainty_alignment_active":
                True,

            "delivery_alignment_active":
                True,

            "clarity_alignment_active":
                True,

            "conviction_alignment_active":
                True
        }

        if (
            "conviction: high"
            in raw_message
        ):

            conviction_profile[
                "level"
            ] = "elevated"

        if (
            "conviction: max"
            in raw_message
        ):

            conviction_profile[
                "level"
            ] = "maximum"

        message_object.cognitive_state[
            "conviction_profile"
        ] = conviction_profile

        message_object.enrichment_layers.append({

            "engine":
                self.engine_name,

            "wave":
                message_object.recursion_state[
                    "current_wave"
                ],

            "type":
                "conviction_alignment",

            "content":
                conviction_profile
        })

        return message_object
