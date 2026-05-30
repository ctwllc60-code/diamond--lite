import logging

from services.cognition_worker import (
    CognitionWorker
)

from infrastructure.worker_state_tracker import (
    WorkerStateTracker
)


class WorkerManager:

    def __init__(
        self
    ):

        self.workers = [

            CognitionWorker(
                worker_id="worker_alpha"
            ),

            CognitionWorker(
                worker_id="worker_beta"
            )
        ]

        self.current_worker_index = 0

        self.worker_tracker = (
            WorkerStateTracker()
        )

        logging.info(
            "Worker manager initialized."
        )

    def get_next_worker(
        self
    ):

        worker = self.workers[
            self.current_worker_index
        ]

        self.current_worker_index = (
            (
                self.current_worker_index + 1
            )
            %
            len(self.workers)
        )

        self.worker_tracker.record_worker_assignment(
            worker.worker_id
        )

        logging.info(
            f"Assigned worker: "
            f"{worker.worker_id}"
        )

        return worker

    def get_worker_snapshot(
        self
    ):

        return (
            self.worker_tracker.get_worker_snapshot()
        )
