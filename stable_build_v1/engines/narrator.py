from core.base_engine import BaseEngine

class Narrator(BaseEngine):

    def __init__(self):
        super().__init__("narrator")

    def process(self, message_object):

        reasoning_layers = []

        current_wave = (
            message_object.recursion_state["current_wave"]
        )

        for layer in message_object.enrichment_layers:

            if (
                layer["engine"] == "reasoning_adapter"
                and layer.get("wave") == current_wave
            ):

                reasoning_layers.extend(
                    layer["content"]["expanded_reasoning"]
                )

        response_parts = []

        if reasoning_layers:

            response_parts.append(
                "I reflected on your question carefully."
            )

            for reasoning in reasoning_layers:

                response_parts.append(reasoning)

            response_parts.append(
                "Taken together, these patterns suggest "
                "that uncertainty may feel threatening "
                "because it disrupts psychological "
                "orientation and predictability."
            )

        else:

            response_parts.append(
                "I am still organizing the cognitive "
                "structure of the response."
            )

        final_response = "\n\n".join(response_parts)

        message_object.final_response = final_response

        message_object.enrichment_layers.append({
            "engine": self.engine_name,
            "wave": current_wave,
            "type": "response_manifestation",
            "content": {
                "response_generated": True
            }
        })

        return message_object
