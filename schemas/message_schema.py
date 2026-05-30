class MessageObject:

    def __init__(self, raw_message):

        self.raw_message = raw_message

        self.enrichment_layers = []

        self.cognitive_state = {}

        self.emotional_state = {}

        self.salience_map = {}

        self.recursion_state = {
            "depth": 0,
            "revisits": [],
            "recursive_thinking_required": False,
            "recursive_trigger_engine": None,
            "loop_count": 0,
            "max_loops": 3,
            "current_wave": 0
        }

        self.final_response = None
