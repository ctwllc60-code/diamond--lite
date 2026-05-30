import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from users.user_manager import (
    UserManager
)


class RuntimeSession:

    def __init__(
        self,
        user_id
    ):

        self.user_id = user_id

        self.user_manager = (
            UserManager()
        )

        self.user_instance = (
            self.user_manager.create_user_instance(
                user_id
            )
        )

    def get_user_context(
        self
    ):

        return {

            "user_id":
                self.user_id,

            "user_directory":
                self.user_instance[
                    "user_directory"
                ],

            "memory_directory":
                self.user_instance[
                    "memory_directory"
                ]
        }
