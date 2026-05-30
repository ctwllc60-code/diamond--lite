FEEDBACK_LOOP = {
    "purpose": (
        "Adjust behavior during a session "
        "based on user feedback without "
        "permanent memory storage."
    ),

    "trigger_conditions": {
        "pattern_based_detection": True,
        "case_insensitive_detection": True,

        "trigger_patterns": [
            "not what i wanted",
            "wrong",
            "try again",
            "direct correction",
            "contradiction"
        ]
    },

    "failure_handling": {
        "increase_failure_count": True,
        "record_failed_interaction": True,

        "adjustments": {
            "change_approach": True,
            "avoid_previous_structure": True,
            "improve_alignment": True,
            "prevent_repeated_failure_patterns": True
        }
    },

    "success_handling": {
        "success_conditions": [
            "no_correction_detected",
            "conversation_progression"
        ],

        "reduce_failure_count_gradually": True,
        "minimum_failure_count": 0
    },

    "state_rules": {
        "session_only_memory_state": True,
        "no_permanent_storage": True,
        "temporary_feedback_history": True
    },

    "execution_influence": {
        "affect_input_interpretation": True,
        "affect_step_selection": True,
        "affect_response_structure": True,

        "restrictions": {
            "cannot_break_system_rules": True,
            "cannot_introduce_invalid_actions": True,
            "cannot_override_constraints": True
        }
    },

    "output_behavior": {
        "do_not_expose_feedback_system": True,
        "adjust_internally": True,
        "maintain_structure": True,
        "maintain_clarity": True
    },

    "initial_state": {
        "failure_count": 0,
        "failure_log": []
    }
}
