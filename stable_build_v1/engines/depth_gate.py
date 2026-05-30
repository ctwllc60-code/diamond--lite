from core.base_engine import BaseEngine


class DepthGate(BaseEngine):

    def __init__(self):

        super().__init__(
            "depth_gate"
        )

    def process(self, message_object):

        total_layers = len(
            message_object.enrichment_layers
        )

        recursion_state = (
            message_object.recursion_state
        )

        current_depth = (
            recursion_state.get(
                "depth",
                0
            )
        )

        max_depth = (
            recursion_state.get(
                "max_loops",
                2
            )
        )

        raw_message = (
            message_object.raw_message
            .strip()
        )

        word_count = len(
            raw_message.split()
        )

        emotional_language = [

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

        emotionally_weighted = any(

            word in raw_message.lower()

            for word in emotional_language
        )

        recursive_required = False

        depth_status = "stable"

        if (

            word_count > 120
            and current_depth < 1
            and not emotionally_weighted
        ):

            recursive_required = True

            depth_status = (
                "recursive_expansion"
            )

        elif (

            word_count > 250
            and current_depth < max_depth
            and not emotionally_weighted
        ):

            recursive_required = True

            depth_status = (
                "deep_recursive_expansion"
            )

        elif (

            emotionally_weighted
            and word_count < 220
        ):

            recursive_required = False

            depth_status = (
                "emotionally_stabilized_depth"
            )

        recursion_state[
            "recursive_thinking_required"
        ] = recursive_required

        recursion_state[
            "recursive_trigger_engine"
        ] = self.engine_name

        depth_analysis = {

            "depth_status":
                depth_status,

            "total_layers_seen":
                total_layers,

            "word_count":
                word_count,

            "current_depth":
                current_depth,

            "max_depth":
                max_depth,

            "emotionally_weighted":
                emotionally_weighted,

            "requires_recursive_thinking":
                recursive_required
        }

        message_object.enrichment_layers.append({

            "engine":
                self.engine_name,

            "wave":
                recursion_state.get(
                    "current_wave",
                    0
                ),

            "type":
                "depth_evaluation",

            "content":
                depth_analysis
        })

        return message_object
