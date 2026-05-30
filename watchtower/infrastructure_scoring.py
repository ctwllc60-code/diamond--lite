class InfrastructureScorer:

    def __init__(self):

        self.scorer_name = (
            "watchtower_infrastructure_scorer"
        )

        self.maximum_score = 100

    def calculate_infrastructure_score(
        self,
        runtime_visibility,
        drift_analysis
    ):

        infrastructure_score = (
            self.maximum_score
        )

        if not runtime_visibility.get(
            "runtime_detected"
        ):

            infrastructure_score -= 50

        if (
            runtime_visibility.get(
                "runtime_health"
            )
            != "stable"
        ):

            infrastructure_score -= 20

        if (
            runtime_visibility.get(
                "scheduler_health"
            )
            != "stable"
        ):

            infrastructure_score -= 15

        if (
            runtime_visibility.get(
                "cycle_status"
            )
            != "completed"
        ):

            infrastructure_score -= 15

        if drift_analysis.get(
            "drift_detected"
        ):

            detected_drift = (
                drift_analysis.get(
                    "detected_drift",
                    []
                )
            )

            infrastructure_score -= (
                len(detected_drift) * 10
            )

        if infrastructure_score < 0:

            infrastructure_score = 0

        return {
            "infrastructure_score": (
                infrastructure_score
            ),

            "maximum_score": (
                self.maximum_score
            ),

            "score_status": (
                self.determine_score_status(
                    infrastructure_score
                )
            )
        }

    def determine_score_status(
        self,
        infrastructure_score
    ):

        if infrastructure_score >= 90:

            return "optimal"

        if infrastructure_score >= 75:

            return "stable"

        if infrastructure_score >= 50:

            return "degraded"

        return "critical"
