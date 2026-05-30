from datetime import (
    datetime,
    UTC
)


class SupervisoryPriorityEngine:

    def __init__(self):

        self.engine_name = (
            "watchtower_supervisory_priority_engine"
        )

    def evaluate_supervisory_priorities(
        self,
        predictive_analysis,
        coordination_analysis,
        adaptive_pacing_analysis,
        recursive_load_analysis,
        human_signal_analysis,
        diamond_protection_analysis
    ):

        arbitration_score = 100

        supervisory_alignment = (
            "aligned_supervision"
        )

        dominant_priority = (
            "continuity_preservation"
        )

        supervisory_conflicts = []

        predictive_score = (
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

        pacing_score = (
            adaptive_pacing_analysis.get(
                "pacing_score",
                100
            )
        )

        recursive_load_score = (
            recursive_load_analysis.get(
                "recursive_load_score",
                100
            )
        )

        human_signal_score = (
            human_signal_analysis.get(
                "human_signal_score",
                100
            )
        )

        protection_score = (
            diamond_protection_analysis.get(
                "protection_score",
                100
            )
        )

        if predictive_score < 90:

            supervisory_conflicts.append(
                "predictive_pressure_priority"
            )

            dominant_priority = (
                "predictive_stabilization"
            )

            arbitration_score -= 10

        if coordination_required:

            supervisory_conflicts.append(
                "coordination_pressure_priority"
            )

            dominant_priority = (
                "coordination_alignment"
            )

            arbitration_score -= 10

        if pacing_score < 90:

            supervisory_conflicts.append(
                "adaptive_pacing_pressure"
            )

            dominant_priority = (
                "adaptive_balancing"
            )

            arbitration_score -= 10

        if recursive_load_score < 90:

            supervisory_conflicts.append(
                "recursive_load_pressure"
            )

            dominant_priority = (
                "recursive_stabilization"
            )

            arbitration_score -= 10

        if human_signal_score < 90:

            supervisory_conflicts.append(
                "interaction_continuity_pressure"
            )

            dominant_priority = (
                "interaction_stabilization"
            )

            arbitration_score -= 10

        if protection_score < 90:

            supervisory_conflicts.append(
                "diamond_protection_pressure"
            )

            dominant_priority = (
                "diamond_protection"
            )

            arbitration_score -= 10

        if arbitration_score >= 90:

            supervisory_alignment = (
                "aligned_supervision"
            )

        elif arbitration_score >= 75:

            supervisory_alignment = (
                "priority_monitoring_active"
            )

        elif arbitration_score >= 50:

            supervisory_alignment = (
                "supervisory_conflict_detected"
            )

        else:

            supervisory_alignment = (
                "supervisory_stabilization_required"
            )

        if arbitration_score < 0:

            arbitration_score = 0

        return {

            "arbitration_score": (
                arbitration_score
            ),

            "supervisory_alignment": (
                supervisory_alignment
            ),

            "dominant_priority": (
                dominant_priority
            ),

            "supervisory_conflicts": (
                supervisory_conflicts
            ),

            "analysis_timestamp": (
                datetime.now(
                    UTC
                ).isoformat()
            )
        }
