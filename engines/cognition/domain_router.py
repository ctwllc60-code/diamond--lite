from core.base.base_engine import (
    BaseEngine
)


class DomainRouter(BaseEngine):

    def __init__(self):

        super().__init__(
            "domain_router"
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

        detected_domains = []

        matched_keywords = []

        domain_keywords = {

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
                "orchestration"
            ],

            "cybersecurity": [
                "cybersecurity",
                "security",
                "exploit",
                "breach",
                "firewall"
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

        domain_scores = {}

        for domain, keywords in (
            domain_keywords.items()
        ):

            score = 0

            for keyword in keywords:

                if keyword in raw_message:

                    score += 1

                    matched_keywords.append(
                        keyword
                    )

            if score > 0:

                domain_scores[
                    domain
                ] = score

                detected_domains.append(
                    domain
                )

        domain_analysis = {

            "detected_domains":
                detected_domains,

            "domain_scores":
                domain_scores,

            "matched_keywords":
                matched_keywords,

            "domain_routing_active":
                True
        }

        if detected_domains:

            domain_analysis[
                "primary_domain"
            ] = detected_domains[0]

            message_object.cognitive_state[
                "active_domain"
            ] = detected_domains[0]

        message_object.cognitive_state[
            "domain_routing"
        ] = domain_analysis

        message_object.enrichment_layers.append({

            "engine":
                self.engine_name,

            "wave":
                current_wave,

            "type":
                "domain_routing",

            "content":
                domain_analysis
        })

        return message_object
