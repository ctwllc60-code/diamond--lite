from core.base_engine import BaseEngine

class HumanReception(BaseEngine):

    def __init__(self):
        super().__init__("human_reception")

    def process(self, message_object):

        response = message_object.final_response

        response_length = len(response)

        reception_analysis = {
            "response_density": "moderate",
            "emotional_pressure": "controlled",
            "psychological_accessibility": "high",
            "cognitive_load": "manageable"
        }

        if response_length > 1200:
            reception_analysis[
                "cognitive_load"
            ] = "heavy"

        if "uncertainty" in response.lower():
            reception_analysis[
                "emotional_pressure"
            ] = "elevated"

        message_object.enrichment_layers.append({
            "engine": self.engine_name,
            "wave":
                message_object.recursion_state[
                    "current_wave"
                ],
            "type": "human_reception_analysis",
            "content": reception_analysis
        })

        return message_object
