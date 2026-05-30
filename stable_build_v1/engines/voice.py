from core.base_engine import BaseEngine
import random


class Voice(BaseEngine):

    def __init__(self):
        super().__init__(
            "voice"
        )

    def process(self, message_object):

        response = (
            message_object.final_response
        )

        presence_modes = [

            "reflective",
            "grounded",
            "analytical",
            "conversational",
            "interpretive",
            "relational"
        ]

        pacing_styles = [

            "fluid",
            "measured",
            "layered",
            "natural"
        ]

        tone_balancing = [

            "warm",
            "neutral",
            "thoughtful",
            "human"
        ]

        selected_presence = (
            random.choice(
                presence_modes
            )
        )

        selected_pacing = (
            random.choice(
                pacing_styles
            )
        )

        selected_tone = (
            random.choice(
                tone_balancing
            )
        )

        relational_openings = [

            "I think part of what you're noticing is that",
            "What you're touching on here is something a lot of people quietly experience.",
            "One thing I think you're picking up on is that",
            "What makes this complicated for people is that",
            "I think the deeper tension underneath this is that",
            "You're pointing toward something psychologically important here."
        ]

        reflective_bridges = [

            "And once that starts happening, people usually begin looking for emotional stability somewhere.",
            "That tends to shape behavior more than people initially realize.",
            "Over time, that pressure can quietly influence decision-making.",
            "That is usually where emotional reassurance starts becoming psychologically important.",
            "A lot of people do not consciously realize that this is happening while it is happening."
        ]

        if selected_presence == "reflective":

            response = response.replace(
                "Humans fear uncertainty because",
                "One way to understand the fear of uncertainty is that"
            )

        elif selected_presence == "grounded":

            response = response.replace(
                "Humans fear uncertainty because",
                "In practical terms, people often fear uncertainty because"
            )

        elif selected_presence == "conversational":

            response = response.replace(
                "Humans fear uncertainty because",
                "A big part of why people fear uncertainty is that"
            )

        elif selected_presence == "interpretive":

            response = response.replace(
                "Humans fear uncertainty because",
                "At a deeper level, uncertainty can feel threatening because"
            )

        elif selected_presence == "relational":

            relational_intro = random.choice(
                relational_openings
            )

            response = (
                relational_intro
                + "\n\n"
                + response
            )

        if selected_tone == "warm":

            response = response.replace(
                "This fear",
                "For many people, this fear"
            )

        elif selected_tone == "human":

            response = response.replace(
                "people",
                "people emotionally"
            )

        if selected_pacing == "layered":

            response = response.replace(
                ". ",
                ".\n\n",
                2
            )

        elif selected_pacing == "natural":

            response += (
                "\n\n"
                + random.choice(
                    reflective_bridges
                )
            )

        message_object.final_response = (
            response.strip()
        )

        message_object.cognitive_state[
            "presence_identity"
        ] = {

            "presence_mode":
                selected_presence,

            "pacing_style":
                selected_pacing,

            "tone_balance":
                selected_tone
        }

        message_object.enrichment_layers.append({

            "engine":
                self.engine_name,

            "wave":
                message_object.recursion_state[
                    "current_wave"
                ],

            "type":
                "presence_modulation",

            "content": {

                "presence_mode":
                    selected_presence,

                "pacing_style":
                    selected_pacing,

                "tone_balance":
                    selected_tone,

                "presence_modulation_active":
                    True,

                "relational_cognition_active":
                    True
            }
        })

        return message_object
