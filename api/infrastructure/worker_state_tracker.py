import logging


class WorkerStateTracker:

    def __init__(
        self
    ):

        self.last_assigned_worker = None

        self.total_worker_assignments = 0

        self.worker_usage = {}

        logging.info(
            "Worker state tracker initialized."
        )

    def record_worker_assignment(
        self,
        worker_id
    ):

        self.last_assigned_worker = (
            worker_id
        )

        self.total_worker_assignments += 1

        if worker_id not in self.worker_usage:

            self.worker_usage[
                worker_id
            ] = 0

        self.worker_usage[
            worker_id
        ] += 1

        logging.info(
            f"Tracked worker assignment: "
            f"{worker_id}"
        )

    def get_worker_snapshot(
        self
    ):

        return {

            "last_assigned_worker":
                self.last_assigned_worker,

            "total_worker_assignments":
                self.total_worker_assignments,

            "worker_usage":
                self.worker_usage
        }
