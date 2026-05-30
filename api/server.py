import os
import json
import logging

from datetime import (
    datetime,
    UTC
)

from flask import (
    Flask,
    jsonify
)

from dotenv import (
    load_dotenv
)

from routes.message_routes import (
    message_routes
)

from routes.admin_routes import (
    admin_routes
)

from infrastructure.service_container import (
    ServiceContainer
)


load_dotenv(
    "../.env"
)


SERVER_HOST = os.getenv(
    "DIAMOND_SERVER_HOST",
    "0.0.0.0"
)

SERVER_PORT = int(
    os.getenv(
        "DIAMOND_SERVER_PORT",
        "5000"
    )
)

DEBUG_MODE = (
    os.getenv(
        "DIAMOND_DEBUG",
        "True"
    ).lower() == "true"
)


BASE_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

LOG_DIRECTORY = os.path.join(
    BASE_DIR,
    "logs"
)

LOG_FILE = os.path.join(
    LOG_DIRECTORY,
    "runtime.log"
)

STATE_DIRECTORY = os.path.join(
    BASE_DIR,
    "state"
)

STATE_FILE = os.path.join(
    STATE_DIRECTORY,
    "server_runtime_state.json"
)


if not os.path.exists(
    LOG_DIRECTORY
):

    os.makedirs(
        LOG_DIRECTORY
    )


if not os.path.exists(
    STATE_DIRECTORY
):

    os.makedirs(
        STATE_DIRECTORY
    )


logging.basicConfig(

    filename=LOG_FILE,

    level=logging.INFO,

    format=(
        "%(asctime)s "
        "%(levelname)s "
        "%(message)s"
    )
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


runtime_state = load_runtime_state()

runtime_state[
    "runtime_status"
] = "online"

runtime_state[
    "server_start_time"
] = datetime.now(
    UTC
).isoformat()

save_runtime_state(
    runtime_state
)


service_container = (
    ServiceContainer()
)

service_container.initialize_services()

runtime_monitor = (
    service_container.get_runtime_monitor()
)


app = Flask(__name__)


app.register_blueprint(
    message_routes
)

app.register_blueprint(
    admin_routes
)


@app.route(
    "/health",
    methods=["GET"]
)
def health_check():

    logging.info(
        "Health check requested."
    )

    runtime_monitor.mark_runtime_heartbeat()

    runtime_snapshot = (
        runtime_monitor.get_runtime_snapshot()
    )

    return jsonify({

        "status":
            "online",

        "runtime":
            os.getenv(
                "DIAMOND_RUNTIME_NAME",
                "diamond_lite_runtime"
            ),

        "environment":
            os.getenv(
                "DIAMOND_ENVIRONMENT",
                "development"
            ),

        "runtime_snapshot":
            runtime_snapshot
    })


if __name__ == "__main__":

    logging.info(
        "Diamond Lite server starting."
    )

    app.run(

        host=SERVER_HOST,

        port=SERVER_PORT,

        debug=DEBUG_MODE
    )
