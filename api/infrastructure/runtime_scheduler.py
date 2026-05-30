import time
import threading
import logging

from infrastructure.runtime_monitor import (
    RuntimeMonitor
)


class RuntimeScheduler:

    def __init__(
        self
    ):

        self.runtime_monitor = (
            RuntimeMonitor()
        )

        self.scheduler_active = False

        self.scheduler_thread = None

    def heartbeat_loop(
        self
    ):

        logging.info(
            "Runtime scheduler heartbeat loop started."
        )

        while self.scheduler_active:

            try:

                self.runtime_monitor.mark_runtime_heartbeat()

            except Exception as error:

                logging.exception(
                    f"Scheduler heartbeat failure: {error}"
                )

            time.sleep(
                30
            )

    def start_scheduler(
        self
    ):

        if self.scheduler_active:

            return

        self.scheduler_active = True

        self.scheduler_thread = threading.Thread(

            target=self.heartbeat_loop,

            daemon=True
        )

        self.scheduler_thread.start()

        logging.info(
            "Runtime scheduler activated."
        )

    def stop_scheduler(
        self
    ):

        self.scheduler_active = False

        logging.info(
            "Runtime scheduler stopped."
        )
