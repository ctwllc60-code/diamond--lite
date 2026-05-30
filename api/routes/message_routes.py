import os
import json
import traceback
import logging

from datetime import (
    datetime,
    UTC
)

from flask import (
    Blueprint,
    request,
    jsonify
)

from auth.api_guard import (
    validate_api_key
)

from services.cognition_service import (
    CognitionService
)


message_routes = Blueprint(
    "message_routes",
    __name__
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


def load_runtime_state():

    with open(
        STATE_FILE,
        "r"
    ) as file:

        return json.load(
            file
        )


def save_runtime_state(
    runtime_state
):

    with open(
        STATE_FILE,
        "w"
    ) as file:

        json.dump(

            runtime_state,

            file,

            indent=4
        )


@message_routes.route(
    "/message",
    methods=["POST"]
)
def process_message():

    authorization_failure = (
        validate_api_key()
    )

    if authorization_failure:

        return authorization_failure

    runtime_state = load_runtime_state()

    runtime_state[
        "total_requests"
    ] += 1

    try:

        request_packet = request.get_json()

        if not request_packet:

            runtime_state[
                "failed_requests"
            ] += 1

            save_runtime_state(
                runtime_state
            )

            logging.warning(
                "Missing JSON request body."
            )

            return jsonify({

                "status":
                    "error",

                "error":
                    "Missing JSON request body"
            }), 400

        user_id = request_packet.get(
            "user_id",
            "default_user"
        )

        runtime_state[
            "last_active_user"
        ] = user_id

        runtime_state[
            "last_request_timestamp"
        ] = datetime.now(
            UTC
        ).isoformat()

        logging.info(
            f"Processing request "
            f"for user: {user_id}"
        )

        cognition_service = (
            CognitionService(
                user_id
            )
        )

        result = (
            cognition_service.process_cognition_request(
                request_packet
            )
        )

        runtime_state[
            "successful_requests"
        ] += 1

        save_runtime_state(
            runtime_state
        )

        logging.info(
            f"Request completed "
            f"for user: {user_id}"
        )

        return jsonify(
            result
        )

    except Exception as error:

        runtime_state[
            "failed_requests"
        ] += 1

        save_runtime_state(
            runtime_state
        )

        traceback.print_exc()

        logging.exception(
            "Runtime exception occurred."
        )

        return jsonify({

            "status":
                "error",

            "runtime":
                os.getenv(
                    "DIAMOND_RUNTIME_NAME",
                    "diamond_lite_runtime"
                ),

            "error_type":
                type(error).__name__,

            "error_message":
                str(error)
        }), 500
