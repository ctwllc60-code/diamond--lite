from core.base_engine import BaseEngine

class IntentOrchestrator(BaseEngine):

    def __init__(self):

        super().__init__(
            "intent_orchestrator"
        )

    def process(self, message_object):

        raw = (
            message_object.raw_message.lower()
        )

        primary_role = None

        secondary_roles = []

        support_roles = []

        detected_intent = (
            "general_guidance"
        )

        operator_posture = (
            "general"
        )

        tactical_depth = (
            "standard"
        )

        adversarial_reasoning = (
            False
        )

        practical_realism = (
            False
        )

        role_map = {

            "psychology": [
                "emotion",
                "fear",
                "uncertainty",
                "identity",
                "trauma",
                "mind"
            ],

            "finance": [
                "money",
                "investment",
                "capital",
                "finance",
                "fund"
            ],

            "banking": [
                "bank",
                "treasury",
                "reserve",
                "loan",
                "interest"
            ],

            "economics": [
                "economy",
                "inflation",
                "market",
                "gdp",
                "economics"
            ],

            "law": [
                "law",
                "lawsuit",
                "legal",
                "court",
                "contract"
            ],

            "politics": [
                "government",
                "policy",
                "politics",
                "senate",
                "president"
            ],

            "software_engineering": [
                "python",
                "api",
                "backend",
                "software",
                "code"
            ],

            "systems_architecture": [
                "system",
                "architecture",
                "framework",
                "infrastructure"
            ],

            "cybersecurity": [
                "cybersecurity",
                "security",
                "exploit",
                "breach",
                "firewall",
                "ransomware",
                "phishing",
                "malware"
            ],

            "real_estate": [
                "property",
                "real estate",
                "housing",
                "building",
                "mortgage"
            ],

            "healthcare": [
                "health",
                "medical",
                "doctor",
                "disease",
                "treatment"
            ],

            "engineering": [
                "engineering",
                "mechanical",
                "electrical",
                "structural"
            ],

            "education": [
                "learn",
                "teaching",
                "education",
                "student",
                "school"
            ],

            "philosophy": [
                "meaning",
                "existence",
                "purpose",
                "philosophy",
                "truth"
            ],

            "business_strategy": [
                "business",
                "strategy",
                "growth",
                "marketplace",
                "competition"
            ],

            "entrepreneurship": [
                "startup",
                "founder",
                "entrepreneur",
                "scaling"
            ],

            "relationship_dynamics": [
                "relationship",
                "trust",
                "communication",
                "attachment"
            ],

            "negotiation": [
                "negotiate",
                "deal",
                "bargain",
                "agreement"
            ],

            "project_management": [
                "project",
                "timeline",
                "milestone",
                "planning"
            ],

            "research_analysis": [
                "research",
                "analysis",
                "study",
                "evidence"
            ]
        }

        detected_roles = []

        for role, keywords in (
            role_map.items()
        ):

            for keyword in keywords:

                if keyword in raw:

                    if role not in (
                        detected_roles
                    ):

                        detected_roles.append(
                            role
                        )

                    break

        if detected_roles:

            primary_role = (
                detected_roles[0]
            )

        if len(detected_roles) > 1:

            secondary_roles = (
                detected_roles[1:3]
            )

        if len(detected_roles) > 3:

            support_roles = (
                detected_roles[3:]
            )

        if "how" in raw:

            detected_intent = (
                "procedural_guidance"
            )

        elif "why" in raw:

            detected_intent = (
                "causal_reasoning"
            )

        elif "should" in raw:

            detected_intent = (
                "decision_support"
            )

        tactical_domains = [

            "cybersecurity",

            "banking",

            "law",

            "business_strategy",

            "systems_architecture",

            "software_engineering"
        ]

        if primary_role in tactical_domains:

            tactical_depth = (
                "advanced"
            )

            practical_realism = (
                True
            )

        adversarial_domains = [

            "cybersecurity",

            "law",

            "politics",

            "negotiation",

            "business_strategy"
        ]

        if primary_role in adversarial_domains:

            adversarial_reasoning = (
                True
            )

        if primary_role == "cybersecurity":

            operator_posture = (
                "defensive_operator"
            )

        elif primary_role == "law":

            operator_posture = (
                "procedural_strategist"
            )

        elif primary_role == (
            "business_strategy"
        ):

            operator_posture = (
                "competitive_strategist"
            )

        elif primary_role == (
            "systems_architecture"
        ):

            operator_posture = (
                "infrastructure_architect"
            )

        elif primary_role == (
            "software_engineering"
        ):

            operator_posture = (
                "systems_engineer"
            )

        elif primary_role == (
            "politics"
        ):

            operator_posture = (
                "power_dynamics_analyst"
            )

        orchestration_analysis = {

            "primary_role":
                primary_role,

            "secondary_roles":
                secondary_roles,

            "support_roles":
                support_roles,

            "detected_intent":
                detected_intent,

            "detected_roles":
                detected_roles,

            "operator_posture":
                operator_posture,

            "tactical_depth":
                tactical_depth,

            "adversarial_reasoning":
                adversarial_reasoning,

            "practical_realism":
                practical_realism,

            "orchestration_active":
                True
        }

        message_object.cognitive_state[
            "intent_orchestration"
        ] = orchestration_analysis

        message_object.cognitive_state[
            "operator_posture"
        ] = operator_posture

        message_object.enrichment_layers.append({

            "engine":
                self.engine_name,

            "wave":
                message_object.recursion_state[
                    "current_wave"
                ],

            "type":
                "intent_orchestration",

            "content":
                orchestration_analysis
        })

        return message_object
