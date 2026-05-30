from core.base.base_engine import (
    BaseEngine
)


class DepthGate(BaseEngine):

    def __init__(self):

        super().__init__(
            "depth_gate"
        )

    def process(
        self,
        message_object
    ):

        raw_message = (
            message_object.raw_message
            or ""
        ).strip().lower()

        recursion_state = (
            message_object.recursion_state
        )

        current_depth = (

            recursion_state.get(
                "depth",
                0
            )
        )

        current_wave = (

            recursion_state.get(
                "current_wave",
                0
            )
        )

        depth_analysis = {

            "current_depth":
                current_depth,

            "depth_enrichment_active":
                True
        }

        if any(

            keyword in raw_message

            for keyword in [

                "feel",
                "emotion",
                "trust",
                "fear",
                "uncertainty",
                "pressure",
                "validation",
                "connection",
                "understood",
                "overwhelmed",
                "anxiety",
                "confidence"
            ]
        ):

            depth_analysis[
                "emotional_depth_alignment"
            ] = "active"

        if any(

            keyword in raw_message

            for keyword in [

                "architecture",
                "reasoning",
                "system",
                "pipeline",
                "framework",
                "orchestration",
                "philosophy",
                "meaning",
                "infrastructure"
            ]
        ):

            depth_analysis[
                "conceptual_depth_alignment"
            ] = "active"

        recursion_state[
            "recursive_trigger_engine"
        ] = self.engine_name

        message_object.cognitive_state[
            "depth_gate"
        ] = depth_analysis

        message_object.enrichment_layers.append({

            "engine":
                self.engine_name,

            "wave":
                current_wave,

            "type":
                "depth_alignment",

            "content":
                depth_analysis
        })

        return message_object
