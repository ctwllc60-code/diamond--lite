from core.base.base_engine import (
    BaseEngine
)


class ContentBalancer(BaseEngine):

    def __init__(self):

        super().__init__(
            "content_balancer"
        )

    def process(
        self,
        message_object
    ):

        response = str(
            message_object.final_response
        )

        memory_state = (

            message_object.cognitive_state.get(
                "memory",
                {}
            )
        )

        working_memory = (

            memory_state.get(
                "working_memory",
                []
            )
        )

        retrieval_reinforcement = []

        for memory in working_memory:

            input_text = str(

                memory.get(
                    "input",
                    ""
                )
            )

            if (
                input_text
                and input_text not in response
            ):

                retrieval_reinforcement.append(
                    input_text
                )

        repetitive_patterns = [

            "As an AI language model,",

            "As a large language model,"
        ]

        preserved_response = response

        for pattern in repetitive_patterns:

            preserved_response = (
                preserved_response.replace(
                    pattern,
                    ""
                )
            )

            preserved_response = (
                preserved_response.replace(
                    pattern + "\n\n",
                    ""
                )
            )

        preserved_response = (
            preserved_response.strip()
        )

        message_object.cognitive_state[
            "retrieval_reinforcement"
        ] = retrieval_reinforcement

        message_object.final_response = (
            preserved_response
        )

        message_object.enrichment_layers.append({

            "engine":
                self.engine_name,

            "wave":
                message_object.recursion_state[
                    "current_wave"
                ],

            "type":
                "content_stabilization",

            "content": {

                "content_preserved":
                    True,

                "manifestation_integrity_preserved":
                    True,

                "artifact_cleanup_active":
                    True,

                "retrieval_reinforcement_active":
                    True
            }
        })

        return message_object
