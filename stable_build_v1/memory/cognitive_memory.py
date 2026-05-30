import json
import os
from datetime import datetime


MEMORY_FILE = (
    "memory/cognitive_memory.json"
)


class CognitiveMemory:

    def __init__(self):

        if not os.path.exists(
            MEMORY_FILE
        ):

            with open(
                MEMORY_FILE,
                "w"
            ) as file:

                json.dump(
                    [],
                    file
                )

    def load_memory(self):

        with open(
            MEMORY_FILE,
            "r"
        ) as file:

            return json.load(
                file
            )

    def save_memory(
        self,
        memory_log
    ):

        with open(
            MEMORY_FILE,
            "w"
        ) as file:

            json.dump(
                memory_log,
                file,
                indent=4
            )

    def store_reflection(
        self,
        raw_message,
        final_response,
        reflection_notes
    ):

        memory_log = (
            self.load_memory()
        )

        conceptual_patterns = []

        lowered_message = (
            raw_message.lower()
        )

        if (
            "uncertainty"
            in lowered_message
        ):

            conceptual_patterns.append(
                "uncertainty_reasoning"
            )

        if (
            "leadership"
            in lowered_message
        ):

            conceptual_patterns.append(
                "leadership_analysis"
            )

        if (
            "economics"
            in lowered_message
            or "inflation"
            in lowered_message
        ):

            conceptual_patterns.append(
                "economic_reasoning"
            )

        if (
            "lawsuit"
            in lowered_message
            or "legal"
            in lowered_message
        ):

            conceptual_patterns.append(
                "legal_reasoning"
            )

        if (
            "emotion"
            in lowered_message
            or "validation"
            in lowered_message
            or "trust"
            in lowered_message
        ):

            conceptual_patterns.append(
                "emotional_reasoning"
            )

        response_characteristics = {

            "response_length":
                len(
                    final_response
                ),

            "paragraph_count":
                final_response.count(
                    "\n\n"
                ) + 1,

            "reflective_tone":

                (
                    "One way to understand"
                    in final_response

                    or

                    "At a deeper level"
                    in final_response
                ),

            "systemic_reasoning":

                (
                    "systems"
                    in final_response.lower()

                    or

                    "structure"
                    in final_response.lower()
                ),

            "relational_presence":

                (
                    "you're"
                    in final_response.lower()

                    or

                    "what you're noticing"
                    in final_response.lower()

                    or

                    "part of what you're"
                    in final_response.lower()
                )
        }

        operational_state = {

            "timestamp":
                datetime.utcnow().isoformat(),

            "response_generated":
                True,

            "response_stable":

                len(
                    final_response.split()
                ) >= 40,

            "deployment_ready_memory":
                True
        }

        entry = {

            "raw_message":
                raw_message,

            "final_response":
                final_response,

            "reflection_notes":
                reflection_notes,

            "conceptual_patterns":
                conceptual_patterns,

            "response_characteristics":
                response_characteristics,

            "operational_state":
                operational_state
        }

        memory_log.append(
            entry
        )

        if len(memory_log) > 200:

            memory_log = (
                memory_log[-200:]
            )

        self.save_memory(
            memory_log
        )

    def retrieve_recent_reflections(
        self,
        limit=5
    ):

        memory_log = (
            self.load_memory()
        )

        return memory_log[-limit:]

    def retrieve_reasoning_patterns(
        self
    ):

        memory_log = (
            self.load_memory()
        )

        pattern_summary = {

            "uncertainty_reasoning":
                0,

            "leadership_analysis":
                0,

            "economic_reasoning":
                0,

            "legal_reasoning":
                0,

            "emotional_reasoning":
                0
        }

        for entry in memory_log:

            for pattern in (
                entry.get(
                    "conceptual_patterns",
                    []
                )
            ):

                if pattern in (
                    pattern_summary
                ):

                    pattern_summary[
                        pattern
                    ] += 1

        return pattern_summary

    def retrieve_operational_state(
        self
    ):

        memory_log = (
            self.load_memory()
        )

        if not memory_log:

            return {}

        latest_entry = (
            memory_log[-1]
        )

        return latest_entry.get(
            "operational_state",
            {}
        )
