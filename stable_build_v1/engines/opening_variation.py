from core.base_engine import BaseEngine

class OpeningVariation(BaseEngine):

    def __init__(self):

        super().__init__(
            "opening_variation"
        )

    def process(self, message_object):

        current_wave = (
            message_object.recursion_state[
                "current_wave"
            ]
        )

        continuity_state = (
            message_object.cognitive_state.get(
                "continuity_weighting",
                {}
            )
        )

        continuity_weight = (
            continuity_state.get(
                "continuity_weight",
                "neutral"
            )
        )

        semantic_fields = (
            message_object.cognitive_state.get(
                "semantic_fields",
                []
            )
        )

        active_domain = (
            message_object.cognitive_state.get(
                "active_domain",
                "general"
            )
        )

        recursion_depth = (
            message_object.recursion_state.get(
                "depth",
                0
            )
        )

        explanatory_flow = (
            "layered_exploration"
        )

        reasoning_posture = (
            "interpretive"
        )

        abstraction_level = (
            "hybrid"
        )

        transition_style = (
            "fluid"
        )

        conceptual_priority = (
            "causal"
        )

        if active_domain in [
            "law",
            "banking",
            "finance",
            "economics"
        ]:

            explanatory_flow = (
                "systemic_breakdown"
            )

            reasoning_posture = (
                "strategic"
            )

            conceptual_priority = (
                "structural"
            )

        if active_domain in [
            "psychology",
            "philosophy",
            "relationship_dynamics"
        ]:

            explanatory_flow = (
                "conceptual_unfolding"
            )

            reasoning_posture = (
                "reflective"
            )

            abstraction_level = (
                "conceptual"
            )

        if recursion_depth >= 1:

            transition_style = (
                "progressive"
            )

        for field in semantic_fields:

            perspective = (
                field.get(
                    "perspective",
                    ""
                )
            )

            if perspective == (
                "evolutionary_psychology"
            ):

                reasoning_posture = (
                    "behavioral"
                )

                conceptual_priority = (
                    "adaptive"
                )

            elif perspective == (
                "cognitive_science"
            ):

                reasoning_posture = (
                    "analytical"
                )

                abstraction_level = (
                    "hybrid"
                )

            elif perspective == (
                "existential_philosophy"
            ):

                reasoning_posture = (
                    "interpretive"
                )

                abstraction_level = (
                    "conceptual"
                )

            elif perspective == (
                "neuroscience"
            ):

                explanatory_flow = (
                    "systemic_breakdown"
                )

                reasoning_posture = (
                    "mechanistic"
                )

        variability_vectors = {

            "explanatory_flow":
                explanatory_flow,

            "reasoning_posture":
                reasoning_posture,

            "abstraction_level":
                abstraction_level,

            "transition_style":
                transition_style,

            "conceptual_priority":
                conceptual_priority
        }

        message_object.cognitive_state[
            "variability_vectors"
        ] = variability_vectors

        message_object.enrichment_layers.append({

            "engine": self.engine_name,

            "wave":
                current_wave,

            "type":
                "contextual_variability",

            "content": {

                "continuity_weight":
                    continuity_weight,

                "variability_vectors":
                    variability_vectors,

                "contextual_variability_active":
                    True
            }
        })

        return message_object
