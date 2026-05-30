class WorkingMemory:

    def __init__(self):

        self.active_retrievals = []

    def register_memory(
        self,
        memory
    ):

        self.active_retrievals.append(
            memory
        )

        self.active_retrievals = (
            self.active_retrievals[-15:]
        )

    def retrieve_active_memories(
        self
    ):

        return self.active_retrievals

    def clear_working_memory(
        self
    ):

        self.active_retrievals = []
