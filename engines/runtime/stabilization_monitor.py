from core.base.base_engine import (
    BaseEngine
)


class StabilizationMonitor(BaseEngine):

    def __init__(self):

        super().__init__(
            "stabilization_monitor"
        )

    def process(
        self,
        message_object
    ):

        recursion_depth = (

            message_object.recursion_state[
                "depth"
            ]
        )

        runtime_integrity = True

        corruption_detected = False

        response_exists = bool(

            str(
                message_object.final_response
                or ""
            ).strip()
        )

        stabilization_status = (
            "stable"
        )

        if recursion_depth <= 0:

            stabilization_status = (
                "initializing"
            )

        elif recursion_depth == 1:

            stabilization_status = (
                "active"
            )

        elif recursion_depth >= 2:

            stabilization_status = (
                "stable"
            )

        if not hasattr(
            message_object,
            "cognitive_state"
        ):

            runtime_integrity = False
            corruption_detected = True

        if not hasattr(
            message_object,
            "enrichment_layers"
        ):

            runtime_integrity = False
            corruption_detected = True

        stabilization_analysis = {

            "stabilization_status":
                stabilization_status,

            "runtime_integrity":
                runtime_integrity,

            "corruption_detected":
                corruption_detected,

            "response_exists":
                response_exists,

            "recursion_depth":
                recursion_depth,

            "monitoring_scope":
                "runtime_integrity_only"
        }

        message_object.recursion_state[
            "recursive_thinking_required"
        ] = False

        message_object.cognitive_state[
            "runtime_integrity"
        ] = stabilization_analysis

        message_object.enrichment_layers.append({

            "engine":
                self.engine_name,

            "wave":

                message_object.recursion_state[
                    "current_wave"
                ],

            "type":
                "runtime_integrity_monitoring",

            "content":
                stabilization_analysis
        })

        return message_object
