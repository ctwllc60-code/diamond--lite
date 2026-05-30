import json
import os

from datetime import (
    datetime,
    UTC
)


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)


class CognitiveMemory:

    def __init__(
        self
    ):

        self.instance_id = os.getenv(
            "DIAMOND_INSTANCE_ID",
            "default_instance"
        )

        self.instance_memory_dir = os.path.join(

            BASE_DIR,
            "users",
            self.instance_id,
            "memory"
        )

        if not os.path.exists(
            self.instance_memory_dir
        ):

            os.makedirs(
                self.instance_memory_dir
            )

        self.memory_file = os.path.join(

            self.instance_memory_dir,
            "cognitive_memory.json"
        )

        if not os.path.exists(
            self.memory_file
        ):

            with open(
                self.memory_file,
                "w"
            ) as file:

                json.dump(
                    [],
                    file
                )

    def load_memory(
        self
    ):

        with open(
            self.memory_file,
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
            self.memory_file,
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

        behavioral_preferences = []

        lowered_message = (
            raw_message.lower()
        )

        lowered_response = str(
            final_response
        ).lower()

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

        if (
            "repeat"
            in lowered_message
            or "repetitive"
            in lowered_message
        ):

            behavioral_preferences.append(
                "avoid_repetitive_expression"
            )

        if (
            "creative"
            in lowered_message
            or "variation"
            in lowered_message
        ):

            behavioral_preferences.append(
                "increase_creative_variation"
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
                    "one way to understand"
                    in lowered_response

                    or

                    "at a deeper level"
                    in lowered_response
                ),

            "systemic_reasoning":
                (
                    "systems"
                    in lowered_response

                    or

                    "structure"
                    in lowered_response
                ),

            "relational_presence":
                (
                    "you're"
                    in lowered_response

                    or

                    "what you're noticing"
                    in lowered_response

                    or

                    "part of what you're"
                    in lowered_response
                ),

            "creative_variation_expected":
                (
                    "avoid_repetitive_expression"
                    in behavioral_preferences
                )
        }

        repetitive_response_detected = False

        recent_entries = memory_log[-5:]

        normalized_response = (
            lowered_response.strip()
        )

        for entry in recent_entries:

            previous_response = str(

                entry.get(
                    "final_response",
                    ""
                )

            ).lower().strip()

            if (
                previous_response
                == normalized_response
            ):

                repetitive_response_detected = True

                break

        operational_state = {

            "timestamp":
                datetime.now(
                    UTC
                ).isoformat(),

            "response_generated":
                True,

            "response_stable":
                len(
                    final_response.split()
                ) >= 40,

            "deployment_ready_memory":
                True,

            "adaptive_behavior_active":
                True,

            "repetitive_response_detected":
                repetitive_response_detected,

            "instance_id":
                self.instance_id
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

            "behavioral_preferences":
                behavioral_preferences,

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

        return memory_log[
            -limit:
        ]

    def retrieve_reasoning_patterns(
        self
    ):

        memory_log = (
            self.load_memory()
        )

        pattern_summary = {

            "leadership_analysis":
                0,

            "economic_reasoning":
                0,

            "legal_reasoning":
                0,

            "emotional_reasoning":
                0,

            "avoid_repetitive_expression":
                0,

            "increase_creative_variation":
                0
        }

        for entry in memory_log:

            for pattern in (
                entry.get(
                    "conceptual_patterns",
                    []
                )
            ):

                if pattern in pattern_summary:

                    pattern_summary[
                        pattern
                    ] += 1

            for preference in (
                entry.get(
                    "behavioral_preferences",
                    []
                )
            ):

                if preference in pattern_summary:

                    pattern_summary[
                        preference
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
