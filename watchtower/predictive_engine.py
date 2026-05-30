from datetime import (
    datetime,
    UTC
)


class PredictiveEngine:

    def __init__(self):

        self.engine_name = (
            "watchtower_predictive_engine"
        )

    def evaluate_predictive_stability(
        self,
        recent_history,
        drift_analysis,
        infrastructure_score,
        resilience_analysis
    ):

        predictive_risks = []

        predictive_score = 100

        history_length = len(
            recent_history
        )

        if history_length < 3:

            predictive_risks.append(
                "limited_operational_history"
            )

            predictive_score -= 10

        if drift_analysis.get(
            "drift_detected"
        ):

            predictive_risks.append(
                "active_operational_drift"
            )

            predictive_score -= 20

        infrastructure_value = (
            infrastructure_score.get(
                "infrastructure_score",
                0
            )
        )

        if infrastructure_value < 80:

            predictive_risks.append(
                "infrastructure_instability_risk"
            )

            predictive_score -= 20

        resilience_value = (
            resilience_analysis.get(
                "resilience_score",
                0
            )
        )

        if resilience_value < 80:

            predictive_risks.append(
                "resilience_degradation_risk"
            )

            predictive_score -= 20

        instability_events = 0

        for state in recent_history:

            if (
                state.get(
                    "runtime_health"
                )
                != "stable"
            ):

                instability_events += 1

        if instability_events > 0:

            predictive_risks.append(
                "historical_instability_detected"
            )

            predictive_score -= (
                instability_events * 5
            )

        if predictive_score < 0:

            predictive_score = 0

        predictive_status = (
            self.determine_predictive_status(
                predictive_score
            )
        )

        return {
            "predictive_score": (
                predictive_score
            ),

            "predictive_status": (
                predictive_status
            ),

            "predictive_risks": (
                predictive_risks
            ),

            "instability_events": (
                instability_events
            ),

            "analysis_timestamp": (
                datetime.now(
                    UTC
                ).isoformat()
            )
        }

    def determine_predictive_status(
        self,
        predictive_score
    ):

        if predictive_score >= 90:

            return "predictively_stable"

        if predictive_score >= 75:

            return "monitoring_recommended"

        if predictive_score >= 50:

            return "predictive_degradation_risk"

        return "predictive_instability_risk"
