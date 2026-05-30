from core.base_engine import BaseEngine

class ManifestationArbiter(BaseEngine):

    def __init__(self):
        super().__init__(
            "manifestation_arbiter"
        )

    def process(self, message_object):

        response = message_object.final_response

        repetitive_patterns = [
            "I reflected on your question carefully.",
            "I spent some time sitting with your question before responding."
        ]

        removed_patterns = []

        for pattern in repetitive_patterns:

            if response.count(pattern) > 0:

                if pattern.startswith(
                    "I reflected"
                ):

                    response = response.replace(
                        pattern + "\n\n",
                        ""
                    )

                    removed_patterns.append(
                        pattern
                    )

        message_object.final_response = (
            response
        )

        message_object.enrichment_layers.append({
            "engine": self.engine_name,
            "wave":
                message_object.recursion_state[
                    "current_wave"
                ],
            "type": "manifestation_arbitration",
            "content": {
                "removed_patterns":
                    removed_patterns,

                "manifestation_compression":
                    True
            }
        })

        return message_object
