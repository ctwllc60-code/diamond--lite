import os
import subprocess

from dotenv import (
    load_dotenv
)


BASE_DIR = os.path.abspath(
    os.path.dirname(__file__)
)

ENV_PATH = os.path.join(
    BASE_DIR,
    ".env"
)

API_DIRECTORY = os.path.join(
    BASE_DIR,
    "api"
)


load_dotenv(
    ENV_PATH
)


print(
    "\nStarting Diamond Lite Server...\n"
)

print(
    f"Environment: "
    f"{os.getenv('DIAMOND_ENVIRONMENT')}"
)

print(
    f"Runtime: "
    f"{os.getenv('DIAMOND_RUNTIME_NAME')}"
)

print(
    f"Host: "
    f"{os.getenv('DIAMOND_SERVER_HOST')}"
)

print(
    f"Port: "
    f"{os.getenv('DIAMOND_SERVER_PORT')}\n"
)


subprocess.run(

    [
        "python",
        "server.py"
    ],

    cwd=API_DIRECTORY
)
