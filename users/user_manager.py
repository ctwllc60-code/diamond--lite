import os
import json


USERS_DIRECTORY = (
    "users"
)


class UserManager:

    def __init__(self):

        if not os.path.exists(
            USERS_DIRECTORY
        ):

            os.makedirs(
                USERS_DIRECTORY
            )

    def create_user_instance(
        self,
        user_id
    ):

        user_directory = os.path.join(
            USERS_DIRECTORY,
            user_id
        )

        memory_directory = os.path.join(
            user_directory,
            "memory"
        )

        if not os.path.exists(
            memory_directory
        ):

            os.makedirs(
                memory_directory
            )

        cognitive_memory_file = os.path.join(
            memory_directory,
            "cognitive_memory.json"
        )

        if not os.path.exists(
            cognitive_memory_file
        ):

            with open(
                cognitive_memory_file,
                "w"
            ) as file:

                json.dump(
                    [],
                    file,
                    indent=4
                )

        return {

            "user_id":
                user_id,

            "user_directory":
                user_directory,

            "memory_directory":
                memory_directory
        }

    def user_exists(
        self,
        user_id
    ):

        return os.path.exists(

            os.path.join(
                USERS_DIRECTORY,
                user_id
            )
        )
