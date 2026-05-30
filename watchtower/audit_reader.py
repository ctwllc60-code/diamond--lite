import json

from datetime import (
    datetime,
    UTC
)


AUDIT_LOG = (
    "../state/operational_audit.json"
)


class AuditReader:

    def __init__(self):

        self.reader_name = (
            "watchtower_audit_reader"
        )

        self.maximum_audit_entries = 25

    def audit_log_exists(
        self
    ):

        try:

            with open(
                AUDIT_LOG,
                "r"
            ):

                return True

        except FileNotFoundError:

            return False

    def load_audit_log(
        self
    ):

        if not self.audit_log_exists():

            return []

        with open(
            AUDIT_LOG,
            "r"
        ) as file:

            return json.load(
                file
            )

    def retrieve_recent_audit_events(
        self,
        limit=None
    ):

        audit_log = (
            self.load_audit_log()
        )

        if limit is None:

            limit = (
                self.maximum_audit_entries
            )

        return audit_log[-limit:]

    def analyze_audit_activity(
        self
    ):

        audit_log = (
            self.load_audit_log()
        )

        total_events = len(
            audit_log
        )

        event_type_counts = {}

        for event in audit_log:

            event_type = event.get(
                "event_type",
                "unknown"
            )

            if (
                event_type
                not in event_type_counts
            ):

                event_type_counts[
                    event_type
                ] = 0

            event_type_counts[
                event_type
            ] += 1

        return {
            "audit_entries_detected": (
                total_events > 0
            ),

            "total_audit_events": (
                total_events
            ),

            "event_type_counts": (
                event_type_counts
            ),

            "analysis_timestamp": (
                datetime.now(
                    UTC
                ).isoformat()
            )
        }
