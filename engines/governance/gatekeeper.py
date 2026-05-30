from core.base_engine import BaseEngine

class Gatekeeper(BaseEngine):

    def __init__(self):
        super().__init__("gatekeeper")

    def process(self, message_object):

        raw = message_object.raw_message.lower()

        cognitive_mode = "general"

        if "why" in raw:
            cognitive_mode = "reflective"

        elif "how" in raw:
            cognitive_mode = "instructional"

        elif "feel" in raw:
            cognitive_mode = "emotional"

        gatekeeper_analysis = {
            "cognitive_mode": cognitive_mode,
            "enrichment_layers_seen": len(message_object.enrichment_layers)
        }

        message_object.enrichment_layers.append({
            "engine": self.engine_name,
            "type": "cognitive_posture",
            "content": gatekeeper_analysis
        })

        return message_object
