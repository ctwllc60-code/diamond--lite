from core.base_engine import BaseEngine

class ContinuityWeighting(BaseEngine):

    def __init__(self):
        super().__init__(
            "continuity_weighting"
        )

    def process(self, message_object):

        momentum_state = (
            message_object.cognitive_state.get(
                "conversation_momentum",
                {}
            )
        )

        dominant_theme = (
            momentum_state.get(
                "dominant_theme"
            )
        )

        continuity_weight = "neutral"

        if dominant_theme in [
            "uncertainty",
            "identity",
            "safety",
            "stability"
        ]:

            continuity_weight = "high"

        weighting_analysis = {
            "dominant_theme":
                dominant_theme,

            "continuity_weight":
                continuity_weight,

            "weighting_active":
                dominant_theme is not None
        }

        message_object.cognitive_state[
            "continuity_weighting"
        ] = weighting_analysis

        message_object.enrichment_layers.append({
            "engine": self.engine_name,
            "wave":
                message_object.recursion_state[
                    "current_wave"
                ],
            "type": "continuity_weighting",
            "content": weighting_analysis
        })

        return message_object
