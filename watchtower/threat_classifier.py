from datetime import (
    datetime,
    UTC
)


class ThreatClassifier:

    def __init__(self):

        self.classifier_name = (
            "watchtower_threat_classifier"
        )

    def classify_operational_threat(
        self,
        infrastructure_score,
        resilience_analysis,
        predictive_analysis,
        memory_patterns
    ):

        threat_level = (
            "minimal"
        )

        threat_score = 0

        threat_categories = []

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

        if infrastructure_value < 90:

            threat_score += 15

            threat_categories.append(
                "infrastructure_instability"
            )

        if infrastructure_value < 75:

            threat_score += 20

        if resilience_value < 90:

            threat_score += 15

            threat_categories.append(
                "resilience_instability"
            )

        if resilience_value < 75:

            threat_score += 20

        if predictive_value < 90:

            threat_score += 15

            threat_categories.append(
                "predictive_instability"
            )

        if predictive_value < 75:

            threat_score += 20

        if instability_events > 0:

            threat_score += (
                instability_events * 5
            )

            threat_categories.append(
                "historical_instability"
            )

        if degraded_events > 0:

            threat_score += (
                degraded_events * 5
            )

            threat_categories.append(
                "historical_degradation"
            )

        threat_level = (
            self.determine_threat_level(
                threat_score
            )
        )

        return {
            "threat_level": (
                threat_level
            ),

            "threat_score": (
                threat_score
            ),

            "threat_categories": (
                threat_categories
            ),

            "analysis_timestamp": (
                datetime.now(
                    UTC
                ).isoformat()
            )
        }

    def determine_threat_level(
        self,
        threat_score
    ):

        if threat_score < 20:

            return "minimal"

        if threat_score < 40:

            return "elevated"

        if threat_score < 60:

            return "high"

        return "critical"
