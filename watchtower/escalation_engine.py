from datetime import (
    datetime,
    UTC
)


class EscalationEngine:

    def __init__(self):

        self.engine_name = (
            "watchtower_escalation_engine"
        )

    def evaluate_escalation_conditions(
        self,
        threat_analysis,
        recovery_analysis,
        infrastructure_score,
        resilience_analysis,
        predictive_analysis
    ):

        escalation_active = False

        escalation_level = (
            "normal"
        )

        escalation_triggers = []

        threat_level = (
            threat_analysis.get(
                "threat_level",
                "minimal"
            )
        )

        recovery_priority = (
            recovery_analysis.get(
                "recovery_priority",
                "routine"
            )
        )

        infrastructure_value = (
            infrastructure_score.get(
                "infrastructure_score",
                100
            )
        )

        resilience_value = (
            resilience_analysis.get(
                "resilience_score",
                100
            )
        )

        predictive_value = (
            predictive_analysis.get(
                "predictive_score",
                100
            )
        )

        if threat_level == "elevated":

            escalation_active = True

            escalation_level = (
                "elevated_monitoring"
            )

            escalation_triggers.append(
                "elevated_threat_detected"
            )

        if threat_level == "high":

            escalation_active = True

            escalation_level = (
                "high_alert"
            )

            escalation_triggers.append(
                "high_threat_detected"
            )

        if threat_level == "critical":

            escalation_active = True

            escalation_level = (
                "critical_emergency"
            )

            escalation_triggers.append(
                "critical_threat_detected"
            )

        if recovery_priority == "high_priority":

            escalation_active = True

            escalation_triggers.append(
                "high_priority_recovery_required"
            )

        if recovery_priority == "critical_response":

            escalation_active = True

            escalation_level = (
                "critical_emergency"
            )

            escalation_triggers.append(
                "critical_recovery_required"
            )

        if infrastructure_value < 60:

            escalation_active = True

            escalation_level = (
                "infrastructure_emergency"
            )

            escalation_triggers.append(
                "severe_infrastructure_degradation"
            )

        if resilience_value < 60:

            escalation_active = True

            escalation_triggers.append(
                "severe_resilience_instability"
            )

        if predictive_value < 60:

            escalation_active = True

            escalation_triggers.append(
                "severe_predictive_instability"
            )

        return {
            "escalation_active": (
                escalation_active
            ),

            "escalation_level": (
                escalation_level
            ),

            "escalation_triggers": (
                escalation_triggers
            ),

            "analysis_timestamp": (
                datetime.now(
                    UTC
                ).isoformat()
            )
        }
