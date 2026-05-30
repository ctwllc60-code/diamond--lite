from core.base_engine import BaseEngine

class ConversationMomentum(BaseEngine):

    def __init__(self):
        super().__init__(
            "conversation_momentum"
        )

    def process(self, message_object):

        resonance_signals = (
            message_object.cognitive_state.get(
                "resonance_signals",
                []
            )
        )

        momentum_map = {}

        for signal in resonance_signals:

            if signal not in momentum_map:

                momentum_map[signal] = 0

            momentum_map[signal] += 1

        dominant_theme = None

        if momentum_map:

            dominant_theme = max(
                momentum_map,
                key=momentum_map.get
            )

        momentum_analysis = {
            "momentum_map":
                momentum_map,

            "dominant_theme":
                dominant_theme,

            "momentum_active":
                dominant_theme is not None
        }

        message_object.cognitive_state[
            "conversation_momentum"
        ] = momentum_analysis

        message_object.enrichment_layers.append({
            "engine": self.engine_name,
            "wave":
                message_object.recursion_state[
                    "current_wave"
                ],
            "type": "conversation_momentum",
            "content": momentum_analysis
        })

        return message_object
