from orchestration.orchestrator import (
    Orchestrator
)

from core.message_object import (
    MessageObject
)

orchestrator = Orchestrator()

while True:

    print(
        "\nWagg: ",
        end=""
    )

    user_lines = []

    while True:

        line = input()

        if line.strip() == "":

            break

        user_lines.append(
            line
        )

    user_input = "\n".join(
        user_lines
    ).strip()

    if not user_input:

        continue

    if (
        user_input.lower()
        == "exit"
    ):

        break

    message = MessageObject(
        raw_message=user_input,
        developer_mode=False
    )

    result = orchestrator.run(
        message
    )

    cleaned_response = (
        result.final_response.strip()
    )

    print(
        f"\nDiamond: {cleaned_response}"
    )

    if result.developer_mode:

        print(
            "\nENRICHMENT LAYERS:\n"
        )

        print(
            result.enrichment_layers
        )
