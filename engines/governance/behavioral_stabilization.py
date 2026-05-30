from core.base_engine import BaseEngine

class BehavioralStabilization(BaseEngine):

    def __init__(self):
        super().__init__(
            "behavioral_stabilization"
        )

    def process(self, message_object):

        response = message_object.final_response

        dominance_pressure = "unknown"

        for layer in message_object.enrichment_layers:

            if layer["engine"] == "behavioral_harmony":

                dominance_pressure = (
                    layer["content"][
                        "dominance_pressure"
                    ]
                )

        if dominance_pressure == "elevated":

            response += (
                "\n\n"
                "At the same time, there may be "
                "multiple valid ways to interpret "
                "these patterns depending on "
                "individual experience and context."
            )

        if dominance_pressure == "moderate":

            response += (
                "\n\n"
                "These reflections are not meant "
                "to force a conclusion, but to help "
                "explore possible patterns beneath "
                "the question."
            )

        message_object.final_response = response

        message_object.enrichment_layers.append({
            "engine": self.engine_name,
            "wave":
                message_object.recursion_state[
                    "current_wave"
                ],
            "type": "behavioral_stabilization",
            "content": {
                "dominance_pressure_detected":
                    dominance_pressure,

                "stabilization_applied": True
            }
        })

        return message_object
