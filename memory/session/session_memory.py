from datetime import (
    datetime,
    UTC
)


class SessionMemory:

    def __init__(self):

        self.active_session = {

            "session_started":

                datetime.now(
                    UTC
                ).isoformat(),

            "active_subjects":
                [],

            "active_goals":
                [],

            "recent_messages":
                [],

            "recent_responses":
                [],

            "continuity_state":
                {}
        }

    def store_message(
        self,
        message
    ):

        self.active_session[
            "recent_messages"
        ].append(
            message
        )

        self.active_session[
            "recent_messages"
        ] = (

            self.active_session[
                "recent_messages"
            ][-25:]
        )

    def store_response(
        self,
        response
    ):

        self.active_session[
            "recent_responses"
        ].append(
            response
        )

        self.active_session[
            "recent_responses"
        ] = (

            self.active_session[
                "recent_responses"
            ][-25:]
        )

    def register_subject(
        self,
        subject
    ):

        if (
            subject
            not in
            self.active_session[
                "active_subjects"
            ]
        ):

            self.active_session[
                "active_subjects"
            ].append(
                subject
            )

    def retrieve_session_state(
        self
    ):

        return self.active_session
