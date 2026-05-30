from core.base_engine import BaseEngine

class BehavioralHarmony(BaseEngine):

    def __init__(self):
        super().__init__("behavioral_harmony")

    def process(self, message_object):

        response = message_object.final_response

        dominance_pressure = "moderate"

        cooperative_alignment = "stable"

        if len(response) > 1500:
            dominance_pressure = "elevated"

        if (
            "you must" in response.lower()
            or "obviously" in response.lower()
        ):
            cooperative_alignment = "reduced"

        harmony_analysis = {
            "dominance_pressure":
                dominance_pressure,

            "cooperative_alignment":
                cooperative_alignment,

            "behavioral_state":
                "regulated"
        }

        message_object.enrichment_layers.append({
            "engine": self.engine_name,
            "wave":
                message_object.recursion_state[
                    "current_wave"
                ],
            "type": "behavioral_regulation",
            "content": harmony_analysis
        })

        return message_object
