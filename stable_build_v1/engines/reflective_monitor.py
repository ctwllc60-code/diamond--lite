from core.base_engine import BaseEngine

class ReflectiveMonitor(BaseEngine):

    def __init__(self):
        super().__init__("reflective_monitor")

    def process(self, message_object):

        response = message_object.final_response

        fulfillment_status = "partial"

        reflection_notes = []

        if len(response) > 400:

            fulfillment_status = "substantial"

            reflection_notes.append(
                "response reached reflective depth"
            )

        if (
            "part of being human"
            in response.lower()
        ):

            reflection_notes.append(
                "response included emotional grounding"
            )

        if (
            "not meant to force a conclusion"
            in response.lower()
        ):

            reflection_notes.append(
                "response preserved interpretive openness"
            )

        reflection_analysis = {
            "fulfillment_status":
                fulfillment_status,

            "reflection_notes":
                reflection_notes,

            "meta_cognition_active":
                True
        }

        message_object.enrichment_layers.append({
            "engine": self.engine_name,
            "wave":
                message_object.recursion_state[
                    "current_wave"
                ],
            "type": "meta_cognitive_reflection",
            "content": reflection_analysis
        })

        return message_object
