from core.base_engine import BaseEngine

class ReasoningAdapter(BaseEngine):

    def __init__(self):

        super().__init__(
            "reasoning_adapter"
        )

    def process(self, message_object):

        recursion_depth = (
            message_object.recursion_state[
                "depth"
            ]
        )

        current_wave = (
            message_object.recursion_state[
                "current_wave"
            ]
        )

        semantic_fields = (
            message_object.cognitive_state.get(
                "semantic_fields",
                []
            )
        )

        operator_posture = (
            message_object.cognitive_state.get(
                "operator_posture",
                "general"
            )
        )

        reasoning_vectors = []

        practical_scenarios = []

        for field in semantic_fields:

            concept = (
                field.get(
                    "concept",
                    ""
                )
            )

            semantic_weights = (
                field.get(
                    "semantic_weights",
                    []
                )
            )

            reasoning_directions = [

                "causal_analysis",

                "systemic_interpretation",

                "behavioral_implications",

                "strategic_considerations",

                "adaptive_response"
            ]

            if operator_posture == (
                "defensive_operator"
            ):

                reasoning_directions.extend([

                    "threat_modeling",

                    "attack_surface_analysis",

                    "containment_strategy",

                    "infrastructure_resilience"
                ])

            elif operator_posture == (
                "procedural_strategist"
            ):

                reasoning_directions.extend([

                    "liability_exposure",

                    "procedural_risk",

                    "strategic_positioning",

                    "dispute_navigation"
                ])

            elif operator_posture == (
                "competitive_strategist"
            ):

                reasoning_directions.extend([

                    "competitive_pressure",

                    "market_positioning",

                    "resource_leverage",

                    "strategic_advantage"
                ])

            if concept == "cybersecurity":

                practical_scenarios.extend([

                    "phishing campaigns used to harvest employee credentials",

                    "ransomware propagating laterally through unsegmented networks",

                    "malware exploiting outdated infrastructure systems",

                    "attackers targeting privileged administrative accounts"
                ])

            elif concept == "banking":

                practical_scenarios.extend([

                    "unauthorized transaction attempts against financial systems",

                    "credential compromise affecting internal banking access",

                    "service disruption impacting customer account access",

                    "fraud detection systems identifying abnormal activity"
                ])

            elif concept == "lawsuit":

                practical_scenarios.extend([

                    "discovery disputes delaying legal proceedings",

                    "evidence review affecting liability exposure",

                    "settlement negotiations changing litigation strategy",

                    "procedural motions influencing case trajectory"
                ])

            elif concept == "economy":

                practical_scenarios.extend([

                    "inflation reducing consumer purchasing power",

                    "interest rate increases slowing investment activity",

                    "market instability affecting employment growth",

                    "supply chain disruptions impacting pricing structures"
                ])

            reasoning_vectors.append({

                "concept":
                    concept,

                "reasoning_directions":
                    reasoning_directions,

                "semantic_weights":
                    semantic_weights,

                "recursion_depth":
                    recursion_depth,

                "operator_posture":
                    operator_posture
            })

        reasoning_analysis = {

            "reasoning_vectors":
                reasoning_vectors,

            "practical_scenarios":
                practical_scenarios,

            "recursion_depth":
                recursion_depth,

            "current_wave":
                current_wave,

            "layers_seen":
                len(
                    message_object.enrichment_layers
                ),

            "adaptive_reasoning_active":
                True,

            "practical_reasoning_active":
                True
        }

        message_object.cognitive_state[
            "reasoning_vectors"
        ] = reasoning_vectors

        message_object.cognitive_state[
            "practical_scenarios"
        ] = practical_scenarios

        message_object.enrichment_layers.append({

            "engine":
                self.engine_name,

            "wave":
                current_wave,

            "type":
                "adaptive_reasoning",

            "content":
                reasoning_analysis
        })

        return message_object
