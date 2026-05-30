import logging

from services.worker_manager import (
    WorkerManager
)


class CognitionService:

    worker_manager = (
        WorkerManager()
    )

    def __init__(
        self,
        user_id
    ):

        self.user_id = user_id

    def process_cognition_request(
        self,
        request_packet
    ):

        logging.info(
            f"Cognition service routing "
            f"user: {self.user_id}"
        )

        worker = (
            self.worker_manager.get_next_worker()
        )

        result = (
            worker.execute_request(

                self.user_id,

                request_packet
            )
        )

        logging.info(
            f"Cognition service completed "
            f"user: {self.user_id}"
        )

        return result
