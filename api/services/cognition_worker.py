import logging

from runtime_bridge import (
    RuntimeBridge
)


class CognitionWorker:

    def __init__(
        self,
        worker_id
    ):

        self.worker_id = worker_id

        logging.info(
            f"Cognition worker initialized: "
            f"{worker_id}"
        )

    def execute_request(
        self,
        user_id,
        request_packet
    ):

        logging.info(
            f"Worker {self.worker_id} "
            f"processing user: {user_id}"
        )

        runtime_bridge = (
            RuntimeBridge(
                user_id=user_id
            )
        )

        result = (
            runtime_bridge.process_request_packet(
                request_packet
            )
        )

        logging.info(
            f"Worker {self.worker_id} "
            f"completed user: {user_id}"
        )

        return result
