from runtime_session import (
    RuntimeSession
)


session = RuntimeSession(
    "user_001"
)

print(
    session.get_user_context()
)
