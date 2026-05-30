from overseer import (
    WatchtowerOverseer
)


overseer = (
    WatchtowerOverseer()
)


oversight_cycle = (
    overseer.execute_oversight_cycle()
)


print(
    "\nWATCHTOWER RUNTIME VISIBILITY:\n"
)

print(
    oversight_cycle[
        "runtime_visibility"
    ]
)


print(
    "\nWATCHTOWER STATE HISTORY:\n"
)

print(
    oversight_cycle[
        "recent_history"
    ]
)


print(
    "\nWATCHTOWER DRIFT ANALYSIS:\n"
)

print(
    oversight_cycle[
        "drift_analysis"
    ]
)


print(
    "\nWATCHTOWER INFRASTRUCTURE SCORE:\n"
)

print(
    oversight_cycle[
        "infrastructure_score"
    ]
)
