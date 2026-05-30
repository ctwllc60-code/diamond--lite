from core.base.base_engine import (
    BaseEngine
)


class SequenceDesigner(BaseEngine):

    def __init__(self):

        super().__init__(
            "sequence_designer"
        )

    def process(
        self,
        message_object
    ):

        response = (
            str(
                message_object.final_response
            )
        )

        paragraphs = (
            response.split("\n\n")
        )

        preserved_paragraphs = []

        for paragraph in paragraphs:

            preserved_paragraphs.append(
                paragraph.strip()
            )

        sequenced_response = (

            "\n\n".join(
                preserved_paragraphs
            )
        )

        message_object.final_response = (
            sequenced_response
        )

        message_object.enrichment_layers.append({

            "engine":
                self.engine_name,

            "wave":
                message_object.recursion_state[
                    "current_wave"
                ],

            "type":
                "sequence_stabilization",

            "content": {

                "sequence_preserved":
                    True,

                "manifestation_integrity_preserved":
                    True,

                "delivery_order_stabilized":
                    True
            }
        })

        return message_object
