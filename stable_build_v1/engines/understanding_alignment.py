from core.base_engine import BaseEngine

class UnderstandingAlignment(BaseEngine):

    def __init__(self):
        super().__init__("understanding_alignment")

    def process(self, message_object):

        raw = message_object.raw_message.lower()

        inferred_need = "general_understanding"

        if "why" in raw:
            inferred_need = "deep_reflection"

        elif "how" in raw:
            inferred_need = "guided_instruction"

        elif "help" in raw:
            inferred_need = "support"

        alignment_analysis = {
            "inferred_need": inferred_need,
            "layers_processed": len(message_object.enrichment_layers)
        }

        message_object.enrichment_layers.append({
            "engine": self.engine_name,
            "type": "understanding_alignment",
            "content": alignment_analysis
        })

        return message_object
