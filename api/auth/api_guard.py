import os

from flask import (
    request,
    jsonify
)

from dotenv import (
    load_dotenv
)


load_dotenv(
    "../.env"
)


EXPECTED_API_KEY = os.getenv(
    "DIAMOND_API_KEY",
    "development_key"
)


def validate_api_key():

    provided_api_key = request.headers.get(
        "X-API-KEY"
    )

    if not provided_api_key:

        return jsonify({

            "status":
                "error",

            "error":
                "Missing API key"
        }), 401

    if provided_api_key != EXPECTED_API_KEY:

        return jsonify({

            "status":
                "error",

            "error":
                "Invalid API key"
        }), 403

    return None
