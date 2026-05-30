from core.base_engine import BaseEngine

class RhythmBalancer(BaseEngine):

    def __init__(self):
        super().__init__(
            "rhythm_balancer"
        )

    def process(self, message_object):

        response = (
            message_object.final_response
        )

        response = response.replace(
            "\r",
            ""
        )

        while "\n\n\n" in response:

            response = response.replace(
                "\n\n\n",
                "\n\n"
            )

        response = response.replace(
            "orientation\nWhen viewed",
            "orientation.\n\nWhen viewed"
        )

        response = response.replace(
            "predictability.\nQuestions",
            "predictability.\n\nQuestions"
        )

        response = response.replace(
            "situations.\nThese reflections",
            "situations.\n\nThese reflections"
        )

        response = response.replace(
            "question.\nAt the same time",
            "question.\n\nAt the same time"
        )

        response = "\n".join(
            line.strip()
            for line in response.splitlines()
        )

        message_object.final_response = (
            response.strip()
        )

        message_object.enrichment_layers.append({
            "engine": self.engine_name,
            "wave":
                message_object.recursion_state[
                    "current_wave"
                ],
            "type": "rhythm_balancing",
            "content": {
                "rhythm_adjusted": True
            }
        })

        return message_object
