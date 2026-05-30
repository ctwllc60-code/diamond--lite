from core.base.base_engine import (
    BaseEngine
)


class IntentDecomposition(BaseEngine):

    def __init__(self):

        super().__init__(
            "intent_decomposition"
        )

    def process(
        self,
        message_object
    ):

        raw_message = (
            message_object.raw_message
            or ""
        )

        lowered_message = (
            raw_message.lower()
        )

        current_wave = (

            message_object.recursion_state[
                "current_wave"
            ]
        )

        detected_domains = []

        detected_intents = []

        domain_intent_map = []

        continuity_anchors = []

        response_obligations = []

        domain_patterns = {

            "coding": [
                "code",
                "python",
                "engine",
                "pipeline",
                "debug",
                "architecture",
                "runtime",
                "system"
            ],

            "finance": [
                "finance",
                "money",
                "funding",
                "grant",
                "treasury",
                "budget",
                "capital",
                "investment"
            ],

            "real_estate": [
                "property",
                "building",
                "real estate",
                "facility",
                "land",
                "renovation",
                "acquisition"
            ],

            "identity": [
                "identity",
                "who are you",
                "presence",
                "role",
                "personality"
            ],

            "memory": [
                "memory",
                "continuity",
                "remember",
                "recall",
                "retention"
            ],

            "relationships": [
                "relationship",
                "alignment",
                "connection",
                "partnership",
                "trust"
            ],

            "strategy": [
                "strategy",
                "plan",
                "direction",
                "approach",
                "goal"
            ],

            "learning": [
                "understand",
                "explain",
                "teach",
                "help me understand",
                "describe"
            ]
        }

        intent_patterns = {

            "debugging": [
                "fix",
                "debug",
                "repair",
                "issue",
                "problem"
            ],

            "planning": [
                "plan",
                "structure",
                "organize",
                "design"
            ],

            "guidance": [
                "help",
                "guide",
                "show",
                "teach"
            ],

            "analysis": [
                "analyze",
                "understand",
                "explain",
                "break down"
            ],

            "creation": [
                "build",
                "create",
                "develop",
                "expand"
            ],

            "continuity_preservation": [
                "remember",
                "maintain",
                "preserve",
                "continue"
            ]
        }

        for domain, keywords in (
            domain_patterns.items()
        ):

            if any(
                keyword in lowered_message
                for keyword in keywords
            ):

                detected_domains.append(
                    domain
                )

        for intent, keywords in (
            intent_patterns.items()
        ):

            if any(
                keyword in lowered_message
                for keyword in keywords
            ):

                detected_intents.append(
                    intent
                )

        for domain in detected_domains:

            domain_intent_map.append({

                "domain":
                    domain,

                "intents":
                    detected_intents
            })

        if (
            "continuity"
            in lowered_message
        ):

            continuity_anchors.append(
                "continuity"
            )

        if (
            "remember"
            in lowered_message
        ):

            continuity_anchors.append(
                "memory_recall"
            )

        if (
            "again"
            in lowered_message
        ):

            continuity_anchors.append(
                "continuation"
            )

        for mapping in (
            domain_intent_map
        ):

            response_obligations.append({

                "domain":
                    mapping["domain"],

                "intents":
                    mapping["intents"]
            })

        intent_analysis = {

            "detected_domains":
                detected_domains,

            "detected_intents":
                detected_intents,

            "domain_intent_map":
                domain_intent_map,

            "continuity_anchors":
                continuity_anchors,

            "response_obligations":
                response_obligations,

            "coverage_alignment_active":
                True,

            "multi_domain_alignment_active":
                True,

            "intent_decomposition_active":
                True
        }

        message_object.cognitive_state[
            "intent_decomposition"
        ] = intent_analysis

        message_object.enrichment_layers.append({

            "engine":
                self.engine_name,

            "wave":
                current_wave,

            "type":
                "intent_decomposition",

            "content":
                intent_analysis
        })

        return message_object
