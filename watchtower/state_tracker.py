import json
import os

from datetime import (
    datetime,
    UTC
)


STATE_HISTORY_LOG = (
    "../state/watchtower_state_history.json"
)


class StateTracker:

    def __init__(self):

        self.tracker_name = (
            "watchtower_state_tracker"
        )

        self.maximum_history_size = 250

        self.ensure_state_history_exists()

    def ensure_state_history_exists(
        self
    ):

        if not os.path.exists(
            STATE_HISTORY_LOG
        ):

            with open(
                STATE_HISTORY_LOG,
                "w"
            ) as file:

                json.dump(
                    [],
                    file,
                    indent=4
                )

    def load_state_history(
        self
    ):

        with open(
            STATE_HISTORY_LOG,
            "r"
        ) as file:

            return json.load(
                file
            )

    def save_state_history(
        self,
        history_log
    ):

        with open(
            STATE_HISTORY_LOG,
            "w"
        ) as file:

            json.dump(
                history_log,
                file,
                indent=4
            )

    def record_runtime_visibility(
        self,
        runtime_visibility
    ):

        history_log = (
            self.load_state_history()
        )

        observation_entry = {
            "timestamp": (
                datetime.now(
                    UTC
                ).isoformat()
            ),

            "runtime_detected": (
                runtime_visibility.get(
                    "runtime_detected"
                )
            ),

            "runtime_health": (
                runtime_visibility.get(
                    "runtime_health"
                )
            ),

            "infrastructure_score": (
                runtime_visibility.get(
                    "infrastructure_score"
                )
            ),

            "cycle_status": (
                runtime_visibility.get(
                    "cycle_status"
                )
            ),

            "scheduler_health": (
                runtime_visibility.get(
                    "scheduler_health"
                )
            )
        }

        history_log.append(
            observation_entry
        )

        if (
            len(history_log)
            > self.maximum_history_size
        ):

            history_log = (
                history_log[
                    -self.maximum_history_size:
                ]
            )

        self.save_state_history(
            history_log
        )

    def retrieve_recent_history(
        self,
        limit=10
    ):

        history_log = (
            self.load_state_history()
        )

        return history_log[-limit:]
