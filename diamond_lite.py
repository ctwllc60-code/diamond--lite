import sys
import os
import json

from datetime import (
    datetime,
    UTC
)

sys.path.append(
    os.path.abspath(
        os.path.dirname(__file__)
    )
)

from orchestration.orchestrator import (
    Orchestrator
)

from core.schemas.message_object import (
    MessageObject
)

from app.runtime_session import (
    RuntimeSession
)


APP_STATE_FILE = (
    "app/state/app_state.json"
)


class DiamondLiteApp:

    def __init__(
        self,
        user_id="default_user"
    ):

        self.app_name = (
            "Diamond Lite"
        )

        self.runtime_status = (
            "active"
        )

        self.user_session = (
            RuntimeSession(
                user_id
            )
        )

        self.user_context = (
            self.user_session.get_user_context()
        )

        os.environ[
            "DIAMOND_INSTANCE_ID"
        ] = self.user_context[
            "user_id"
        ]

        self.orchestrator = (
            Orchestrator()
        )

        self.initialize_app_state()

    def initialize_app_state(
        self
    ):

        if not os.path.exists(
            APP_STATE_FILE
        ):

            with open(
                APP_STATE_FILE,
                "w"
            ) as file:

                json.dump(
                    {},
                    file,
                    indent=4
                )

    def load_app_state(
        self
    ):

        with open(
            APP_STATE_FILE,
            "r"
        ) as file:

            return json.load(
                file
            )

    def save_app_state(
        self,
        app_state
    ):

        with open(
            APP_STATE_FILE,
            "w"
        ) as file:

            json.dump(

                app_state,

                file,

                indent=4
            )

    def update_runtime_state(
        self,
        user_input
    ):

        app_state = (
            self.load_app_state()
        )

        app_state[
            "active_user"
        ] = self.user_context[
            "user_id"
        ]

        app_state[
            "last_user_input"
        ] = user_input

        app_state[
            "last_activity"
        ] = datetime.now(
            UTC
        ).isoformat()

        app_state[
            "runtime_status"
        ] = "active"

        self.save_app_state(
            app_state
        )

    def process_message(
        self,
        user_input
    ):

        self.update_runtime_state(
            user_input
        )

        message = MessageObject(

            raw_message=user_input,

            developer_mode=False
        )

        result = self.orchestrator.run(
            message
        )

        return str(
            result.final_response
        ).strip()


if __name__ == "__main__":

    user_id = input(
        "\nEnter User ID: "
    ).strip()

    if not user_id:

        user_id = (
            "default_user"
        )

    app = (
        DiamondLiteApp(
            user_id
        )
    )

    print(
        f"\nDiamond Lite Active For: {user_id}\n"
    )

    while True:

        lines = []

        while True:

            line = input(
                "\nUser: "
                if not lines
                else ""
            )

            if (
                line.lower().strip()
                == "exit"
            ):
                exit()

            if (
                line.lower().strip()
                == "send"
            ):
                break

            lines.append(
                line
            )

        user_input = (
            "\n".join(
                lines
            ).strip()
        )

        if not user_input:
            continue

        response = app.process_message(
            user_input
        )

        print(
            f"\nDiamond Lite: {response}"
        )
