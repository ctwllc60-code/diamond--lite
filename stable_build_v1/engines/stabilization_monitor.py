from core.base_engine import BaseEngine

class StabilizationMonitor(BaseEngine):

    def __init__(self):
        super().__init__("stabilization_monitor")

    def process(self, message_object):

        recursion_depth = (
            message_object.recursion_state["depth"]
        )

        stabilization_status = "unstable"

        if recursion_depth >= 1:
            stabilization_status = "stabilizing"

        if recursion_depth >= 2:
            stabilization_status = "stable"

            message_object.recursion_state[
                "recursive_thinking_required"
            ] = False

        stabilization_analysis = {
            "stabilization_status":
                stabilization_status,

            "recursion_depth":
                recursion_depth,

            "recursive_thinking_required":
                message_object.recursion_state[
                    "recursive_thinking_required"
                ]
        }

        message_object.enrichment_layers.append({
            "engine": self.engine_name,
            "wave":
                message_object.recursion_state[
                    "current_wave"
                ],
            "type": "cognitive_stabilization",
            "content": stabilization_analysis
        })

        return message_object
