from flask import (
    Blueprint,
    jsonify
)

from infrastructure.runtime_monitor import (
    RuntimeMonitor
)

from auth.api_guard import (
    validate_api_key
)

from services.cognition_service import (
    CognitionService
)


admin_routes = Blueprint(
    "admin_routes",
    __name__
)


runtime_monitor = (
    RuntimeMonitor()
)


@admin_routes.route(
    "/admin/runtime",
    methods=["GET"]
)
def runtime_admin_snapshot():

    authorization_failure = (
        validate_api_key()
    )

    if authorization_failure:

        return authorization_failure

    runtime_snapshot = (
        runtime_monitor.get_runtime_snapshot()
    )

    worker_snapshot = (
        CognitionService.worker_manager.get_worker_snapshot()
    )

    return jsonify({

        "status":
            "success",

        "admin_runtime_snapshot":
            runtime_snapshot,

        "worker_snapshot":
            worker_snapshot
    })
