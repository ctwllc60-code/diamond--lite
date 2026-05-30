from core.base_engine import BaseEngine

class Doorman(BaseEngine):

    def __init__(self):
        super().__init__("doorman")

    def process(self, message_object):

        raw = message_object.raw_message

        current_wave = (
            message_object.recursion_state["current_wave"]
        )

        signal_analysis = {
            "message_length": len(raw),
            "contains_question": "?" in raw,
            "uppercase_detected": raw.isupper()
        }

        message_object.enrichment_layers.append({
            "engine": self.engine_name,
            "wave": current_wave,
            "type": "signal_preservation",
            "content": signal_analysis
        })

        return message_object
