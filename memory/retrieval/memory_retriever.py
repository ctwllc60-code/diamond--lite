from memory.retrieval.retrieval_prioritizer import (
    RetrievalPrioritizer
)


class MemoryRetriever:

    def __init__(self):

        self.prioritizer = (
            RetrievalPrioritizer()
        )

    def retrieve(
        self,
        memory_log,
        query="",
        limit=10
    ):

        query_text = str(
            query or ""
        ).lower()

        matched_memories = []

        for memory in memory_log:

            input_text = str(
                memory.get(
                    "input",
                    ""
                )
            ).lower()

            output_text = str(
                memory.get(
                    "output",
                    ""
                )
            ).lower()

            combined = (
                input_text
                + " "
                + output_text
            )

            if any(
                word in combined
                for word in query_text.split()
            ):

                matched_memories.append(
                    memory
                )

        if not matched_memories:

            matched_memories = memory_log

        prioritized = (
            self.prioritizer.prioritize(

                matched_memories,

                limit
            )
        )

        return prioritized
