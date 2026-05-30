class MemoryCompressor:

    def compress(
        self,
        memory_entries,
        limit=100
    ):

        if len(
            memory_entries
        ) <= limit:

            return memory_entries

        return memory_entries[
            -limit:
        ]
