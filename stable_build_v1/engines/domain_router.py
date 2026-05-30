from core.base_engine import BaseEngine

class DomainRouter(BaseEngine):

    def __init__(self):
        super().__init__(
            "domain_router"
        )

    def process(self, message_object):

        raw = (
            message_object.raw_message.lower()
        )

        detected_domain = "general"

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
                "infrastructure"
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

        for domain, keywords in (
            domain_keywords.items()
        ):

            for keyword in keywords:

                if keyword in raw:

                    detected_domain = domain

                    break

            if detected_domain != "general":
                break

        domain_analysis = {
            "detected_domain":
                detected_domain,

            "domain_routing_active":
                True
        }

        message_object.cognitive_state[
            "active_domain"
        ] = detected_domain

        message_object.enrichment_layers.append({
            "engine": self.engine_name,
            "wave":
                message_object.recursion_state[
                    "current_wave"
                ],
            "type": "domain_routing",
            "content": domain_analysis
        })

        return message_object
