from runtime_bridge import (
    RuntimeBridge
)


bridge = (
    RuntimeBridge()
)

result = bridge.process_user_message(
    "hello"
)

print(
    result
)
