from core.base.base_engine import (
    BaseEngine
)


class Doorman(BaseEngine):

    def __init__(self):

        super().__init__(
            "doorman"
        )

    def process(
        self,
        message_object
    ):

        raw_message = (
            message_object.raw_message
            or ""
        ).strip()

        current_wave = (

            message_object.recursion_state[
                "current_wave"
            ]
        )

        lowered_message = (
            raw_message.lower()
        )

        signal_analysis = {

            "message_length":
                len(raw_message),

            "signal_presence":
                "active"
        }

        if "?" in raw_message:

            signal_analysis[
                "inquiry_signal"
            ] = "active"

        if raw_message.isupper():

            signal_analysis[
                "intensity_signal"
            ] = "active"

        if any(

            keyword in lowered_message

            for keyword in [

                "how",
                "why",
                "explain",
                "teach",
                "understand",
                "break down",
                "walk me through",
                "help me understand"
            ]
        ):

            signal_analysis[
                "understanding_signal"
            ] = "active"

        if any(

            keyword in lowered_message

            for keyword in [

                "build",
                "create",
                "design",
                "structure",
                "develop",
                "improve"
            ]
        ):

            signal_analysis[
                "construction_signal"
            ] = "active"

        if any(

            keyword in lowered_message

            for keyword in [

                "confused",
                "lost",
                "overwhelmed",
                "stuck",
                "frustrated",
                "uncertain"
            ]
        ):

            signal_analysis[
                "clarification_signal"
            ] = "active"

        if any(

            keyword in lowered_message

            for keyword in [

                "excited",
                "motivated",
                "confident",
                "focused",
                "clear"
            ]
        ):

            signal_analysis[
                "engagement_signal"
            ] = "active"

        signal_analysis[
            "signal_preservation_active"
        ] = True

        message_object.cognitive_state[
            "doorman"
        ] = signal_analysis

        message_object.enrichment_layers.append({

            "engine":
                self.engine_name,

            "wave":
                current_wave,

            "type":
                "signal_preservation",

            "content":
                signal_analysis
        })

        return message_object
