from datetime import (
    datetime,
    UTC
)


class AdaptiveStabilityEngine:

    def __init__(self):

        self.engine_name = (
            "watchtower_adaptive_stability_engine"
        )

    def evaluate_adaptive_stability(
        self,
        memory_patterns,
        incident_patterns,
        predictive_analysis,
        resilience_analysis
    ):

        adaptive_stability_score = 100

        adaptive_adjustments = []

        instability_events = (
            memory_patterns.get(
                "instability_events",
                0
            )
        )

        degraded_events = (
            memory_patterns.get(
                "degraded_infrastructure_events",
                0
            )
        )

        total_incidents = (
            incident_patterns.get(
                "total_incidents",
                0
            )
        )

        critical_incidents = (
            incident_patterns.get(
                "critical_incidents",
                0
            )
        )

        predictive_score = (
            predictive_analysis.get(
                "predictive_score",
                100
            )
        )

        resilience_score = (
            resilience_analysis.get(
                "resilience_score",
                100
            )
        )

        if instability_events > 0:

            adaptive_adjustments.append(
                "increase_runtime_monitoring"
            )

            adaptive_stability_score -= (
                instability_events * 2
            )

        if degraded_events > 0:

            adaptive_adjustments.append(
                "increase_infrastructure_sensitivity"
            )

            adaptive_stability_score -= (
                degraded_events * 3
            )

        if total_incidents > 0:

            adaptive_adjustments.append(
                "increase_incident_awareness"
            )

            adaptive_stability_score -= (
                total_incidents * 2
            )

        if critical_incidents > 0:

            adaptive_adjustments.append(
                "activate_critical_stability_protection"
            )

            adaptive_stability_score -= (
                critical_incidents * 5
            )

        if predictive_score < 90:

            adaptive_adjustments.append(
                "increase_predictive_sensitivity"
            )

            adaptive_stability_score -= 10

        if resilience_score < 90:

            adaptive_adjustments.append(
                "increase_resilience_monitoring"
            )

            adaptive_stability_score -= 10

        if adaptive_stability_score < 0:

            adaptive_stability_score = 0

        adaptive_status = (
            self.determine_adaptive_status(
                adaptive_stability_score
            )
        )

        return {

            "adaptive_stability_score": (
                adaptive_stability_score
            ),

            "adaptive_status": (
                adaptive_status
            ),

            "adaptive_adjustments": (
                adaptive_adjustments
            ),

            "analysis_timestamp": (
                datetime.now(
                    UTC
                ).isoformat()
            )
        }

    def determine_adaptive_status(
        self,
        adaptive_stability_score
    ):

        if adaptive_stability_score >= 90:

            return "adaptive_stability_optimal"

        if adaptive_stability_score >= 75:

            return "adaptive_monitoring_active"

        if adaptive_stability_score >= 50:

            return "adaptive_protection_elevated"

        return "adaptive_stability_critical"
