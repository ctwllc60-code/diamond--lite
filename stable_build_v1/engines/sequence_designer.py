from core.base_engine import BaseEngine
import random


class SequenceDesigner(BaseEngine):

    def __init__(self):

        super().__init__(
            "sequence_designer"
        )

    def process(self, message_object):

        response = (
            message_object.final_response
        )

        paragraphs = (
            response.split("\n\n")
        )

        soft_prefixes = [

            "One important layer here is that",
            "What makes this more complicated is that",
            "Another factor worth paying attention to is that",
            "In practice,",
            "At a systems level,",
            "One thing many people underestimate is that"
        ]

        reflective_endings = [

            "That pressure tends to accumulate gradually.",
            "This tends to influence behavior more than expected.",
            "Over time, these pressures reshape decision-making.",
            "That dynamic can slowly alter the broader environment."
        ]

        relational_protection_phrases = [

            "I think",
            "You're pointing toward",
            "What you're noticing",
            "What makes this difficult",
            "A lot of people quietly",
            "Part of what happens",
            "It's interesting how",
            "You can start seeing how",
            "What often starts happening"
        ]

        redesigned_paragraphs = []

        connector_words = [

            "moreover",
            "furthermore",
            "additionally",
            "ultimately",
            "in essence",
            "firstly",
            "secondly"
        ]

        total_paragraphs = len(
            paragraphs
        )

        for index, paragraph in enumerate(
            paragraphs
        ):

            paragraph = (
                paragraph.strip()
            )

            if not paragraph:
                continue

            lowered = (

                paragraph[:1].lower()
                + paragraph[1:]
            )

            first_word = (

                lowered.split(" ")[0]
                .replace(",", "")
                .lower()
            )

            protected_relational = any(

                lowered.startswith(
                    phrase.lower()
                )

                for phrase in relational_protection_phrases
            )

            rebuilt = lowered

            if first_word not in connector_words:

                should_prefix = (

                    index > 0
                    and not protected_relational
                    and len(paragraph.split()) > 22
                    and random.random() > 0.72
                )

                if should_prefix:

                    selected_prefix = (
                        random.choice(
                            soft_prefixes
                        )
                    )

                    rebuilt = (
                        selected_prefix
                        + " "
                        + rebuilt
                    )

            should_close = (

                not protected_relational
                and index < (
                    total_paragraphs - 1
                )
                and len(paragraph.split()) > 45
                and random.random() > 0.92
            )

            if should_close:

                selected_ending = (
                    random.choice(
                        reflective_endings
                    )
                )

                if selected_ending.lower() not in rebuilt.lower():

                    rebuilt = (
                        rebuilt
                        + " "
                        + selected_ending
                    )

            rebuilt = (
                rebuilt[:1].upper()
                + rebuilt[1:]
            )

            redesigned_paragraphs.append(
                rebuilt
            )

        sequenced_response = (

            "\n\n".join(
                redesigned_paragraphs
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
                "natural_sequence_design",

            "content": {

                "sequence_optimized":
                    True,

                "academic_reduction_active":
                    True,

                "natural_flow_cleanup":
                    True,

                "relational_flow_stabilized":
                    True,

                "artifact_suppression_active":
                    True,

                "behavioral_stabilization_active":
                    True
            }
        })

        return message_object
