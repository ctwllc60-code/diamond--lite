from core.base_engine import (
    BaseEngine
)


class Narrator(BaseEngine):

    def __init__(self):

        super().__init__(
            "narrator"
        )

    def process(
        self,
        message_object
    ):

        current_wave = (

            message_object.recursion_state[
                "current_wave"
            ]
        )

        synthesis_state = (

            message_object.cognitive_state.get(
                "synthesis_coordinator",
                {}
            )
        )

        active_reasoning_stream = (

            synthesis_state.get(
                "active_reasoning_stream",
                []
            )
        )

        cognition_environment = []

        for enrichment in active_reasoning_stream:

            cognition_environment.append({

                "engine":
                    enrichment.get(
                        "engine",
                        "unknown_engine"
                    ),

                "type":
                    enrichment.get(
                        "type",
                        "general"
                    ),

                "content":
                    enrichment.get(
                        "content",
                        {}
                    )
            })

        narrator_state = {

            "cognition_environment":
                cognition_environment,

            "manifestation_environment_ready":
                True
        }

        if cognition_environment:

            narrator_state[
                "environment_presence"
            ] = "active"

        message_object.cognitive_state[
            "narrator"
        ] = narrator_state

        message_object.enrichment_layers.append({

            "engine":
                self.engine_name,

            "wave":
                current_wave,

            "type":
                "manifestation_preparation",

            "content": {

                "manifestation_environment_ready":
                    True,

                "environment_presence":
                    "active"
            }
        })

        return message_object
