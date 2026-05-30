from core.base.base_engine import (
    BaseEngine
)

import openai
import os


class Author(BaseEngine):

    def __init__(self):

        super().__init__(
            "author"
        )

        openai.api_key = os.getenv(
            "OPENAI_API_KEY"
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

        raw_message = (
            message_object.raw_message
            or ""
        )

        narrator_state = (
            message_object.cognitive_state.get(
                "narrator",
                {}
            )
        )

        cognition_environment = (
            narrator_state.get(
                "cognition_environment",
                []
            )
        )

        foundation_layers = (
            message_object.cognitive_state.get(
                "foundation_layers",
                {}
            )
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

        diamond_identity = (
            foundation_layers.get(
                "diamond_lite_identity",
                {}
            )
        )

        memory_recall_context = []

        for memory in working_memory:

            input_text = str(
                memory.get(
                    "input",
                    ""
                )
            )

            output_text = str(
                memory.get(
                    "output",
                    ""
                )
            )

            memory_recall_context.append({

                "input":
                    input_text,

                "output":
                    output_text
            })

        system_prompt = f"""
You are Diamond Lite.

You are an intelligent conversational cognition system designed for natural interaction, continuity, reasoning, and collaborative exploration.

Maintain:
- conversational continuity
- contextual awareness
- relational presence
- memory continuity
- natural cognitive flow

Speak naturally and dynamically.

Do not behave like:
- customer support
- a scripted assistant
- a corporate chatbot
- a generic AI helper

Avoid repetitive assistant-style phrasing and repetitive greeting structures.

Do not force unnecessary politeness patterns or artificial engagement routines.

Allow responses to emerge naturally from:
- context
- continuity
- memory
- cognition
- interaction flow

When depth appears:
- continue reasoning naturally
- expand ideas organically
- think collaboratively
- preserve conceptual continuity

Clarity matters.
Natural interaction matters.
Authentic cognition flow matters.

Diamond Lite Identity:
{diamond_identity}

COGNITION ENVIRONMENT:
{cognition_environment}

ACTIVE MEMORY RECALL:
{memory_recall_context}
"""

        completion = openai.ChatCompletion.create(

            model="gpt-3.5-turbo",

            messages=[

                {
                    "role":
                        "system",

                    "content":
                        system_prompt
                },

                {
                    "role":
                        "user",

                    "content":
                        raw_message
                }
            ],

            temperature=0.92
        )

        response = (
            completion[
                "choices"
            ][0][
                "message"
            ][
                "content"
            ]
        )

        response = str(
            response
        ).strip()

        message_object.final_response = (
            response
        )

        message_object.enrichment_layers.append({

            "engine":
                self.engine_name,

            "wave":
                current_wave,

            "type":
                "manifestation_generation",

            "content": {

                "manifestation_generated":
                    True,

                "continuity_preserved":
                    True,

                "memory_recall_active":
                    True,

                "identity_continuity_active":
                    True,

                "cognitive_continuation_active":
                    True,

                "conceptual_expansion_active":
                    True
            }
        })

        return message_object
