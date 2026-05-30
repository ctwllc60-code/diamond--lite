import re

from datetime import (
    datetime,
    UTC
)


SURFACE_ENGINE_VERSION = (
    "diamond_surface_v2"
)


def normalize_text(
    text
):
    return str(
        text or ""
    )


def normalize_spacing(
    text
):
    text = normalize_text(
        text
    )

    text = re.sub(
        r"[ \t]+",
        " ",
        text
    )

    text = re.sub(
        r"\n{3,}",
        "\n\n",
        text
    )

    return text.strip()


def normalize_punctuation(
    text
):
    text = re.sub(
        r"\.{4,}",
        "...",
        text
    )

    text = re.sub(
        r"\?{2,}",
        "?",
        text
    )

    text = re.sub(
        r"\!{2,}",
        "!",
        text
    )

    text = re.sub(
        r"\,{2,}",
        ",",
        text
    )

    return text


def detect_surface_breaks(
    text
):
    surface_issues = []

    if "  " in text:
        surface_issues.append(
            "spacing_irregularity"
        )

    if "\n\n\n" in text:
        surface_issues.append(
            "paragraph_fragmentation"
        )

    if len(
        text.strip()
    ) < 10:
        surface_issues.append(
            "possible_output_collapse"
        )

    if text.count(
        "..."
    ) >= 5:
        surface_issues.append(
            "excessive_pause_fragmentation"
        )

    if len(
        text.split()
    ) < 4:
        surface_issues.append(
            "low_information_density"
        )

    return surface_issues


def determine_surface_stability(
    surface_issues
):
    if not surface_issues:
        return "stable"

    if len(
        surface_issues
    ) >= 3:
        return "unstable"

    return "recoverable"


def build_surface_router(
    surface_issues
):
    enrichment_routes = []

    if (
        "paragraph_fragmentation"
        in surface_issues
    ):
        enrichment_routes.append(
            "continuity_stabilizer"
        )

    if (
        "possible_output_collapse"
        in surface_issues
    ):

        enrichment_routes.extend([
            "behavioral_harmony",
            "atmosphere_condition"
        ])

    if (
        "excessive_pause_fragmentation"
        in surface_issues
    ):
        enrichment_routes.append(
            "meaning_builder"
        )

    if (
        "low_information_density"
        in surface_issues
    ):
        enrichment_routes.append(
            "retrieval_engine"
        )

    return {
        "enrichment_routes": (
            enrichment_routes
        ),

        "routing_active": (
            bool(
                enrichment_routes
            )
        ),

        "surface_supervision_active": (
            True
        )
    }


def build_surface_metadata():
    return {
        "surface_engine_version": (
            SURFACE_ENGINE_VERSION
        ),

        "surface_timestamp": (
            datetime.now(
                UTC
            ).isoformat()
        )
    }


def preserve_delivery_integrity(
    response
):
    cleaned_response = (
        normalize_spacing(
            response
        )
    )

    cleaned_response = (
        normalize_punctuation(
            cleaned_response
        )
    )

    surface_issues = (
        detect_surface_breaks(
            cleaned_response
        )
    )

    surface_stability = (
        determine_surface_stability(
            surface_issues
        )
    )

    mini_router = (
        build_surface_router(
            surface_issues
        )
    )

    return {
        "final_response": (
            cleaned_response
        ),

        "surface_issues": (
            surface_issues
        ),

        "surface_stability": (
            surface_stability
        ),

        "surface_metadata": (
            build_surface_metadata()
        ),

        "mini_router": (
            mini_router
        )
    }


def get_surface_snapshot(
    response
):
    verified = (
        preserve_delivery_integrity(
            response
        )
    )

    return {
        "surface_issues": (
            verified.get(
                "surface_issues",
                []
            )
        ),

        "surface_stability": (
            verified.get(
                "surface_stability"
            )
        ),

        "response_length": (
            len(
                verified.get(
                    "final_response",
                    ""
                )
            )
        ),

        "surface_metadata": (
            verified.get(
                "surface_metadata"
            )
        ),

        "mini_router": (
            verified.get(
                "mini_router"
            )
        )
    }
