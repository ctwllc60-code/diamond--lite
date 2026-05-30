import json
import os

from datetime import (
    datetime,
    UTC
)


INCIDENT_LOG = (
    "../state/watchtower_incident_log.json"
)


class IncidentLogger:

    def __init__(self):

        self.logger_name = (
            "watchtower_incident_logger"
        )

        self.maximum_incident_history = 500

        self.ensure_incident_log_exists()

    def ensure_incident_log_exists(
        self
    ):

        if not os.path.exists(
            INCIDENT_LOG
        ):

            with open(
                INCIDENT_LOG,
                "w"
            ) as file:

                json.dump(
                    [],
                    file,
                    indent=4
                )

    def load_incident_log(
        self
    ):

        with open(
            INCIDENT_LOG,
            "r"
        ) as file:

            return json.load(
                file
            )

    def save_incident_log(
        self,
        incident_log
    ):

        with open(
            INCIDENT_LOG,
            "w"
        ) as file:

            json.dump(
                incident_log,
                file,
                indent=4
            )

    def record_incident(
        self,
        threat_analysis,
        recovery_analysis,
        escalation_analysis
    ):

        incident_log = (
            self.load_incident_log()
        )

        escalation_active = (
            escalation_analysis.get(
                "escalation_active",
                False
            )
        )

        if not escalation_active:

            return {
                "incident_recorded": False,
                "reason": (
                    "no_active_escalation"
                )
            }

        incident_entry = {

            "timestamp": (
                datetime.now(
                    UTC
                ).isoformat()
            ),

            "threat_level": (
                threat_analysis.get(
                    "threat_level"
                )
            ),

            "threat_score": (
                threat_analysis.get(
                    "threat_score"
                )
            ),

            "recovery_priority": (
                recovery_analysis.get(
                    "recovery_priority"
                )
            ),

            "escalation_level": (
                escalation_analysis.get(
                    "escalation_level"
                )
            ),

            "escalation_triggers": (
                escalation_analysis.get(
                    "escalation_triggers"
                )
            )
        }

        incident_log.append(
            incident_entry
        )

        if (
            len(incident_log)
            > self.maximum_incident_history
        ):

            incident_log = (
                incident_log[
                    -self.maximum_incident_history:
                ]
            )

        self.save_incident_log(
            incident_log
        )

        return {
            "incident_recorded": True,
            "incident_entry": (
                incident_entry
            )
        }

    def retrieve_recent_incidents(
        self,
        limit=25
    ):

        incident_log = (
            self.load_incident_log()
        )

        return incident_log[-limit:]

    def analyze_incident_patterns(
        self
    ):

        incident_log = (
            self.load_incident_log()
        )

        total_incidents = len(
            incident_log
        )

        critical_incidents = 0

        high_alert_incidents = 0

        for incident in incident_log:

            escalation_level = (
                incident.get(
                    "escalation_level"
                )
            )

            if (
                escalation_level
                == "critical_emergency"
            ):

                critical_incidents += 1

            if (
                escalation_level
                == "high_alert"
            ):

                high_alert_incidents += 1

        return {

            "total_incidents": (
                total_incidents
            ),

            "critical_incidents": (
                critical_incidents
            ),

            "high_alert_incidents": (
                high_alert_incidents
            ),

            "analysis_timestamp": (
                datetime.now(
                    UTC
                ).isoformat()
            )
        }
