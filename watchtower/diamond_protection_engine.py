from datetime import (
    datetime,
    UTC
)


class DiamondProtectionEngine:

    def __init__(self):

        self.engine_name = (
            "watchtower_diamond_protection_engine"
        )

    def evaluate_diamond_protection(
        self,
        infrastructure_score,
        resilience_analysis,
        predictive_analysis,
        coordination_analysis,
        behavioral_forecast_analysis,
        memory_patterns,
        incident_patterns
    ):

        protection_score = 100

        protection_risks = []

        protection_status = (
            "diamond_stable"
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

        coordination_required = (
            coordination_analysis.get(
                "coordination_required",
                False
            )
        )

        forecast_score = (
            behavioral_forecast_analysis.get(
                "forecast_score",
                100
            )
        )

        instability_events = (
            memory_patterns.get(
                "instability_events",
                0
            )
        )

        total_incidents = (
            incident_patterns.get(
                "total_incidents",
                0
            )
        )

        if infrastructure_value < 90:

            protection_risks.append(
                "infrastructure_pressure_detected"
            )

            protection_score -= 10

        if resilience_value < 90:

            protection_risks.append(
                "resilience_pressure_detected"
            )

            protection_score -= 10

        if predictive_value < 90:

            protection_risks.append(
                "predictive_pressure_detected"
            )

            protection_score -= 10

        if coordination_required:

            protection_risks.append(
                "coordination_pressure_active"
            )

            protection_score -= 10

        if forecast_score < 90:

            protection_risks.append(
                "continuity_forecast_pressure"
            )

            protection_score -= 10

        if instability_events > 0:

            protection_risks.append(
                "historical_instability_detected"
            )

            protection_score -= (
                instability_events * 2
            )

        if total_incidents > 0:

            protection_risks.append(
                "incident_pressure_detected"
            )

            protection_score -= (
                total_incidents * 2
            )

        if protection_score >= 90:

            protection_status = (
                "diamond_stable"
            )

        elif protection_score >= 75:

            protection_status = (
                "diamond_monitoring_active"
            )

        elif protection_score >= 50:

            protection_status = (
                "diamond_stability_pressure"
            )

        else:

            protection_status = (
                "diamond_protection_critical"
            )

        if protection_score < 0:

            protection_score = 0

        return {

            "protection_score": (
                protection_score
            ),

            "protection_status": (
                protection_status
            ),

            "protection_risks": (
                protection_risks
            ),

            "analysis_timestamp": (
                datetime.now(
                    UTC
                ).isoformat()
            )
        }
