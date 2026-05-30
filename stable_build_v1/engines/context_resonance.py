from core.base_engine import BaseEngine

class ContextResonance(BaseEngine):

    def __init__(self):
        super().__init__(
            "context_resonance"
        )

    def process(self, message_object):

        raw_message = (
            message_object.raw_message.lower()
        )

        resonance_signals = []

        recurring_patterns = [
            "uncertainty",
            "fear",
            "control",
            "identity",
            "safety",
            "stability"
        ]

        for pattern in recurring_patterns:

            if pattern in raw_message:

                resonance_signals.append(
                    pattern
                )

        resonance_analysis = {
            "resonance_signals":
                resonance_signals,

            "resonance_detected":
                len(resonance_signals) > 0
        }

        message_object.cognitive_state[
            "resonance_signals"
        ] = resonance_signals

        message_object.enrichment_layers.append({
            "engine": self.engine_name,
            "wave":
                message_object.recursion_state[
                    "current_wave"
                ],
            "type": "context_resonance",
            "content": resonance_analysis
        })

        return message_object
