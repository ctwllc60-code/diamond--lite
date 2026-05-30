from datetime import (
    datetime,
    UTC
)


class ResilienceEngine:

    def __init__(self):

        self.engine_name = (
            "watchtower_resilience_engine"
        )

        self.maximum_resilience_score = 100

    def evaluate_resilience(
        self,
        runtime_visibility,
        drift_analysis,
        infrastructure_score,
        audit_activity
    ):

        resilience_score = (
            self.maximum_resilience_score
        )

        resilience_risks = []

        if not runtime_visibility.get(
            "runtime_detected"
        ):

            resilience_score -= 40

            resilience_risks.append(
                "runtime_not_detected"
            )

        if (
            runtime_visibility.get(
                "runtime_health"
            )
            != "stable"
        ):

            resilience_score -= 20

            resilience_risks.append(
                "runtime_instability"
            )

        if (
            runtime_visibility.get(
                "scheduler_health"
            )
            != "stable"
        ):

            resilience_score -= 15

            resilience_risks.append(
                "scheduler_instability"
            )

        if drift_analysis.get(
            "drift_detected"
        ):

            detected_drift = (
                drift_analysis.get(
                    "detected_drift",
                    []
                )
            )

            resilience_score -= (
                len(detected_drift) * 10
            )

            resilience_risks.append(
                "operational_drift_detected"
            )

        infrastructure_value = (
            infrastructure_score.get(
                "infrastructure_score",
                0
            )
        )

        if infrastructure_value < 75:

            resilience_score -= 15

            resilience_risks.append(
                "infrastructure_degradation"
            )

        total_audit_events = (
            audit_activity.get(
                "total_audit_events",
                0
            )
        )

        if total_audit_events == 0:

            resilience_score -= 10

            resilience_risks.append(
                "audit_visibility_low"
            )

        if resilience_score < 0:

            resilience_score = 0

        resilience_status = (
            self.determine_resilience_status(
                resilience_score
            )
        )

        return {
            "resilience_score": (
                resilience_score
            ),

            "maximum_resilience_score": (
                self.maximum_resilience_score
            ),

            "resilience_status": (
                resilience_status
            ),

            "resilience_risks": (
                resilience_risks
            ),

            "analysis_timestamp": (
                datetime.now(
                    UTC
                ).isoformat()
            )
        }

    def determine_resilience_status(
        self,
        resilience_score
    ):

        if resilience_score >= 90:

            return "high_resilience"

        if resilience_score >= 75:

            return "stable_resilience"

        if resilience_score >= 50:

            return "degraded_resilience"

        return "critical_resilience"
