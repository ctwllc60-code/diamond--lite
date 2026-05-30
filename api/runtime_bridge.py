import sys
import os

from datetime import (
    datetime,
    UTC
)

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from orchestration.orchestrator import (
    Orchestrator
)

from core.schemas.message_object import (
    MessageObject
)

from app.runtime_session import (
    RuntimeSession
)

from memory.storage.cognitive_memory import (
    CognitiveMemory
)


class RuntimeBridge:

    def __init__(
        self,
        user_id="default_user"
    ):

        self.user_session = (
            RuntimeSession(
                user_id
            )
        )

        self.user_context = (
            self.user_session.get_user_context()
        )

        os.environ[
            "DIAMOND_INSTANCE_ID"
        ] = self.user_context[
            "user_id"
        ]

        self.memory = (
            CognitiveMemory()
        )

        self.orchestrator = (
            Orchestrator()
        )

    def process_request_packet(
        self,
        request_packet
    ):

        user_id = request_packet.get(
            "user_id",
            "default_user"
        )

        session_id = request_packet.get(
            "session_id",
            "default_session"
        )

        device = request_packet.get(
            "device",
            "unknown_device"
        )

        user_input = request_packet.get(
            "message",
            ""
        )

        timestamp = request_packet.get(
            "timestamp",
            datetime.now(
                UTC
            ).isoformat()
        )

        message = MessageObject(

            raw_message=user_input,

            developer_mode=False
        )

        result = self.orchestrator.run(
            message
        )

        response = str(
            result.final_response
        ).strip()

        recent_memory = (
            self.memory.retrieve_recent_reflections(
                limit=3
            )
        )

        continuity_snapshot = []

        for memory in recent_memory:

            continuity_snapshot.append({

                "user_message":
                    memory.get(
                        "raw_message",
                        ""
                    ),

                "diamond_lite_response":
                    memory.get(
                        "final_response",
                        ""
                    )
            })

        return {

            "status":
                "success",

            "runtime":
                "diamond_lite_runtime",

            "user_id":
                user_id,

            "session_id":
                session_id,

            "device":
                device,

            "timestamp":
                timestamp,

            "response":
                response,

            "continuity_snapshot":
                continuity_snapshot
        }
