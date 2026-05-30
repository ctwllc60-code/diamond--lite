from datetime import (
    datetime,
    UTC
)


VALIDATION_VERSION = (
    "diamond_validation_v2"
)


def normalize_validation_text(
    text
):
    return str(
        text or ""
    ).strip()


def validate_response_integrity(
    text
):
    text = normalize_validation_text(
        text
    )

    validation = {
        "has_content": (
            len(text) > 0
        ),

        "minimum_structure": (
            len(
                text.split()
            ) >= 4
        ),

        "surface_stability": (
            "  " not in text
        ),

        "collapse_risk": (
            len(text) < 20
        ),

        "punctuation_stability": (
            "...." not in text
        ),

        "continuity_stability": (
            "\n\n\n" not in text
        ),

        "payload_stability": (
            isinstance(
                text,
                str
            )
        ),

        "retrieval_injection_stability": (
            "{}}" not in text
        ),

        "orchestration_stability": (
            len(
                text
            ) < 50000
        )
    }

    validation[
        "healthy_response"
    ] = all([
        validation[
            "has_content"
        ],

        validation[
            "minimum_structure"
        ],

        validation[
            "surface_stability"
        ],

        validation[
            "punctuation_stability"
        ],

        validation[
            "payload_stability"
        ],

        validation[
            "continuity_stability"
        ],

        validation[
            "orchestration_stability"
        ]
    ])

    return validation


def determine_validation_pressure(
    validation
):
    if validation.get(
        "collapse_risk"
    ):
        return "high"

    if not validation.get(
        "surface_stability"
    ):
        return "active"

    if not validation.get(
        "orchestration_stability"
    ):
        return "elevated"

    return "stable"


def build_validation_router(
    validation
):
    enrichment_routes = []

    if validation.get(
        "collapse_risk"
    ):
        enrichment_routes.extend([
            "surface_integrity_verification",
            "continuity_stabilizer"
        ])

    if not validation.get(
        "surface_stability"
    ):
        enrichment_routes.append(
            "behavioral_harmony"
        )

    if not validation.get(
        "punctuation_stability"
    ):
        enrichment_routes.append(
            "surface_integrity_verification"
        )

    if not validation.get(
        "continuity_stability"
    ):
        enrichment_routes.append(
            "continuity_stabilizer"
        )

    if not validation.get(
        "orchestration_stability"
    ):
        enrichment_routes.extend([
            "memory_distillation",
            "behavioral_harmony"
        ])

    return {
        "enrichment_routes": (
            list(
                dict.fromkeys(
                    enrichment_routes
                )
            )
        ),

        "routing_active": (
            bool(
                enrichment_routes
            )
        ),

        "validation_pressure": (
            determine_validation_pressure(
                validation
            )
        )
    }


def validate_output(
    text
):
    validation = (
        validate_response_integrity(
            text
        )
    )

    return validation.get(
        "healthy_response",
        False
    )


def build_validation_metadata():
    return {
        "validation_version": (
            VALIDATION_VERSION
        ),

        "validation_timestamp": (
            datetime.now(
                UTC
            ).isoformat()
        )
    }


def get_validation_result(
    text
):
    validation = (
        validate_response_integrity(
            text
        )
    )

    mini_router = (
        build_validation_router(
            validation
        )
    )

    return {
        "healthy_response": (
            validation.get(
                "healthy_response",
                False
            )
        ),

        "collapse_risk": (
            validation.get(
                "collapse_risk",
                False
            )
        ),

        "surface_stability": (
            validation.get(
                "surface_stability",
                False
            )
        ),

        "punctuation_stability": (
            validation.get(
                "punctuation_stability",
                False
            )
        ),

        "continuity_stability": (
            validation.get(
                "continuity_stability",
                False
            )
        ),

        "payload_stability": (
            validation.get(
                "payload_stability",
                False
            )
        ),

        "retrieval_injection_stability": (
            validation.get(
                "retrieval_injection_stability",
                False
            )
        ),

        "orchestration_stability": (
            validation.get(
                "orchestration_stability",
                False
            )
        ),

        "checked_text": (
            text
        ),

        "mini_router": (
            mini_router
        ),

        "validation_metadata": (
            build_validation_metadata()
        )
    }
