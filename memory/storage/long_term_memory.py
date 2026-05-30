import json
import os

from datetime import (
    datetime,
    UTC
)


BASE_DIRECTORY = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        ".."
    )
)

MEMORY_FILE = os.path.join(
    BASE_DIRECTORY,
    "memory",
    "storage",
    "long_term_memory.json"
)


class LongTermMemory:

    def __init__(self):

        memory_directory = os.path.dirname(
            MEMORY_FILE
        )

        if not os.path.exists(
            memory_directory
        ):

            os.makedirs(
                memory_directory
            )

        if not os.path.exists(
            MEMORY_FILE
        ):

            with open(
                MEMORY_FILE,
                "w"
            ) as file:

                json.dump(
                    [],
                    file
                )

    def load_memory(
        self
    ):

        with open(
            MEMORY_FILE,
            "r"
        ) as file:

            return json.load(
                file
            )

    def save_memory(
        self,
        memory_log
    ):

        with open(
            MEMORY_FILE,
            "w"
        ) as file:

            json.dump(

                memory_log,

                file,

                indent=4
            )

    def store_memory(
        self,
        memory_entry
    ):

        memory_log = (
            self.load_memory()
        )

        memory_entry[
            "stored_at"
        ] = (

            datetime.now(
                UTC
            ).isoformat()
        )

        memory_log.append(
            memory_entry
        )

        memory_log = (
            memory_log[-1000:]
        )

        self.save_memory(
            memory_log
        )

    def retrieve_recent_memories(
        self,
        limit=10
    ):

        memory_log = (
            self.load_memory()
        )

        return memory_log[
            -limit:
        ]
