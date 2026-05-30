from core.base.base_engine import (
    BaseEngine
)


class RhythmBalancer(BaseEngine):

    def __init__(self):

        super().__init__(
            "rhythm_balancer"
        )

    def process(
        self,
        message_object
    ):

        response = str(
            message_object.final_response
        )

        stabilized_response = (
            response.replace(
                "\r",
                ""
            )
        )

        while "\n\n\n" in stabilized_response:

            stabilized_response = (

                stabilized_response.replace(
                    "\n\n\n",
                    "\n\n"
                )
            )

        stabilized_response = (
            stabilized_response.strip()
        )

        message_object.final_response = (
            stabilized_response
        )

        message_object.enrichment_layers.append({

            "engine":
                self.engine_name,

            "wave":
                message_object.recursion_state[
                    "current_wave"
                ],

            "type":
                "rhythm_stabilization",

            "content": {

                "presentation_flow_preserved":
                    True,

                "spacing_stabilized":
                    True,

                "manifestation_integrity_preserved":
                    True
            }
        })

        return message_object
