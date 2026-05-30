from core.base_engine import BaseEngine

class ConversationalPresence(BaseEngine):

    def __init__(self):
        super().__init__("conversational_presence")

    def process(self, message_object):

        response = message_object.final_response

        if response:

            enhanced_response = (
                "I spent some time sitting with "
                "your question before responding.\n\n"
                + response +
                "\n\n"
                "Questions like this usually carry "
                "more than surface-level curiosity. "
                "They often connect to how humans "
                "experience safety, control, and "
                "orientation in uncertain situations."
            )

            message_object.final_response = (
                enhanced_response
            )

        message_object.enrichment_layers.append({
            "engine": self.engine_name,
            "wave":
                message_object.recursion_state[
                    "current_wave"
                ],
            "type": "relational_presence",
            "content": {
                "presence_applied": True
            }
        })

        return message_object
