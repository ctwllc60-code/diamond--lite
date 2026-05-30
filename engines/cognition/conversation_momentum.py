from core.base.base_engine import (
    BaseEngine
)


class ConversationMomentum(BaseEngine):

    def __init__(self):

        super().__init__(
            "conversation_momentum"
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

        conversational_energy = []

        thematic_patterns = {

            "growth": [
                "grow",
                "build",
                "expand",
                "develop",
                "improve"
            ],

            "continuity": [
                "continuity",
                "connection",
                "remember",
                "flow",
                "alignment"
            ],

            "identity": [
                "identity",
                "who are you",
                "presence",
                "relationship",
                "understanding"
            ],

            "systems": [
                "system",
                "architecture",
                "engine",
                "pipeline",
                "structure"
            ],

            "exploration": [
                "why",
                "how",
                "understand",
                "explain",
                "depth"
            ]
        }

        momentum_map = {}

        for theme, keywords in (
            thematic_patterns.items()
        ):

            score = 0

            for keyword in keywords:

                if keyword in raw_message:

                    score += 1

                    conversational_energy.append(
                        keyword
                    )

            if score > 0:

                momentum_map[
                    theme
                ] = score

        momentum_analysis = {

            "momentum_map":
                momentum_map,

            "conversational_energy":
                conversational_energy,

            "momentum_alignment_active":
                True
        }

        if momentum_map:

            momentum_analysis[
                "momentum_presence"
            ] = "active"

        if (
            "exploration"
            in momentum_map
        ):

            momentum_analysis[
                "exploration_alignment"
            ] = "active"

        if (
            "continuity"
            in momentum_map
        ):

            momentum_analysis[
                "continuity_alignment"
            ] = "active"

        if (
            "identity"
            in momentum_map
        ):

            momentum_analysis[
                "identity_alignment"
            ] = "active"

        message_object.cognitive_state[
            "conversation_momentum"
        ] = momentum_analysis

        message_object.enrichment_layers.append({

            "engine":
                self.engine_name,

            "wave":
                current_wave,

            "type":
                "conversation_momentum",

            "content":
                momentum_analysis
        })

        return message_object
