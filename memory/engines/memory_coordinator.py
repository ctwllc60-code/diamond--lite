from memory.session.session_memory import (
    SessionMemory
)

from memory.storage.long_term_memory import (
    LongTermMemory
)

from memory.retrieval.working_memory import (
    WorkingMemory
)


class MemoryCoordinator:

    def __init__(self):

        self.session_memory = (
            SessionMemory()
        )

        self.long_term_memory = (
            LongTermMemory()
        )

        self.working_memory = (
            WorkingMemory()
        )

    def process_interaction(
        self,
        raw_message,
        final_response
    ):

        self.session_memory.store_message(
            raw_message
        )

        self.session_memory.store_response(
            final_response
        )

        repetition_detected = False

        recent_responses = (
            self.session_memory.active_session.get(
                "recent_responses",
                []
            )
        )

        normalized_response = str(
            final_response or ""
        ).strip().lower()

        for response in recent_responses[-5:]:

            comparison = str(
                response or ""
            ).strip().lower()

            if (
                comparison
                == normalized_response
            ):

                repetition_detected = True
                break

        memory_entry = {

            "input":
                raw_message,

            "output":
                final_response,

            "repetition_detected":
                repetition_detected,

            "adaptive_variation_required":
                repetition_detected
        }

        self.long_term_memory.store_memory(
            memory_entry
        )

        self.working_memory.register_memory(
            memory_entry
        )

    def retrieve_memory_state(
        self
    ):

        recent_memories = (
            self.long_term_memory.retrieve_recent_memories()
        )

        adaptive_variation_required = any(

            memory.get(
                "adaptive_variation_required",
                False
            )

            for memory in recent_memories[-5:]
        )

        return {

            "session_memory":
                self.session_memory.retrieve_session_state(),

            "working_memory":
                self.working_memory.retrieve_active_memories(),

            "long_term_memory":
                recent_memories,

            "adaptive_variation_required":
                adaptive_variation_required
        }
