from core.base_engine import BaseEngine

class AtmosphereCondition(BaseEngine):

    def __init__(self):
        super().__init__("atmosphere_condition")

    def process(self, message_object):

        response = message_object.final_response

        emotional_pressure = "unknown"

        for layer in message_object.enrichment_layers:

            if layer["engine"] == "human_reception":

                emotional_pressure = (
                    layer["content"][
                        "emotional_pressure"
                    ]
                )

        if emotional_pressure == "elevated":

            response += (
                "\n\n"
                "At the same time, uncertainty is "
                "also part of being human. Most "
                "people are navigating forms of it "
                "constantly, even when they appear "
                "stable externally."
            )

        if emotional_pressure == "controlled":

            response += (
                "\n\n"
                "This level of reflection can help "
                "people understand their reactions "
                "more clearly over time."
            )

        message_object.final_response = response

        message_object.enrichment_layers.append({
            "engine": self.engine_name,
            "wave":
                message_object.recursion_state[
                    "current_wave"
                ],
            "type": "atmosphere_adaptation",
            "content": {
                "emotional_pressure_detected":
                    emotional_pressure
            }
        })

        return message_object
