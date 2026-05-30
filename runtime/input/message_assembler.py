# runtime/input/message_assembler.py


class MessageAssembler:

    def __init__(self):

        self.buffer = []

    def receive(
        self,
        user_input
    ):

        line = str(
            user_input
        ).rstrip()

        self.buffer.append(
            line
        )

    def finalize(self):

        message = "\n".join(
            self.buffer
        ).strip()

        self.buffer = []

        return message
