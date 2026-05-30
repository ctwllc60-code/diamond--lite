from core.base.base_engine import (
    BaseEngine
)


class Influencer(BaseEngine):

    def __init__(self):

        super().__init__(
            "influencer"
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

        influence_signals = []

        influence_patterns = {

            "identity": [
                "identity",
                "purpose",
                "meaning",
                "who am i",
                "self"
            ],

            "trust": [
                "trust",
                "truth",
                "honest",
                "real",
                "confidence"
            ],

            "growth": [
                "grow",
                "expand",
                "develop",
                "build",
                "improve"
            ],

            "continuity": [
                "continuity",
                "connection",
                "alignment",
                "presence",
                "relationship"
            ],

            "exploration": [
                "why",
                "how",
                "understand",
                "explain",
                "depth"
            ]
        }

        influence_map = {}

        for category, keywords in (
            influence_patterns.items()
        ):

            score = 0

            for keyword in keywords:

                if keyword in raw_message:

                    score += 1

                    influence_signals.append(
                        keyword
                    )

            if score > 0:

                influence_map[
                    category
                ] = score

        influence_analysis = {

            "influence_map":
                influence_map,

            "influence_signals":
                influence_signals,

            "influence_alignment_active":
                True
        }

        if (
            "identity"
            in influence_map
        ):

            influence_analysis[
                "identity_alignment"
            ] = "active"

        if (
            "trust"
            in influence_map
        ):

            influence_analysis[
                "trust_alignment"
            ] = "active"

        if (
            "growth"
            in influence_map
        ):

            influence_analysis[
                "growth_alignment"
            ] = "active"

        if (
            "continuity"
            in influence_map
        ):

            influence_analysis[
                "continuity_alignment"
            ] = "active"

        if (
            "exploration"
            in influence_map
        ):

            influence_analysis[
                "exploration_alignment"
            ] = "active"

        message_object.cognitive_state[
            "influencer"
        ] = influence_analysis

        message_object.enrichment_layers.append({

            "engine":
                self.engine_name,

            "wave":
                current_wave,

            "type":
                "influence_alignment",

            "content":
                influence_analysis
        })

        return message_object
