import json
import os

from datetime import (
    datetime,
    UTC
)

from core.base.base_engine import (
    BaseEngine
)


RUNTIME_STATE_PATH = (
    "state/runtime_state.json"
)


class ReflectiveMonitor(BaseEngine):

    def __init__(self):

        super().__init__(
            "reflective_monitor"
        )

    def ensure_runtime_directory(
        self
    ):

        runtime_directory = os.path.dirname(
            RUNTIME_STATE_PATH
        )

        if runtime_directory:

            os.makedirs(

                runtime_directory,

                exist_ok=True
            )

    def export_runtime_state(
        self,
        message_object,
        reflection_analysis
    ):

        self.ensure_runtime_directory()

        runtime_state = {

            "runtime_detected":
                True,

            "runtime_health":
                "stable",

            "pipeline_connected":
                True,

            "pipeline_status":
                "active",

            "watchtower_bridge_active":
                True,

            "active_pipeline":
                "diamond_primary_pipeline",

            "active_engine":
                self.engine_name,

            "cycle_status":
                "completed",

            "scheduler_health":
                "stable",

            "infrastructure_score":
                "operational",

            "last_runtime_cycle":
                datetime.now(
                    UTC
                ).isoformat(),

            "reflection_analysis":
                reflection_analysis,

            "enrichment_layer_count":
                len(
                    message_object.enrichment_layers
                ),

            "current_wave":
                message_object.recursion_state.get(
                    "current_wave"
                )
        }

        with open(
            RUNTIME_STATE_PATH,
            "w"
        ) as runtime_file:

            json.dump(

                runtime_state,

                runtime_file,

                indent=4
            )

    def process(
        self,
        message_object
    ):

        response = (
            message_object.final_response
        )

        if response is None:

            response = ""

        response = str(
            response
        )

        fulfillment_status = (
            "partial"
        )

        reflection_notes = []

        if len(response) > 400:

            fulfillment_status = (
                "substantial"
            )

            reflection_notes.append(
                "response reached reflective depth"
            )

        if (
            "part of being human"
            in response.lower()
        ):

            reflection_notes.append(
                "response included emotional grounding"
            )

        if (
            "not meant to force a conclusion"
            in response.lower()
        ):

            reflection_notes.append(
                "response preserved interpretive openness"
            )

        reflection_analysis = {

            "fulfillment_status":
                fulfillment_status,

            "reflection_notes":
                reflection_notes,

            "meta_cognition_active":
                True,

            "watchtower_bridge_active":
                True
        }

        self.export_runtime_state(

            message_object,

            reflection_analysis
        )

        message_object.enrichment_layers.append({

            "engine":
                self.engine_name,

            "wave":
                message_object.recursion_state[
                    "current_wave"
                ],

            "type":
                "meta_cognitive_reflection",

            "content":
                reflection_analysis
        })

        return message_object
