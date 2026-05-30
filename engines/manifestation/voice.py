from core.base.base_engine import (
    BaseEngine
)


class Voice(BaseEngine):

    def __init__(self):

        super().__init__(
            "voice"
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

        message_object.cognitive_state[
            "presence_identity"
        ] = {

            "delivery_preserved":
                True,

            "manifestation_stable":
                True,

            "voice_passthrough_active":
                True
        }

        message_object.enrichment_layers.append({

            "engine":
                self.engine_name,

            "wave":
                message_object.recursion_state[
                    "current_wave"
                ],

            "type":
                "voice_stabilization",

            "content": {

                "delivery_preserved":
                    True,

                "manifestation_integrity_preserved":
                    True,

                "voice_passthrough_active":
                    True
            }
        })

        return message_object
