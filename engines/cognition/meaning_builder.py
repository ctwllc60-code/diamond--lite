from core.base.base_engine import (
    BaseEngine
)

import random


class MeaningBuilder(BaseEngine):

    def __init__(self):

        super().__init__(
            "meaning_builder"
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

        semantic_fields = []

        semantic_universes = {

            "fear": [

                {
                    "perspective":
                        "evolutionary_psychology",

                    "semantic_weights": [

                        "survival",
                        "threat_detection",
                        "adaptation",
                        "risk_assessment",
                        "environmental_uncertainty"
                    ]
                },

                {
                    "perspective":
                        "cognitive_science",

                    "semantic_weights": [

                        "prediction",
                        "ambiguity",
                        "mental_processing",
                        "decision_strain",
                        "pattern_disruption"
                    ]
                },

                {
                    "perspective":
                        "existential_philosophy",

                    "semantic_weights": [

                        "meaning",
                        "identity",
                        "mortality",
                        "uncertainty",
                        "human_limitation"
                    ]
                }
            ],

            "uncertainty": [

                {
                    "perspective":
                        "decision_theory",

                    "semantic_weights": [

                        "prediction",
                        "risk",
                        "outcome_modeling",
                        "ambiguity",
                        "probability"
                    ]
                },

                {
                    "perspective":
                        "identity_stability",

                    "semantic_weights": [

                        "orientation",
                        "continuity",
                        "belief_structures",
                        "adaptation",
                        "self_concept"
                    ]
                },

                {
                    "perspective":
                        "neuroscience",

                    "semantic_weights": [

                        "stress_response",
                        "threat_activation",
                        "cognitive_load",
                        "neural_processing",
                        "emotional_signaling"
                    ]
                }
            ],

            "economy": [

                {
                    "perspective":
                        "macroeconomics",

                    "semantic_weights": [

                        "inflation",
                        "markets",
                        "growth",
                        "employment",
                        "interest_rates"
                    ]
                },

                {
                    "perspective":
                        "behavioral_economics",

                    "semantic_weights": [

                        "consumer_psychology",
                        "risk_behavior",
                        "market_confidence",
                        "financial_perception",
                        "decision_patterns"
                    ]
                },

                {
                    "perspective":
                        "systems_theory",

                    "semantic_weights": [

                        "resource_flow",
                        "economic_interdependence",
                        "system_stability",
                        "feedback_loops",
                        "structural_resilience"
                    ]
                }
            ],

            "systems": [

                {
                    "perspective":
                        "systems_architecture",

                    "semantic_weights": [

                        "modularity",
                        "pipeline_coordination",
                        "distributed_cognition",
                        "orchestration_flow",
                        "structural_specialization"
                    ]
                },

                {
                    "perspective":
                        "infrastructure_design",

                    "semantic_weights": [

                        "scalability",
                        "stability",
                        "coordination_layers",
                        "system_resilience",
                        "execution_flow"
                    ]
                }
            ]
        }

        for concept, perspectives in (
            semantic_universes.items()
        ):

            if concept in raw_message:

                selected_perspective = (

                    random.choice(
                        perspectives
                    )
                )

                semantic_fields.append({

                    "concept":
                        concept,

                    "perspective":
                        selected_perspective[
                            "perspective"
                        ],

                    "semantic_weights":
                        selected_perspective[
                            "semantic_weights"
                        ]
                })

        meaning_analysis = {

            "semantic_fields":
                semantic_fields,

            "current_wave":
                current_wave,

            "semantic_expansion_active":
                True,

            "perspective_distribution_active":
                True,

            "meaning_enrichment_active":
                True
        }

        if semantic_fields:

            meaning_analysis[
                "semantic_presence"
            ] = "active"

        message_object.cognitive_state[
            "semantic_fields"
        ] = semantic_fields

        message_object.cognitive_state[
            "meaning_builder"
        ] = meaning_analysis

        message_object.enrichment_layers.append({

            "engine":
                self.engine_name,

            "wave":
                current_wave,

            "type":
                "meaning_enrichment",

            "content":
                meaning_analysis
        })

        return message_object
