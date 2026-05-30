from core.base.base_engine import (
    BaseEngine
)


class Gatekeeper(BaseEngine):

    def __init__(self):

        super().__init__(
            "gatekeeper"
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

        detected_roles = []

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
                "infrastructure",
                "pipeline",
                "orchestration",
                "engine",
                "llm",
                "reasoning",
                "cognition",
                "alignment"
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

        for role, keywords in (
            role_map.items()
        ):

            for keyword in keywords:

                if keyword in raw_message:

                    if role not in (
                        detected_roles
                    ):

                        detected_roles.append(
                            role
                        )

                    break

        gatekeeper_analysis = {

            "detected_roles":
                detected_roles,

            "role_alignment_active":
                True
        }

        if detected_roles:

            gatekeeper_analysis[
                "primary_role"
            ] = detected_roles[0]

        if len(
            detected_roles
        ) > 1:

            gatekeeper_analysis[
                "secondary_roles"
            ] = detected_roles[1:]

        if "how" in raw_message:

            gatekeeper_analysis[
                "intent_alignment"
            ] = "execution_guidance"

        if "why" in raw_message:

            gatekeeper_analysis[
                "intent_alignment"
            ] = "causal_understanding"

        if "should" in raw_message:

            gatekeeper_analysis[
                "intent_alignment"
            ] = "strategic_evaluation"

        if "what" in raw_message:

            gatekeeper_analysis[
                "intent_alignment"
            ] = "structural_interpretation"

        message_object.cognitive_state[
            "gatekeeper"
        ] = gatekeeper_analysis

        message_object.cognitive_state[
            "operator_posture"
        ] = gatekeeper_analysis.get(
            "primary_role",
            "general"
        )

        message_object.enrichment_layers.append({

            "engine":
                self.engine_name,

            "wave":
                current_wave,

            "type":
                "role_alignment",

            "content":
                gatekeeper_analysis
        })

        return message_object
