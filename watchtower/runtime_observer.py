import json
import os

from datetime import (
    datetime,
    UTC
)


RUNTIME_LOG = (
    "../state/runtime_state.json"
)


class RuntimeObserver:

    def __init__(self):

        self.observer_name = (
            "watchtower_runtime_observer"
        )

        self.last_observation = None

        self.runtime_visibility = {
            "runtime_detected": False,
            "runtime_health": None,
            "infrastructure_score": None,
            "cycle_status": None,
            "scheduler_health": None
        }

    def runtime_exists(
        self
    ):

        return os.path.exists(
            RUNTIME_LOG
        )

    def load_runtime_state(
        self
    ):

        if not self.runtime_exists():

            return None

        with open(
            RUNTIME_LOG,
            "r"
        ) as file:

            return json.load(
                file
            )

    def observe_runtime(
        self
    ):

        runtime_state = (
            self.load_runtime_state()
        )

        if not runtime_state:

            self.runtime_visibility[
                "runtime_detected"
            ] = False

            return (
                self.runtime_visibility
            )

        self.runtime_visibility[
            "runtime_detected"
        ] = True

        self.runtime_visibility[
            "runtime_health"
        ] = runtime_state.get(
            "runtime_health"
        )

        self.runtime_visibility[
            "infrastructure_score"
        ] = runtime_state.get(
            "infrastructure_score"
        )

        self.runtime_visibility[
            "cycle_status"
        ] = runtime_state.get(
            "cycle_status"
        )

        self.runtime_visibility[
            "scheduler_health"
        ] = runtime_state.get(
            "scheduler_health"
        )

        self.last_observation = (
            datetime.now(
                UTC
            ).isoformat()
        )

        return (
            self.runtime_visibility
        )
