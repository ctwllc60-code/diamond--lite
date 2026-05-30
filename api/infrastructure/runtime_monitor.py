import os
import json
import logging

from datetime import (
    datetime,
    UTC
)


BASE_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "../.."
    )
)

STATE_FILE = os.path.join(
    BASE_DIR,
    "state",
    "server_runtime_state.json"
)


class RuntimeMonitor:

    def __init__(
        self
    ):

        self.runtime_state_file = (
            STATE_FILE
        )

    def load_runtime_state(
        self
    ):

        with open(
            self.runtime_state_file,
            "r"
        ) as file:

            return json.load(
                file
            )

    def save_runtime_state(
        self,
        runtime_state
    ):

        with open(
            self.runtime_state_file,
            "w"
        ) as file:

            json.dump(

                runtime_state,

                file,

                indent=4
            )

    def mark_runtime_heartbeat(
        self
    ):

        runtime_state = (
            self.load_runtime_state()
        )

        runtime_state[
            "last_heartbeat"
        ] = datetime.now(
            UTC
        ).isoformat()

        self.save_runtime_state(
            runtime_state
        )

        logging.info(
            "Runtime heartbeat updated."
        )

    def get_runtime_snapshot(
        self
    ):

        runtime_state = (
            self.load_runtime_state()
        )

        return {

            "runtime_status":
                runtime_state.get(
                    "runtime_status"
                ),

            "total_requests":
                runtime_state.get(
                    "total_requests"
                ),

            "successful_requests":
                runtime_state.get(
                    "successful_requests"
                ),

            "failed_requests":
                runtime_state.get(
                    "failed_requests"
                ),

            "last_active_user":
                runtime_state.get(
                    "last_active_user"
                ),

            "last_heartbeat":
                runtime_state.get(
                    "last_heartbeat"
                )
        }
