import json
import os


class MemoryPersistence:

    def save(
        self,
        filepath,
        data
    ):

        directory = os.path.dirname(
            filepath
        )

        if (
            directory
            and not os.path.exists(
                directory
            )
        ):

            os.makedirs(
                directory
            )

        with open(
            filepath,
            "w"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )

    def load(
        self,
        filepath,
        default=None
    ):

        if not os.path.exists(
            filepath
        ):

            return (
                default
                if default is not None
                else {}
            )

        with open(
            filepath,
            "r"
        ) as file:

            return json.load(
                file
            )
