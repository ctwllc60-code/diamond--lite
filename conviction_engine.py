from core.base.base_engine import (
    BaseEngine
)


class ConvictionEngine(BaseEngine):

    def __init__(self):
        super().__init__(
            "conviction_engine"
        )

    def process(
        self,
        message_object
    ):

        raw_message = (
            message_object.raw_message
            or ""
        ).lower()

        current_wave = (
            message_object.recursion_state[
                "current_wave"
            ]
        )

        conviction_level = (
            "grounded"
        )

        reasoning_posture = (
            "confident"
        )

        delivery_weight = (
            "balanced"
        )

        clarity_pressure = (
            "standard"
        )

        certainty_bias = (
            "stable"
        )

        leadership_energy = (
            "measured"
        )

        forbidden_hedging = [

            "maybe",

            "might",

            "perhaps",

            "possibly",

            "it could be argued",

            "one could argue",

            "you may want to",

            "consider trying",

            "i think",

            "it seems"
        ]

        # --------------------------------------------------
        # CONVICTION SIGNAL DETECTION
        # --------------------------------------------------

        if any(
            keyword in raw_message
            for keyword in [
                "how",
                "build",
                "design",
                "create",
                "fix",
                "solve",
                "implement"
            ]
        ):

            conviction_level = (
                "elevated"
            )

            delivery_weight = (
                "direct"
            )

            clarity_pressure = (
                "high"
            )

        if any(
            keyword in raw_message
            for keyword in [
                "architecture",
                "system",
                "pipeline",
                "orchestration",
                "framework",
                "reasoning",
                "cognition"
            ]
        ):

            conviction_level = (
                "high"
            )

            leadership_energy = (
                "active"
            )

            delivery_weight = (
                "assertive"
            )

        if any(
            keyword in raw_message
            for keyword in [
                "confused",
                "uncertain",
                "stuck",
                "lost",
                "overwhelmed"
            ]
        ):

            reasoning_posture = (
                "stabilizing"
            )

            clarity_pressure = (
                "very_high"
            )

            certainty_bias = (
                "grounded"
            )

        # --------------------------------------------------
        # CONVICTION PROFILE
        # --------------------------------------------------

        conviction_profile = {

            "level":
                conviction_level,

            "confidence_calibration":
                "active",

            "certainty_weighting":
                "active",

            "conclusion_stabilization":
                "active",

            "hesitation_reduction":
                "active",

            "delivery_reinforcement":
                "active",

            "grounded_decisiveness_tuning":
                "active",

            "voice_directive":
                "assertive",

            "reasoning_posture":
                reasoning_posture,

            "communication_weight":
                delivery_weight,

            "clarity_pressure":
                clarity_pressure,

            "leadership_energy":
                leadership_energy,

            "certainty_bias":
                certainty_bias,

            "hedging_forbidden":
                True,

            "forbidden_hedging":
                forbidden_hedging
        }

        message_object.cognitive_state[
            "conviction_profile"
        ] = conviction_profile

        message_object.enrichment_layers.append({

            "engine":
                self.engine_name,

            "wave":
                current_wave,

            "type":
                "conviction_alignment",

            "content":
                conviction_profile
        })

        return message_object
