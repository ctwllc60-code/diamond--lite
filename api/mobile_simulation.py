from datetime import (
    datetime,
    UTC
)

from runtime_bridge import (
    RuntimeBridge
)


bridge = RuntimeBridge(
    user_id="mobile_user_001"
)

request_packet = {

    "user_id":
        "mobile_user_001",

    "session_id":
        "session_alpha",

    "device":
        "android_mobile",

    "timestamp":
        datetime.now(
            UTC
        ).isoformat(),

    "message":
        "I enjoy building intelligent systems."
}

result = bridge.process_request_packet(
    request_packet
)

print(
    result
)
