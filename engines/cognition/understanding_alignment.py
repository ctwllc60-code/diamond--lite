from core.base.base_engine import (
    BaseEngine
)


class UnderstandingAlignment(BaseEngine):

    def __init__(self):

        super().__init__(
            "understanding_alignment"
        )

    def process(
        self,
        message_object
    ):

        raw_message = (
            message_object.raw_message
            or ""
        ).lower()

        current_wave = (

            message_object.recursion_state[
                "current_wave"
            ]
        )

        active_intentions = []

        understanding_analysis = {

            "active_intentions":
                active_intentions,

            "understanding_alignment_active":
                True
        }

        if any(

            keyword in raw_message

            for keyword in [

                "why",
                "meaning",
                "purpose",
                "understand",
                "explain",
                "depth"
            ]
        ):

            active_intentions.append(
                "deep_exploration"
            )

            understanding_analysis[
                "exploration_alignment"
            ] = "active"

            understanding_analysis[
                "conceptual_alignment"
            ] = "active"

        if any(

            keyword in raw_message

            for keyword in [

                "relationship",
                "alignment",
                "continuity",
                "presence",
                "connection"
            ]
        ):

            active_intentions.append(
                "relational_continuity"
            )

            understanding_analysis[
                "relationship_alignment"
            ] = "active"

        if any(

            keyword in raw_message

            for keyword in [

                "confused",
                "unclear",
                "lost",
                "stuck"
            ]
        ):

            active_intentions.append(
                "clarification_support"
            )

            understanding_analysis[
                "clarification_alignment"
            ] = "active"

        message_object.cognitive_state[
            "understanding_alignment"
        ] = understanding_analysis

        message_object.enrichment_layers.append({

            "engine":
                self.engine_name,

            "wave":
                current_wave,

            "type":
                "understanding_alignment",

            "content":
                understanding_analysis
        })

        return message_object
