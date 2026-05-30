import logging

from infrastructure.runtime_monitor import (
    RuntimeMonitor
)

from infrastructure.runtime_scheduler import (
    RuntimeScheduler
)


class ServiceContainer:

    def __init__(
        self
    ):

        self.runtime_monitor = (
            RuntimeMonitor()
        )

        self.runtime_scheduler = (
            RuntimeScheduler()
        )

    def initialize_services(
        self
    ):

        logging.info(
            "Initializing infrastructure services."
        )

        self.runtime_monitor.mark_runtime_heartbeat()

        self.runtime_scheduler.start_scheduler()

        logging.info(
            "Infrastructure services initialized."
        )

    def get_runtime_monitor(
        self
    ):

        return self.runtime_monitor

    def get_runtime_scheduler(
        self
    ):

        return self.runtime_scheduler
