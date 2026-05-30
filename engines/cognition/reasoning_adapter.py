from core.base.base_engine import (
    BaseEngine
)


class ReasoningAdapter(BaseEngine):

    def __init__(self):

        super().__init__(
            "reasoning_adapter"
        )

    def process(
        self,
        message_object
    ):

        raw_message = (
            message_object.raw_message
            or ""
        ).lower()

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

        reasoning_vectors = []

        reasoning_modes = []

        if any(

            keyword in raw_message

            for keyword in [

                "why",
                "cause",
                "reason",
                "meaning",
                "understand"
            ]
        ):

            reasoning_modes.extend([

                "causal_analysis",
                "systemic_interpretation",
                "behavioral_implications"
            ])

        if any(

            keyword in raw_message

            for keyword in [

                "how",
                "build",
                "implement",
                "develop",
                "structure"
            ]
        ):

            reasoning_modes.extend([

                "strategic_considerations",
                "adaptive_structuring",
                "execution_modeling"
            ])

        if any(

            keyword in raw_message

            for keyword in [

                "cybersecurity",
                "security",
                "attack",
                "breach",
                "malware"
            ]
        ):

            reasoning_modes.extend([

                "threat_modeling",
                "attack_surface_analysis",
                "containment_strategy",
                "infrastructure_resilience"
            ])

        if any(

            keyword in raw_message

            for keyword in [

                "business",
                "competition",
                "market",
                "growth",
                "strategy"
            ]
        ):

            reasoning_modes.extend([

                "competitive_analysis",
                "market_positioning",
                "resource_leverage",
                "strategic_advantage"
            ])

        if any(

            keyword in raw_message

            for keyword in [

                "law",
                "lawsuit",
                "legal",
                "contract"
            ]
        ):

            reasoning_modes.extend([

                "liability_analysis",
                "procedural_analysis",
                "strategic_positioning",
                "dispute_navigation"
            ])

        reasoning_vectors.append({

            "reasoning_modes":
                list(
                    set(reasoning_modes)
                ),

            "recursion_depth":
                recursion_depth
        })

        reasoning_analysis = {

            "reasoning_vectors":
                reasoning_vectors,

            "recursion_depth":
                recursion_depth,

            "current_wave":
                current_wave,

            "adaptive_reasoning_active":
                True,

            "reasoning_enrichment_active":
                True
        }

        if reasoning_modes:

            reasoning_analysis[
                "reasoning_presence"
            ] = "active"

        message_object.cognitive_state[
            "reasoning_adapter"
        ] = reasoning_analysis

        message_object.cognitive_state[
            "reasoning_vectors"
        ] = reasoning_vectors

        message_object.enrichment_layers.append({

            "engine":
                self.engine_name,

            "wave":
                current_wave,

            "type":
                "reasoning_enrichment",

            "content":
                reasoning_analysis
        })

        return message_object
