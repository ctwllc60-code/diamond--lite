class RetrievalPrioritizer:

    def prioritize(
        self,
        memories,
        limit=10
    ):

        prioritized = sorted(

            memories,

            key=lambda memory:

                memory.get(
                    "retrieval_priority",
                    1
                ),

            reverse=True
        )

        return prioritized[
            :limit
        ]
