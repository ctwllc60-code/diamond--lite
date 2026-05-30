import json

from datetime import (
    datetime,
    UTC
)


STATE_HISTORY_LOG = (
    "../state/watchtower_state_history.json"
)


class AnomalyWatcher:

    def __init__(self):

        self.watcher_name = (
            "watchtower_anomaly_watcher"
        )

        self.minimum_history_required = 2

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

    def evaluate_operational_drift(
        self
    ):

        history_log = (
            self.load_state_history()
        )

        if (
            len(history_log)
            < self.minimum_history_required
        ):

            return {
                "drift_detected": False,
                "drift_reason": (
                    "insufficient_history"
                ),
                "analysis_timestamp": (
                    datetime.now(
                        UTC
                    ).isoformat()
                )
            }

        latest_state = (
            history_log[-1]
        )

        previous_state = (
            history_log[-2]
        )

        detected_drift = []

        if (
            latest_state.get(
                "runtime_health"
            )
            != previous_state.get(
                "runtime_health"
            )
        ):

            detected_drift.append(
                "runtime_health_changed"
            )

        if (
            latest_state.get(
                "scheduler_health"
            )
            != previous_state.get(
                "scheduler_health"
            )
        ):

            detected_drift.append(
                "scheduler_health_changed"
            )

        if (
            latest_state.get(
                "cycle_status"
            )
            != previous_state.get(
                "cycle_status"
            )
        ):

            detected_drift.append(
                "cycle_status_changed"
            )

        return {
            "drift_detected": (
                len(detected_drift) > 0
            ),

            "detected_drift": (
                detected_drift
            ),

            "analysis_timestamp": (
                datetime.now(
                    UTC
                ).isoformat()
            )
        }
