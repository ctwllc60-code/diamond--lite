import json

import os

from datetime import (
    datetime,
    UTC
)


MEMORY_LOG = (
    "../state/watchtower_operational_memory.json"
)


class OperationalMemory:

    def __init__(self):

        self.memory_name = (
            "watchtower_operational_memory"
        )

        self.maximum_memory_entries = 1000

        self.ensure_memory_log_exists()

    def ensure_memory_log_exists(
        self
    ):

        if not os.path.exists(
            MEMORY_LOG
        ):

            with open(
                MEMORY_LOG,
                "w"
            ) as file:

                json.dump(
                    [],
                    file,
                    indent=4
                )

    def load_memory_log(
        self
    ):

        with open(
            MEMORY_LOG,
            "r"
        ) as file:

            return json.load(
                file
            )

    def save_memory_log(
        self,
        memory_log
    ):

        with open(
            MEMORY_LOG,
            "w"
        ) as file:

            json.dump(
                memory_log,
                file,
                indent=4
            )

    def record_operational_memory(
        self,
        oversight_cycle
    ):

        memory_log = (
            self.load_memory_log()
        )

        memory_entry = {
            "timestamp": (
                datetime.now(
                    UTC
                ).isoformat()
            ),

            "runtime_health": (
                oversight_cycle[
                    "runtime_visibility"
                ].get(
                    "runtime_health"
                )
            ),

            "cycle_status": (
                oversight_cycle[
                    "runtime_visibility"
                ].get(
                    "cycle_status"
                )
            ),

            "scheduler_health": (
                oversight_cycle[
                    "runtime_visibility"
                ].get(
                    "scheduler_health"
                )
            ),

            "infrastructure_score": (
                oversight_cycle[
                    "infrastructure_score"
                ].get(
                    "infrastructure_score"
                )
            ),

            "resilience_score": (
                oversight_cycle[
                    "resilience_analysis"
                ].get(
                    "resilience_score"
                )
            ),

            "predictive_score": (
                oversight_cycle[
                    "predictive_analysis"
                ].get(
                    "predictive_score"
                )
            )
        }

        memory_log.append(
            memory_entry
        )

        if (
            len(memory_log)
            > self.maximum_memory_entries
        ):

            memory_log = (
                memory_log[
                    -self.maximum_memory_entries:
                ]
            )

        self.save_memory_log(
            memory_log
        )

    def retrieve_operational_memory(
        self,
        limit=25
    ):

        memory_log = (
            self.load_memory_log()
        )

        return memory_log[-limit:]

    def analyze_memory_patterns(
        self
    ):

        memory_log = (
            self.load_memory_log()
        )

        total_entries = len(
            memory_log
        )

        instability_events = 0

        degraded_scores = 0

        for entry in memory_log:

            if (
                entry.get(
                    "runtime_health"
                )
                != "stable"
            ):

                instability_events += 1

            if (
                entry.get(
                    "infrastructure_score",
                    100
                )
                < 80
            ):

                degraded_scores += 1

        return {
            "memory_entries": (
                total_entries
            ),

            "instability_events": (
                instability_events
            ),

            "degraded_infrastructure_events": (
                degraded_scores
            ),

            "analysis_timestamp": (
                datetime.now(
                    UTC
                ).isoformat()
            )
        }
