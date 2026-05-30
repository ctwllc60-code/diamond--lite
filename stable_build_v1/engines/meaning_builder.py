from core.base_engine import BaseEngine

import random

class MeaningBuilder(BaseEngine):

    def __init__(self):

        super().__init__(
            "meaning_builder"
        )

    def process(self, message_object):

        raw = (
            message_object.raw_message.lower()
        )

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
                        "threat detection",
                        "adaptation",
                        "risk assessment",
                        "environmental uncertainty"
                    ]
                },

                {
                    "perspective":
                        "cognitive_science",

                    "semantic_weights": [

                        "prediction",
                        "ambiguity",
                        "mental processing",
                        "decision strain",
                        "pattern disruption"
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
                        "human limitation"
                    ]
                },

                {
                    "perspective":
                        "behavioral_adaptation",

                    "semantic_weights": [

                        "control",
                        "response behavior",
                        "stability seeking",
                        "emotional regulation",
                        "adaptive strategy"
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
                        "outcome modeling",
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
                        "belief structures",
                        "adaptation",
                        "self-concept"
                    ]
                },

                {
                    "perspective":
                        "neuroscience",

                    "semantic_weights": [

                        "stress response",
                        "threat activation",
                        "cognitive load",
                        "neural processing",
                        "emotional signaling"
                    ]
                },

                {
                    "perspective":
                        "social_behavior",

                    "semantic_weights": [

                        "group stability",
                        "social trust",
                        "coordination",
                        "communication",
                        "environmental response"
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
                        "interest rates"
                    ]
                },

                {
                    "perspective":
                        "behavioral_economics",

                    "semantic_weights": [

                        "consumer psychology",
                        "risk behavior",
                        "market confidence",
                        "financial perception",
                        "decision patterns"
                    ]
                },

                {
                    "perspective":
                        "systems_theory",

                    "semantic_weights": [

                        "resource flow",
                        "economic interdependence",
                        "system stability",
                        "feedback loops",
                        "structural resilience"
                    ]
                },

                {
                    "perspective":
                        "institutional_strategy",

                    "semantic_weights": [

                        "central banking pressure",
                        "capital allocation",
                        "monetary intervention",
                        "policy leverage",
                        "systemic stabilization"
                    ]
                }
            ],

            "lawsuit": [

                {
                    "perspective":
                        "legal_procedure",

                    "semantic_weights": [

                        "court process",
                        "evidence",
                        "liability",
                        "resolution",
                        "judicial structure"
                    ]
                },

                {
                    "perspective":
                        "conflict_resolution",

                    "semantic_weights": [

                        "dispute management",
                        "negotiation",
                        "strategic positioning",
                        "power dynamics",
                        "settlement behavior"
                    ]
                },

                {
                    "perspective":
                        "institutional_analysis",

                    "semantic_weights": [

                        "legal systems",
                        "governance",
                        "social order",
                        "regulatory enforcement",
                        "structural accountability"
                    ]
                },

                {
                    "perspective":
                        "litigation_strategy",

                    "semantic_weights": [

                        "procedural leverage",
                        "discovery pressure",
                        "liability exposure",
                        "case positioning",
                        "adversarial negotiation"
                    ]
                }
            ],

            "politics": [

                {
                    "perspective":
                        "power_dynamics",

                    "semantic_weights": [

                        "influence",
                        "authority",
                        "coalition building",
                        "institutional control",
                        "public perception"
                    ]
                },

                {
                    "perspective":
                        "mass_psychology",

                    "semantic_weights": [

                        "group behavior",
                        "emotional mobilization",
                        "tribal alignment",
                        "narrative shaping",
                        "social influence"
                    ]
                },

                {
                    "perspective":
                        "governance_strategy",

                    "semantic_weights": [

                        "policy enforcement",
                        "resource coordination",
                        "institutional stability",
                        "strategic communication",
                        "decision pressure"
                    ]
                },

                {
                    "perspective":
                        "competitive_politics",

                    "semantic_weights": [

                        "power competition",
                        "strategic positioning",
                        "political leverage",
                        "narrative warfare",
                        "public influence operations"
                    ]
                }
            ],

            "business": [

                {
                    "perspective":
                        "competitive_strategy",

                    "semantic_weights": [

                        "market positioning",
                        "competitive pressure",
                        "resource leverage",
                        "growth strategy",
                        "operational scaling"
                    ]
                },

                {
                    "perspective":
                        "organizational_behavior",

                    "semantic_weights": [

                        "leadership structure",
                        "decision systems",
                        "team coordination",
                        "operational efficiency",
                        "adaptation"
                    ]
                },

                {
                    "perspective":
                        "market_dynamics",

                    "semantic_weights": [

                        "consumer demand",
                        "market volatility",
                        "pricing pressure",
                        "competitive differentiation",
                        "capital flow"
                    ]
                },

                {
                    "perspective":
                        "enterprise_operations",

                    "semantic_weights": [

                        "infrastructure scaling",
                        "risk management",
                        "operational resilience",
                        "resource allocation",
                        "execution systems"
                    ]
                }
            ],

            "real estate": [

                {
                    "perspective":
                        "asset_strategy",

                    "semantic_weights": [

                        "ownership structures",
                        "equity positioning",
                        "cash flow",
                        "property leverage",
                        "investment risk"
                    ]
                },

                {
                    "perspective":
                        "development_operations",

                    "semantic_weights": [

                        "zoning pressure",
                        "construction coordination",
                        "infrastructure planning",
                        "project financing",
                        "regulatory navigation"
                    ]
                },

                {
                    "perspective":
                        "market_positioning",

                    "semantic_weights": [

                        "regional demand",
                        "asset valuation",
                        "market cycles",
                        "location strategy",
                        "occupancy pressure"
                    ]
                },

                {
                    "perspective":
                        "risk_distribution",

                    "semantic_weights": [

                        "liability segmentation",
                        "holding structures",
                        "operational exposure",
                        "insurance layering",
                        "financial protection"
                    ]
                }
            ],

            "cybersecurity": [

                {
                    "perspective":
                        "defensive_operations",

                    "semantic_weights": [

                        "attack surface",
                        "threat detection",
                        "endpoint hardening",
                        "network segmentation",
                        "incident response"
                    ]
                },

                {
                    "perspective":
                        "adversarial_behavior",

                    "semantic_weights": [

                        "lateral movement",
                        "credential harvesting",
                        "privilege escalation",
                        "persistence mechanisms",
                        "attack vectors"
                    ]
                },

                {
                    "perspective":
                        "enterprise_security",

                    "semantic_weights": [

                        "zero-trust architecture",
                        "identity federation",
                        "SIEM visibility",
                        "EDR containment",
                        "security posture"
                    ]
                },

                {
                    "perspective":
                        "infrastructure_resilience",

                    "semantic_weights": [

                        "service continuity",
                        "infrastructure redundancy",
                        "cloud resilience",
                        "authentication layers",
                        "operational containment"
                    ]
                }
            ]
        }

        for concept, perspectives in (
            semantic_universes.items()
        ):

            if concept in raw:

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

            "layers_seen":
                len(
                    message_object.enrichment_layers
                ),

            "semantic_divergence_active":
                True,

            "operator_distribution_active":
                True
        }

        message_object.cognitive_state[
            "semantic_fields"
        ] = semantic_fields

        message_object.enrichment_layers.append({

            "engine":
                self.engine_name,

            "wave":
                current_wave,

            "type":
                "semantic_divergence",

            "content":
                meaning_analysis
        })

        return message_object
